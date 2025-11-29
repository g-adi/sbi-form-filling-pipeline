"""
Intelligent Form Filler using Ollama LLM
Uses Llama 3.1 8B to parse raw/messy input and map it to form fields.
"""
import json
import sys
from step4_fill_form import PDFFormFiller


def flatten_nested_dict(d: dict, parent_key: str = '') -> dict:
    """
    Flatten a nested dictionary to a single level.
    
    Args:
        d: Dictionary to flatten
        parent_key: Key prefix for nested keys
        
    Returns:
        Flattened dictionary
    """
    items = []
    for k, v in d.items():
        if isinstance(v, dict):
            # Recursively flatten nested dicts
            items.extend(flatten_nested_dict(v, parent_key).items())
        else:
            items.append((k, v))
    return dict(items)


def call_ollama_llm(raw_input: str) -> dict:
    """
    Call Ollama LLM to parse raw input and extract structured form data.
    
    Args:
        raw_input: Raw/messy text input from user
        
    Returns:
        Dictionary with structured form field data
    """
    try:
        import ollama
    except ImportError:
        raise ImportError("ollama package not installed. Install with: pip install ollama")
    
    # Define the system prompt with all form fields
    system_prompt = """You are an AI assistant that extracts information from raw text to fill an SBI bank account opening form.

**FORM FIELDS TO EXTRACT:**

1. PERSONAL DETAILS:
   - full_name (uppercase)
   - father_name (uppercase)
   - mother_name (uppercase)
   - date_of_birth (DD/MM/YYYY format)
   - gender (Male/Female)
   - marital_status (Married/Unmarried/Others)

2. RESIDENTIAL ADDRESS:
   - residential_address_line1 (max 25 chars, uppercase)
   - residential_address_line2 (max 25 chars, uppercase)
   - residential_address_line3 (max 25 chars, uppercase)
   - residential_landmark (max 27 chars, uppercase)
   - city (max 18 chars, uppercase)
   - state (max 30 chars, uppercase)
   - pincode (6 digits)
   - phone_no (with STD code, max 12 digits)
   - mobile_number (10 digits)
   - email_id_1 (max 29 chars, lowercase)
   - email_id_2 (optional, max 29 chars, lowercase)

3. OFFICE/BUSINESS ADDRESS:
   - office_address_line1 (max 25 chars, uppercase)
   - office_address_line2 (max 25 chars, uppercase)
   - office_address_line3 (max 25 chars, uppercase)
   - office_landmark (max 27 chars, uppercase)
   - office_city (max 18 chars, uppercase)
   - office_state (max 30 chars, uppercase)
   - office_pincode (6 digits)
   - office_phone_no (with STD code, max 16 digits)
   - office_fax_no (optional, max 16 digits)

4. BANK DETAILS:
   - branch (bank branch name, max 23 chars, uppercase)
   - code_no (branch code, max 5 digits)
   - date (today's date in DD/MM/YYYY format)
   - cif_no (Customer ID, 11 digits if available)

5. IDENTITY & NATIONALITY:
   - income_tax_pan_form (PAN number, 10 chars, uppercase)
   - nationality (max 10 chars, uppercase, default: INDIAN)

6. SELECTIONS:
   - customer_type (Public/Staff)
   - correspondence_address (B for Residential / C for Office)

7. IMAGES (optional):
   - photograph (path to photo file, or null)
   - signature (path to signature file, or null)

**CRITICAL INSTRUCTIONS:**
- Extract all available information from the provided text
- For missing fields, use empty string ""
- Convert all names and addresses to UPPERCASE
- Convert emails to lowercase
- Ensure dates are in DD/MM/YYYY format
- Truncate text to fit character limits
- Return ONLY valid JSON with the field names exactly as specified
- Do not nest the JSON - use FLAT structure with all fields at root level
- Put ALL values in quotes as strings, including numbers
- Do not include any explanation or markdown, just the raw JSON object

**OUTPUT FORMAT (FLAT STRUCTURE - ALL VALUES AS STRINGS):**
{
  "full_name": "JOHN DOE",
  "father_name": "JAMES DOE",
  "pincode": "201301",
  "mobile_number": "9876543210",
  "customer_type": "Public",
  ...
}

Return valid JSON with this exact flat structure."""

    user_prompt = f"""Extract form data from this raw input:

{raw_input}

Return valid JSON only."""

    print("\n" + "="*60)
    print("CALLING OLLAMA LLM (Llama 3.1 8B Instruct)")
    print("="*60)
    print("Analyzing input and extracting form fields...")
    
    try:
        # Call Ollama API
        response = ollama.chat(
            model='llama3.1:8b-instruct-q8_0',  # Llama 3.1 8B Instruct
            messages=[
                {
                    'role': 'system',
                    'content': system_prompt
                },
                {
                    'role': 'user',
                    'content': user_prompt
                }
            ],
            options={
                'temperature': 0.1,  # Lower temperature for more deterministic output
                'top_p': 0.9,
            }
        )
        
        # Extract the response content
        llm_output = response['message']['content']
        print("\n✓ LLM Response received")
        print("\n--- Raw LLM Output ---")
        print(llm_output)
        print("--- End Raw Output ---\n")
        
        # Parse JSON from response
        # Try to extract JSON if wrapped in markdown code blocks
        if '```json' in llm_output:
            json_start = llm_output.find('```json') + 7
            json_end = llm_output.find('```', json_start)
            llm_output = llm_output[json_start:json_end].strip()
        elif '```' in llm_output:
            json_start = llm_output.find('```') + 3
            json_end = llm_output.find('```', json_start)
            llm_output = llm_output[json_start:json_end].strip()
        
        # Parse JSON
        extracted_data = json.loads(llm_output)
        
        # Flatten if nested structure
        if any(isinstance(v, dict) for v in extracted_data.values()):
            print("⚠️  Detected nested structure, flattening...")
            extracted_data = flatten_nested_dict(extracted_data)
        
        # Clean up and validate data
        cleaned_data = clean_extracted_data(extracted_data)
        
        print("✓ Successfully parsed and validated form data")
        return cleaned_data
        
    except json.JSONDecodeError as e:
        print(f"\n❌ Error: Failed to parse JSON from LLM output: {e}")
        print("LLM output was:", llm_output)
        raise ValueError(f"Failed to parse JSON from LLM: {e}")
    except Exception as e:
        print(f"\n❌ Error calling Ollama: {e}")
        print("Make sure Ollama is running: ollama serve")
        print("And the model is installed: ollama pull llama3.1:8b-instruct-q8_0")
        raise


