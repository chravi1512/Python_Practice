import PyPDF2
from reportlab.pdfgen import canvas

# Open the PDF file in read binary mode
with open('Form_8_English.pdf', 'rb') as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)

    # Create a PDF writer object
    writer = PyPDF2.PdfWriter()

    # Iterate through each page in the PDF
    for page_number in range(len(reader.pages)):
        # Get the page and add it to the writer object
        page = reader.pages[page_number]
        writer.add_page(page)

        # Modify the content of the page (e.g., add a watermark)
        c = canvas.Canvas("watermark.pdf")
        c.drawString(100, 100, "Watermark Text")
        c.save()

        # Merge the modified page with the original page
        modified_page = PyPDF2.PdfReader("watermark.pdf")
        modified_page = modified_page.pages[0]
        modified_page.merge_page(page)
        writer.add_page(modified_page)

    # Save the modified PDF to a new file
    with open('output.pdf', 'wb') as output_file:
        writer.write(output_file)
