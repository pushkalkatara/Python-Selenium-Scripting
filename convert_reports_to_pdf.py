"""
A tool to convert all eLab reports into a single PDF.

Requirements:

Python == 3.6.3
img2pdf == 0.2.4

Instructions:
1. Go to the folder that holds all your eLab reports. Right-click on any report, go to Properties
and copy the Location to 'path_to_dir' as shown below.
2. Run this program.
3. A PDF with the same name as the folder will be created with all the generated reports in ordered form. 
"""

import os
import img2pdf
from os import path

def printpdf(path_to_dir):
    out_filename = path_to_dir.split('\\')[-1]
    os.chdir(path_to_dir)
    if path.exists('report.png'):
        os.rename('report.png', 'report (0).png')
    for j in range(0,10):
        if path.exists(f'report ({str(j)}).png'):
            os.rename(f'report ({str(j)}).png', f'report (0{str(j)}).png')

    with open(out_filename+'.pdf', "wb") as f:
        f.write(img2pdf.convert([i for i in os.listdir(path_to_dir) if i.endswith(".png")]))

#Go to the folder that holds all your eLab reports. Right-click on any report, go to Properties
#and copy the Location to 'path_to_dir' as shown below
path_to_dir = r"C:\Users\Issam\Desktop\ELAB\issamada"  

printpdf(path_to_dir)
