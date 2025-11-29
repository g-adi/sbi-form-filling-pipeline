# SBI Account Opening Form - Automated PDF Filling Pipeline

This pipeline provides pixel-perfect coordinate-based PDF form filling for the SBI Account Opening Form.

## 📋 Overview

The pipeline uses a coordinate-based approach where each form field's exact position is manually calibrated once and then used repeatedly for accurate form filling.

## 🏗️ Project Structure

```
Form filling pipeline 1/
├── 45679523-SBI-Account-Opening-Form-I (1)_removed.pdf  # Original blank form
├── step1_inspect_pdf.py                  # Inspect PDF dimensions & coordinate system
├── step2_generate_grid.py                # Generate grid overlay for coordinate reading
├── step3_fill_form.py                    # Main form filling script
├── step4_calibration_helper.py           # Helper for fine-tuning coordinates
├── layout_config.py                      # Coordinate mappings (SINGLE SOURCE OF TRUTH)
├── dummy_data.py                         # Test data generator
└── README.md                             # This file
```

## 🚀 Quick Start

### Prerequisites

```bash
pip install PyMuPDF  # For PDF manipulation
```

### Step-by-Step Usage

#### **Step 1: Inspect the PDF**

Understand the page dimensions and coordinate system:

```bash
python step1_inspect_pdf.py
```

This creates `debug_origin.pdf` showing:
- Page dimensions
- Coordinate system orientation (Y-axis direction)
- Corner markers for reference

#### **Step 2: Generate Grid Debug PDF**

Create a PDF with coordinate grid overlay:

```bash
python step2_generate_grid.py
```

This creates `SBI_grid_debug.pdf` with:
- 20-point grid spacing
- Coordinate labels every 100 points
- Light gray grid lines

**Use this file to read coordinates visually!**

#### **Step 3: Initial Form Filling**

Fill the form with dummy data using current coordinates:

```bash
python step4_fill_form.py
```

This creates `SBI_filled_form.pdf` using coordinates from `layout_config.py`.

#### **Step 4: Calibrate Coordinates**

Compare the filled form with the original and adjust coordinates:

```bash
# Test individual fields
python step5_calibration_helper.py
```

This creates test PDFs with:
- Red text at specified coordinates
- Blue crosshairs marking exact positions
- Coordinate labels for reference

**Calibration Guide:**
- Text too HIGH → INCREASE `y` value
- Text too LOW → DECREASE `y` value
- Text too LEFT → INCREASE `x` value
- Text too RIGHT → DECREASE `x` value
- Text too SMALL → INCREASE `font_size`
- Text too LARGE → DECREASE `font_size`

#### **Step 5: Update and Re-test**

1. Open `layout_config.py`
2. Adjust coordinates for misaligned fields
3. Re-run `python step4_fill_form.py`
4. Repeat until perfect alignment

## 📝 Configuration Files

### `layout_config.py`

The **single source of truth** for all field coordinates. Contains three types of fields:

1. **Text Fields** (`FORM_LAYOUT`)
   - Standard text input fields
   - Each has: `page`, `x`, `y`, `max_width`, `font_size`

2. **Boxed Fields** (`BOXED_FIELDS`)
   - Fields with one character per box (PAN, Aadhaar, etc.)
   - Each has: `page`, `x_start`, `y`, `dx` (box spacing), `max_chars`

3. **Checkbox Fields** (`CHECKBOX_FIELDS`)
   - Radio buttons and checkboxes
   - Each option has: `x`, `y` (center coordinates)

### `dummy_data.py`

Generates realistic test data for all form fields:
- Personal details
- Address information
- ID numbers (PAN, Aadhaar)
- Account details
- Nominee information

## 🎯 Coordinate System

```
(0,0) -------- X increases ------->
  |
  |
  Y increases
  |
  ↓
```

- **Origin:** Top-left corner
- **X-axis:** Increases to the right
- **Y-axis:** Increases downward
- **Units:** PDF points (1/72 inch)

## 📐 Field Types

### 1. Standard Text Fields

