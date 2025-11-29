"""
Step 3: Layout Configuration
This file contains the coordinate mappings for all form fields.
Coordinates are manually calibrated to match the exact positions on the PDF.

COORDINATE SYSTEM: 
- Origin (0, 0) is at TOP-LEFT
- X increases to the RIGHT
- Y increases DOWNWARD
- Units are in PDF points (1/72 inch)
"""

# Page configuration
PAGE_CONFIG = {
    "width": 666,  # Actual page width in points (from inspection)
    "height": 864,  # Actual page height in points (from inspection)
}

# Standard text field configuration
# Each field has: page number, x, y (baseline), max_width, font_size
FORM_LAYOUT = {
    # === PERSONAL DETAILS SECTION ===
    # Note: full_name, father_name, mother_name, date_of_birth moved to BOXED_FIELDS
    # Note: All address fields moved to BOXED_FIELDS
    
    # === BRANCH AND ACCOUNT DETAILS ===
    # Note: branch, code_no, date, cif_no moved to BOXED_FIELDS as they use character boxes
    "account_type": {
        "page": 0,
        "x": 120,
        "y": 520,
        "max_width": 200,
        "font_size": 9,
        "type": "text"
    },
    "nominee_name": {
        "page": 0,
        "x": 120,
        "y": 570,
        "max_width": 300,
        "font_size": 9,
        "type": "text"
    },
    "nominee_relation": {
        "page": 0,
        "x": 120,
        "y": 600,
        "max_width": 150,
        "font_size": 9,
        "type": "text"
    },
}

