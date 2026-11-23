# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_image_digital_options.py">
#   Copyright (c) Aspose Pty Ltd
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

from groupdocs_signature_cloud import (DeleteOptions, OptionsBase, PdfDigitalSignatureAppearance,
                                       Signature, SignImageDigitalOptions, SignOptions, UpdateOptions,
                                       VerifyImageDigitalOptions, VerifyOptions)
from groupdocs_signature_cloud.api_client import ApiClient
from groupdocs_signature_cloud.configuration import Configuration


class TestImageDigitalOptions(unittest.TestCase):
    """ImageDigital models unit tests (do not require a cloud connection)"""

    def test_sign_options(self):
        options = SignImageDigitalOptions(password="embed-password", signature_type="ImageDigital")
        self.assertIsInstance(options, SignOptions)
        self.assertEqual("embed-password", options.password)
        self.assertEqual("ImageDigital", options.signature_type)

    def test_sign_options_serialization(self):
        options = SignImageDigitalOptions(password="embed-password", signature_type="ImageDigital")
        data = ApiClient(Configuration("sid", "key")).sanitize_for_serialization(options)
        self.assertEqual("embed-password", data["Password"])
        self.assertEqual("ImageDigital", data["SignatureType"])

    def test_verify_options(self):
        options = VerifyImageDigitalOptions(password="embed-password", detection_threshold_percent=75,
                                            use_full_data_extraction=True, signature_type="ImageDigital")
        self.assertIsInstance(options, VerifyOptions)
        self.assertEqual("embed-password", options.password)
        self.assertEqual(75, options.detection_threshold_percent)
        self.assertTrue(options.use_full_data_extraction)

    def test_verify_options_serialization(self):
        options = VerifyImageDigitalOptions(password="embed-password", detection_threshold_percent=75,
                                            use_full_data_extraction=True, signature_type="ImageDigital")
        data = ApiClient(Configuration("sid", "key")).sanitize_for_serialization(options)
        self.assertEqual("embed-password", data["Password"])
        self.assertEqual(75, data["DetectionThresholdPercent"])
        self.assertEqual(True, data["UseFullDataExtraction"])
        self.assertEqual("ImageDigital", data["SignatureType"])

    def test_image_digital_signature_type_is_supported(self):
        for model in (OptionsBase, DeleteOptions, UpdateOptions, Signature):
            instance = model(signature_type="ImageDigital")
            self.assertEqual("ImageDigital", instance.signature_type)

    def test_image_digital_signature_type_by_index(self):
        # the service may return enum as a number, ImageDigital is the last item of the enum
        self.assertEqual("ImageDigital", OptionsBase(signature_type="9").signature_type)

    def test_unknown_signature_type_is_rejected(self):
        with self.assertRaises(ValueError):
            OptionsBase(signature_type="Unknown")

    def test_foreground_image_appearance(self):
        appearance = PdfDigitalSignatureAppearance(is_foreground_image=True)
        self.assertTrue(appearance.is_foreground_image)
        data = ApiClient(Configuration("sid", "key")).sanitize_for_serialization(appearance)
        self.assertEqual(True, data["IsForegroundImage"])


if __name__ == '__main__':
    unittest.main()