```python
"full_name": {
    "page": 0,
    "x": 120,      # Left edge of text
    "y": 150,      # Text baseline
    "max_width": 350,
    "font_size": 9,
    "type": "text"
}
```

### 2. Boxed Fields (One Char Per Box)

```python
"pan_number": {
    "page": 0,
    "x_start": 150,  # Center of first box
    "y": 330,        # Text baseline
    "dx": 18,        # Distance between box centers
    "font_size": 10,
    "max_chars": 10,
    "type": "boxed"
}
```

### 3. Checkboxes/Radio Buttons

```python
"gender": {
    "page": 0,
    "type": "checkbox",
    "options": {
        "Male": {"x": 180, "y": 120},      # Center of checkbox
        "Female": {"x": 240, "y": 120},
        "Other": {"x": 310, "y": 120},
    }
}
```

## 🔧 Advanced Usage

### Testing Specific Fields

```python
from step5_calibration_helper import CalibrationHelper

helper = CalibrationHelper("45679523-SBI-Account-Opening-Form-I (1)_removed.pdf")

# Test one field
helper.test_single_field(
    field_name="full_name",
    test_value="TEST NAME",
    output_pdf="test_name.pdf"
)

# Test multiple fields
helper.test_multiple_fields([
    ("full_name", "RAJESH SHARMA"),
    ("pan_number", "ABCDE1234F"),
], output_pdf="test_multiple.pdf")
```

### Custom Data

```python
from step4_fill_form import PDFFormFiller

custom_data = {
    "full_name": "YOUR NAME HERE",
    "father_name": "FATHER NAME",
    # ... more fields
}

filler = PDFFormFiller(
    "45679523-SBI-Account-Opening-Form-I (1)_removed.pdf",
    "output.pdf"
)
filler.fill_and_save(custom_data)
```

## 📊 Workflow Diagram

```
┌─────────────────────┐
│  1. Inspect PDF     │
│  (dimensions, axes) │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  2. Generate Grid   │
│  (coordinate ruler) │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  3. Read Coords     │
│  (from grid PDF)    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  4. Update Config   │
│  (layout_config.py) │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  5. Test Fill       │
│  (with dummy data)  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  6. Calibrate       │
│  (adjust coords)    │
└──────────┬──────────┘
           │
           ▼
        Perfect! ✓
```

## 🎓 Tips & Best Practices

1. **Use the Grid:** Always reference `SBI_grid_debug.pdf` for initial coordinate guessing
2. **Start with Key Fields:** Calibrate important fields first (name, PAN, etc.)
3. **Test Incrementally:** Don't calibrate all fields at once
4. **Use Crosshairs:** The calibration helper's crosshairs show exact coordinate positions
5. **Document Changes:** Add notes to `CALIBRATION_NOTES` in `layout_config.py`
6. **Version Control:** Commit `layout_config.py` after successful calibration

## 🐛 Troubleshooting

### Text Not Visible
- Check if coordinates are within page bounds
- Verify font size isn't too small
- Ensure text color is not white

### Text Overflowing Boxes
- Reduce `font_size`
- Check `max_width` setting
- For boxed fields, adjust `dx` (box spacing)

### Checkmarks Misaligned
- Boxed fields need `x_start` at the CENTER of the first box
- Adjust `x` and `y` to center of checkbox
- Try different checkbox characters: ✓ ✔ X ☑

### Wrong Coordinate System
- Check `debug_origin.pdf` to verify Y-axis direction
- If Y increases upward, adjust formulas in fill scripts

## 📦 Output Files

- `debug_origin.pdf` - Coordinate system test
- `SBI_grid_debug.pdf` - Grid overlay for reading coordinates
- `SBI_filled_form.pdf` - Final filled form
- `calibration_test_*.pdf` - Calibration test outputs

## 🔒 Security Note

This pipeline is designed for **fixed template PDFs**. Coordinates are hardcoded and will not work with different form versions. Any changes to the PDF template require recalibration.

## 📄 License

For internal use only.

## 👤 Author

Created for SBI Account Opening Form automation project.

---

**Need help?** Check the generated PDFs at each step to understand what's happening!
