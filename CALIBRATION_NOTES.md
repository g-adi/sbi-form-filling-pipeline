# Field Calibration Notes

## Recently Added Boxed Fields (Need Calibration)

### Personal Details Section:
1. **`father_name`** (Name of Father/Husband)
   - Current: `x_start: 200, y: 270, dx: 15`
   - Max chars: 40 boxes
   - Line 186-194 in layout_config.py

2. **`date_of_birth`** (Date of Birth)
   - Current: `x_start: 200, y: 295, dx: 15`
   - Max chars: 10 boxes (for DD/MM/YYYY)
   - Line 195-203 in layout_config.py

3. **`mother_name`** (Mother's maiden name)
   - Current: `x_start: 200, y: 345, dx: 15`
   - Max chars: 40 boxes
   - Line 204-212 in layout_config.py

### Checkboxes Updated:

4. **`gender`** (Sex)
   - Male: `x: 650, y: 295`
   - Female: `x: 780, y: 295`
   - Line 218-225 in layout_config.py

5. **`marital_status`** (Marital Status)
   - Married: `x: 245, y: 320`
   - Unmarried: `x: 410, y: 320`
   - Others: `x: 620, y: 320`
   - Line 226-234 in layout_config.py

## All Boxed Fields Summary

Now the form has **11 boxed fields** total:

1. ✅ `full_name` - Calibrated (x_start: 153, y: 252, dx: 15)
2. 🔧 `father_name` - Needs calibration
3. 🔧 `date_of_birth` - Needs calibration
4. 🔧 `mother_name` - Needs calibration
5. ⚠️ `pan_number` - Old estimate (x_start: 150, y: 330, dx: 18)
6. ⚠️ `aadhaar_number` - Old estimate (x_start: 150, y: 550, dx: 18)
7. ⚠️ `account_number` - Old estimate (x_start: 150, y: 650, dx: 18)
8. ✅ `branch` - Calibrated (x_start: 133, y: 131, dx: 15)
9. ✅ `code_no` - Calibrated (x_start: 528, y: 131, dx: 15)
10. ✅ `date` - Calibrated (x_start: 154, y: 154, dx: 15)
11. ✅ `cif_no` - Calibrated (x_start: 353, y: 154, dx: 15)

## Calibration Workflow

### For Boxed Fields:
1. Open `SBI_grid_debug.pdf` to see coordinate grid
2. Find the field on the form
3. Measure:
   - **x_start**: Center of the **first box**
   - **y**: Text baseline (same for all boxes in the row)
   - **dx**: Distance between centers of adjacent boxes
4. Update values in `layout_config.py`
5. Run: `python3 step4_fill_form.py`
6. Check `SBI_filled_form.pdf`
7. Repeat until perfect

### For Checkboxes:
1. Open `SBI_grid_debug.pdf`
2. Find each checkbox on the form
3. Measure the **center** of each checkbox box:
   - **x**: Horizontal center
   - **y**: Vertical center
4. Update values in `layout_config.py`
5. Run: `python3 step4_fill_form.py`
6. Check if ✓ appears centered in the box
7. Adjust and repeat if needed

## Quick Adjustment Guide

### If character is:
- **Too far left** → INCREASE `x_start`
- **Too far right** → DECREASE `x_start`
- **Too high** → INCREASE `y`
- **Too low** → DECREASE `y`
- **Too close together** → INCREASE `dx`
- **Too far apart** → DECREASE `dx`
- **Too small** → INCREASE `font_size`
- **Too large** → DECREASE `font_size`

### If checkbox ✓ is:
- **Left of box** → INCREASE `x`
- **Right of box** → DECREASE `x`
- **Above box** → INCREASE `y`
- **Below box** → DECREASE `y`

## Testing Tips

1. Use the calibration helper for specific fields:
   ```bash
   python3 step5_calibration_helper.py
   ```

2. Test with different data lengths to ensure all boxes are used

3. Keep the grid PDF open while calibrating for quick reference

4. Calibrate one section at a time (e.g., all personal details, then all checkboxes)

5. Document any special adjustments here for future reference
