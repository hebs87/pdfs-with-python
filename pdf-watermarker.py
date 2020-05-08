import PyPDF2

# Create the template object, which is the opened super.pdf file in rb mode - this is a shorthand method of
# opening it, rather than having to use the 'with open' line in pdf.py
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# Create a watermark object
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# Create an output object which combines the two files
output = PyPDF2.PdfFileWriter()

# We loop through all the pages - we pass in the template object to the range() method and use the getNumPages() PyPDF
# method to get the number of pages in the PDF document - this will be the number value for the range() method
for i in range(template.getNumPages()):
    # Create a page object which is the relevant iterated page of the template object
    page = template.getPage(i)
    # Merge it with the watermark, which is the first page of the watermark object
    # pdfFileMerger simply merges the PDF files to create a master file, but mergePage actually merges the contents
    # of the page onto the same page - so the watermark will be merged onto the relevant page
    page.mergePage(watermark.getPage(0))
    # Add the page to the output - each page will be added with each iteration
    output.addPage(page)

    # Write the output to a new file
    with open('watermarked-output.pdf', 'wb') as file:
        output.write(file)
