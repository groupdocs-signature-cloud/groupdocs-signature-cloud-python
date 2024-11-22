# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd">
#   Copyright (c) 2003-2023 Aspose Pty Ltd
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

from __future__ import absolute_import

import unittest
import os

from groupdocs_signature_cloud import *
from test.test_context import TestContext
from test.test_file import TestFile

class TestSearchCollection(TestContext):

    def test_search_collection_image(self):
        test_file = TestFile.image_signed()
        opts1 = SearchBarcodeOptions()
        self.populate_barcode_options(opts1)
        opts2 = SearchQRCodeOptions()
        self.populate_qr_code_options(opts2)
        settings = SearchSettings()
        settings.file_info = test_file.ToFileInfo()
        settings.options = [opts1, opts2]
        response = self.sign_api.search_signatures(SearchSignaturesRequest(settings))
        self.check_response([opts1, opts2], response, test_file)

    def test_search_collection_pdf(self):
        test_file = TestFile.pdf_signed()
        opts1 = SearchBarcodeOptions()
        self.populate_barcode_options(opts1)
        opts2 = SearchQRCodeOptions()
        self.populate_qr_code_options(opts2)
        opts3 = SearchDigitalOptions()
        opts3.signature_type = 'Digital'
        settings = SearchSettings()
        settings.file_info = test_file.ToFileInfo()
        settings.options = [opts1, opts2, opts3]
        response = self.sign_api.search_signatures(SearchSignaturesRequest(settings))
        self.check_response([opts1, opts2, opts3], response, test_file)

    def test_search_collection_presentation(self):
        test_file = TestFile.presentation_signed()
        opts1 = SearchBarcodeOptions()
        self.populate_barcode_options(opts1)
        opts2 = SearchQRCodeOptions()
        self.populate_qr_code_options(opts2)
        settings = SearchSettings()
        settings.file_info = test_file.ToFileInfo()
        settings.options = [opts1, opts2]
        response = self.sign_api.search_signatures(SearchSignaturesRequest(settings))
        self.check_response([opts1, opts2], response, test_file)         

    def test_search_collection_spreadsheet(self):
        test_file = TestFile.spreadsheet_signed()
        opts1 = SearchBarcodeOptions()
        self.populate_barcode_options(opts1)
        opts2 = SearchQRCodeOptions()
        self.populate_qr_code_options(opts2)
        opts3 = SearchDigitalOptions()
        opts3.signature_type = 'Digital'
        settings = SearchSettings()
        settings.file_info = test_file.ToFileInfo()
        settings.options = [opts1, opts2, opts3]
        response = self.sign_api.search_signatures(SearchSignaturesRequest(settings))
        self.check_response([opts1, opts2, opts3], response, test_file)        

    def test_search_collection_wordprocessing(self):
        test_file = TestFile.wordprocessing_signed()
        opts1 = SearchBarcodeOptions()
        self.populate_barcode_options(opts1)
        opts2 = SearchQRCodeOptions()
        self.populate_qr_code_options(opts2)
        opts3 = SearchDigitalOptions()
        opts3.signature_type = 'Digital'
        settings = SearchSettings()
        settings.file_info = test_file.ToFileInfo()
        settings.options = [opts1, opts2, opts3]
        response = self.sign_api.search_signatures(SearchSignaturesRequest(settings))
        self.check_response([opts1, opts2, opts3], response, test_file)                                    

    @staticmethod
    def populate_barcode_options(opts):
        opts.page = 1
        opts.all_pages = True
        ps = PagesSetup()
        ps.even_pages = False
        ps.first_page = True
        ps.last_page = False
        ps.odd_pages = False
        ps.page_numbers = [1]
        opts.pages_setup = ps
        opts.signature_type = 'Barcode'
        opts.barcode_type = 'Code39'
        opts.text = '123456789012'
        opts.match_type = 'Contains'

    @staticmethod
    def populate_qr_code_options(opts):
        opts.page = 1
        opts.all_pages = True
        ps = PagesSetup()
        ps.even_pages = False
        ps.first_page = True
        ps.last_page = False
        ps.odd_pages = False
        ps.page_numbers = [1]
        opts.pages_setup = ps
        opts.signature_type = 'QRCode'
        opts.qr_code_type = 'Aztec'
        opts.text = 'John Smith'
        opts.match_type = 'Contains'        
    
    def check_response(self, opts, response, test_file):
        self.assertTrue(response)
        self.assertEqual(response.size, test_file.size)
        self.assertTrue(response.file_info)
        self.assertEqual(response.file_info.file_path, test_file.FilePath())
        self.assertTrue(response.signatures)
        self.assertGreater(len(response.signatures), 0)
        for opt in opts:
            exists = False
            for signature in response.signatures:
                if (signature.signature_type == opt.signature_type):
                    exists = True
                    break
            self.assertTrue(exists)

if __name__ == '__main__':
    unittest.main()
