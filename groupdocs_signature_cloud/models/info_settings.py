# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="InfoSettings.py">
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

from groupdocs_signature_cloud.models import BaseSettings

class InfoSettings(BaseSettings):
    """
    Defines document information request settings
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'show_deleted_signatures_info': 'bool'
    }

    attribute_map = {
        'show_deleted_signatures_info': 'ShowDeletedSignaturesInfo'
    }

    def __init__(self, show_deleted_signatures_info=None, **kwargs):  # noqa: E501
        """Initializes new instance of InfoSettings"""  # noqa: E501

        self._show_deleted_signatures_info = None

        if show_deleted_signatures_info is not None:
            self.show_deleted_signatures_info = show_deleted_signatures_info

        base = super(InfoSettings, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def show_deleted_signatures_info(self):
        """
        Gets the show_deleted_signatures_info.  # noqa: E501

        Gets or sets flag that includes deleted signatures into Document Info result.  # noqa: E501

        :return: The show_deleted_signatures_info.  # noqa: E501
        :rtype: bool
        """
        return self._show_deleted_signatures_info

    @show_deleted_signatures_info.setter
    def show_deleted_signatures_info(self, show_deleted_signatures_info):
        """
        Sets the show_deleted_signatures_info.

        Gets or sets flag that includes deleted signatures into Document Info result.  # noqa: E501

        :param show_deleted_signatures_info: The show_deleted_signatures_info.  # noqa: E501
        :type: bool
        """
        if show_deleted_signatures_info is None:
            raise ValueError("Invalid value for `show_deleted_signatures_info`, must not be `None`")  # noqa: E501
        self._show_deleted_signatures_info = show_deleted_signatures_info

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
        if not isinstance(other, InfoSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
