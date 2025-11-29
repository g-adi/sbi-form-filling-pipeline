# Address Fields - Boxed Fields Summary

## ✅ Successfully Added 19 New Boxed Address Fields

All address fields in sections (B) Residential Address and (C) Office/Business Address are now configured as boxed fields where each character goes in a separate box.

---

## 📋 Section (B): Residential Address - 11 Fields

### 1. **residential_address_line1** (Address Line 1)
- Line: 158-166 in layout_config.py
- Current: `x_start: 265, y: 370, dx: 15`
- Max chars: 50 boxes

### 2. **residential_address_line2** (Address Line 2)
- Line: 167-175 in layout_config.py
- Current: `x_start: 265, y: 395, dx: 15`
- Max chars: 50 boxes

### 3. **residential_address_line3** (Address Line 3)
- Line: 176-184 in layout_config.py
- Current: `x_start: 265, y: 420, dx: 15`
- Max chars: 50 boxes

### 4. **residential_landmark** (Landmark)
- Line: 185-193 in layout_config.py
- Current: `x_start: 200, y: 445, dx: 15`
- Max chars: 50 boxes

### 5. **city** (City)
- Line: 194-202 in layout_config.py
- Current: `x_start: 130, y: 470, dx: 15`
- Max chars: 30 boxes

### 6. **pincode** (PIN Code)
- Line: 203-211 in layout_config.py
- Current: `x_start: 660, y: 470, dx: 15`
- Max chars: 10 boxes (for 6-digit PIN)

### 7. **state** (State)
- Line: 212-220 in layout_config.py
- Current: `x_start: 130, y: 495, dx: 15`
- Max chars: 40 boxes

### 8. **phone_no** (Phone No. with STD Code)
- Line: 221-229 in layout_config.py
- Current: `x_start: 180, y: 520, dx: 15`
- Max chars: 20 boxes

### 9. **mobile_number** (Mobile No.)
- Line: 230-238 in layout_config.py
- Current: `x_start: 540, y: 520, dx: 15`
- Max chars: 15 boxes (for 10-digit mobile)

### 10. **email_id_1** (E-mail ID - Line 1)
- Line: 239-247 in layout_config.py
- Current: `x_start: 150, y: 545, dx: 15`
- Max chars: 50 boxes

### 11. **email_id_2** (E-mail ID - Line 2)
- Line: 248-256 in layout_config.py
- Current: `x_start: 150, y: 570, dx: 15`
- Max chars: 50 boxes

---

## 📋 Section (C): Office/Business Address - 9 Fields

### 12. **office_address_line1** (Address Line 1)
- Line: 259-267 in layout_config.py
- Current: `x_start: 265, y: 610, dx: 15`
- Max chars: 50 boxes

### 13. **office_address_line2** (Address Line 2)
- Line: 268-276 in layout_config.py
- Current: `x_start: 265, y: 635, dx: 15`
- Max chars: 50 boxes

### 14. **office_address_line3** (Address Line 3)
- Line: 277-285 in layout_config.py
- Current: `x_start: 265, y: 660, dx: 15`
- Max chars: 50 boxes

### 15. **office_landmark** (Landmark)
- Line: 286-294 in layout_config.py
- Current: `x_start: 200, y: 685, dx: 15`
- Max chars: 50 boxes

### 16. **office_city** (City)
- Line: 295-303 in layout_config.py
- Current: `x_start: 160, y: 710, dx: 15`
- Max chars: 40 boxes

### 17. **office_state** (State)
- Line: 304-312 in layout_config.py
- Current: `x_start: 160, y: 735, dx: 15`
- Max chars: 40 boxes

### 18. **office_pincode** (PIN Code)
- Line: 313-321 in layout_config.py
- Current: `x_start: 200, y: 760, dx: 15`
- Max chars: 10 boxes

### 19. **office_phone_no** (Phone No.)
- Line: 322-330 in layout_config.py
- Current: `x_start: 250, y: 785, dx: 15`
- Max chars: 20 boxes

