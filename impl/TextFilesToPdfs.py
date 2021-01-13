from fpdf import FPDF 
import os.path
import textwrap
from FileWriterPermissiver import canWriteToFile

def text_to_pdf(text, filename):
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    # file = open(filename, 'w+')
    if canWriteToFile(filename):
        pdf.output(filename, 'F')
        print("File ", filename, " successfully saved")
    else:
        print("Cannot save file ", filename)


import sys
droppedFiles = [f for f in sys.argv[1:] if os.path.isfile(f)]

for file in droppedFiles:
    base = os.path.basename(file);   
    print("Converting " + base) 
    f = open(file, "r") 
    text_to_pdf(f.read(), os.path.join(os.getcwd(), os.path.splitext(base)[0] + ".pdf"))