def clean_extracted_data(data: dict) -> dict:
    """
    Clean and validate extracted data.
    
    Args:
        data: Raw extracted data from LLM
        
    Returns:
        Cleaned and validated data
    """
    # Convert None/null values to empty strings or appropriate defaults
    cleaned = {}
    
    # Text fields - ensure uppercase where needed
    text_upper_fields = [
        'full_name', 'father_name', 'mother_name',
        'residential_address_line1', 'residential_address_line2', 'residential_address_line3',
        'residential_landmark', 'city', 'state',
        'office_address_line1', 'office_address_line2', 'office_address_line3',
        'office_landmark', 'office_city', 'office_state',
        'branch', 'income_tax_pan_form', 'nationality'
    ]
    
    text_lower_fields = ['email_id_1', 'email_id_2']
    
    for field in text_upper_fields:
        if field in data and data[field]:
            cleaned[field] = str(data[field]).upper()
        else:
            cleaned[field] = ""
    
    for field in text_lower_fields:
        if field in data and data[field]:
            cleaned[field] = str(data[field]).lower()
        else:
            cleaned[field] = ""
    
    # Numeric fields
    numeric_fields = ['pincode', 'phone_no', 'mobile_number', 'office_pincode', 
                     'office_phone_no', 'office_fax_no', 'code_no', 'cif_no']
    
    for field in numeric_fields:
        if field in data and data[field]:
            # Remove any non-numeric characters
            cleaned[field] = ''.join(filter(str.isdigit, str(data[field])))
        else:
            cleaned[field] = ""
    
    # Date fields
    if 'date_of_birth' in data and data['date_of_birth']:
        cleaned['date_of_birth'] = data['date_of_birth']
    else:
        cleaned['date_of_birth'] = ""
    
    if 'date' in data and data['date']:
        cleaned['date'] = data['date']
    else:
        # Use current date
        from datetime import datetime
        cleaned['date'] = datetime.now().strftime('%d/%m/%Y')
    
    # Checkboxes/selections
    if 'gender' in data and data['gender']:
        gender = str(data['gender']).strip()
        if gender.lower() in ['male', 'm']:
            cleaned['gender'] = 'Male'
        elif gender.lower() in ['female', 'f']:
            cleaned['gender'] = 'Female'
        else:
            cleaned['gender'] = 'Male'  # Default
    else:
        cleaned['gender'] = 'Male'
    
    if 'marital_status' in data and data['marital_status']:
        status = str(data['marital_status']).strip()
        if status.lower() in ['married', 'yes']:
            cleaned['marital_status'] = 'Married'
        elif status.lower() in ['unmarried', 'no', 'single']:
            cleaned['marital_status'] = 'Unmarried'
        else:
            cleaned['marital_status'] = 'Others'
    else:
        cleaned['marital_status'] = 'Unmarried'
    
    if 'customer_type' in data and data['customer_type']:
        ctype = str(data['customer_type']).strip()
        if ctype.lower() in ['staff', 'employee']:
            cleaned['customer_type'] = 'Staff'
        else:
            cleaned['customer_type'] = 'Public'
    else:
        cleaned['customer_type'] = 'Public'
    
    if 'correspondence_address' in data and data['correspondence_address']:
        addr = str(data['correspondence_address']).strip().upper()
        if addr in ['C', 'OFFICE', 'WORK']:
            cleaned['correspondence_address'] = 'C'
        else:
            cleaned['correspondence_address'] = 'B'
    else:
        cleaned['correspondence_address'] = 'B'
    
    # Image paths (optional)
    if 'photograph' in data and data['photograph']:
        cleaned['photograph'] = str(data['photograph'])
    else:
        cleaned['photograph'] = None
    
    if 'signature' in data and data['signature']:
        cleaned['signature'] = str(data['signature'])
    else:
        cleaned['signature'] = None
    
    return cleaned


