import os
from pypdf import PdfMerger
class pdfMerger():
    def __init__(self, folder):
        self.folder = folder
        self.files = os.listdir(self.folder) # list of files in the folder
        print(self.files)
    def merger(self , filename = "merged"):
        # the condition to remove the extension of the file
        if filename.endswith('.pdf'):
            filename = filename[:-4]
        merger = PdfMerger()
        pdfs = [os.path.join(self.folder, pdf) for pdf in self.files if pdf.endswith('.pdf')]
        for pdf in pdfs:
            merger.append(pdf)
        output_path = os.path.join(self.folder, f"{filename}.pdf")
        merger.write(output_path)
        merger.close()
"""
    users space to test the code
"""
folder = "F:\\ME\\pdfmerger\\backupfiles" # folder defined by the user
pdfMerger(folder).merger('nelw.pdf') #.merger() method takes a name as a parameter which is optional