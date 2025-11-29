"""
Step 5: Calibration Helper
This script helps fine-tune specific field coordinates by testing them individually.
"""
import fitz  # PyMuPDF
from layout_config import get_field_config, get_all_text_fields, get_all_boxed_fields, get_all_checkbox_fields


class CalibrationHelper:
    """Helper class for calibrating individual field coordinates."""
    
    def __init__(self, template_pdf):
        self.template_pdf = template_pdf
        self.font_name = "helv"
        
    def test_single_field(self, field_name, test_value, output_pdf):
        """
        Test a single field by drawing its value and coordinate markers.
        
        Args:
            field_name: Name of the field to test
            test_value: Test value to draw
            output_pdf: Path to save the test PDF
        """
        config = get_field_config(field_name)
        if not config:
            print(f"❌ Field '{field_name}' not found in layout config")
            return
        
        doc = fitz.open(self.template_pdf)
        page = doc[config["page"]]
        
        print(f"\n{'='*60}")
        print(f"TESTING FIELD: {field_name}")
        print(f"{'='*60}")
        print(f"Configuration:")
        for key, value in config.items():
            print(f"  {key}: {value}")
        
        field_type = config.get("type", "text")
        
        if field_type == "text":
            self._test_text_field(page, field_name, test_value, config)
        elif field_type == "boxed":
            self._test_boxed_field(page, field_name, test_value, config)
        elif field_type == "checkbox":
            self._test_checkbox_field(page, field_name, test_value, config)
        
        doc.save(output_pdf)
        doc.close()
        
        print(f"\n✓ Test PDF saved: {output_pdf}")
        print("\nCALIBRATION GUIDE:")
        print("  - Text too HIGH → INCREASE y value")
        print("  - Text too LOW → DECREASE y value")
        print("  - Text too LEFT → INCREASE x value")
        print("  - Text too RIGHT → DECREASE x value")
        print("  - Text too SMALL → INCREASE font_size")
        print("  - Text too LARGE → DECREASE font_size")
        
    def _test_text_field(self, page, field_name, test_value, config):
        """Test a standard text field."""
        x = config["x"]
        y = config["y"]
        font_size = config.get("font_size", 9)
        
        # Draw the test value in RED
        page.insert_text(
            (x, y),
            str(test_value).upper(),
            fontsize=font_size,
            fontname=self.font_name,
            color=(1, 0, 0)  # Red
        )
        
        # Draw crosshair at the coordinate
        self._draw_crosshair(page, x, y, color=(0, 0, 1), size=10)
        
        # Add coordinate label
        page.insert_text(
            (x, y - 15),
            f"({x}, {y})",
            fontsize=6,
            color=(0, 0, 1)
        )
        
        print(f"\n✓ Drew text at ({x}, {y})")
        print(f"  Value: {test_value}")
        print(f"  Font size: {font_size}")
        
    def _test_boxed_field(self, page, field_name, test_value, config):
        """Test a boxed field."""
        x_start = config["x_start"]
        y = config["y"]
        dx = config["dx"]
        font_size = config.get("font_size", 10)
        
        # Draw each character in RED
        x = x_start
        for char in str(test_value).upper():
            page.insert_text(
                (x, y),
                char,
                fontsize=font_size,
                fontname=self.font_name,
                color=(1, 0, 0)  # Red
            )
            # Draw small crosshair at each position
            self._draw_crosshair(page, x, y, color=(0, 0, 1), size=5)
            x += dx
        
        # Draw coordinate labels
        page.insert_text(
            (x_start, y - 15),
            f"start({x_start}, {y}) dx={dx}",
            fontsize=6,
            color=(0, 0, 1)
        )
        
        print(f"\n✓ Drew boxed text starting at ({x_start}, {y})")
        print(f"  Value: {test_value}")
        print(f"  Font size: {font_size}")
        print(f"  Box spacing (dx): {dx}")
        
    def _test_checkbox_field(self, page, field_name, selected_option, config):
        """Test a checkbox field."""
        if selected_option not in config["options"]:
            print(f"❌ Option '{selected_option}' not found")
            return
        
        # Draw all checkbox positions with labels
        for option_name, option_config in config["options"].items():
            x = option_config["x"]
            y = option_config["y"]
            
            # Draw crosshair
            self._draw_crosshair(page, x, y, color=(0.5, 0.5, 0.5), size=8)
            
            # If this is the selected option, draw checkmark in RED
            if option_name == selected_option:
                page.insert_text(
                    (x, y),
                    "✓",
                    fontsize=12,
                    fontname=self.font_name,
                    color=(1, 0, 0)  # Red
                )
            
            # Label
            page.insert_text(
                (x, y - 12),
                f"{option_name}({x},{y})",
                fontsize=5,
                color=(0, 0, 1)
            )
        
        print(f"\n✓ Drew checkbox options")
        print(f"  Selected: {selected_option}")
        
    def _draw_crosshair(self, page, x, y, color=(1, 0, 0), size=10):
        """Draw a crosshair marker at the given coordinates."""
        # Horizontal line
        page.draw_line(
            (x - size, y),
            (x + size, y),
            width=0.5,
            color=color
        )
        # Vertical line
        page.draw_line(
            (x, y - size),
            (x, y + size),
            width=0.5,
            color=color
        )
        # Center dot
        page.draw_circle((x, y), 1, fill=color)
        
    def test_multiple_fields(self, field_tests, output_pdf):
        """
        Test multiple fields at once.
        
        Args:
            field_tests: List of tuples (field_name, test_value)
            output_pdf: Path to save the test PDF
        """
        doc = fitz.open(self.template_pdf)
        
        print(f"\n{'='*60}")
        print(f"TESTING MULTIPLE FIELDS")
        print(f"{'='*60}")
        
        for field_name, test_value in field_tests:
            config = get_field_config(field_name)
            if not config:
                print(f"⚠️  Skipping '{field_name}' - not found")
                continue
            
            page = doc[config["page"]]
            field_type = config.get("type", "text")
            
            print(f"\n{field_name}:")
            
            if field_type == "text":
                self._test_text_field(page, field_name, test_value, config)
            elif field_type == "boxed":
                self._test_boxed_field(page, field_name, test_value, config)
            elif field_type == "checkbox":
                self._test_checkbox_field(page, field_name, test_value, config)
        
        doc.save(output_pdf)
        doc.close()
        
        print(f"\n{'='*60}")
        print(f"✓ Test PDF saved: {output_pdf}")
        print(f"{'='*60}")


