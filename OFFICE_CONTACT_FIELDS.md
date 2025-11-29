# Office/Business Address Contact Fields (Section C)

## ✅ Successfully Added 5 New Boxed Fields

All contact fields for Section (C) Office/Business Address are now configured as boxed fields where each character goes in a separate box.

---

## 📋 Section (C): Office Contact Fields - 5 New Fields

### 1. **office_city** (City)
- Line: 295-303 in layout_config.py
- Current: `x_start: 160, y: 710, dx: 15`
- Max chars: 40 boxes
- Dummy data: `GURGAON`

### 2. **office_state** (State)
- Line: 304-312 in layout_config.py
- Current: `x_start: 160, y: 735, dx: 15`
- Max chars: 40 boxes
- Dummy data: `HARYANA`

### 3. **office_pincode** (PIN Code)
- Line: 313-321 in layout_config.py
- Current: `x_start: 200, y: 760, dx: 15`
- Max chars: 10 boxes (for 6-digit PIN)
- Dummy data: `122002`

### 4. **office_phone_no** (Phone No. with STD Code)
- Line: 322-330 in layout_config.py
- Current: `x_start: 250, y: 785, dx: 15`
- Max chars: 20 boxes
- Dummy data: `01244567890`

### 5. **office_fax_no** (Fax No.)
- Line: 331-339 in layout_config.py
- Current: `x_start: 250, y: 810, dx: 15`
- Max chars: 20 boxes
- Dummy data: `01244567891`

---

## 📊 Complete Office/Business Address Section (C)

Now Section C has **9 boxed fields total**:

| # | Field Name | Type | Max Chars |
|---|------------|------|-----------|
| 1 | office_address_line1 | Address | 50 |
| 2 | office_address_line2 | Address | 50 |
| 3 | office_address_line3 | Address | 50 |
| 4 | office_landmark | Address | 50 |
| 5 | **office_city** | **Contact** | **40** |
| 6 | **office_state** | **Contact** | **40** |
| 7 | **office_pincode** | **Contact** | **10** |
| 8 | **office_phone_no** | **Contact** | **20** |
| 9 | **office_fax_no** | **Contact** | **20** |

---

## 📊 Updated Total Field Count

| Field Type | Count |
|------------|-------|
| **Boxed Fields** | **31** (26 previously + 5 new office contact fields) |
| Text Fields | 3 |
| Checkbox Groups | 4 |
| **TOTAL** | **38 fields** |

---

## 🎯 Key Differences: Section B vs Section C

### Residential Address (B):
- City, State, PIN Code, Phone No., Mobile No., E-mail ID

### Office/Business Address (C):
- City, State, PIN Code, Phone No., **Fax No.** (instead of Mobile & Email)

Note: Section C has Fax No. while Section B has Mobile No. and Email ID lines.

---

## 📝 Dummy Data for Office Contact Fields

```
City: GURGAON
State: HARYANA
PIN Code: 122002
Phone No. (with STD Code): 01244567890
Fax No.: 01244567891
```

Complete Office Address:
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

## 🔧 Calibration Required

All 5 new fields have **initial estimated coordinates** that need calibration:

### From Image Reference:

1. **City** - Full width boxes across the line
2. **State** - Full width boxes across the line
3. **PIN Code** - Shorter field (6 digits)
4. **Phone No.** - Full width boxes (with STD Code)
5. **Fax No.** - Full width boxes

### Calibration Steps:

1. Open `SBI_grid_debug.pdf` to see coordinate grid
2. Open `SBI_filled_form.pdf` to see current output
3. For each field:
   - Find the first box on the form
   - Read `x_start` (horizontal center of first box)
   - Read `y` (text baseline)
   - Measure `dx` (distance between box centers)
4. Update values in `layout_config.py` (lines 295-339)
5. Re-run: `python3 step4_fill_form.py`
6. Repeat until perfect alignment

---

## 💡 Calibration Tips

### Based on Image:

1. **City and State** appear to be full-width fields
   - May use same `x_start` (left-aligned)
   - Likely same `dx` spacing

2. **PIN Code** is shorter
   - Check exact position on form
   - Usually 6-10 boxes for Indian PIN codes

3. **Phone and Fax** numbers likely aligned
   - May start at same `x_start`
   - Both need space for STD code + number

4. **Vertical Spacing**
   - All 5 fields are stacked vertically
   - Consistent `y` spacing between rows (estimate: 25 points)

---

## 🎉 Status

✅ All office contact fields configured as boxed fields  
✅ Dummy data added and tested  
✅ Form filling script updated  
⚠️ **Calibration required** - Use grid PDF to get exact coordinates

**Next Step:** Open the filled PDF, compare with grid, and calibrate the coordinates!
