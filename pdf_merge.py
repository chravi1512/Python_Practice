import PyPDF2

def merge_pdfs(input_paths, output_path):
    merger = PyPDF2.PdfMerger()
    
    for path in input_paths:
        merger.append(path)
    
    merger.write(output_path)
    merger.close()

# Example usage
input_files = ['C:/Users/chila/OneDrive/Documents/My Scans/file1.pdf','C:/Users/chila/OneDrive/Documents/immunizations-2.pdf']
output_file = 'C:/Users/chila/OneDrive/Documents/immunizations-2_merge.pdf'

merge_pdfs(input_files, output_file)