# Section (D): Income Tax & Nationality Fields

## ✅ Successfully Added 3 New Fields

Added 2 boxed fields and 1 checkbox field for Section D (Income Tax & Nationality) and correspondence address preference.

---

## 📋 New Fields Added

### Boxed Fields (2):

#### 1. **income_tax_pan_form** (Income Tax PAN or Form 60/61)
- Line: 342-350 in layout_config.py
- Current: `x_start: 600, y: 850, dx: 15`
- Max chars: 20 boxes
- Dummy data: `ABCDE1234F`
- Purpose: Income Tax PAN number or Form 60/61 reference as per IT Act

#### 2. **nationality** (Nationality)
- Line: 351-359 in layout_config.py
- Current: `x_start: 600, y: 875, dx: 15`
- Max chars: 20 boxes
- Dummy data: `INDIAN`
- Purpose: Applicant's nationality

### Checkbox Field (1):

#### 3. **correspondence_address** (Address on which correspondence is required)
- Line: 399-406 in layout_config.py
- Type: Checkbox
- Options:
  - **B** (Residential Address) - `x: 680, y: 825`
  - **C** (Office/Business Address) - `x: 820, y: 825`
- Dummy data: `B` (Residential address selected)
- Purpose: Select where correspondence should be sent

---

## 📊 Updated Total Field Count

| Field Type | Count |
|------------|-------|
| **Boxed Fields** | **33** (31 previously + 2 new from Section D) |
| Text Fields | 3 |
| **Checkbox Groups** | **5** (4 previously + 1 correspondence address) |
| **TOTAL** | **41 fields** |

---

## 📝 Field Details from Image

### From the Form Image:

1. **Income Tax PAN or Form 60/61** appears as a row of boxes after the correspondence address checkbox
2. **Nationality** appears as a second row of boxes below the Income Tax field
3. **Correspondence Address** has two checkboxes labeled:
   - ख / B (Residential Address - Section B)
   - ग / C (Office Address - Section C)

---

## 🎯 Field Layout

```
पत्राचार का पता / Address on which correspondence is required:
    [  ] ख / B    [  ] ग / C

(घ)  i)  आयकर पैन या फार्म 60 / 61 (आयकर अधिनियम) /
(D)      Income Tax PAN or Form 60/61 (IT Act)
         [_][_][_][_][_][_][_][_][_][_][_][_][_][_][_][_][_][_][_][_]

     ii) राष्ट्रीयता / Nationality
         [_][_][_][_][_][_][_][_][_][_][_][_][_][_][_][_][_][_][_][_]
```

---

## 📝 Dummy Data Provided

```
Income Tax PAN or Form 60/61: ABCDE1234F
Nationality: INDIAN
Correspondence Address: B (Residential)
```

### Notes on Data:
- **Income Tax PAN**: Can be a 10-character PAN number (e.g., ABCDE1234F) or Form 60/61 reference
- **Nationality**: Full nationality name in capital letters (e.g., INDIAN, AMERICAN, BRITISH)
- **Correspondence Address**: Either "B" for residential or "C" for office address

---

## 🔧 Calibration Required

All 3 new fields have **initial estimated coordinates** that need calibration:

### Boxed Fields:

1. **income_tax_pan_form** (line 342-350)
   - Current: `x_start: 600, y: 850, dx: 15`
   - Find first box center on the form
   - Measure spacing between boxes

2. **nationality** (line 351-359)
   - Current: `x_start: 600, y: 875, dx: 15`
   - Likely same x_start as income_tax_pan_form (aligned)
   - Verify y-coordinate spacing

### Checkbox Field:

3. **correspondence_address** (line 399-406)
   - Option B: `x: 680, y: 825`
   - Option C: `x: 820, y: 825`
   - Find center of each checkbox
   - Both should have same y-coordinate (on same line)

---

## 💡 Calibration Tips

### From Image Analysis:

1. **Income Tax and Nationality boxes appear aligned**
   - Both fields likely start at same `x_start`
   - Vertical spacing between them (estimate: 25 points)

2. **Correspondence address checkboxes**
   - Appear ABOVE the Income Tax field
   - Two checkboxes on same horizontal line
   - Moderate spacing between B and C options

3. **Box characteristics**
   - Standard size boxes consistent with other fields
   - Full-width row for both fields

### Calibration Steps:

1. Open `SBI_grid_debug.pdf` for coordinate reference
2. Open `SBI_filled_form.pdf` to see current output
3. Locate Section D on the form
4. For each field:
   - **Boxed fields**: Measure `x_start`, `y`, and `dx`
   - **Checkboxes**: Measure center `x` and `y` for each option
5. Update `layout_config.py`
6. Re-run: `python3 step4_fill_form.py`
7. Verify alignment and repeat if needed

---

## 🔄 Relationship with Other Fields

### Correspondence Address Logic:
- Option **B** refers to Section (B) - Residential Address
  - Includes: 11 fields (address lines, landmark, city, state, PIN, phone, mobile, email)
- Option **C** refers to Section (C) - Office/Business Address
  - Includes: 9 fields (address lines, landmark, city, state, PIN, phone, fax)

### Data Flow:
When user selects:
- **B**: Correspondence should be sent to residential address
- **C**: Correspondence should be sent to office address

---

## 📊 Complete Section D Summary

| # | Field Name | Type | Max Chars | Purpose |
|---|------------|------|-----------|---------|
| 1 | correspondence_address | Checkbox | N/A | Select B or C for correspondence |
| 2 | income_tax_pan_form | Boxed | 20 | Income Tax PAN or Form 60/61 |
| 3 | nationality | Boxed | 20 | Applicant's nationality |

---

## 🎉 Status

✅ All Section D fields configured  
✅ Dummy data added and tested  
✅ Form filling script updated  
⚠️ **Calibration required** - Use grid PDF to get exact coordinates

### Output Verification:
```
✓ Filled boxed 'income_tax_pan_form': ABCDE1234F starting at (600, 850)
✓ Filled boxed 'nationality': INDIAN starting at (600, 875)
✓ Checked 'correspondence_address': B at (680, 825)
```

**Next Step:** Open the filled PDF, compare with grid, and calibrate the coordinates for perfect alignment! 🎯
