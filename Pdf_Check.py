import PyPDF2

# Open the PDF file in read binary mode
with open('Form_8_English.pdf', 'rb') as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)

    # Get the total number of pages in the PDF
    total_pages = len(reader.pages)

    # Initialize an empty string to store the extracted text
    extracted_text = ""

    # Iterate through each page in the PDF
    for page_number in range(total_pages):
        # Get the text content of the page
        page = reader.pages[page_number]
        text = page.extract_text()

        # Append the extracted text to the final string
        extracted_text += text

# Print the extracted text
print(extracted_text)
