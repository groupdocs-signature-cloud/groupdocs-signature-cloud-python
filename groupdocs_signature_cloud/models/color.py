# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Color.py">
#   Copyright (c) 2003-2022 Aspose Pty Ltd
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

class Color(object):
    """
    Keep color value
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'web': 'str',
        'alpha': 'int'
    }

    attribute_map = {
        'web': 'Web',
        'alpha': 'Alpha'
    }

    def __init__(self, web=None, alpha=None, **kwargs):  # noqa: E501
        """Initializes new instance of Color"""  # noqa: E501

        self._web = None
        self._alpha = None

        if web is not None:
            self.web = web
        if alpha is not None:
            self.alpha = alpha
    
    @property
    def web(self):
        """
        Gets the web.  # noqa: E501

        HTML string color representation  # noqa: E501

        :return: The web.  # noqa: E501
        :rtype: str
        """
        return self._web

    @web.setter
    def web(self, web):
        """
        Sets the web.

        HTML string color representation  # noqa: E501

        :param web: The web.  # noqa: E501
        :type: str
        """
        self._web = web
    
    @property
    def alpha(self):
        """
        Gets the alpha.  # noqa: E501

        Alpha component of color structure  # noqa: E501

        :return: The alpha.  # noqa: E501
        :rtype: int
        """
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        """
        Sets the alpha.

        Alpha component of color structure  # noqa: E501

        :param alpha: The alpha.  # noqa: E501
        :type: int
        """
        if alpha is None:
            raise ValueError("Invalid value for `alpha`, must not be `None`")  # noqa: E501
        self._alpha = alpha

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
        if not isinstance(other, Color):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
