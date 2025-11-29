"""
Master Pipeline Runner
Executes all steps of the PDF form filling pipeline in sequence.
"""
import sys
import os
from pathlib import Path

def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def run_step(step_num, description, script_name):
    """Run a pipeline step."""
    print_header(f"STEP {step_num}: {description}")
    
    print(f"Running: {script_name}")
    print("-" * 70)
    
    try:
        # Import and run the script
        if script_name == "step1_inspect_pdf.py":
            from step1_inspect_pdf import inspect_pdf
            inspect_pdf("45679523-SBI-Account-Opening-Form-I (1)_removed.pdf")
            
        elif script_name == "step2_generate_grid.py":
            from step2_generate_grid import generate_grid_debug_pdf
            generate_grid_debug_pdf(
                "45679523-SBI-Account-Opening-Form-I (1)_removed.pdf",
                "SBI_grid_debug.pdf",
                step=20
            )
            
        elif script_name == "dummy_data.py":
            from dummy_data import print_dummy_data
            print_dummy_data()
            
        elif script_name == "step4_fill_form.py":
            from step4_fill_form import main as fill_main
            fill_main()
            
        print("\n✓ Step completed successfully!")
        return True
        
    except ImportError as e:
        print(f"\n❌ Error importing module: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Error during execution: {e}")
        return False


def check_dependencies():
    """Check if required dependencies are installed."""
    print_header("CHECKING DEPENDENCIES")
    
    try:
        import fitz
        print(f"✓ PyMuPDF (fitz) version: {fitz.__version__}")
        return True
    except ImportError:
        print("❌ PyMuPDF not found!")
        print("\nPlease install required dependencies:")
        print("  pip install -r requirements.txt")
        print("\nOr install directly:")
        print("  pip install PyMuPDF")
        return False


def check_files():
    """Check if required files exist."""
    print_header("CHECKING FILES")
    
    required_files = [
        "45679523-SBI-Account-Opening-Form-I (1)_removed.pdf",
        "layout_config.py",
        "dummy_data.py",
        "step1_inspect_pdf.py",
        "step2_generate_grid.py",
        "step4_fill_form.py",
    ]
    
    all_exist = True
    for file in required_files:
        if Path(file).exists():
            print(f"✓ {file}")
        else:
            print(f"❌ {file} - NOT FOUND")
            all_exist = False
    
    return all_exist


def show_menu():
    """Display interactive menu."""
    print_header("PDF FORM FILLING PIPELINE")
    
    print("Select an option:")
    print()
    print("  [1] Run Complete Pipeline (Steps 1-4)")
    print("  [2] Step 1: Inspect PDF")
    print("  [3] Step 2: Generate Grid")
    print("  [4] Step 3: View Dummy Data")
    print("  [5] Step 4: Fill Form")
    print("  [6] Run Calibration Helper")
    print("  [0] Exit")
    print()
    
    choice = input("Enter your choice: ").strip()
    return choice


def run_calibration_helper():
    """Run the calibration helper."""
    print_header("CALIBRATION HELPER")
    
    try:
        from step5_calibration_helper import main as calib_main
        calib_main()
        print("\n✓ Calibration helper completed!")
    except Exception as e:
        print(f"\n❌ Error: {e}")


def main():
    """Main function with interactive menu."""
    
    # Initial checks
    if not check_dependencies():
        return
    
    if not check_files():
        print("\n❌ Missing required files. Please ensure all files are present.")
        return
    
    while True:
        choice = show_menu()
        
        if choice == "0":
            print("\n👋 Goodbye!")
            break
            
        elif choice == "1":
            # Run complete pipeline
            steps = [
                (1, "Inspect PDF", "step1_inspect_pdf.py"),
                (2, "Generate Grid", "step2_generate_grid.py"),
                (3, "View Dummy Data", "dummy_data.py"),
                (4, "Fill Form", "step4_fill_form.py"),
            ]
            
            for step_num, desc, script in steps:
                success = run_step(step_num, desc, script)
                if not success:
                    print(f"\n❌ Pipeline stopped at step {step_num}")
                    break
                
                if step_num < len(steps):
                    input("\nPress Enter to continue to next step...")
            
            print_header("PIPELINE COMPLETE")
            print("Next steps:")
            print("  1. Open 'SBI_filled_form.pdf' to see the results")
            print("  2. Compare with 'SBI_grid_debug.pdf' for coordinates")
            print("  3. Use option [6] to run calibration helper if needed")
            print("  4. Adjust coordinates in 'layout_config.py'")
            print("  5. Re-run option [5] to test adjusted coordinates")
            
            input("\nPress Enter to return to menu...")
            
        elif choice == "2":
            run_step(1, "Inspect PDF", "step1_inspect_pdf.py")
            input("\nPress Enter to return to menu...")
            
        elif choice == "3":
            run_step(2, "Generate Grid", "step2_generate_grid.py")
            input("\nPress Enter to return to menu...")
            
        elif choice == "4":
            run_step(3, "View Dummy Data", "dummy_data.py")
            input("\nPress Enter to return to menu...")
            
        elif choice == "5":
            run_step(4, "Fill Form", "step4_fill_form.py")
            input("\nPress Enter to return to menu...")
            
        elif choice == "6":
            run_calibration_helper()
            input("\nPress Enter to return to menu...")
            
        else:
            print("\n❌ Invalid choice. Please try again.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
