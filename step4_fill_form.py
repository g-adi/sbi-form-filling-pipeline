"""
Step 4: Fill Form with Dummy Data
This script fills the PDF form using the coordinates from layout_config.py
"""
import fitz  # PyMuPDF
import os
from layout_config import (
    get_all_text_fields,
    get_all_boxed_fields,
    get_all_date_fields,
    get_all_image_fields,
    get_all_checkbox_fields,
    PAGE_CONFIG
)
from dummy_data import generate_dummy_data


class PDFFormFiller:
    """Fill PDF forms using coordinate-based layout configuration."""
    
    def __init__(self, template_pdf_path, output_pdf_path):
        """
        Initialize the form filler.
        
        Args:
            template_pdf_path: Path to the blank form template
            output_pdf_path: Path to save the filled form
        """
        self.template_path = template_pdf_path
        self.output_path = output_pdf_path
        self.doc = None
        self.font_name = "helv"  # Helvetica - standard PDF font
        
    def open_template(self):
        """Open the PDF template."""
        self.doc = fitz.open(self.template_path)
        print(f"✓ Opened template: {self.template_path}")
        
    def fill_text_field(self, page, field_name, value, config):
        """
        Fill a standard text field.
        
        Args:
            page: PDF page object
            field_name: Name of the field
            value: Text value to fill
            config: Field configuration dict
        """
        if not value:
            return
            
        x = config["x"]
        y = config["y"]
        font_size = config.get("font_size", 9)
        max_width = config.get("max_width", 300)
        
        # Convert to uppercase for consistency
        value = str(value).upper()
        
        # Insert text
        page.insert_text(
            (x, y),
            value,
            fontsize=font_size,
            fontname=self.font_name,
            color=(0, 0, 0)  # Black color
        )
        
        print(f"  ✓ Filled '{field_name}': {value} at ({x}, {y})")
        
    def fill_boxed_field(self, page, field_name, value, config):
        """
        Fill a boxed field where each character goes in a separate box.
        
        Args:
            page: PDF page object
            field_name: Name of the field
            value: Text value to fill (one char per box)
            config: Field configuration dict
        """
        if not value:
            return
            
        x_start = config["x_start"]
        y = config["y"]
        dx = config["dx"]
        font_size = config.get("font_size", 10)
        max_chars = config.get("max_chars", 10)
        
        # Convert to uppercase and limit length
        value = str(value).upper()[:max_chars]
        
        # Fill character by character
        x = x_start
        for char in value:
            page.insert_text(
                (x, y),
                char,
                fontsize=font_size,
                fontname=self.font_name,
                color=(0, 0, 0)
            )
            x += dx
        
        print(f"  ✓ Filled boxed '{field_name}': {value} starting at ({x_start}, {y})")
        
    def fill_date_field(self, page, field_name, value, config):
        """
        Fill a date field with separate DD/MM/YYYY sections.
        
        Args:
            page: PDF page object
            field_name: Name of the field
            value: Date string (DD/MM/YYYY format)
            config: Field configuration dict with dd, mm, yyyy sections
        """
        if not value:
            return
        
        # Parse date value - expect DD/MM/YYYY format
        value = str(value).strip()
        parts = value.replace('-', '/').split('/')
        
        if len(parts) != 3:
            print(f"  ⚠️  Skipped '{field_name}': Invalid date format (expected DD/MM/YYYY)")
            return
        
        dd = parts[0].zfill(2)  # Ensure 2 digits
        mm = parts[1].zfill(2)  # Ensure 2 digits
        yyyy = parts[2].zfill(4)  # Ensure 4 digits
        
        font_size = config.get("font_size", 9)
        
        # Fill DD section
        dd_config = config["dd"]
        x = dd_config["x_start"]
        y = dd_config["y"]
        dx = dd_config["dx"]
        for char in dd:
            page.insert_text(
                (x, y),
                char,
                fontsize=font_size,
                fontname=self.font_name,
                color=(0, 0, 0)
            )
            x += dx
        
        # Fill MM section
        mm_config = config["mm"]
        x = mm_config["x_start"]
        y = mm_config["y"]
        dx = mm_config["dx"]
        for char in mm:
            page.insert_text(
                (x, y),
                char,
                fontsize=font_size,
                fontname=self.font_name,
                color=(0, 0, 0)
            )
            x += dx
        
        # Fill YYYY section
        yyyy_config = config["yyyy"]
        x = yyyy_config["x_start"]
        y = yyyy_config["y"]
        dx = yyyy_config["dx"]
        for char in yyyy:
            page.insert_text(
                (x, y),
                char,
                fontsize=font_size,
                fontname=self.font_name,
                color=(0, 0, 0)
            )
            x += dx
        
        print(f"  ✓ Filled date '{field_name}': {dd}/{mm}/{yyyy}")
        
    def fill_checkbox(self, page, field_name, selected_option, config):
        """
        Fill a checkbox or radio button.
        
        Args:
            page: PDF page object
            field_name: Name of the field
            selected_option: Which option is selected
            config: Field configuration dict with options
        """
        if not selected_option or selected_option not in config["options"]:
            return
            
        option_config = config["options"][selected_option]
        x = option_config["x"]
        y = option_config["y"]
        
        # Draw a checkmark using ZapfDingbats font
        # In ZapfDingbats, character "4" is a checkmark
        page.insert_text(
            (x, y),
            "4",
            fontsize=10,
            fontname="zadb",  # ZapfDingbats font for checkmark symbol
            color=(0, 0, 0)
        )
        
        print(f"  ✓ Checked '{field_name}': {selected_option} at ({x}, {y})")
        
    def fill_image(self, page, field_name, image_path, config):
        """
        Insert an image into the PDF at specified coordinates.
        
        Args:
            page: PDF page object
            field_name: Name of the field
            image_path: Path to the image file
            config: Field configuration dict with coordinates
        """
        if not image_path:
            print(f"  ⚠️  Skipped '{field_name}': No image path provided")
            return
        
        # Check if image file exists
        if not os.path.exists(image_path):
            print(f"  ⚠️  Skipped '{field_name}': Image file not found at {image_path}")
            return
        
        x = config["x"]
        y = config["y"]
        width = config["width"]
        height = config["height"]
        
        # Create rectangle for image placement
        rect = fitz.Rect(x, y, x + width, y + height)
        
        try:
            # Insert image into the rectangle
            page.insert_image(rect, filename=image_path)
            print(f"  ✓ Inserted image '{field_name}' at ({x}, {y}) size ({width}x{height})")
        except Exception as e:
            print(f"  ❌ Failed to insert '{field_name}': {str(e)}")
        
    def fill_form(self, data):
        """
        Fill the entire form with provided data.
        
        Args:
            data: Dictionary with field names and values
        """
        if not self.doc:
            self.open_template()
        
        print("\n" + "=" * 60)
        print("FILLING FORM WITH DATA")
        print("=" * 60)
        
        # Get all field configurations
        text_fields = get_all_text_fields()
        boxed_fields = get_all_boxed_fields()
        date_fields = get_all_date_fields()
        image_fields = get_all_image_fields()
        checkbox_fields = get_all_checkbox_fields()
        
        # Process each page
        for page_num, page in enumerate(self.doc):
            print(f"\n--- Processing Page {page_num} ---")
            
            # Fill text fields
            for field_name, config in text_fields.items():
                if config["page"] == page_num and field_name in data:
                    self.fill_text_field(page, field_name, data[field_name], config)
            
            # Fill boxed fields
            for field_name, config in boxed_fields.items():
                if config["page"] == page_num and field_name in data:
                    self.fill_boxed_field(page, field_name, data[field_name], config)
            
            # Fill date fields (DD/MM/YYYY with separate sections)
            for field_name, config in date_fields.items():
                if config["page"] == page_num and field_name in data:
                    self.fill_date_field(page, field_name, data[field_name], config)
            
            # Fill images
            for field_name, config in image_fields.items():
                if config["page"] == page_num and field_name in data:
                    self.fill_image(page, field_name, data[field_name], config)
            
            # Fill checkboxes
            for field_name, config in checkbox_fields.items():
                if config["page"] == page_num and field_name in data:
                    self.fill_checkbox(page, field_name, data[field_name], config)
        
        print("\n" + "=" * 60)
        
    def save(self):
        """Save the filled PDF."""
        if self.doc:
            self.doc.save(self.output_path)
            self.doc.close()
            print(f"\n✓ Filled form saved to: {self.output_path}")
            print("\nNEXT STEPS:")
            print("  1. Open the filled PDF")
            print("  2. Compare with the original template")
            print("  3. Adjust coordinates in layout_config.py if needed")
            print("  4. Re-run this script until perfect alignment")
        
    def fill_and_save(self, data):
        """Convenience method to fill and save in one call."""
        self.fill_form(data)
        self.save()


def main():
    """Main function to run the form filling process."""
    # Configuration
    TEMPLATE_PDF = "45679523-SBI-Account-Opening-Form-I (1)_removed.pdf"
    OUTPUT_PDF = "SBI_filled_form.pdf"
    
    # Generate dummy data
    print("\n" + "=" * 60)
    print("GENERATING DUMMY DATA")
    print("=" * 60)
    data = generate_dummy_data()
    
    # Print summary
    print(f"\nGenerated {len(data)} fields")
    print("Sample data:")
    for key, value in list(data.items())[:5]:
        print(f"  {key}: {value}")
    print("  ...")
    
    # Fill the form
    filler = PDFFormFiller(TEMPLATE_PDF, OUTPUT_PDF)
    filler.fill_and_save(data)
    
    print("\n" + "=" * 60)
    print("FORM FILLING COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
