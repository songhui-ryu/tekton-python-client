# Copyright 2021 The Tekton Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Tekton

    Tekton Pipeline  # noqa: E501

    The version of the OpenAPI document: v0.49.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tekton_pipeline.configuration import Configuration


class V1RefSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'digest': 'dict(str, str)',
        'entry_point': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'digest': 'digest',
        'entry_point': 'entryPoint',
        'uri': 'uri'
    }

    def __init__(self, digest=None, entry_point=None, uri=None, local_vars_configuration=None):  # noqa: E501
        """V1RefSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._digest = None
        self._entry_point = None
        self._uri = None
        self.discriminator = None

        if digest is not None:
            self.digest = digest
        if entry_point is not None:
            self.entry_point = entry_point
        if uri is not None:
            self.uri = uri

    @property
    def digest(self):
        """Gets the digest of this V1RefSource.  # noqa: E501

        Digest is a collection of cryptographic digests for the contents of the artifact specified by URI. Example: {\"sha1\": \"f99d13e554ffcb696dee719fa85b695cb5b0f428\"}  # noqa: E501

        :return: The digest of this V1RefSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this V1RefSource.

        Digest is a collection of cryptographic digests for the contents of the artifact specified by URI. Example: {\"sha1\": \"f99d13e554ffcb696dee719fa85b695cb5b0f428\"}  # noqa: E501

        :param digest: The digest of this V1RefSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._digest = digest

    @property
    def entry_point(self):
        """Gets the entry_point of this V1RefSource.  # noqa: E501

        EntryPoint identifies the entry point into the build. This is often a path to a build definition file and/or a target label within that file. Example: \"task/git-clone/0.8/git-clone.yaml\"  # noqa: E501

        :return: The entry_point of this V1RefSource.  # noqa: E501
        :rtype: str
        """
        return self._entry_point

    @entry_point.setter
    def entry_point(self, entry_point):
        """Sets the entry_point of this V1RefSource.

        EntryPoint identifies the entry point into the build. This is often a path to a build definition file and/or a target label within that file. Example: \"task/git-clone/0.8/git-clone.yaml\"  # noqa: E501

        :param entry_point: The entry_point of this V1RefSource.  # noqa: E501
        :type: str
        """

        self._entry_point = entry_point

    @property
    def uri(self):
        """Gets the uri of this V1RefSource.  # noqa: E501

        URI indicates the identity of the source of the build definition. Example: \"https://github.com/tektoncd/catalog\"  # noqa: E501

        :return: The uri of this V1RefSource.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this V1RefSource.

        URI indicates the identity of the source of the build definition. Example: \"https://github.com/tektoncd/catalog\"  # noqa: E501

        :param uri: The uri of this V1RefSource.  # noqa: E501
        :type: str
        """

        self._uri = uri

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, V1RefSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1RefSource):
            return True

        return self.to_dict() != other.to_dict()
