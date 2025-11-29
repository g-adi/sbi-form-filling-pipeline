"""
Step 4: Dummy Data Generator
Generates realistic test data for all form fields to test coordinate accuracy.
"""
from datetime import datetime, timedelta
import random

def generate_dummy_data():
    """
    Generate dummy data for all form fields.
    Returns a dictionary with field names as keys and test values.
    """
    dummy_data = {
        # === PERSONAL DETAILS ===
        "full_name": "RAJESH KUMAR SHARMA",
        "father_name": "SURESH KUMAR SHARMA",
        "mother_name": "SUNITA DEVI SHARMA",
        "date_of_birth": "15/08/1990",
        
        # === RESIDENTIAL ADDRESS (B) ===
        "residential_address_line1": "FLAT NO 301 TOWER B GROW",
        "residential_address_line2": "NEAR CITY MALL SECTOR 18",
        "residential_address_line3": "NOIDA SECTOR 62",
        "residential_landmark": "NEAR CITY CENTRE METRO STN",
        "city": "NOIDA",
        "state": "UTTAR PRADESH",
        "pincode": "201301",
        "phone_no": "01204567890",
        "mobile_number": "9876543210",
        "email_id_1": "rajesh.sharma@gmail.com",
        "email_id_2": "rajesh.kumar.sharma@gmail.com",
        
        # === OFFICE/BUSINESS ADDRESS (C) ===
        "office_address_line1": "ABC SOLUTIONS PVT LTD",
        "office_address_line2": "TOWER A CORPORATE PARK",
        "office_address_line3": "GOLF COURSE ROAD",
        "office_landmark": "NEAR CYBER HUB",
        "office_city": "GURGAON",
        "office_state": "HARYANA",
        "office_pincode": "122002",
        "office_phone_no": "01244567890",
        "office_fax_no": "01244567891",
        
        # === BOXED FIELDS ===
        "branch": "CONNAUGHT PLACE DELHI",
        "code_no": "12345",
        "date": "30/11/2025",
        "cif_no": "12345678901",
        
        
        # === SECTION (D): INCOME TAX & NATIONALITY ===
        "income_tax_pan_form": "ABCDE1234F",
        "nationality": "INDIAN",
        
        # === IMAGES ===
        # Image paths (relative to script location)
        "photograph": "photograph.jpg",  # Path to photograph image (2.5 cm X 3.5 cm)
        "signature": "signature.png",   # Path to signature image
        
        # === CHECKBOXES ===
        "gender": "Female",
        "marital_status": "Others",
        "customer_type": "Staff",
        "correspondence_address": "C",  # B = Residential, C = Office
    }
    
    return dummy_data


def generate_test_data_variations():
    """
    Generate multiple test data sets with different lengths and cases.
    Useful for testing edge cases.
    """
    variations = {
        "short_names": {
            "full_name": "RAM LAL",
            "father_name": "DEV LAL",
            "mother_name": "SITA DEVI",
            "date_of_birth": "01/01/1995",
            "mobile_number": "9999999999",
            "email_id": "ram@test.com",
        },
        
        "long_names": {
            "full_name": "RAMAKRISHNAN VENKATASUBRAMANIAN PADMANABHAN",
            "father_name": "VENKATASUBRAMANIAN SRINIVASAN PADMANABHAN",
            "mother_name": "LAKSHMI PADMANABHAN VENKATARAMAN",
            "date_of_birth": "31/12/1985",
            "mobile_number": "8888888888",
            "email_id": "ramakrishnan.venkatasubramanian@longdomain.com",
        },
        
        "max_length": {
            "full_name": "A" * 50,
            "residential_address_line1": "X" * 80,
            "residential_address_line2": "Y" * 80,
            "city": "THIRUVANANTHAPURAM",
            "state": "HIMACHAL PRADESH",
        }
    }
    
    return variations


def print_dummy_data():
    """Print the dummy data in a readable format."""
    data = generate_dummy_data()
    
    print("\n" + "=" * 60)
    print("GENERATED DUMMY DATA FOR TESTING")
    print("=" * 60)
    
    print("\n--- PERSONAL DETAILS ---")
    print(f"Full Name: {data['full_name']}")
    print(f"Father's Name: {data['father_name']}")
    print(f"Mother's Name: {data['mother_name']}")
    print(f"Date of Birth: {data['date_of_birth']}")
    
    print("\n--- RESIDENTIAL ADDRESS (B) ---")
    print(f"Address Line 1: {data['residential_address_line1']}")
    print(f"Address Line 2: {data['residential_address_line2']}")
    print(f"Address Line 3: {data['residential_address_line3']}")
    print(f"Landmark: {data['residential_landmark']}")
    print(f"City: {data['city']}")
    print(f"State: {data['state']}")
    print(f"PIN Code: {data['pincode']}")
    print(f"Phone No.: {data['phone_no']}")
    print(f"Mobile No.: {data['mobile_number']}")
    print(f"E-mail ID (Line 1): {data['email_id_1']}")
    print(f"E-mail ID (Line 2): {data['email_id_2']}")
    
    print("\n--- OFFICE/BUSINESS ADDRESS (C) ---")
    print(f"Address Line 1: {data['office_address_line1']}")
    print(f"Address Line 2: {data['office_address_line2']}")
    print(f"Address Line 3: {data['office_address_line3']}")
    print(f"Landmark: {data['office_landmark']}")
    print(f"City: {data['office_city']}")
    print(f"State: {data['office_state']}")
    print(f"PIN Code: {data['office_pincode']}")
    print(f"Phone No.: {data['office_phone_no']}")
    print(f"Fax No.: {data['office_fax_no']}")
    
    print("\n--- IDENTIFICATION ---")
    print(f"PAN Number: {data['pan_number']}")
    print(f"Aadhaar Number: {data['aadhaar_number']}")
    
    print("\n--- BRANCH & FORM DETAILS ---")
    print(f"Branch: {data['branch']}")
    print(f"Code No.: {data['code_no']}")
    print(f"Date: {data['date']}")
    print(f"CIF No.: {data['cif_no']}")
    
    print("\n--- ACCOUNT DETAILS ---")
    print(f"Account Type: {data['account_type']}")
    print(f"Account Number: {data['account_number']}")
    
    print("\n--- NOMINEE ---")
    print(f"Nominee Name: {data['nominee_name']}")
    print(f"Relation: {data['nominee_relation']}")
    
    print("\n--- SECTION (D): INCOME TAX & NATIONALITY ---")
    print(f"Income Tax PAN or Form 60/61: {data['income_tax_pan_form']}")
    print(f"Nationality: {data['nationality']}")
    
    print("\n--- IMAGES ---")
    print(f"Photograph: {data.get('photograph', 'Not provided')}")
    print(f"Signature: {data.get('signature', 'Not provided')}")
    
    print("\n--- SELECTIONS ---")
    print(f"Gender: {data['gender']}")
    print(f"Marital Status: {data['marital_status']}")
    print(f"Account Type (Radio): {data['account_type_radio']}")
    print(f"Customer Type: {data['customer_type']}")
    print(f"Correspondence Address: {data['correspondence_address']}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    print_dummy_data()
    
    print("\n\nTest data variations available:")
    variations = generate_test_data_variations()
    for var_name in variations.keys():
        print(f"  - {var_name}")
