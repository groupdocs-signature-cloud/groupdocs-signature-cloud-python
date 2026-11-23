# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_settings.py">
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

import os


def _setting(name, default):
    """Returns value of the environment variable if it is set and not empty, default value otherwise."""
    value = os.environ.get(name)
    return value if value else default


class TestSettings:
    # Get your AppSID and AppKey at https://dashboard.groupdocs.cloud (free registration is required).
    # Values can be overridden with TEST_APP_SID, TEST_APP_KEY and TEST_API_BASE_URL environment variables.
    APP_SID = _setting("TEST_APP_SID", "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX")
    APP_KEY = _setting("TEST_APP_KEY", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    API_BASE_URL = _setting("TEST_API_BASE_URL", "https://api.groupdocs.cloud")
