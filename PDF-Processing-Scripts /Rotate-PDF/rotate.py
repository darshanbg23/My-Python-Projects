import PyPDF2

with open("first.pdf", "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)  
    writer = PyPDF2.PdfWriter()  

    for page in reader.pages:
        page.rotate(180)  
        writer.add_page(page)  

    with open("rotated.pdf", "wb") as output_pdf:
        writer.write(output_pdf)  

print("Rotated PDF has been saved as 'rotated.pdf'.")
