"""
Step 1: Inspect PDF page size and coordinate system
This script checks the page dimensions and orientation of the PDF.
"""
import fitz  # PyMuPDF

def inspect_pdf(pdf_path):
    """Inspect the PDF to understand its coordinate system."""
    doc = fitz.open(pdf_path)
    
    print("=" * 60)
    print("PDF INSPECTION REPORT")
    print("=" * 60)
    
    print(f"\nTotal pages: {len(doc)}")
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        rect = page.rect
        
        print(f"\n--- Page {page_num} ---")
        print(f"Page rectangle: {rect}")
        print(f"Width: {rect.width} points ({rect.width / 72:.2f} inches)")
        print(f"Height: {rect.height} points ({rect.height / 72:.2f} inches)")
        print(f"Top-left: ({rect.x0}, {rect.y0})")
        print(f"Bottom-right: ({rect.x1}, {rect.y1})")
    
    # Check coordinate orientation
    print("\n" + "=" * 60)
    print("COORDINATE SYSTEM TEST")
    print("=" * 60)
    print("\nGenerating 'debug_origin.pdf' to check coordinate orientation...")
    
    page = doc[0]
    page.insert_text((0, 0), "A(0,0)", fontsize=10, color=(1, 0, 0))
    page.insert_text((50, 50), "B(50,50)", fontsize=10, color=(0, 0, 1))
    page.insert_text((rect.width - 50, 50), f"C({rect.width-50:.0f},50)", fontsize=10, color=(0, 1, 0))
    page.insert_text((50, rect.height - 20), f"D(50,{rect.height-20:.0f})", fontsize=10, color=(1, 0, 1))
    
    doc.save("debug_origin.pdf")
    doc.close()
    
    print("\n✓ Created 'debug_origin.pdf'")
    print("  Open this file to see:")
    print("  - Red 'A' should be at origin (top-left or bottom-left)")
    print("  - Blue 'B' at (50, 50)")
    print("  - Green 'C' at top-right area")
    print("  - Magenta 'D' at bottom-left area")
    print("\n  If A is at TOP-LEFT: Y increases DOWNWARD")
    print("  If A is at BOTTOM-LEFT: Y increases UPWARD")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    PDF_PATH = "45679523-SBI-Account-Opening-Form-I (1)_removed.pdf"
    inspect_pdf(PDF_PATH)
