# Image Fields Guide - Photograph & Signature

## 📸 Overview

The SBI Account Opening Form requires two image fields:
1. **Photograph** - Applicant's passport-size photo (2.5 cm × 3.5 cm)
2. **Signature** - Customer's signature

These fields are now supported in the form filling pipeline and will automatically insert images at specified coordinates.

---

## 🗂️ Image Field Configuration

### In `layout_config.py` (Lines 362-383):

```python
IMAGE_FIELDS = {
    "photograph": {
        "page": 0,
        "x": 135,        # X coordinate (left edge) - CALIBRATE THIS
        "y": 20,         # Y coordinate (top edge) - CALIBRATE THIS
        "width": 80,     # Width in points (2.5 cm ≈ 71 points)
        "height": 100,   # Height in points (3.5 cm ≈ 99 points)
        "type": "image",
        "description": "Photograph (2.5 cm X 3.5 cm)"
    },
    "signature": {
        "page": 0,
        "x": 30,         # X coordinate (left edge) - CALIBRATE THIS
        "y": 300,        # Y coordinate (top edge) - CALIBRATE THIS
        "width": 400,    # Width in points - CALIBRATE THIS
        "height": 120,   # Height in points - CALIBRATE THIS
        "type": "image",
        "description": "Signature of the Customer"
    },
}
```

---

## 📐 Understanding Coordinates

### For Image Fields:
- **x**: Left edge of the image rectangle (in PDF points)
- **y**: Top edge of the image rectangle (in PDF points)
- **width**: Width of the image rectangle
- **height**: Height of the image rectangle

### Size Conversions:
- **1 cm = 28.35 points**
- **1 inch = 72 points**
- Photograph (2.5 × 3.5 cm) ≈ 71 × 99 points

---

## 🖼️ How to Use Image Fields

### Method 1: Update Dummy Data

In `dummy_data.py`, update the image paths:

```python
dummy_data = {
    # ... other fields ...
    
    # === IMAGES ===
    "photograph": "/path/to/passport_photo.jpg",
    "signature": "/path/to/signature.png",
    
    # ... other fields ...
}
```

### Method 2: Provide Custom Data

```python
from step4_fill_form import PDFFormFiller
from dummy_data import generate_dummy_data

# Get dummy data
data = generate_dummy_data()

# Update with your image paths
data["photograph"] = "/Users/username/Documents/my_photo.jpg"
data["signature"] = "/Users/username/Documents/my_signature.png"

# Fill form
filler = PDFFormFiller(
    "45679523-SBI-Account-Opening-Form-I (1)_removed.pdf",
    "filled_form.pdf"
)
filler.fill_and_save(data)
```

---

## 📝 Supported Image Formats

The form filler supports all standard image formats:
- ✅ **JPEG/JPG** (`.jpg`, `.jpeg`)
- ✅ **PNG** (`.png`)
- ✅ **BMP** (`.bmp`)
- ✅ **TIFF** (`.tiff`, `.tif`)
- ✅ **GIF** (`.gif`)

---

## ⚠️ Important Notes

### 1. Image Paths Must Be Absolute or Relative
```python
# ✅ Good - Absolute path
"photograph": "/Users/adityagupta/Photos/passport.jpg"

# ✅ Good - Relative to script location
"photograph": "./images/passport.jpg"

# ❌ Bad - File doesn't exist
"photograph": "nonexistent.jpg"
```

### 2. If No Image Provided
When no image path is provided (or `None`), the script will:
- Skip the image field gracefully
- Print a warning: `⚠️  Skipped 'photograph': No image path provided`
- Continue filling other fields

### 3. If Image File Not Found
If the path is provided but file doesn't exist:
- Skip the image field
- Print a warning: `⚠️  Skipped 'photograph': Image file not found at /path/to/image.jpg`
- Continue filling other fields

---

## 🎯 Calibration Process

### Step 1: Generate Grid PDF
```bash
python3 step2_generate_grid.py
```

### Step 2: Identify Image Box Locations

On the form, locate:
1. **Photograph box** (upper right area) - 2.5 × 3.5 cm
2. **Signature box** (lower left area) - Large rectangular area

### Step 3: Read Coordinates from Grid