### 20. **office_fax_no** (Fax No.)
- Line: 331-339 in layout_config.py
- Current: `x_start: 250, y: 810, dx: 15`
- Max chars: 20 boxes

---

## 📊 Current Total Field Count

| Field Type | Count |
|------------|-------|
| **Boxed Fields** | **31** (11 personal + 11 residential + 9 office address fields) |
| Text Fields | 3 (account_type, nominee_name, nominee_relation) |
| Checkbox Groups | 4 (gender, marital_status, account_type_radio, customer_type) |
| **TOTAL** | **38 fields** |

---

## 🎯 Calibration Priority

### High Priority (Visible on Form Image):
1. ✅ All 3 residential address lines (line1, line2, line3)
2. ✅ Residential landmark
3. ✅ City, State, PIN Code
4. ✅ Phone No., Mobile No.
5. ✅ E-mail ID (both lines)

### Medium Priority:
6. ✅ All 9 office address fields (line1, line2, line3, landmark, city, state, pincode, phone, fax)

---

## 🔧 Calibration Instructions

### Step-by-Step Process:

1. **Open Reference Grid**
   ```bash
   # Open these files side by side
   - SBI_grid_debug.pdf (coordinate reference)
   - SBI_filled_form.pdf (current output)
   ```

2. **For Each Field:**
   - Locate the field on the form
   - Find the first box in the row
   - Read coordinates from grid:
     - **x_start**: Center of first box (horizontal)
     - **y**: Text baseline (vertical)
     - **dx**: Distance between box centers

3. **Update layout_config.py**
   - Find the field (use line numbers above)
   - Update x_start, y, and dx values
   - Save file

4. **Test Changes**
   ```bash
   python3 step4_fill_form.py
   ```

5. **Verify Output**
   - Open SBI_filled_form.pdf
   - Check if characters fit in boxes
   - Repeat until perfect

---

## 📝 Dummy Data Provided

### Residential Address (B):
```
Address Line 1: FLAT NO 301 TOWER B GREENFIELD APARTMENTS
Address Line 2: NEAR CITY MALL SECTOR 18
Address Line 3: NOIDA SECTOR 62
Landmark: NEAR CITY CENTRE METRO STATION
City: NOIDA
State: UTTAR PRADESH
PIN Code: 201301
Phone No.: 01204567890
Mobile No.: 9876543210
E-mail ID (Line 1): rajesh.sharma@email.com
E-mail ID (Line 2): rajesh.kumar.sharma@company.co.in
```

### Office Address (C):
```
Address Line 1: ABC SOLUTIONS PVT LTD 5TH FLOOR
Address Line 2: TOWER A CORPORATE PARK
Address Line 3: GOLF COURSE ROAD
Landmark: NEAR CYBER HUB
City: GURGAON
State: HARYANA
PIN Code: 122002
Phone No.: 01244567890
Fax No.: 01244567891
```

---

## ⚠️ Common Calibration Issues

| Issue | Solution |
|-------|----------|
| Characters overlap | Increase `dx` value |
| Characters too far apart | Decrease `dx` value |
| Text doesn't start at first box | Adjust `x_start` |
| Text too high/low | Adjust `y` value |
| Characters cut off at end | Check `max_chars` count |

---

## 💡 Pro Tips

1. **Use same dx for fields on same line**: If City and PIN Code are on the same row, they likely use the same `dx` value

2. **Address lines usually aligned**: All 3 address lines typically start at the same x_start

3. **Email fields need more boxes**: Email addresses are usually longer, ensure max_chars is sufficient (50 recommended)

4. **Phone vs Mobile**: Phone number includes STD code, so it needs more boxes than mobile

5. **Test with long data**: Use the longest possible values to ensure all boxes are properly positioned

---

## 🎉 Next Steps

1. Open `SBI_filled_form.pdf` to see current output
2. Compare with `SBI_grid_debug.pdf` to read coordinates
3. Start calibrating from top to bottom (residential address first)
4. Update coordinates in `layout_config.py`
5. Re-run form filler and verify
6. Repeat until all fields are perfectly aligned!

Good luck with calibration! 🎯