def main():
    """Main function demonstrating calibration helper usage."""
    TEMPLATE_PDF = "45679523-SBI-Account-Opening-Form-I (1)_removed.pdf"
    
    helper = CalibrationHelper(TEMPLATE_PDF)
    
    # Example 1: Test a single field
    print("\n" + "="*60)
    print("EXAMPLE 1: Testing Single Field")
    print("="*60)
    helper.test_single_field(
        field_name="full_name",
        test_value="RAJESH KUMAR SHARMA",
        output_pdf="calibration_test_single.pdf"
    )
    
    # Example 2: Test multiple fields at once
    print("\n" + "="*60)
    print("EXAMPLE 2: Testing Multiple Fields")
    print("="*60)
    
    field_tests = [
        ("full_name", "RAJESH KUMAR SHARMA"),
        ("father_name", "SURESH KUMAR SHARMA"),
        ("pan_number", "ABCDE1234F"),
        ("mobile_number", "9876543210"),
        ("gender", "Male"),
    ]
    
    helper.test_multiple_fields(
        field_tests,
        output_pdf="calibration_test_multiple.pdf"
    )
    
    print("\n" + "="*60)
    print("CALIBRATION HELPER DEMO COMPLETE")
    print("="*60)
    print("\nUSAGE:")
    print("  1. Identify fields that need adjustment")
    print("  2. Use this script to test them individually")
    print("  3. Look at the crosshairs and coordinate labels")
    print("  4. Adjust values in layout_config.py")
    print("  5. Repeat until perfect")


if __name__ == "__main__":
    main()