For each image box:
- **x**: Find LEFT edge of the box on X-axis
- **y**: Find TOP edge of the box on Y-axis  
- **width**: Measure horizontal span
- **height**: Measure vertical span

### Step 4: Update `layout_config.py`

Update lines 365-382 with measured coordinates.

### Step 5: Test with Sample Images

```bash
# Place test images
mkdir -p test_images
# Add sample photo and signature images

# Update dummy_data.py with test paths
# Run fill script
python3 step4_fill_form.py

# Check output
open SBI_filled_form.pdf
```

### Step 6: Fine-tune

If images don't fit perfectly:
- Adjust `x` and `y` for position
- Adjust `width` and `height` for size
- Re-run and verify

---

## 🔧 Image Preparation Tips

### For Photograph:
1. **Size**: Passport size (2.5 cm × 3.5 cm or 1" × 1.4")
2. **Resolution**: At least 300 DPI recommended
3. **Background**: Plain white or light color
4. **Format**: JPEG or PNG
5. **File size**: Keep under 500 KB for faster processing

### For Signature:
1. **Clear signature** on white paper
2. **Scan or photograph** in good lighting
3. **Crop** to just the signature area
4. **Remove background** if possible (use PNG with transparency)
5. **Format**: PNG preferred for transparency

### Sample Image Preparation:

```bash
# Using ImageMagick (if installed)
# Resize photograph to exact dimensions
convert photo.jpg -resize 71x99! passport_photo.jpg

# Crop and clean signature
convert signature.jpg -trim -bordercolor white -border 10 signature.png
```

---

## 📊 Current Status

| Field | Status | Coordinates |
|-------|--------|-------------|
| photograph | ⚠️ Needs Calibration | x: 135, y: 20, 80×100 pts |
| signature | ⚠️ Needs Calibration | x: 30, y: 300, 400×120 pts |

---

## 🔍 Troubleshooting

### Issue: Image Not Appearing
**Solution:**
1. Check file path is correct
2. Verify file exists at that location
3. Ensure image format is supported
4. Check console for error messages

### Issue: Image Too Large/Small
**Solution:**
1. Adjust `width` and `height` in layout_config.py
2. Or resize source image before using

### Issue: Image Position Wrong
**Solution:**
1. Use grid PDF to find correct x, y coordinates
2. Remember: x, y represent TOP-LEFT corner of image
3. Adjust coordinates in layout_config.py

### Issue: Image Quality Poor
**Solution:**
1. Use higher resolution source image
2. Ensure original image is at least 300 DPI
3. Use JPEG quality 90+ or PNG format

---

## 📚 Example: Complete Workflow

```python
# 1. Prepare images
# - Save your photo as: /Users/you/photo.jpg
# - Save your signature as: /Users/you/signature.png

# 2. Update dummy_data.py
dummy_data = {
    # ... other fields ...
    "photograph": "/Users/you/photo.jpg",
    "signature": "/Users/you/signature.png",
}

# 3. Run the script
python3 step4_fill_form.py

# 4. Output will show:
#   ✓ Inserted image 'photograph' at (135, 20) size (80x100)
#   ✓ Inserted image 'signature' at (30, 300) size (400x120)

# 5. Open and verify
open SBI_filled_form.pdf
```

---

## 📊 Updated Field Count

With image fields added:

| Field Type | Count |
|------------|-------|
| Boxed Fields | 33 |
| **Image Fields** | **2** ✨ |
| Text Fields | 3 |
| Checkbox Groups | 5 |
| **TOTAL** | **43 fields** |

---

## 🎉 Summary

✅ **Image field support added**  
✅ **Two image fields configured** (photograph, signature)  
✅ **Automatic image insertion** from file paths  
✅ **Graceful error handling** for missing images  
✅ **Multiple format support** (JPEG, PNG, etc.)  
⚠️ **Calibration required** for accurate positioning

**Next Steps:**
1. Calibrate photograph and signature box coordinates using grid PDF
2. Prepare your photograph (2.5×3.5 cm) and signature images
3. Update dummy_data.py with image file paths
4. Run form filler to test
5. Verify images appear correctly in output PDF
6. Fine-tune coordinates if needed

---

**Need help?** Check the console output for specific error messages about images!
