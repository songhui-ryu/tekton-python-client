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


class V1Step(object):
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
        'args': 'list[str]',
        'command': 'list[str]',
        'compute_resources': 'V1ResourceRequirements',
        'env': 'list[V1EnvVar]',
        'env_from': 'list[V1EnvFromSource]',
        'image': 'str',
        'image_pull_policy': 'str',
        'name': 'str',
        'on_error': 'str',
        'script': 'str',
        'security_context': 'V1SecurityContext',
        'stderr_config': 'V1StepOutputConfig',
        'stdout_config': 'V1StepOutputConfig',
        'timeout': 'V1Duration',
        'volume_devices': 'list[V1VolumeDevice]',
        'volume_mounts': 'list[V1VolumeMount]',
        'working_dir': 'str',
        'workspaces': 'list[V1WorkspaceUsage]'
    }

    attribute_map = {
        'args': 'args',
        'command': 'command',
        'compute_resources': 'computeResources',
        'env': 'env',
        'env_from': 'envFrom',
        'image': 'image',
        'image_pull_policy': 'imagePullPolicy',
        'name': 'name',
        'on_error': 'onError',
        'script': 'script',
        'security_context': 'securityContext',
        'stderr_config': 'stderrConfig',
        'stdout_config': 'stdoutConfig',
        'timeout': 'timeout',
        'volume_devices': 'volumeDevices',
        'volume_mounts': 'volumeMounts',
        'working_dir': 'workingDir',
        'workspaces': 'workspaces'
    }

    def __init__(self, args=None, command=None, compute_resources=None, env=None, env_from=None, image=None, image_pull_policy=None, name='', on_error=None, script=None, security_context=None, stderr_config=None, stdout_config=None, timeout=None, volume_devices=None, volume_mounts=None, working_dir=None, workspaces=None, local_vars_configuration=None):  # noqa: E501
        """V1Step - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._args = None
        self._command = None
        self._compute_resources = None
        self._env = None
        self._env_from = None
        self._image = None
        self._image_pull_policy = None
        self._name = None
        self._on_error = None
        self._script = None
        self._security_context = None
        self._stderr_config = None
        self._stdout_config = None
        self._timeout = None
        self._volume_devices = None
        self._volume_mounts = None
        self._working_dir = None
        self._workspaces = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if command is not None:
            self.command = command
        if compute_resources is not None:
            self.compute_resources = compute_resources
        if env is not None:
            self.env = env
        if env_from is not None:
            self.env_from = env_from
        if image is not None:
            self.image = image
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        self.name = name
        if on_error is not None:
            self.on_error = on_error
        if script is not None:
            self.script = script
        if security_context is not None:
            self.security_context = security_context
        if stderr_config is not None:
            self.stderr_config = stderr_config
        if stdout_config is not None:
            self.stdout_config = stdout_config
        if timeout is not None:
            self.timeout = timeout
        if volume_devices is not None:
            self.volume_devices = volume_devices
        if volume_mounts is not None:
            self.volume_mounts = volume_mounts
        if working_dir is not None:
            self.working_dir = working_dir
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def args(self):
        """Gets the args of this V1Step.  # noqa: E501

        Arguments to the entrypoint. The image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell  # noqa: E501

        :return: The args of this V1Step.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this V1Step.

        Arguments to the entrypoint. The image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell  # noqa: E501

        :param args: The args of this V1Step.  # noqa: E501
        :type: list[str]
        """

        self._args = args

    @property
    def command(self):
        """Gets the command of this V1Step.  # noqa: E501

        Entrypoint array. Not executed within a shell. The image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell  # noqa: E501

        :return: The command of this V1Step.  # noqa: E501
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this V1Step.

        Entrypoint array. Not executed within a shell. The image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell  # noqa: E501

        :param command: The command of this V1Step.  # noqa: E501
        :type: list[str]
        """

        self._command = command

    @property
    def compute_resources(self):
        """Gets the compute_resources of this V1Step.  # noqa: E501


        :return: The compute_resources of this V1Step.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._compute_resources

    @compute_resources.setter
    def compute_resources(self, compute_resources):
        """Sets the compute_resources of this V1Step.


        :param compute_resources: The compute_resources of this V1Step.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._compute_resources = compute_resources

    @property
    def env(self):
        """Gets the env of this V1Step.  # noqa: E501

        List of environment variables to set in the Step. Cannot be updated.  # noqa: E501

        :return: The env of this V1Step.  # noqa: E501
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this V1Step.

        List of environment variables to set in the Step. Cannot be updated.  # noqa: E501

        :param env: The env of this V1Step.  # noqa: E501
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def env_from(self):
        """Gets the env_from of this V1Step.  # noqa: E501

        List of sources to populate environment variables in the Step. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the Step is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.  # noqa: E501

        :return: The env_from of this V1Step.  # noqa: E501
        :rtype: list[V1EnvFromSource]
        """
        return self._env_from

    @env_from.setter
    def env_from(self, env_from):
        """Sets the env_from of this V1Step.

        List of sources to populate environment variables in the Step. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the Step is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.  # noqa: E501

        :param env_from: The env_from of this V1Step.  # noqa: E501
        :type: list[V1EnvFromSource]
        """

        self._env_from = env_from

    @property
    def image(self):
        """Gets the image of this V1Step.  # noqa: E501

        Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images  # noqa: E501

        :return: The image of this V1Step.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this V1Step.

        Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images  # noqa: E501

        :param image: The image of this V1Step.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this V1Step.  # noqa: E501

        Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images  # noqa: E501

        :return: The image_pull_policy of this V1Step.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this V1Step.

        Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images  # noqa: E501

        :param image_pull_policy: The image_pull_policy of this V1Step.  # noqa: E501
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def name(self):
        """Gets the name of this V1Step.  # noqa: E501

        Name of the Step specified as a DNS_LABEL. Each Step in a Task must have a unique name.  # noqa: E501

        :return: The name of this V1Step.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1Step.

        Name of the Step specified as a DNS_LABEL. Each Step in a Task must have a unique name.  # noqa: E501

        :param name: The name of this V1Step.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def on_error(self):
        """Gets the on_error of this V1Step.  # noqa: E501

        OnError defines the exiting behavior of a container on error can be set to [ continue | stopAndFail ]  # noqa: E501

        :return: The on_error of this V1Step.  # noqa: E501
        :rtype: str
        """
        return self._on_error

    @on_error.setter
    def on_error(self, on_error):
        """Sets the on_error of this V1Step.

        OnError defines the exiting behavior of a container on error can be set to [ continue | stopAndFail ]  # noqa: E501

        :param on_error: The on_error of this V1Step.  # noqa: E501
        :type: str
        """

        self._on_error = on_error

    @property
    def script(self):
        """Gets the script of this V1Step.  # noqa: E501

        Script is the contents of an executable file to execute.  If Script is not empty, the Step cannot have an Command and the Args will be passed to the Script.  # noqa: E501

        :return: The script of this V1Step.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this V1Step.

        Script is the contents of an executable file to execute.  If Script is not empty, the Step cannot have an Command and the Args will be passed to the Script.  # noqa: E501

        :param script: The script of this V1Step.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def security_context(self):
        """Gets the security_context of this V1Step.  # noqa: E501


        :return: The security_context of this V1Step.  # noqa: E501
        :rtype: V1SecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """Sets the security_context of this V1Step.


        :param security_context: The security_context of this V1Step.  # noqa: E501
        :type: V1SecurityContext
        """

        self._security_context = security_context

    @property
    def stderr_config(self):
        """Gets the stderr_config of this V1Step.  # noqa: E501


        :return: The stderr_config of this V1Step.  # noqa: E501
        :rtype: V1StepOutputConfig
        """
        return self._stderr_config

    @stderr_config.setter
    def stderr_config(self, stderr_config):
        """Sets the stderr_config of this V1Step.


        :param stderr_config: The stderr_config of this V1Step.  # noqa: E501
        :type: V1StepOutputConfig
        """

        self._stderr_config = stderr_config

    @property
    def stdout_config(self):
        """Gets the stdout_config of this V1Step.  # noqa: E501


        :return: The stdout_config of this V1Step.  # noqa: E501
        :rtype: V1StepOutputConfig
        """
        return self._stdout_config

    @stdout_config.setter
    def stdout_config(self, stdout_config):
        """Sets the stdout_config of this V1Step.


        :param stdout_config: The stdout_config of this V1Step.  # noqa: E501
        :type: V1StepOutputConfig
        """

        self._stdout_config = stdout_config

    @property
    def timeout(self):
        """Gets the timeout of this V1Step.  # noqa: E501


        :return: The timeout of this V1Step.  # noqa: E501
        :rtype: V1Duration
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this V1Step.


        :param timeout: The timeout of this V1Step.  # noqa: E501
        :type: V1Duration
        """

        self._timeout = timeout

    @property
    def volume_devices(self):
        """Gets the volume_devices of this V1Step.  # noqa: E501

        volumeDevices is the list of block devices to be used by the Step.  # noqa: E501

        :return: The volume_devices of this V1Step.  # noqa: E501
        :rtype: list[V1VolumeDevice]
        """
        return self._volume_devices

    @volume_devices.setter
    def volume_devices(self, volume_devices):
        """Sets the volume_devices of this V1Step.

        volumeDevices is the list of block devices to be used by the Step.  # noqa: E501

        :param volume_devices: The volume_devices of this V1Step.  # noqa: E501
        :type: list[V1VolumeDevice]
        """

        self._volume_devices = volume_devices

    @property
    def volume_mounts(self):
        """Gets the volume_mounts of this V1Step.  # noqa: E501

        Volumes to mount into the Step's filesystem. Cannot be updated.  # noqa: E501

        :return: The volume_mounts of this V1Step.  # noqa: E501
        :rtype: list[V1VolumeMount]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """Sets the volume_mounts of this V1Step.

        Volumes to mount into the Step's filesystem. Cannot be updated.  # noqa: E501

        :param volume_mounts: The volume_mounts of this V1Step.  # noqa: E501
        :type: list[V1VolumeMount]
        """

        self._volume_mounts = volume_mounts

    @property
    def working_dir(self):
        """Gets the working_dir of this V1Step.  # noqa: E501

        Step's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.  # noqa: E501

        :return: The working_dir of this V1Step.  # noqa: E501
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        """Sets the working_dir of this V1Step.

        Step's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.  # noqa: E501

        :param working_dir: The working_dir of this V1Step.  # noqa: E501
        :type: str
        """

        self._working_dir = working_dir

    @property
    def workspaces(self):
        """Gets the workspaces of this V1Step.  # noqa: E501

        This is an alpha field. You must set the \"enable-api-fields\" feature flag to \"alpha\" for this field to be supported.  Workspaces is a list of workspaces from the Task that this Step wants exclusive access to. Adding a workspace to this list means that any other Step or Sidecar that does not also request this Workspace will not have access to it.  # noqa: E501

        :return: The workspaces of this V1Step.  # noqa: E501
        :rtype: list[V1WorkspaceUsage]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        """Sets the workspaces of this V1Step.

        This is an alpha field. You must set the \"enable-api-fields\" feature flag to \"alpha\" for this field to be supported.  Workspaces is a list of workspaces from the Task that this Step wants exclusive access to. Adding a workspace to this list means that any other Step or Sidecar that does not also request this Workspace will not have access to it.  # noqa: E501

        :param workspaces: The workspaces of this V1Step.  # noqa: E501
        :type: list[V1WorkspaceUsage]
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
        if not isinstance(other, V1Step):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Step):
            return True

        return self.to_dict() != other.to_dict()
