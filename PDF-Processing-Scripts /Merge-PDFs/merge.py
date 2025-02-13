import PyPDF2

pdfs_to_merge = ["first.pdf","second.pdf"]  

writer = PyPDF2.PdfWriter()  

for pdf in pdfs_to_merge:
    with open(pdf, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            writer.add_page(page)  

with open("merged.pdf", "wb") as output_pdf:
    writer.write(output_pdf)  

print("PDFs have been merged and saved as 'merged.pdf'.")
