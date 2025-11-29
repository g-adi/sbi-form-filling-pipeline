# Complete SBI Account Opening Form - Field Summary

## 📊 Complete Field Inventory

**Total Fields: 43**
- Boxed Fields: 33 (each character in separate box)
- Image Fields: 2 (photograph and signature)
- Text Fields: 3 (regular text)
- Checkbox Groups: 5 (with 12 total checkbox options)

---

## 🗂️ Fields Organized by Section

### Section A: Form Header Information (5 fields)

| Field | Type | Max Chars | Line in Config |
|-------|------|-----------|----------------|
| branch | Boxed | 30 | 174-182 |
| code_no | Boxed | 10 | 183-191 |
| date | Boxed | 10 | 192-200 |
| cif_no | Boxed | 20 | 201-209 |
| customer_type | Checkbox (Public/Staff) | - | 391-398 |

---

### Personal Details (4 fields)

| Field | Type | Max Chars | Line in Config |
|-------|------|-----------|----------------|
| full_name | Boxed | 30 | 57-65 |
| father_name | Boxed | 40 | 129-137 |
| date_of_birth | Boxed | 10 | 138-146 |
| mother_name | Boxed | 40 | 147-155 |

**Checkboxes:**
- gender (Male/Female) - Lines 365-372
- marital_status (Married/Unmarried/Others) - Lines 373-380

---

### Section B: Residential Address (11 fields)

| Field | Type | Max Chars | Line in Config |
|-------|------|-----------|----------------|
| residential_address_line1 | Boxed | 50 | 158-166 |
| residential_address_line2 | Boxed | 50 | 167-175 |
| residential_address_line3 | Boxed | 50 | 176-184 |
| residential_landmark | Boxed | 50 | 185-193 |
| city | Boxed | 30 | 194-202 |
| pincode | Boxed | 10 | 203-211 |
| state | Boxed | 40 | 212-220 |
| phone_no | Boxed | 20 | 221-229 |
| mobile_number | Boxed | 15 | 230-238 |
| email_id_1 | Boxed | 50 | 239-247 |
| email_id_2 | Boxed | 50 | 248-256 |

---

### Section C: Office/Business Address (9 fields)

| Field | Type | Max Chars | Line in Config |
|-------|------|-----------|----------------|
| office_address_line1 | Boxed | 50 | 259-267 |
| office_address_line2 | Boxed | 50 | 268-276 |
| office_address_line3 | Boxed | 50 | 277-285 |
| office_landmark | Boxed | 50 | 286-294 |
| office_city | Boxed | 40 | 295-303 |
| office_state | Boxed | 40 | 304-312 |
| office_pincode | Boxed | 10 | 313-321 |
| office_phone_no | Boxed | 20 | 322-330 |
| office_fax_no | Boxed | 20 | 331-339 |

**Checkbox:**
- correspondence_address (B/C) - Lines 399-406

---

### Section D: Income Tax & Nationality (2 fields)

| Field | Type | Max Chars | Line in Config |
|-------|------|-----------|----------------|
| income_tax_pan_form | Boxed | 20 | 342-350 |
| nationality | Boxed | 20 | 351-359 |

---

### Account & Identification (4 fields)

| Field | Type | Max Chars | Line in Config |
|-------|------|-----------|----------------|
| pan_number | Boxed | 10 | 66-74 |
| aadhaar_number | Boxed | 12 | 75-83 |
| account_number | Boxed | 15 | 84-92 |
| account_type | Text | - | 28-35 |

**Checkbox:**
- account_type_radio (Savings/Current/Recurring) - Lines 381-388

---

### Nominee Details (2 fields - Text)

| Field | Type | Max Chars | Line in Config |
|-------|------|-----------|----------------|
| nominee_name | Text | 300 | 36-43 |
| nominee_relation | Text | 150 | 44-51 |

---

### Image Fields (2 fields)

| Field | Type | Size | Line in Config |
|-------|------|------|----------------|
| photograph | Image | 80×100 pts (2.5×3.5 cm) | 365-373 |
| signature | Image | 400×120 pts | 374-382 |

**Note:** Image fields require actual image file paths. See `IMAGE_FIELDS_GUIDE.md` for details.

---

## 📋 Complete Checkbox Summary

| Checkbox Group | Options | Line in Config |
|----------------|---------|----------------|
| customer_type | Public, Staff | 391-398 |
| gender | Male, Female | 365-372 |
| marital_status | Married, Unmarried, Others | 373-380 |
| account_type_radio | Savings, Current, Recurring | 381-388 |
| correspondence_address | B (Residential), C (Office) | 399-406 |

---

## 🎨 Boxed Fields by Category

### Header & Form Info (4):
- branch, code_no, date, cif_no

### Personal Details (4):
- full_name, father_name, date_of_birth, mother_name

### Residential Address (11):
- 3 address lines, landmark, city, state, pincode, phone, mobile, 2 email lines

### Office Address (9):
- 3 address lines, landmark, city, state, pincode, phone, fax

### Tax & ID (4):
- pan_number, aadhaar_number, income_tax_pan_form, nationality

### Account (1):
- account_number

**Total Boxed: 33 fields**

---

## 📝 Sample Dummy Data