def print_extracted_data(data: dict):
    """Print extracted data in a readable format."""
    print("\n" + "="*60)
    print("EXTRACTED FORM DATA")
    print("="*60)
    
    print("\n--- PERSONAL DETAILS ---")
    print(f"Name: {data.get('full_name', 'N/A')}")
    print(f"Father's Name: {data.get('father_name', 'N/A')}")
    print(f"Mother's Name: {data.get('mother_name', 'N/A')}")
    print(f"Date of Birth: {data.get('date_of_birth', 'N/A')}")
    print(f"Gender: {data.get('gender', 'N/A')}")
    print(f"Marital Status: {data.get('marital_status', 'N/A')}")
    
    print("\n--- RESIDENTIAL ADDRESS ---")
    print(f"Line 1: {data.get('residential_address_line1', 'N/A')}")
    print(f"Line 2: {data.get('residential_address_line2', 'N/A')}")
    print(f"Line 3: {data.get('residential_address_line3', 'N/A')}")
    print(f"Landmark: {data.get('residential_landmark', 'N/A')}")
    print(f"City: {data.get('city', 'N/A')}")
    print(f"State: {data.get('state', 'N/A')}")
    print(f"Pincode: {data.get('pincode', 'N/A')}")
    print(f"Phone: {data.get('phone_no', 'N/A')}")
    print(f"Mobile: {data.get('mobile_number', 'N/A')}")
    print(f"Email 1: {data.get('email_id_1', 'N/A')}")
    print(f"Email 2: {data.get('email_id_2', 'N/A')}")
    
    print("\n--- OFFICE ADDRESS ---")
    print(f"Line 1: {data.get('office_address_line1', 'N/A')}")
    print(f"Line 2: {data.get('office_address_line2', 'N/A')}")
    print(f"Line 3: {data.get('office_address_line3', 'N/A')}")
    print(f"Landmark: {data.get('office_landmark', 'N/A')}")
    print(f"City: {data.get('office_city', 'N/A')}")
    print(f"State: {data.get('office_state', 'N/A')}")
    print(f"Pincode: {data.get('office_pincode', 'N/A')}")
    print(f"Phone: {data.get('office_phone_no', 'N/A')}")
    print(f"Fax: {data.get('office_fax_no', 'N/A')}")
    
    print("\n--- BANK & IDENTITY ---")
    print(f"Branch: {data.get('branch', 'N/A')}")
    print(f"Branch Code: {data.get('code_no', 'N/A')}")
    print(f"Date: {data.get('date', 'N/A')}")
    print(f"CIF No: {data.get('cif_no', 'N/A')}")
    print(f"PAN: {data.get('income_tax_pan_form', 'N/A')}")
    print(f"Nationality: {data.get('nationality', 'N/A')}")
    
    print("\n--- SELECTIONS ---")
    print(f"Customer Type: {data.get('customer_type', 'N/A')}")
    print(f"Correspondence: {data.get('correspondence_address', 'N/A')}")
    
    print("\n" + "="*60)


