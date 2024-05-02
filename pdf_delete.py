import fitz  # PyMuPDF

def remove_page(input_pdf, output_pdf, page_number):
    """
    Remove a specific page from a PDF and save the result.

    Parameters:
    - input_pdf: The input PDF file path.
    - output_pdf: The output PDF file path.
    - page_number: The page number to be removed (1-based index).
    """
    # Open the input PDF
    pdf_document = fitz.open(input_pdf)

    # Check if the specified page number is valid
    if page_number < 1 or page_number > pdf_document.page_count:
        print("Invalid page number.")
        return

    # Remove the specified page
    pdf_document.delete_page(page_number - 1)

    # Save the modified PDF to the output file
    pdf_document.save(output_pdf)
    pdf_document.close()

if __name__ == "__main__":
    input_pdf_path = "C:/Users/chila/OneDrive/Documents/immunizations.pdf"
    output_pdf_path = "C:/Users/chila/OneDrive/Documents/immunizations-2.pdf"
    page_to_remove = 1  # Change this to the page number you want to remove

    remove_page(input_pdf_path, output_pdf_path, page_to_remove)
