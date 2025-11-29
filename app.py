"""
Web Frontend for Intelligent SBI Form Filler
Flask application with form input and PDF download
"""
from flask import Flask, render_template, request, send_file, jsonify
import os
import json
from datetime import datetime
from intelligent_form_filler import call_ollama_llm, clean_extracted_data, print_extracted_data
from step4_fill_form import PDFFormFiller

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create outputs directory
os.makedirs('outputs', exist_ok=True)


@app.route('/')
def index():
    """Render the main form page."""
    return render_template('index.html')


@app.route('/api/fill-form', methods=['POST'])
def fill_form():
    """
    API endpoint to process form input and generate filled PDF.
    
    Expects JSON with 'input_text' field containing raw data.
    Returns JSON with extraction results and download URL.
    """
    try:
        # Get input data
        data = request.get_json()
        if not data or 'input_text' not in data:
            return jsonify({
                'success': False,
                'error': 'No input text provided'
            }), 400
        
        raw_input = data['input_text'].strip()
        
        if not raw_input:
            return jsonify({
                'success': False,
                'error': 'Input text is empty'
            }), 400
        
        print(f"\n{'='*60}")
        print(f"Processing form fill request at {datetime.now()}")
        print(f"{'='*60}")
        print(f"Input text length: {len(raw_input)} characters")
        
        # Step 1: Extract data using LLM
        try:
            extracted_data = call_ollama_llm(raw_input)
        except Exception as e:
            print(f"LLM Error: {str(e)}")
            return jsonify({
                'success': False,
                'error': f'LLM processing failed: {str(e)}',
                'suggestion': 'Make sure Ollama is running: ollama serve'
            }), 500
        
        # Step 2: Clean and validate data
        cleaned_data = clean_extracted_data(extracted_data)
        
        # Step 3: Check for images
        if not cleaned_data.get('photograph') and os.path.exists('photograph.jpg'):
            cleaned_data['photograph'] = 'photograph.jpg'
        
        if not cleaned_data.get('signature') and os.path.exists('signature.png'):
            cleaned_data['signature'] = 'signature.png'
        
        # Step 4: Fill the PDF form
        # Generate unique filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_filename = f'SBI_filled_{timestamp}.pdf'
        output_path = os.path.join('outputs', output_filename)
        
        # Template PDF path
        template_path = '45679523-SBI-Account-Opening-Form-I (1)_removed.pdf'
        
        # Initialize filler with paths
        filler = PDFFormFiller(template_path, output_path)
        filler.open_template()
        filler.fill_form(cleaned_data)
        filler.save()
        
        print(f"\n✓ PDF generated successfully: {output_path}")
        
        # Step 5: Prepare response with extracted data
        response_data = {
            'success': True,
            'message': 'Form filled successfully!',
            'pdf_filename': output_filename,
            'download_url': f'/download/{output_filename}',
            'extracted_data': {
                'personal': {
                    'full_name': cleaned_data.get('full_name', ''),
                    'father_name': cleaned_data.get('father_name', ''),
                    'mother_name': cleaned_data.get('mother_name', ''),
                    'date_of_birth': cleaned_data.get('date_of_birth', ''),
                    'gender': cleaned_data.get('gender', ''),
                    'marital_status': cleaned_data.get('marital_status', '')
                },
                'residential': {
                    'address_line1': cleaned_data.get('residential_address_line1', ''),
                    'address_line2': cleaned_data.get('residential_address_line2', ''),
                    'address_line3': cleaned_data.get('residential_address_line3', ''),
                    'landmark': cleaned_data.get('residential_landmark', ''),
                    'city': cleaned_data.get('city', ''),
                    'state': cleaned_data.get('state', ''),
                    'pincode': cleaned_data.get('pincode', ''),
                    'phone': cleaned_data.get('phone_no', ''),
                    'mobile': cleaned_data.get('mobile_number', ''),
                    'email_1': cleaned_data.get('email_id_1', ''),
                    'email_2': cleaned_data.get('email_id_2', '')
                },
                'office': {
                    'address_line1': cleaned_data.get('office_address_line1', ''),
                    'address_line2': cleaned_data.get('office_address_line2', ''),
                    'address_line3': cleaned_data.get('office_address_line3', ''),
                    'landmark': cleaned_data.get('office_landmark', ''),
                    'city': cleaned_data.get('office_city', ''),
                    'state': cleaned_data.get('office_state', ''),
                    'pincode': cleaned_data.get('office_pincode', ''),
                    'phone': cleaned_data.get('office_phone_no', ''),
                    'fax': cleaned_data.get('office_fax_no', '')
                },
                'bank': {
                    'branch': cleaned_data.get('branch', ''),
                    'code': cleaned_data.get('code_no', ''),
                    'date': cleaned_data.get('date', ''),
                    'cif': cleaned_data.get('cif_no', ''),
                    'pan': cleaned_data.get('income_tax_pan_form', ''),
                    'nationality': cleaned_data.get('nationality', '')
                },
                'preferences': {
                    'customer_type': cleaned_data.get('customer_type', ''),
                    'correspondence': cleaned_data.get('correspondence_address', '')
                }
            }
        }
        
        return jsonify(response_data), 200
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500


@app.route('/download/<filename>')
def download_file(filename):
    """
    Download endpoint for generated PDFs.
    """
    try:
        file_path = os.path.join('outputs', filename)
        
        if not os.path.exists(file_path):
            return jsonify({
                'success': False,
                'error': 'File not found'
            }), 404
        
        return send_file(
            file_path,
            as_attachment=True,
            download_name=filename,
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/health')
def health_check():
    """Health check endpoint."""
    try:
        import ollama
        # Try to list models to check Ollama connection
        models = ollama.list()
        ollama_status = 'connected'
        model_available = any('llama3.1' in str(m) for m in models.get('models', []))
    except:
        ollama_status = 'disconnected'
        model_available = False
    
    return jsonify({
        'status': 'running',
        'ollama': ollama_status,
        'model_llama3.1': model_available,
        'timestamp': datetime.now().isoformat()
    })


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🤖 INTELLIGENT SBI FORM FILLER - Web Interface")
    print("="*60)
    print("\nStarting Flask server...")
    print("Access at: http://localhost:5001")
    print("\nMake sure Ollama is running:")
    print("  ollama serve")
    print("\nPress Ctrl+C to stop the server")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=5001, debug=True)
