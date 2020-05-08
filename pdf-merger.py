import PyPDF2
import sys

# Get the second input (excludes this filename from the run command), followed by all others
inputs = sys.argv[1:]


def pdfCombiner(pdf_list):
    # Create a merger object
    merger = PyPDF2.PdfFileMerger()
    # Loop through the pdf_list and append each PDF to the merger object
    for pdf in pdf_list:
        merger.append(pdf)
    # Write the merger object to a new file
    merger.write('super.pdf')


# Call the function and pass in the input variable (the PDF list) as the argument
pdfCombiner(inputs)
