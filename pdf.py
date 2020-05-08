import PyPDF2

# We need to add 'b' to the read/write command, which stands for binary (without this, it won't work)
with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    # Print the number of pages
    print(reader.numPages)
    # Print the object for the first page
    print(reader.getPage(0))
    # Rotate the page and save it to a new file
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
