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


class V1EmbeddedTask(object):
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
        'api_version': 'str',
        'description': 'str',
        'display_name': 'str',
        'kind': 'str',
        'metadata': 'V1PipelineTaskMetadata',
        'params': 'list[V1ParamSpec]',
        'results': 'list[V1TaskResult]',
        'sidecars': 'list[V1Sidecar]',
        'spec': 'K8sIoApimachineryPkgRuntimeRawExtension',
        'step_template': 'V1StepTemplate',
        'steps': 'list[V1Step]',
        'volumes': 'list[V1Volume]',
        'workspaces': 'list[V1WorkspaceDeclaration]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'description': 'description',
        'display_name': 'displayName',
        'kind': 'kind',
        'metadata': 'metadata',
        'params': 'params',
        'results': 'results',
        'sidecars': 'sidecars',
        'spec': 'spec',
        'step_template': 'stepTemplate',
        'steps': 'steps',
        'volumes': 'volumes',
        'workspaces': 'workspaces'
    }

    def __init__(self, api_version=None, description=None, display_name=None, kind=None, metadata=None, params=None, results=None, sidecars=None, spec=None, step_template=None, steps=None, volumes=None, workspaces=None, local_vars_configuration=None):  # noqa: E501
        """V1EmbeddedTask - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._description = None
        self._display_name = None
        self._kind = None
        self._metadata = None
        self._params = None
        self._results = None
        self._sidecars = None
        self._spec = None
        self._step_template = None
        self._steps = None
        self._volumes = None
        self._workspaces = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if params is not None:
            self.params = params
        if results is not None:
            self.results = results
        if sidecars is not None:
            self.sidecars = sidecars
        if spec is not None:
            self.spec = spec
        if step_template is not None:
            self.step_template = step_template
        if steps is not None:
            self.steps = steps
        if volumes is not None:
            self.volumes = volumes
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def api_version(self):
        """Gets the api_version of this V1EmbeddedTask.  # noqa: E501


        :return: The api_version of this V1EmbeddedTask.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1EmbeddedTask.


        :param api_version: The api_version of this V1EmbeddedTask.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def description(self):
        """Gets the description of this V1EmbeddedTask.  # noqa: E501

        Description is a user-facing description of the task that may be used to populate a UI.  # noqa: E501

        :return: The description of this V1EmbeddedTask.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1EmbeddedTask.

        Description is a user-facing description of the task that may be used to populate a UI.  # noqa: E501

        :param description: The description of this V1EmbeddedTask.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this V1EmbeddedTask.  # noqa: E501

        DisplayName is a user-facing name of the task that may be used to populate a UI.  # noqa: E501

        :return: The display_name of this V1EmbeddedTask.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this V1EmbeddedTask.

        DisplayName is a user-facing name of the task that may be used to populate a UI.  # noqa: E501

        :param display_name: The display_name of this V1EmbeddedTask.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def kind(self):
        """Gets the kind of this V1EmbeddedTask.  # noqa: E501


        :return: The kind of this V1EmbeddedTask.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1EmbeddedTask.


        :param kind: The kind of this V1EmbeddedTask.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this V1EmbeddedTask.  # noqa: E501


        :return: The metadata of this V1EmbeddedTask.  # noqa: E501
        :rtype: V1PipelineTaskMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1EmbeddedTask.


        :param metadata: The metadata of this V1EmbeddedTask.  # noqa: E501
        :type: V1PipelineTaskMetadata
        """

        self._metadata = metadata

    @property
    def params(self):
        """Gets the params of this V1EmbeddedTask.  # noqa: E501

        Params is a list of input parameters required to run the task. Params must be supplied as inputs in TaskRuns unless they declare a default value.  # noqa: E501

        :return: The params of this V1EmbeddedTask.  # noqa: E501
        :rtype: list[V1ParamSpec]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this V1EmbeddedTask.

        Params is a list of input parameters required to run the task. Params must be supplied as inputs in TaskRuns unless they declare a default value.  # noqa: E501

        :param params: The params of this V1EmbeddedTask.  # noqa: E501
        :type: list[V1ParamSpec]
        """

        self._params = params

    @property
    def results(self):
        """Gets the results of this V1EmbeddedTask.  # noqa: E501

        Results are values that this Task can output  # noqa: E501

        :return: The results of this V1EmbeddedTask.  # noqa: E501
        :rtype: list[V1TaskResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this V1EmbeddedTask.

        Results are values that this Task can output  # noqa: E501

        :param results: The results of this V1EmbeddedTask.  # noqa: E501
        :type: list[V1TaskResult]
        """

        self._results = results

    @property
    def sidecars(self):
        """Gets the sidecars of this V1EmbeddedTask.  # noqa: E501

        Sidecars are run alongside the Task's step containers. They begin before the steps start and end after the steps complete.  # noqa: E501

        :return: The sidecars of this V1EmbeddedTask.  # noqa: E501
        :rtype: list[V1Sidecar]
        """
        return self._sidecars

    @sidecars.setter
    def sidecars(self, sidecars):
        """Sets the sidecars of this V1EmbeddedTask.

        Sidecars are run alongside the Task's step containers. They begin before the steps start and end after the steps complete.  # noqa: E501

        :param sidecars: The sidecars of this V1EmbeddedTask.  # noqa: E501
        :type: list[V1Sidecar]
        """

        self._sidecars = sidecars

    @property
    def spec(self):
        """Gets the spec of this V1EmbeddedTask.  # noqa: E501


        :return: The spec of this V1EmbeddedTask.  # noqa: E501
        :rtype: K8sIoApimachineryPkgRuntimeRawExtension
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this V1EmbeddedTask.


        :param spec: The spec of this V1EmbeddedTask.  # noqa: E501
        :type: K8sIoApimachineryPkgRuntimeRawExtension
        """

        self._spec = spec

    @property
    def step_template(self):
        """Gets the step_template of this V1EmbeddedTask.  # noqa: E501


        :return: The step_template of this V1EmbeddedTask.  # noqa: E501
        :rtype: V1StepTemplate
        """
        return self._step_template

    @step_template.setter
    def step_template(self, step_template):
        """Sets the step_template of this V1EmbeddedTask.


        :param step_template: The step_template of this V1EmbeddedTask.  # noqa: E501
        :type: V1StepTemplate
        """

        self._step_template = step_template

    @property
    def steps(self):
        """Gets the steps of this V1EmbeddedTask.  # noqa: E501

        Steps are the steps of the build; each step is run sequentially with the source mounted into /workspace.  # noqa: E501

        :return: The steps of this V1EmbeddedTask.  # noqa: E501
        :rtype: list[V1Step]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this V1EmbeddedTask.

        Steps are the steps of the build; each step is run sequentially with the source mounted into /workspace.  # noqa: E501

        :param steps: The steps of this V1EmbeddedTask.  # noqa: E501
        :type: list[V1Step]
        """

        self._steps = steps

    @property
    def volumes(self):
        """Gets the volumes of this V1EmbeddedTask.  # noqa: E501

        Volumes is a collection of volumes that are available to mount into the steps of the build.  # noqa: E501

        :return: The volumes of this V1EmbeddedTask.  # noqa: E501
        :rtype: list[V1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this V1EmbeddedTask.

        Volumes is a collection of volumes that are available to mount into the steps of the build.  # noqa: E501

        :param volumes: The volumes of this V1EmbeddedTask.  # noqa: E501
        :type: list[V1Volume]
        """

        self._volumes = volumes

    @property
    def workspaces(self):
        """Gets the workspaces of this V1EmbeddedTask.  # noqa: E501

        Workspaces are the volumes that this Task requires.  # noqa: E501

        :return: The workspaces of this V1EmbeddedTask.  # noqa: E501
        :rtype: list[V1WorkspaceDeclaration]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        """Sets the workspaces of this V1EmbeddedTask.

        Workspaces are the volumes that this Task requires.  # noqa: E501

        :param workspaces: The workspaces of this V1EmbeddedTask.  # noqa: E501
        :type: list[V1WorkspaceDeclaration]
        """

        self._workspaces = workspaces

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
        if not isinstance(other, V1EmbeddedTask):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1EmbeddedTask):
            return True

        return self.to_dict() != other.to_dict()
