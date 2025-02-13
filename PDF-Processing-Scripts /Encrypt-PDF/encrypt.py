import PyPDF2

with open("Sample.pdf", "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    writer = PyPDF2.PdfWriter()  

    for page in reader.pages:
        writer.add_page(page)  

    password = "123456"  
    writer.encrypt(password)  

    with open("encrypted.pdf", "wb") as output_pdf:
        writer.write(output_pdf)  

print("Encrypted PDF saved as 'encrypted.pdf'.")