# Box-by-box fields (one character per box)
# Each has: page, x_start (first box center), y (baseline), dx (box spacing), font_size
BOXED_FIELDS = {
    "full_name": {
        "page": 0,
        "x_start": 153,  # X coordinate of first box
        "y": 252,        # Y coordinate (same for all boxes in the row)
        "dx": 15,        # Spacing between box centers - adjust if needed
        "font_size": 9,
        "max_chars": 30, # 30 boxes total
        "type": "boxed"
    },
    "branch": {
        "page": 0,
        "x_start": 133,   # X coordinate of first box - CALIBRATE THIS
        "y": 131,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 23, # Estimated number of boxes
        "type": "boxed"
    },
    "code_no": {
        "page": 0,
        "x_start": 528,  # X coordinate of first box - CALIBRATE THIS
        "y": 131,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 5, # Estimated number of boxes
        "type": "boxed"
    },
    "cif_no": {
        "page": 0,
        "x_start": 353,  # X coordinate of first box - CALIBRATE THIS
        "y": 154,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 20, # Estimated number of boxes
        "type": "boxed"
    },
    "father_name": {
        "page": 0,
        "x_start": 167,  # X coordinate of first box - CALIBRATE THIS
        "y": 282,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 29, # Estimated number of boxes
        "type": "boxed"
    },
    "mother_name": {
        "page": 0,
        "x_start": 198,  # X coordinate of first box - CALIBRATE THIS
        "y": 350,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 25, # Estimated number of boxes
        "type": "boxed"
    },
    
    # === RESIDENTIAL ADDRESS SECTION (B) ===
    "residential_address_line1": {
        "page": 0,
        "x_start": 227,  # X coordinate of first box - CALIBRATE THIS
        "y": 382,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 25, # Estimated number of boxes
        "type": "boxed"
    },
    "residential_address_line2": {
        "page": 0,
        "x_start": 227,  # X coordinate of first box - CALIBRATE THIS
        "y": 398,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 25, # Estimated number of boxes
        "type": "boxed"
    },
    "residential_address_line3": {
        "page": 0,
        "x_start": 227,  # X coordinate of first box - CALIBRATE THIS
        "y": 414,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 25, # Estimated number of boxes
        "type": "boxed"
    },
    "residential_landmark": {
        "page": 0,
        "x_start": 197,  # X coordinate of first box - CALIBRATE THIS
        "y": 430,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 27, # Estimated number of boxes
        "type": "boxed"
    },
    "city": {
        "page": 0,
        "x_start": 153,  # X coordinate of first box - CALIBRATE THIS
        "y": 446,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 18, # Estimated number of boxes
        "type": "boxed"
    },
    "pincode": {
        "page": 0,
        "x_start": 513,  # X coordinate of first box - CALIBRATE THIS
        "y": 446,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 6, # PIN Code boxes
        "type": "boxed"
    },
    "state": {
        "page": 0,
        "x_start": 153,  # X coordinate of first box - CALIBRATE THIS
        "y": 462,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 30, # Estimated number of boxes
        "type": "boxed"
    },
    "phone_no": {
        "page": 0,
        "x_start": 183,  # X coordinate of first box - CALIBRATE THIS
        "y": 478,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 12, # Phone number with STD code
        "type": "boxed"
    },
    "mobile_number": {
        "page": 0,
        "x_start": 453,  # X coordinate of first box - CALIBRATE THIS
        "y": 478,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 10, # Mobile number boxes
        "type": "boxed"
    },
    "email_id_1": {
        "page": 0,
        "x_start": 167,  # X coordinate of first box - CALIBRATE THIS
        "y": 506,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 29, # Email ID boxes (line 1)
        "type": "boxed"
    },
    "email_id_2": {
        "page": 0,
        "x_start": 167,  # X coordinate of first box - CALIBRATE THIS
        "y": 522,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 29, # Email ID boxes (line 2)
        "type": "boxed"
    },
    
    # === OFFICE/BUSINESS ADDRESS SECTION (C) ===
    "office_address_line1": {
        "page": 0,
        "x_start": 227,  # X coordinate of first box - CALIBRATE THIS
        "y": 550,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 25, # Estimated number of boxes
        "type": "boxed"
    },
    "office_address_line2": {
        "page": 0,
        "x_start": 227,  # X coordinate of first box - CALIBRATE THIS
        "y": 566,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 25, # Estimated number of boxes
        "type": "boxed"
    },
    "office_address_line3": {
        "page": 0,
        "x_start": 227,  # X coordinate of first box - CALIBRATE THIS
        "y": 582,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 25, # Estimated number of boxes
        "type": "boxed"
    },
    "office_landmark": {
        "page": 0,
        "x_start": 197,  # X coordinate of first box - CALIBRATE THIS
        "y": 598,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 27, # Estimated number of boxes
        "type": "boxed"
    },
    "office_city": {
        "page": 0,
        "x_start": 153,  # X coordinate of first box - CALIBRATE THIS
        "y": 614,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 18, # Estimated number of boxes
        "type": "boxed"
    },
    "office_state": {
        "page": 0,
        "x_start": 153,  # X coordinate of first box - CALIBRATE THIS
        "y": 630,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 30, # Estimated number of boxes
        "type": "boxed"
    },
    "office_pincode": {
        "page": 0,
        "x_start": 198,  # X coordinate of first box - CALIBRATE THIS
        "y": 646,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 6, # PIN Code boxes (6 digits)
        "type": "boxed"
    },
    "office_phone_no": {
        "page": 0,
        "x_start": 183,  # X coordinate of first box - CALIBRATE THIS
        "y": 662,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 16, # Phone number with STD code
        "type": "boxed"
    },
    "office_fax_no": {
        "page": 0,
        "x_start": 183,  # X coordinate of first box - CALIBRATE THIS
        "y": 695,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 16, # Fax number boxes
        "type": "boxed"
    },
    
    # === SECTION (D): INCOME TAX & NATIONALITY ===
    "income_tax_pan_form": {
        "page": 0,
        "x_start": 300,  # X coordinate of first box - CALIBRATE THIS
        "y": 755,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 10, # Income Tax PAN or Form 60/61 boxes
        "type": "boxed"
    },
    "nationality": {
        "page": 0,
        "x_start": 300,  # X coordinate of first box - CALIBRATE THIS
        "y": 776,        # Y coordinate - CALIBRATE THIS
        "dx": 15,        # Spacing between box centers
        "font_size": 9,
        "max_chars": 10, # Nationality boxes
        "type": "boxed"
    },
}

# Date fields with separate DD, MM, YYYY sections
# Each section has its own x_start position
DATE_FIELDS = {
    "date": {
        "page": 0,
        "type": "date",
        "font_size": 9,
        "dd": {
            "x_start": 152,  # X coordinate for first DD box - CALIBRATE THIS
            "y": 154,        # Y coordinate - CALIBRATE THIS
            "dx": 15,        # Spacing between DD boxes
        },
        "mm": {
            "x_start": 194,  # X coordinate for first MM box - CALIBRATE THIS
            "y": 154,        # Y coordinate - CALIBRATE THIS
            "dx": 15,        # Spacing between MM boxes
        },
        "yyyy": {
            "x_start": 236,  # X coordinate for first YYYY box - CALIBRATE THIS
            "y": 154,        # Y coordinate - CALIBRATE THIS
            "dx": 15,        # Spacing between YYYY boxes
        }
    },
    "date_of_birth": {
        "page": 0,
        "type": "date",
        "font_size": 9,
        "dd": {
            "x_start": 198,  # X coordinate for first DD box - CALIBRATE THIS
            "y": 306,        # Y coordinate - CALIBRATE THIS
            "dx": 15,        # Spacing between DD boxes
        },
        "mm": {
            "x_start": 242,  # X coordinate for first MM box - CALIBRATE THIS
            "y": 306,        # Y coordinate - CALIBRATE THIS
            "dx": 15,        # Spacing between MM boxes
        },
        "yyyy": {
            "x_start": 288,  # X coordinate for first YYYY box - CALIBRATE THIS
            "y": 306,        # Y coordinate - CALIBRATE THIS
            "dx": 15,        # Spacing between YYYY boxes
        }
    }
}

