# PDF Operations using PyPDF2

This repository contains multiple Python scripts that demonstrate various operations on PDFs using the `PyPDF2` library. Below are the explanations for each script, detailing what each line of code does.

---

## 1. Extracting Text from a PDF

```python
import PyPDF2  

with open("sample.pdf", "rb") as pdf_file:  # Open the PDF file in read-binary mode
    reader = PyPDF2.PdfReader(pdf_file)  # Create a PdfReader object to read the file
    
    for page_num in range(len(reader.pages)):  # Loop through all pages in the PDF
        page = reader.pages[page_num]  # Access the specific page
        print(f"Text from Page {page_num + 1}:\n{page.extract_text()}\n")  # Extract and print text from the page
```

---

## 2. Splitting a PDF (Extracting the First Page)

```python
import PyPDF2  

with open("Unsplited.pdf", "rb") as pdf_file:  # Open the source PDF in read-binary mode
    reader = PyPDF2.PdfReader(pdf_file)  # Create a PdfReader object
    writer = PyPDF2.PdfWriter()  # Create a PdfWriter object to write pages

    for page_num in range(1):  # Extract only the first page
        writer.add_page(reader.pages[page_num])  # Add the first page to the writer object

    with open("split_pages.pdf", "wb") as output_pdf:  # Open a new file to save the extracted page
        writer.write(output_pdf)  # Write the extracted page to the new file

print("PDF pages have been extracted and saved as 'split_pages.pdf'.")
```

---

## 3. Merging Multiple PDFs

```python
import PyPDF2

pdfs_to_merge = ["first.pdf", "second.pdf"]  # List of PDF files to merge
writer = PyPDF2.PdfWriter()  # Create a PdfWriter object

for pdf in pdfs_to_merge:  # Loop through each PDF in the list
    with open(pdf, "rb") as pdf_file:  # Open the PDF in read-binary mode
        reader = PyPDF2.PdfReader(pdf_file)  # Create a PdfReader object
        for page in reader.pages:  # Loop through all pages in the PDF
            writer.add_page(page)  # Add each page to the writer object

with open("merged.pdf", "wb") as output_pdf:  # Open a new file to save the merged PDF
    writer.write(output_pdf)  # Write all pages to the new file

print("PDFs have been merged and saved as 'merged.pdf'.")
```

---

## 4. Rotating Pages in a PDF

```python
import PyPDF2

with open("first.pdf", "rb") as pdf_file:  # Open the PDF file in read-binary mode
    reader = PyPDF2.PdfReader(pdf_file)  # Create a PdfReader object
    writer = PyPDF2.PdfWriter()  # Create a PdfWriter object

    for page in reader.pages:  # Loop through each page in the PDF
        page.rotate(180)  # Rotate the page by 180 degrees
        writer.add_page(page)  # Add the rotated page to the writer object

    with open("rotated.pdf", "wb") as output_pdf:  # Open a new file to save the rotated PDF
        writer.write(output_pdf)  # Write the rotated pages to the new file

print("Rotated PDF has been saved as 'rotated.pdf'.")
```

---

## 5. Encrypting a PDF

```python
import PyPDF2

with open("Sample.pdf", "rb") as pdf_file:  # Open the PDF in read-binary mode
    reader = PyPDF2.PdfReader(pdf_file)  # Create a PdfReader object
    writer = PyPDF2.PdfWriter()  # Create a PdfWriter object

    for page in reader.pages:  # Loop through all pages in the PDF
        writer.add_page(page)  # Add each page to the writer object

    password = "123456"  # Define the password for encryption
    writer.encrypt(password)  # Encrypt the PDF with the password

    with open("encrypted.pdf", "wb") as output_pdf:  # Open a new file to save the encrypted PDF
        writer.write(output_pdf)  # Write the encrypted PDF to the new file

print("Encrypted PDF saved as 'encrypted.pdf'.")
```

---

## 6. Decrypting a PDF

```python
import PyPDF2

with open("encrypted.pdf", "rb") as pdf_file:  # Open the encrypted PDF in read-binary mode
    reader = PyPDF2.PdfReader(pdf_file)  # Create a PdfReader object

    password = "123456"  # Define the password used to decrypt the file
    if reader.decrypt(password):  # Attempt to decrypt the file with the password
        writer = PyPDF2.PdfWriter()  # Create a PdfWriter object
        
        for page in reader.pages:  # Loop through all pages in the decrypted PDF
            writer.add_page(page)  # Add each page to the writer object

        with open("decrypted.pdf", "wb") as output_pdf:  # Open a new file to save the decrypted PDF
            writer.write(output_pdf)  # Write the decrypted pages to the new file

        print("Decrypted PDF saved as 'decrypted.pdf'.")
    else:
        print("Wrong password!")  # Print error message if the password is incorrect
```

---

## Summary

- **Extract Text**: Reads and extracts text from all pages of a PDF.
- **Split PDF**: Extracts only the first page and saves it separately.
- **Merge PDFs**: Combines multiple PDFs into one file.
- **Rotate PDF**: Rotates all pages of a PDF by 180 degrees.
- **Encrypt PDF**: Protects a PDF with a password.
- **Decrypt PDF**: Removes password protection if the correct password is provided.

These scripts utilize the `PyPDF2` library, which is a powerful tool for handling PDFs in Python. Ensure you have `PyPDF2` installed before running the scripts using:

```sh
pip install pypdf2
```

---

### Author
Darshan BG

### License
This project is licensed under the MIT License - see the LICENSE file for details.

