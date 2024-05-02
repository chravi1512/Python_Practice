import PyPDF2

def merge_pdfs(input_paths, output_path):
    merger = PyPDF2.PdfMerger()
    
    for path in input_paths:
        merger.append(path)
    
    merger.write(output_path)
    merger.close()

# Example usage
input_files = ['C:/Users/l1.pdf','C:/l2.pdf']
output_file = 'C:/Users/l3mergerd.pdf'

merge_pdfs(input_files, output_file)
