
from FileWriterPermissiver import canWriteToFile

def mergePdf(pdfs, resultPath):
    from PyPDF2 import PdfFileMerger

    merger = PdfFileMerger()

    for pdf in pdfs:
        print("Adding " + pdf) 
        merger.append(pdf)

    if canWriteToFile(resultPath):
        merger.write(resultPath)
        merger.close()

import sys
import os.path
droppedFiles = []
for f in sys.argv[1:]:
    if os.path.isfile(f) and f.endswith('.pdf'):
        droppedFiles.append(f)
    else:
        print("Not a pdf file: " + f)

if droppedFiles:
    mergePdf(droppedFiles, os.path.join(os.getcwd(),"merged.pdf"))