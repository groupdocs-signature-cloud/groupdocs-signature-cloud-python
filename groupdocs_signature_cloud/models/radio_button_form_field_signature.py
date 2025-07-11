# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="RadioButtonFormFieldSignature.py">
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

from groupdocs_signature_cloud.models import FormFieldSignature

class RadioButtonFormFieldSignature(FormFieldSignature):
    """
    Contains radio-button input form field signature properties
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'selected': 'str',
        'items': 'list[str]'
    }

    attribute_map = {
        'selected': 'Selected',
        'items': 'Items'
    }

    def __init__(self, selected=None, items=None, **kwargs):  # noqa: E501
        """Initializes new instance of RadioButtonFormFieldSignature"""  # noqa: E501

        self._selected = None
        self._items = None

        if selected is not None:
            self.selected = selected
        if items is not None:
            self.items = items

        base = super(RadioButtonFormFieldSignature, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def selected(self):
        """
        Gets the selected.  # noqa: E501

        Get or set selected value  # noqa: E501

        :return: The selected.  # noqa: E501
        :rtype: str
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """
        Sets the selected.

        Get or set selected value  # noqa: E501

        :param selected: The selected.  # noqa: E501
        :type: str
        """
        self._selected = selected
    
    @property
    def items(self):
        """
        Gets the items.  # noqa: E501

        Get or set radio options list  # noqa: E501

        :return: The items.  # noqa: E501
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items.

        Get or set radio options list  # noqa: E501

        :param items: The items.  # noqa: E501
        :type: list[str]
        """
        self._items = items

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
        if not isinstance(other, RadioButtonFormFieldSignature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
