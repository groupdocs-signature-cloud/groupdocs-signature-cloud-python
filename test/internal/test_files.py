# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="TestFiles.py">
#   Copyright (c) 2018 Aspose Pty Ltd
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------

from internal.test_file import TestFile

"""Describes collection of files for tests."""

class TestFiles(object):

    # Cells Documents

    def getFile01PagesCells(self):
    
        file = TestFile()
        file.fileName = "01_pages.xlsx"
        file.folder = "storage"
        return file
    
    def getFile02PagesCells(self):
    
        file = TestFile()
        file.fileName = "02_pages.xlsx"
        file.folder = "storage"
        return file

    def getFile01PagesCellsPwd(self):
    
        file = TestFile()
        file.fileName = "01_sheet_pwd.xlsx"
        file.folder = "storage"
        file.password = "1234567890"
        file.url = ""
        return file

    def getFile01PagesCellsUrl(self):
    
        file = TestFile()
        file.fileName = "test.xlsx"
        file.url = "https://www.dropbox.com/s/enuoff7umakf6es/test.xlsx?dl=1"

        return file

    def getFileSignedCells(self):
    
        file = TestFile()
        file.fileName = "SignedForVerificationAll.xlsx"
        file.folder = "signed"
        file.password = ""
        file.url = ""
        return file
    
    def getFileSignedCellsUrl(self):
    
        file = TestFile()
        file.fileName = "SignedForVerificationAll.xlsx"
        file.url = "https://www.dropbox.com/s/o9k7gweapq8k15l/SignedForVerificationAll.xlsx?dl=1"

        return file

   # Images Documents

    def getFile01PagesDocImages(self):
    
        file = TestFile()
        file.fileName = "01_pages.png"
        file.folder = "storage"
        return file

    def getFile01PagesDocImagesUrl(self):
    
        file = TestFile()
        file.fileName = "test.png"
        file.url = "https://www.dropbox.com/s/3hbc18wympow0j1/test.png?dl=1"

        return file        

    def getFileSignedDocImages(self):
    
        file = TestFile()
        file.fileName = "SignedForVerificationAll.png"
        file.folder = "signed"
        return file

    def getFileSignedDocImagesUrl(self):
    
        file = TestFile()
        file.fileName = "SignedForVerificationAll.png"
        file.url = "https://www.dropbox.com/s/5d7a7ggmvklv1by/SignedForVerificationAll.png?dl=1"

        return file        

    # Pdf Documents 

    def getFile01PagesPdf(self):
    
        file = TestFile()
        file.fileName = "01_pages.pdf"
        file.folder = "storage"
        file.password = ""
        file.url = ""
        return file
 
    def getFile02PagesPdf(self):
    
        file = TestFile()
        file.fileName = "02_pages.pdf"
        file.folder = "storage"
        file.password = ""
        file.url = ""
        return file
 
    def getFile01PagesPdfPwd(self):
    
        file = TestFile()
        file.fileName = "01_pages_pwd.pdf"
        file.folder = "storage"
        file.password = "1234567890"
        file.url = ""
        return file
    
    def getFile01PagesPdfUrl(self):
    
        file = TestFile()
        file.fileName = "test.pdf"
        file.url = "https://www.dropbox.com/s/1ciqpmciqzdp9hu/test.pdf?dl=1"

        return file
    
    def getFileSignedPdf(self):
    
        file = TestFile()
        file.fileName = "SignedForVerificationAll.pdf"
        file.folder = "signed"
        file.password = ""
        file.url = ""
        return file
    
    def getFileSignedPdfUrl(self):
    
        file = TestFile()
        file.fileName = "SignedForVerificationAll.pdf"
        file.url = "https://www.dropbox.com/s/7yi03ieximjrh1y/SignedForVerificationAll.pdf?dl=1"

        return file

    # Slides Documents

    def getFile01PagesSlides(self):
    
        file = TestFile()
        file.fileName = "01_pages.pptx"
        file.folder = "storage"
        return file

    def getFile02PagesSlides(self):
    
        file = TestFile()
        file.fileName = "02_pages.pptx"
        file.folder = "storage"
        return file

    def getFile01PageSlidesUrl(self):
    
        file = TestFile()
        file.fileName = "test.pptx"
        file.url = "https://www.dropbox.com/s/xbfanx78371yo6m/test.pptx?dl=1"
        return file

    def getFileSignedSlides(self):
    
        file = TestFile()
        file.fileName = "SignedForVerificationAll.pptx"
        file.folder = "signed"
        file.password = ""
        file.url = ""
        return file  

    def getFileSignedSlidesUrl(self):
    
        file = TestFile()
        file.fileName = "SignedForVerificationAll.pptx"
        file.url = "https://www.dropbox.com/s/dxb9l68kevytz8e/SignedForVerificationAll.pptx?dl=1"

        return file        

    # Words Documents

    def getFile01PagesWords(self):
    
        file = TestFile()
        file.fileName = "01_pages.docx"
        file.folder = "storage"
        return file

    def getFile02PagesWords(self):
    
        file = TestFile()
        file.fileName = "02_pages.docx"
        file.folder = "storage"
        return file

    def getFile01PagesPwdWords(self):
    
        file = TestFile()
        file.fileName = "01_pages_pwd.docx"
        file.folder = "storage"
        file.password = "1234567890"
        return file

    def getFile01PagesWordsUrl(self):
    
        file = TestFile()
        file.fileName = "test.docx"
        file.url = "https://www.dropbox.com/s/j260ve4f90h1p41/test.docx?dl=1"

        return file
    
    def getFileSignedWords(self):
    
        file = TestFile()
        file.fileName = "SignedForVerificationAll.docx"
        file.folder = "signed"
        file.password = ""
        file.url = ""
        return file    

    def getFileSignedWordsUrl(self):
    
        file = TestFile()
        file.fileName = "SignedForVerificationAll.docx"
        file.url = "https://www.dropbox.com/s/zukdkxpuul0p8gm/SignedForVerificationAll.docx?dl=1"

        return file             


    def getAllSignedFiles(self):
        result = []
        result.append(self.getFileSignedCells())
        result.append(self.getFileSignedDocImages())
        result.append(self.getFileSignedPdf())
        result.append(self.getFileSignedSlides())
        result.append(self.getFileSignedWords())

        return result

    def getAllStorageFiles(self):
        result = []
        result.append(self.getFile01PagesCells())
        result.append(self.getFile02PagesCells())
        result.append(self.getFile01PagesCellsPwd())
        result.append(self.getFile01PagesDocImages())
        result.append(self.getFile01PagesPdf())
        result.append(self.getFile02PagesPdf())
        result.append(self.getFile01PagesPdfPwd())
        result.append(self.getFile01PagesSlides())
        result.append(self.getFile02PagesSlides())
        result.append(self.getFile01PagesWords())
        result.append(self.getFile02PagesWords())
        result.append(self.getFile01PagesPwdWords())

        return result

    # Certificates

    def GetDigitalPfx(self):
    
        file = TestFile()
        file.fileName = "SherlockHolmes.pfx"
        file.folder = "certificates"
        return file

    def GetDigitalPfxRsa(self):
    
        file = TestFile()
        file.fileName = "test_rsa_sha1_1024.pfx"
        file.folder = "certificates"
        return file
    
    def GetDigitalCerRsa(self):
    
        file = TestFile()
        file.fileName = "test_rsa_sha1_1024.cer"
        file.folder = "certificates"
        return file
    
    def getAllCertificatesFiles(self):
        result = []
        result.append(self.GetDigitalPfx())
        result.append(self.GetDigitalPfxRsa())
        result.append(self.GetDigitalCerRsa())

        return result
    
    # Image Documents
    def GetImage00(self):
    
        file = TestFile()
        file.fileName = "JohnSmithSign.png"
        file.folder = "images"
        return file
 
    def GetImage01(self):
    
        file = TestFile()
        file.fileName = "signature_01.jpg"
        file.folder = "images"
        return file
    
    def GetImage02(self):
    
        file = TestFile()
        file.fileName = "signature_02.jpg"
        file.folder = "images"
        return file

    def GetImage03(self):
    
        file = TestFile()
        file.fileName = "signature_03.jpg"
        file.folder = "images"
        return file
    
    def getAllImagesFiles(self):
        result = []
        result.append(self.GetImage00())
        result.append(self.GetImage01())
        result.append(self.GetImage02())
        result.append(self.GetImage03())

        return result
