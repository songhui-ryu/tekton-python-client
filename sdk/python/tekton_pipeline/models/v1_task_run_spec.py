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


class V1TaskRunSpec(object):
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
        'compute_resources': 'V1ResourceRequirements',
        'debug': 'V1TaskRunDebug',
        'params': 'list[V1Param]',
        'pod_template': 'PodTemplate',
        'retries': 'int',
        'service_account_name': 'str',
        'sidecar_specs': 'list[V1TaskRunSidecarSpec]',
        'status': 'str',
        'status_message': 'str',
        'step_specs': 'list[V1TaskRunStepSpec]',
        'task_ref': 'V1TaskRef',
        'task_spec': 'V1TaskSpec',
        'timeout': 'V1Duration',
        'workspaces': 'list[V1WorkspaceBinding]'
    }

    attribute_map = {
        'compute_resources': 'computeResources',
        'debug': 'debug',
        'params': 'params',
        'pod_template': 'podTemplate',
        'retries': 'retries',
        'service_account_name': 'serviceAccountName',
        'sidecar_specs': 'sidecarSpecs',
        'status': 'status',
        'status_message': 'statusMessage',
        'step_specs': 'stepSpecs',
        'task_ref': 'taskRef',
        'task_spec': 'taskSpec',
        'timeout': 'timeout',
        'workspaces': 'workspaces'
    }

    def __init__(self, compute_resources=None, debug=None, params=None, pod_template=None, retries=None, service_account_name='', sidecar_specs=None, status=None, status_message=None, step_specs=None, task_ref=None, task_spec=None, timeout=None, workspaces=None, local_vars_configuration=None):  # noqa: E501
        """V1TaskRunSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._compute_resources = None
        self._debug = None
        self._params = None
        self._pod_template = None
        self._retries = None
        self._service_account_name = None
        self._sidecar_specs = None
        self._status = None
        self._status_message = None
        self._step_specs = None
        self._task_ref = None
        self._task_spec = None
        self._timeout = None
        self._workspaces = None
        self.discriminator = None

        if compute_resources is not None:
            self.compute_resources = compute_resources
        if debug is not None:
            self.debug = debug
        if params is not None:
            self.params = params
        if pod_template is not None:
            self.pod_template = pod_template
        if retries is not None:
            self.retries = retries
        if service_account_name is not None:
            self.service_account_name = service_account_name
        if sidecar_specs is not None:
            self.sidecar_specs = sidecar_specs
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if step_specs is not None:
            self.step_specs = step_specs
        if task_ref is not None:
            self.task_ref = task_ref
        if task_spec is not None:
            self.task_spec = task_spec
        if timeout is not None:
            self.timeout = timeout
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def compute_resources(self):
        """Gets the compute_resources of this V1TaskRunSpec.  # noqa: E501


        :return: The compute_resources of this V1TaskRunSpec.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._compute_resources

    @compute_resources.setter
    def compute_resources(self, compute_resources):
        """Sets the compute_resources of this V1TaskRunSpec.


        :param compute_resources: The compute_resources of this V1TaskRunSpec.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._compute_resources = compute_resources

    @property
    def debug(self):
        """Gets the debug of this V1TaskRunSpec.  # noqa: E501


        :return: The debug of this V1TaskRunSpec.  # noqa: E501
        :rtype: V1TaskRunDebug
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """Sets the debug of this V1TaskRunSpec.


        :param debug: The debug of this V1TaskRunSpec.  # noqa: E501
        :type: V1TaskRunDebug
        """

        self._debug = debug

    @property
    def params(self):
        """Gets the params of this V1TaskRunSpec.  # noqa: E501


        :return: The params of this V1TaskRunSpec.  # noqa: E501
        :rtype: list[V1Param]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this V1TaskRunSpec.


        :param params: The params of this V1TaskRunSpec.  # noqa: E501
        :type: list[V1Param]
        """

        self._params = params

    @property
    def pod_template(self):
        """Gets the pod_template of this V1TaskRunSpec.  # noqa: E501


        :return: The pod_template of this V1TaskRunSpec.  # noqa: E501
        :rtype: PodTemplate
        """
        return self._pod_template

    @pod_template.setter
    def pod_template(self, pod_template):
        """Sets the pod_template of this V1TaskRunSpec.


        :param pod_template: The pod_template of this V1TaskRunSpec.  # noqa: E501
        :type: PodTemplate
        """

        self._pod_template = pod_template

    @property
    def retries(self):
        """Gets the retries of this V1TaskRunSpec.  # noqa: E501

        Retries represents how many times this TaskRun should be retried in the event of task failure.  # noqa: E501

        :return: The retries of this V1TaskRunSpec.  # noqa: E501
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this V1TaskRunSpec.

        Retries represents how many times this TaskRun should be retried in the event of task failure.  # noqa: E501

        :param retries: The retries of this V1TaskRunSpec.  # noqa: E501
        :type: int
        """

        self._retries = retries

    @property
    def service_account_name(self):
        """Gets the service_account_name of this V1TaskRunSpec.  # noqa: E501


        :return: The service_account_name of this V1TaskRunSpec.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this V1TaskRunSpec.


        :param service_account_name: The service_account_name of this V1TaskRunSpec.  # noqa: E501
        :type: str
        """

        self._service_account_name = service_account_name

    @property
    def sidecar_specs(self):
        """Gets the sidecar_specs of this V1TaskRunSpec.  # noqa: E501

        Specs to apply to Sidecars in this TaskRun. If a field is specified in both a Sidecar and a SidecarSpec, the value from the SidecarSpec will be used. This field is only supported when the alpha feature gate is enabled.  # noqa: E501

        :return: The sidecar_specs of this V1TaskRunSpec.  # noqa: E501
        :rtype: list[V1TaskRunSidecarSpec]
        """
        return self._sidecar_specs

    @sidecar_specs.setter
    def sidecar_specs(self, sidecar_specs):
        """Sets the sidecar_specs of this V1TaskRunSpec.

        Specs to apply to Sidecars in this TaskRun. If a field is specified in both a Sidecar and a SidecarSpec, the value from the SidecarSpec will be used. This field is only supported when the alpha feature gate is enabled.  # noqa: E501

        :param sidecar_specs: The sidecar_specs of this V1TaskRunSpec.  # noqa: E501
        :type: list[V1TaskRunSidecarSpec]
        """

        self._sidecar_specs = sidecar_specs

    @property
    def status(self):
        """Gets the status of this V1TaskRunSpec.  # noqa: E501

        Used for cancelling a TaskRun (and maybe more later on)  # noqa: E501

        :return: The status of this V1TaskRunSpec.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1TaskRunSpec.

        Used for cancelling a TaskRun (and maybe more later on)  # noqa: E501

        :param status: The status of this V1TaskRunSpec.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this V1TaskRunSpec.  # noqa: E501

        Status message for cancellation.  # noqa: E501

        :return: The status_message of this V1TaskRunSpec.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this V1TaskRunSpec.

        Status message for cancellation.  # noqa: E501

        :param status_message: The status_message of this V1TaskRunSpec.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def step_specs(self):
        """Gets the step_specs of this V1TaskRunSpec.  # noqa: E501

        Specs to apply to Steps in this TaskRun. If a field is specified in both a Step and a StepSpec, the value from the StepSpec will be used. This field is only supported when the alpha feature gate is enabled.  # noqa: E501

        :return: The step_specs of this V1TaskRunSpec.  # noqa: E501
        :rtype: list[V1TaskRunStepSpec]
        """
        return self._step_specs

    @step_specs.setter
    def step_specs(self, step_specs):
        """Sets the step_specs of this V1TaskRunSpec.

        Specs to apply to Steps in this TaskRun. If a field is specified in both a Step and a StepSpec, the value from the StepSpec will be used. This field is only supported when the alpha feature gate is enabled.  # noqa: E501

        :param step_specs: The step_specs of this V1TaskRunSpec.  # noqa: E501
        :type: list[V1TaskRunStepSpec]
        """

        self._step_specs = step_specs

    @property
    def task_ref(self):
        """Gets the task_ref of this V1TaskRunSpec.  # noqa: E501


        :return: The task_ref of this V1TaskRunSpec.  # noqa: E501
        :rtype: V1TaskRef
        """
        return self._task_ref

    @task_ref.setter
    def task_ref(self, task_ref):
        """Sets the task_ref of this V1TaskRunSpec.


        :param task_ref: The task_ref of this V1TaskRunSpec.  # noqa: E501
        :type: V1TaskRef
        """

        self._task_ref = task_ref

    @property
    def task_spec(self):
        """Gets the task_spec of this V1TaskRunSpec.  # noqa: E501


        :return: The task_spec of this V1TaskRunSpec.  # noqa: E501
        :rtype: V1TaskSpec
        """
        return self._task_spec

    @task_spec.setter
    def task_spec(self, task_spec):
        """Sets the task_spec of this V1TaskRunSpec.


        :param task_spec: The task_spec of this V1TaskRunSpec.  # noqa: E501
        :type: V1TaskSpec
        """

        self._task_spec = task_spec

    @property
    def timeout(self):
        """Gets the timeout of this V1TaskRunSpec.  # noqa: E501


        :return: The timeout of this V1TaskRunSpec.  # noqa: E501
        :rtype: V1Duration
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this V1TaskRunSpec.


        :param timeout: The timeout of this V1TaskRunSpec.  # noqa: E501
        :type: V1Duration
        """

        self._timeout = timeout

    @property
    def workspaces(self):
        """Gets the workspaces of this V1TaskRunSpec.  # noqa: E501

        Workspaces is a list of WorkspaceBindings from volumes to workspaces.  # noqa: E501

        :return: The workspaces of this V1TaskRunSpec.  # noqa: E501
        :rtype: list[V1WorkspaceBinding]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        """Sets the workspaces of this V1TaskRunSpec.

        Workspaces is a list of WorkspaceBindings from volumes to workspaces.  # noqa: E501

        :param workspaces: The workspaces of this V1TaskRunSpec.  # noqa: E501
        :type: list[V1WorkspaceBinding]
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
        if not isinstance(other, V1TaskRunSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1TaskRunSpec):
            return True

        return self.to_dict() != other.to_dict()
