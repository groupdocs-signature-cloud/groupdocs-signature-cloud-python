# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="VerifyImageDigitalOptions.py">
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

import pprint
import re  # noqa: F401

import six

from groupdocs_signature_cloud.models import VerifyOptions

class VerifyImageDigitalOptions(VerifyOptions):
    """
    Defines options to verify ImageDigital signature within a document
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'password': 'str',
        'detection_threshold_percent': 'int',
        'use_full_data_extraction': 'bool'
    }

    attribute_map = {
        'password': 'Password',
        'detection_threshold_percent': 'DetectionThresholdPercent',
        'use_full_data_extraction': 'UseFullDataExtraction'
    }

    def __init__(self, password=None, detection_threshold_percent=None, use_full_data_extraction=None, **kwargs):  # noqa: E501
        """Initializes new instance of VerifyImageDigitalOptions"""  # noqa: E501

        self._password = None
        self._detection_threshold_percent = None
        self._use_full_data_extraction = None

        if password is not None:
            self.password = password
        if detection_threshold_percent is not None:
            self.detection_threshold_percent = detection_threshold_percent
        if use_full_data_extraction is not None:
            self.use_full_data_extraction = use_full_data_extraction

        base = super(VerifyImageDigitalOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def password(self):
        """
        Gets the password.  # noqa: E501

        Gets or sets the password used to embed the signature.  # noqa: E501

        :return: The password.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password.

        Gets or sets the password used to embed the signature.  # noqa: E501

        :param password: The password.  # noqa: E501
        :type: str
        """
        self._password = password
    
    @property
    def detection_threshold_percent(self):
        """
        Gets the detection_threshold_percent.  # noqa: E501

        Gets or sets the detection threshold percentage (0-100).  # noqa: E501

        :return: The detection_threshold_percent.  # noqa: E501
        :rtype: int
        """
        return self._detection_threshold_percent

    @detection_threshold_percent.setter
    def detection_threshold_percent(self, detection_threshold_percent):
        """
        Sets the detection_threshold_percent.

        Gets or sets the detection threshold percentage (0-100).  # noqa: E501

        :param detection_threshold_percent: The detection_threshold_percent.  # noqa: E501
        :type: int
        """
        self._detection_threshold_percent = detection_threshold_percent
    
    @property
    def use_full_data_extraction(self):
        """
        Gets the use_full_data_extraction.  # noqa: E501

        Gets or sets whether to use full data extraction for maximum accuracy.  # noqa: E501

        :return: The use_full_data_extraction.  # noqa: E501
        :rtype: bool
        """
        return self._use_full_data_extraction

    @use_full_data_extraction.setter
    def use_full_data_extraction(self, use_full_data_extraction):
        """
        Sets the use_full_data_extraction.

        Gets or sets whether to use full data extraction for maximum accuracy.  # noqa: E501

        :param use_full_data_extraction: The use_full_data_extraction.  # noqa: E501
        :type: bool
        """
        self._use_full_data_extraction = use_full_data_extraction

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VerifyImageDigitalOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