# Image fields
# Each has: page, x (left), y (top), width, height (all in PDF points)
IMAGE_FIELDS = {
    "photograph": {
        "page": 0,
        "x": 490,        # X coordinate (left edge) - CALIBRATE THIS
        "y": 510,         # Y coordinate (top edge) - CALIBRATE THIS
        "width": 71,     # Width in points (2.5 cm ≈ 71 points)
        "height": 290,   # Height in points (3.5 cm ≈ 99 points)
        "type": "image",
        "description": "Photograph (2.5 cm X 3.5 cm)"
    },
    "signature": {
        "page": 0,
        "x": 433,         # X coordinate (left edge) - CALIBRATE THIS
        "y": 712,        # Y coordinate (top edge) - CALIBRATE THIS
        "width": 180,    # Width in points - CALIBRATE THIS
        "height": 40,   # Height in points - CALIBRATE THIS
        "type": "image",
        "description": "Signature of the Customer"
    },
}

# Checkbox/Radio button fields
# Each has: page, x (center), y (center), and the options list
CHECKBOX_FIELDS = {
    "gender": {
        "page": 0,
        "type": "checkbox",
        "options": {
            "Male": {"x": 423, "y": 307},     # CALIBRATE THESE COORDINATES
            "Female": {"x": 484, "y": 307},   # CALIBRATE THESE COORDINATES
        }
    },
    "marital_status": {
        "page": 0,
        "type": "checkbox",
        "options": {
            "Married": {"x": 216, "y": 332},      # CALIBRATE THESE COORDINATES
            "Unmarried": {"x": 296, "y": 332},    # CALIBRATE THESE COORDINATES
            "Others": {"x": 400, "y": 332},       # CALIBRATE THESE COORDINATES
        }
    },
    "customer_type": {
        "page": 0,
        "type": "checkbox",
        "options": {
            "Public": {"x": 217, "y": 211},  # CALIBRATE THESE COORDINATES
            "Staff": {"x": 300, "y": 211},   # CALIBRATE THESE COORDINATES
        }
    },
    "correspondence_address": {
        "page": 0,
        "type": "checkbox",
        "options": {
            "B": {"x": 327, "y": 723},  # CALIBRATE - Residential address (B)
            "C": {"x": 375, "y": 723},  # CALIBRATE - Office address (C)
        }
    },
}

# Combine all layouts for easy access
ALL_FIELDS = {
    **FORM_LAYOUT,
    **BOXED_FIELDS,
    **DATE_FIELDS,
    **IMAGE_FIELDS,
    **CHECKBOX_FIELDS
}


def get_field_config(field_name):
    """Get configuration for a specific field."""
    return ALL_FIELDS.get(field_name)


def get_all_text_fields():
    """Get all standard text fields."""
    return FORM_LAYOUT


def get_all_boxed_fields():
    """Get all box-by-box fields."""
    return BOXED_FIELDS


def get_all_date_fields():
    """Get all date fields with DD/MM/YYYY sections."""
    return DATE_FIELDS


def get_all_image_fields():
    """Get all image fields."""
    return IMAGE_FIELDS


def get_all_checkbox_fields():
    """Get all checkbox/radio fields."""
    return CHECKBOX_FIELDS


# Calibration notes and manual adjustments can be tracked here
CALIBRATION_NOTES = """
CALIBRATION HISTORY:
===================
Version 1.0 - Initial coordinates estimated from grid
  - All coordinates are initial estimates
  - Requires manual calibration

MANUAL ADJUSTMENTS NEEDED:
1. Run step4_fill_form.py with dummy data
2. Open the output PDF and compare with original
3. Adjust x, y values in this file
4. Repeat until perfect alignment

TIPS FOR CALIBRATION:
- Text too high? Increase y value
- Text too low? Decrease y value  
- Text too far left? Increase x value
- Text too far right? Decrease x value
- Text too small/large? Adjust font_size
- Boxed fields misaligned? Adjust x_start and dx
"""