```python
{
    # Form Header
    "branch": "CONNAUGHT PLACE DELHI",
    "code_no": "12345",
    "date": "3011 2025",
    "cif_no": "12345678901",
    
    # Personal
    "full_name": "RAJESH KUMAR SHARMA",
    "father_name": "SURESH KUMAR SHARMA",
    "mother_name": "SUNITA DEVI SHARMA",
    "date_of_birth": "15/08/1990",
    
    # Residential Address (B)
    "residential_address_line1": "FLAT NO 301 TOWER B GREENFIELD APARTMENTS",
    "residential_address_line2": "NEAR CITY MALL SECTOR 18",
    "residential_address_line3": "NOIDA SECTOR 62",
    "residential_landmark": "NEAR CITY CENTRE METRO STATION",
    "city": "NOIDA",
    "state": "UTTAR PRADESH",
    "pincode": "201301",
    "phone_no": "01204567890",
    "mobile_number": "9876543210",
    "email_id_1": "rajesh.sharma@email.com",
    "email_id_2": "rajesh.kumar.sharma@company.co.in",
    
    # Office Address (C)
    "office_address_line1": "ABC SOLUTIONS PVT LTD 5TH FLOOR",
    "office_address_line2": "TOWER A CORPORATE PARK",
    "office_address_line3": "GOLF COURSE ROAD",
    "office_landmark": "NEAR CYBER HUB",
    "office_city": "GURGAON",
    "office_state": "HARYANA",
    "office_pincode": "122002",
    "office_phone_no": "01244567890",
    "office_fax_no": "01244567891",
    
    # Tax & Nationality (D)
    "income_tax_pan_form": "ABCDE1234F",
    "nationality": "INDIAN",
    
    # ID & Account
    "pan_number": "ABCDE1234F",
    "aadhaar_number": "123456789012",
    "account_number": "123456789012345",
    "account_type": "SAVINGS ACCOUNT",
    
    # Nominee
    "nominee_name": "PRIYA SHARMA",
    "nominee_relation": "WIFE",
    
    # Images
    "photograph": None,  # Path to photograph image (2.5×3.5 cm)
    "signature": None,   # Path to signature image
    
    # Checkboxes
    "customer_type": "Public",
    "gender": "Male",
    "marital_status": "Married",
    "account_type_radio": "Savings",
    "correspondence_address": "B"
}
```

---

## 🎯 Calibration Status

### ✅ Calibrated Fields:
- full_name (x_start: 153, y: 252, dx: 15)
- branch (x_start: 133, y: 131, dx: 15)
- code_no (x_start: 528, y: 131, dx: 15)
- date (x_start: 154, y: 154, dx: 15)
- cif_no (x_start: 353, y: 154, dx: 15)

### ⚠️ Need Calibration:
- **28 boxed fields** - All other boxed fields have initial estimated coordinates
- **2 image fields** - photograph and signature need position/size calibration

All require manual calibration using the grid PDF.

---

## 📐 Common Coordinate Patterns

Based on calibrated fields:
- **Standard dx**: Most fields use 15-18 points spacing
- **Vertical spacing**: ~25 points between rows
- **Alignment**: Fields in same section often share x_start values

---

## 🔧 Files Reference

| File | Purpose |
|------|---------|
| layout_config.py | All field coordinates (SOURCE OF TRUTH) |
| dummy_data.py | Test data for all fields |
| step4_fill_form.py | Main form filling script |
| step5_calibration_helper.py | Tool for testing specific fields |
| SBI_grid_debug.pdf | Coordinate reference grid |
| SBI_filled_form.pdf | Output with current coordinates |

---

## 📚 Documentation Files

| File | Content |
|------|---------|
| README.md | Complete pipeline documentation |
| QUICK_START.md | Step-by-step calibration guide |
| CALIBRATION_NOTES.md | Field-by-field calibration history |
| ADDRESS_FIELDS_SUMMARY.md | All address fields (Sections B & C) |
| OFFICE_CONTACT_FIELDS.md | Office contact fields details |
| SECTION_D_FIELDS.md | Tax & nationality fields |
| IMAGE_FIELDS_GUIDE.md | Photograph & signature image fields guide |
| COMPLETE_FORM_SUMMARY.md | This file - complete overview |

---

## 🚀 Quick Commands

```bash
# Generate all PDFs
python3 step1_inspect_pdf.py          # Check PDF structure
python3 step2_generate_grid.py        # Generate coordinate grid
python3 step4_fill_form.py            # Fill form with dummy data
python3 step5_calibration_helper.py   # Test specific fields

# Or use interactive menu
python3 run_pipeline.py
```

---

## 🎉 Project Status

✅ **43 total fields configured** (including 2 image fields)
✅ **All field types supported** (boxed, text, image, checkbox)
✅ **Dummy data created** for all fields
✅ **Form filling working** - generates output PDF
✅ **Image insertion supported** - automatic image placement
✅ **Documentation complete**

⚠️ **Next Steps:** 
- Calibrate remaining 28 boxed fields using grid PDF
- Calibrate 2 image field positions (photograph & signature)
- Provide actual image files for photograph and signature

---

## 💡 Tips for Efficient Calibration

1. **Calibrate by section**: Do all residential address fields together
2. **Use patterns**: Fields in same section often have similar dx values
3. **Vertical alignment**: Check y-coordinates for rows
4. **Test incrementally**: Calibrate 3-5 fields, test, repeat
5. **Document as you go**: Note any special adjustments

---

**Form filling pipeline is complete and ready for calibration!** 🎯
