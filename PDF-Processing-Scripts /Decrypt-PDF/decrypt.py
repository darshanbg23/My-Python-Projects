import PyPDF2 

with open("encrypted.pdf", "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)  

    password = "123456"
    if reader.decrypt(password):  
        writer = PyPDF2.PdfWriter()
        
        for page in reader.pages:
            writer.add_page(page)

        with open("decrypted.pdf", "wb") as output_pdf:
            writer.write(output_pdf)  

        print("Decrypted PDF saved as 'decrypted.pdf'.")
    else:
        print("Wrong password!")
