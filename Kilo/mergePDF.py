# Merges the listed pdf files into a single pdf file :)

from pypdf import PdfWriter as p

merger = p()
for pdf in ["Kilo/file1.pdf", "Kilo/file2.pdf", "Kilo/file3.pdf"]:
    merger.append(pdf)

merger.write("pdf/merged-pdf.pdf")
merger.close()