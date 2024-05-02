import PyPDF2

def rotate_pdf(input_pdf, output_pdf, rotation_angle):
    # Open the input PDF file in read-binary mode
    with open(input_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Create a PDF writer object for the output PDF
        pdf_writer = PyPDF2.PdfWriter()

        # Iterate through each page and rotate it
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page.rotate(rotation_angle)
            pdf_writer.add_page(page)

        # Write the rotated pages to the output PDF file
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf = 'C://Users/chila/Downloads/nikhil_vit_1.pdf'  # Replace with the path to your input PDF file
    output_pdf = 'C://Users/chila/Downloads/nikhil_vit_1.pdf'  # Replace with the desired output PDF file
    rotation_angle = 180  # Specify the rotation angle (90 for clockwise, -90 for counterclockwise)

    rotate_pdf(input_pdf, output_pdf, rotation_angle)
