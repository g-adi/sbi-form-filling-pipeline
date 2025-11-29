"""
Step 2: Generate a debug grid PDF with coordinate overlay
This overlays a grid with coordinate labels on the original PDF.
"""
import fitz  # PyMuPDF

def generate_grid_debug_pdf(template_pdf, out_pdf, step=20):
    """
    Generate a debug PDF with a coordinate grid overlay.
    
    Args:
        template_pdf: Path to the original PDF
        out_pdf: Path to save the grid debug PDF
        step: Grid spacing in points (default: 20)
    """
    doc = fitz.open(template_pdf)
    
    for page_num, page in enumerate(doc):
        rect = page.rect
        width, height = rect.width, rect.height
        
        print(f"\nGenerating grid for page {page_num}...")
        print(f"  Page size: {width:.1f} x {height:.1f} points")
        print(f"  Grid spacing: {step} points")
        
        # Draw vertical lines
        x = 0
        while x <= width:
            # Draw line
            page.draw_line(
                (x, 0), 
                (x, height), 
                width=0.3 if x % (step * 5) == 0 else 0.15,
                color=(0.7, 0.7, 0.7) if x % (step * 5) == 0 else (0.85, 0.85, 0.85)
            )
            
            # Add labels every 5 steps (every 100 points by default)
            if x % (step * 5) == 0:
                page.insert_text(
                    (x + 2, 10), 
                    str(int(x)), 
                    fontsize=6,
                    color=(0.5, 0, 0)
                )
            x += step
        
        # Draw horizontal lines
        y = 0
        while y <= height:
            # Draw line
            page.draw_line(
                (0, y), 
                (width, y), 
                width=0.3 if y % (step * 5) == 0 else 0.15,
                color=(0.7, 0.7, 0.7) if y % (step * 5) == 0 else (0.85, 0.85, 0.85)
            )
            
            # Add labels every 5 steps
            if y % (step * 5) == 0:
                page.insert_text(
                    (2, y + 7), 
                    str(int(y)), 
                    fontsize=6,
                    color=(0, 0, 0.5)
                )
            y += step
        
        # Add corner markers for easy reference
        marker_size = 10
        page.draw_circle((0, 0), marker_size, color=(1, 0, 0), width=2)
        page.draw_circle((width, 0), marker_size, color=(0, 1, 0), width=2)
        page.draw_circle((0, height), marker_size, color=(0, 0, 1), width=2)
        page.draw_circle((width, height), marker_size, color=(1, 1, 0), width=2)
    
    doc.save(out_pdf)
    doc.close()
    
    print(f"\n✓ Grid debug PDF saved to: {out_pdf}")
    print("\nUSAGE:")
    print("  1. Open the grid PDF in a viewer")
    print("  2. For each form field, note the coordinates:")
    print("     - X coordinate: Read from the top ruler (red numbers)")
    print("     - Y coordinate: Read from the left ruler (blue numbers)")
    print("  3. Record these in the layout config file")
    print("\nTIPS:")
    print("  - Thicker lines mark every 100 points")
    print("  - Thin lines mark every 20 points")
    print("  - Corner circles help orient the page")

if __name__ == "__main__":
    PDF_PATH = "45679523-SBI-Account-Opening-Form-I (1)_removed.pdf"
    OUTPUT_PATH = "SBI_grid_debug.pdf"
    GRID_STEP = 20  # 20-point grid spacing
    
    generate_grid_debug_pdf(PDF_PATH, OUTPUT_PATH, step=GRID_STEP)
