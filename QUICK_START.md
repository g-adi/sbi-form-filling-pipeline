# 🚀 Quick Start Guide

## What Just Happened?

The pipeline has generated several PDF files for you:

### 📄 Generated Files

1. **`debug_origin.pdf`** - Shows the coordinate system orientation
2. **`SBI_grid_debug.pdf`** - Grid overlay with coordinate rulers (THIS IS YOUR REFERENCE!)
3. **`SBI_filled_form.pdf`** - Initial filled form with estimated coordinates
4. **`calibration_test_single.pdf`** - Test output for single field
5. **`calibration_test_multiple.pdf`** - Test output for multiple fields

## 🎯 Next Steps: Manual Calibration

### Step 1: Compare PDFs

Open these two files side by side:
- `SBI_grid_debug.pdf` (shows coordinates)
- `SBI_filled_form.pdf` (shows where text was placed)

### Step 2: Identify Misaligned Fields

Look at the filled form and note which fields are:
- ❌ Too high or too low
- ❌ Too far left or right
- ❌ Text size is wrong
- ❌ Not aligned with boxes

### Step 3: Read Correct Coordinates

Using `SBI_grid_debug.pdf`:
1. Find the actual position where text should go
2. Read the X coordinate from the top ruler (red numbers)
3. Read the Y coordinate from the left ruler (blue numbers)
4. Note the coordinates

### Step 4: Update `layout_config.py`

Open `layout_config.py` and adjust the coordinates:

```python
# Example: If "full_name" needs to move down and right
"full_name": {
    "page": 0,
    "x": 120,   # Change this if text needs to move left/right
    "y": 150,   # Change this if text needs to move up/down
    "max_width": 350,
    "font_size": 9,  # Change this if text is too big/small
    "type": "text"
}
```

**Calibration Rules:**
- Text too HIGH → **INCREASE** `y` value
- Text too LOW → **DECREASE** `y` value
- Text too LEFT → **INCREASE** `x` value
- Text too RIGHT → **DECREASE** `x` value
- Text too SMALL → **INCREASE** `font_size`
- Text too LARGE → **DECREASE** `font_size`

### Step 5: Test Your Changes

After updating coordinates, re-fill the form:

```bash
python3 step4_fill_form.py
```

This creates a new `SBI_filled_form.pdf`. Open it and check if the adjustments worked.

### Step 6: Repeat Until Perfect

Keep adjusting coordinates in `layout_config.py` and re-running the fill script until all fields are perfectly aligned.

## 🔧 Advanced Calibration

### Test Individual Fields

To test just one or a few fields:

```bash
python3 step5_calibration_helper.py
```

Or use it programmatically:

```python
from step5_calibration_helper import CalibrationHelper

helper = CalibrationHelper("45679523-SBI-Account-Opening-Form-I (1)_removed.pdf")

# Test one field
helper.test_single_field("full_name", "TEST NAME", "test_output.pdf")
```

This will draw:
- Red text at your coordinates
- Blue crosshairs showing exact positions
- Coordinate labels for reference

### For Boxed Fields (PAN, Aadhaar, etc.)

These need special attention:

```python
"pan_number": {
    "x_start": 150,  # Center of FIRST box
    "y": 330,        # Baseline
    "dx": 18,        # Distance between box centers
    ...
}
```

1. Find the center of the first box using the grid
2. Set `x_start` to that coordinate
3. Measure the distance to the next box center
4. Set `dx` to that distance
5. Test and adjust until all characters fit perfectly

### For Checkboxes

```python
"gender": {
    "options": {
        "Male": {"x": 180, "y": 120},  # Center of the checkbox
        ...
    }
}
```

1. Find the center of each checkbox using the grid
2. Set `x` and `y` to the center coordinates
3. The checkmark (✓) will be centered on these coordinates

## 📊 Current Form Fields

The initial config includes these fields:

**Personal Details:**
- full_name, father_name, mother_name
- date_of_birth, mobile_number, email_id

**Address:**
- residential_address_line1, residential_address_line2
- city, state, pincode

**Identification:**
- pan_number (boxed)
- aadhaar_number (boxed)

**Account:**
- branch_name, account_type, account_number (boxed)

**Nominee:**
- nominee_name, nominee_relation

**Selections:**
- gender (checkbox)
- marital_status (checkbox)
- account_type_radio (checkbox)

## 💡 Pro Tips

1. **Start with a few key fields** - Don't try to calibrate everything at once
2. **Use the calibration helper** - It shows crosshairs and makes alignment easier
3. **Document your changes** - Add notes in the `CALIBRATION_NOTES` section
4. **Test edge cases** - Try long names, short names to ensure everything fits
5. **Save working versions** - Commit `layout_config.py` when you have good coordinates

## 🎓 Understanding the Grid

The grid PDF has:
- **Light gray thin lines** every 20 points
- **Darker gray thick lines** every 100 points
- **Red numbers** on top showing X coordinates
- **Blue numbers** on left showing Y coordinates
- **Colored circles** at corners for orientation

Example: If text should start at position where you see "200" on top and "300" on left, use:
```python
"x": 200,
"y": 300,
```

## 🔄 Workflow Summary

```
1. Open SBI_grid_debug.pdf → Read coordinates
                ↓
2. Update layout_config.py → Adjust values
                ↓
3. Run: python3 step4_fill_form.py → Generate new filled PDF
                ↓
4. Open SBI_filled_form.pdf → Check alignment
                ↓
5. Repeat 2-4 until perfect ✓
```

## ❓ Need Help?

- **Text not visible?** Check if coordinates are within page bounds (0-666 for X, 0-864 for Y)
- **Text overlapping?** Adjust `y` spacing between fields
- **Text cut off?** Check `max_width` or reduce `font_size`
- **Checkmarks misplaced?** Try different characters: ✓ ✔ X ☑

## 🎉 Once Calibrated

After you have perfect coordinates:
1. Your `layout_config.py` is your **permanent reference**
2. You can fill forms automatically using `step4_fill_form.py`
3. Change the data in `dummy_data.py` or pass custom data
4. Never need to calibrate again (unless PDF template changes)

---

**Happy Calibrating! 🎯**
