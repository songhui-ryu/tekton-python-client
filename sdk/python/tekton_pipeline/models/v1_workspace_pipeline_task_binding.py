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

    The version of the OpenAPI document: v0.17.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tekton_pipeline.configuration import Configuration


class V1WorkspacePipelineTaskBinding(object):
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
        'name': 'str',
        'sub_path': 'str',
        'workspace': 'str'
    }

    attribute_map = {
        'name': 'name',
        'sub_path': 'subPath',
        'workspace': 'workspace'
    }

    def __init__(self, name='', sub_path=None, workspace=None, local_vars_configuration=None):  # noqa: E501
        """V1WorkspacePipelineTaskBinding - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._sub_path = None
        self._workspace = None
        self.discriminator = None

        self.name = name
        if sub_path is not None:
            self.sub_path = sub_path
        if workspace is not None:
            self.workspace = workspace

    @property
    def name(self):
        """Gets the name of this V1WorkspacePipelineTaskBinding.  # noqa: E501

        Name is the name of the workspace as declared by the task  # noqa: E501

        :return: The name of this V1WorkspacePipelineTaskBinding.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1WorkspacePipelineTaskBinding.

        Name is the name of the workspace as declared by the task  # noqa: E501

        :param name: The name of this V1WorkspacePipelineTaskBinding.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def sub_path(self):
        """Gets the sub_path of this V1WorkspacePipelineTaskBinding.  # noqa: E501

        SubPath is optionally a directory on the volume which should be used for this binding (i.e. the volume will be mounted at this sub directory).  # noqa: E501

        :return: The sub_path of this V1WorkspacePipelineTaskBinding.  # noqa: E501
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        """Sets the sub_path of this V1WorkspacePipelineTaskBinding.

        SubPath is optionally a directory on the volume which should be used for this binding (i.e. the volume will be mounted at this sub directory).  # noqa: E501

        :param sub_path: The sub_path of this V1WorkspacePipelineTaskBinding.  # noqa: E501
        :type: str
        """

        self._sub_path = sub_path

    @property
    def workspace(self):
        """Gets the workspace of this V1WorkspacePipelineTaskBinding.  # noqa: E501

        Workspace is the name of the workspace declared by the pipeline  # noqa: E501

        :return: The workspace of this V1WorkspacePipelineTaskBinding.  # noqa: E501
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this V1WorkspacePipelineTaskBinding.

        Workspace is the name of the workspace declared by the pipeline  # noqa: E501

        :param workspace: The workspace of this V1WorkspacePipelineTaskBinding.  # noqa: E501
        :type: str
        """

        self._workspace = workspace

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
        if not isinstance(other, V1WorkspacePipelineTaskBinding):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1WorkspacePipelineTaskBinding):
            return True

        return self.to_dict() != other.to_dict()
