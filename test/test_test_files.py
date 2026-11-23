# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_test_files.py">
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

import os
import unittest

from test.test_context import TestContext
from test.test_file import TestFile


class TestTestFiles(unittest.TestCase):
    """Checks that test files are described in an OS independent way (no cloud connection required)"""

    def test_remote_paths_use_forward_slashes(self):
        for test_file in TestFile.get_test_files() + [TestFile.not_exist()]:
            self.assertNotIn("\\", test_file.FilePath())
            self.assertTrue(test_file.folder.endswith("/"), test_file.folder)

    def test_local_files_exist(self):
        # the same code resolves test files on Windows, Linux and macOS (case-sensitive file systems included)
        context = TestContext("get_test_file_path")
        for test_file in TestFile.get_test_files():
            path = context.get_test_file_path(test_file)
            self.assertTrue(os.path.isabs(path), path)
            self.assertTrue(os.path.isfile(path), path)

    def test_local_path_does_not_depend_on_working_directory(self):
        context = TestContext("get_test_file_path")
        test_file = TestFile.pdf_one_page()
        expected = context.get_test_file_path(test_file)
        current = os.getcwd()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        try:
            self.assertEqual(expected, context.get_test_file_path(test_file))
        finally:
            os.chdir(current)

    def test_sizes_of_signed_files_match(self):
        context = TestContext("get_test_file_path")
        for test_file in TestFile.get_test_files():
            if hasattr(test_file, "size"):
                self.assertEqual(test_file.size, os.path.getsize(context.get_test_file_path(test_file)), test_file.FilePath())


if __name__ == '__main__':
    unittest.main()