def main():
    """Main function to run intelligent form filler."""
    print("\n" + "="*60)
    print("INTELLIGENT SBI FORM FILLER")
    print("Powered by Ollama + Llama 3.1 8B Instruct")
    print("="*60)
    
    # Check if input file provided or use sample
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        print(f"\n📄 Reading input from: {input_file}")
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                raw_input = f.read()
        except FileNotFoundError:
            print(f"❌ Error: File not found: {input_file}")
            sys.exit(1)
    else:
        # Use sample input for testing
        print("\n📝 Using sample input (you can provide a file as argument)")
        raw_input = """
        My name is Priya Singh, my father Rajesh Singh and mother Sunita Singh.
        I was born on 25th March 1995. I'm a female and married.
        
        I live at B-204 Green Valley Apartments, Malviya Nagar, near Metro Station,
        New Delhi, Delhi 110017. My phone is 011-26543210 and mobile 9876543210.
        Email: priya.singh@gmail.com
        
        I work at Tech Solutions Pvt Ltd, A-15 Cyber City, Sector 18,
        Gurgaon, Haryana 122015. Office phone: 0124-4567890.
        
        I want to open account at Connaught Place branch, code 12345.
        My PAN is ABCDE1234F. I am Indian citizen.
        I'm a regular customer and want correspondence at my home address.
        """
    
    print("\n--- Raw Input ---")
    print(raw_input)
    print("--- End Input ---\n")
    
    # Step 1: Call LLM to extract data
    extracted_data = call_ollama_llm(raw_input)
    
    # Step 2: Print extracted data
    print_extracted_data(extracted_data)
    
    # Step 3: Ask for confirmation
    print("\n" + "="*60)
    user_input = input("Proceed to fill the form? (y/n): ").strip().lower()
    
    if user_input != 'y':
        print("❌ Form filling cancelled by user.")
        sys.exit(0)
    
    # Step 4: Fill the form using existing pipeline
    print("\n" + "="*60)
    print("FILLING FORM")
    print("="*60)
    
    # Check for image files
    import os
    if not extracted_data.get('photograph') and os.path.exists('photograph.jpg'):
        extracted_data['photograph'] = 'photograph.jpg'
        print("✓ Found photograph.jpg")
    
    if not extracted_data.get('signature') and os.path.exists('signature.png'):
        extracted_data['signature'] = 'signature.png'
        print("✓ Found signature.png")
    
    # Use existing PDF filler
    filler = PDFFormFiller()
    output_file = "SBI_filled_form_intelligent.pdf"
    filler.fill_form(extracted_data)
    filler.save(output_file)
    
    print("\n" + "="*60)
    print("✅ FORM FILLING COMPLETE!")
    print("="*60)
    print(f"📄 Output saved to: {output_file}")
    print("\nNext steps:")
    print("  1. Open the filled PDF")
    print("  2. Review all fields")
    print("  3. Adjust any incorrect information manually if needed")
    print("="*60)


if __name__ == "__main__":
    main()
