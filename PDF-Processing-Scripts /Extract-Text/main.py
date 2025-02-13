import PyPDF2  

with open("sample.pdf", "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file) 
    
    for page_num in range(len(reader.pages)):  
        page = reader.pages[page_num]
        print(f"Text from Page {page_num + 1}:\n{page.extract_text()}\n") 
