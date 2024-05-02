import PyPDF2

def merge_pages(input_pdf, output_pdf, source_page_number, destination_page_number):
    # Open the input PDF file in read-binary mode
    with open(input_pdf, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Loop through each page in the input PDF
        for page_number in range(len(pdf_reader.pages)):
            # Get the current page
            page = pdf_reader.pages[page_number]

            # Check if it's the source page
            if page_number == source_page_number - 1:
                # Get the destination page
                destination_page = pdf_reader.pages[destination_page_number - 1]

                # Merge the content of the source page into the destination page
                destination_page.merge_page(page)

                # Add the modified destination page to the PDF writer
                pdf_writer.add_page(destination_page)
            else:
                # Add the current page to the PDF writer
                pdf_writer.add_page(page)

        # Open the output PDF file in write-binary mode
        with open(output_pdf, 'wb') as output_file:
            # Write the modified PDF to the output file
            pdf_writer.write(output_file)

# Example usage
merge_pages('C:/Users/chila/OneDrive/Documents/pan_nikhil.pdf', 'C:/Users/chila/OneDrive/Documents/pan_nikhil_1.pdf', 1, 2)
