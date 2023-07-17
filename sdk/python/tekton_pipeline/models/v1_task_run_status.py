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


class V1TaskRunStatus(object):
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
        'annotations': 'dict(str, str)',
        'completion_time': 'V1Time',
        'conditions': 'list[KnativeCondition]',
        'observed_generation': 'int',
        'pod_name': 'str',
        'provenance': 'V1Provenance',
        'results': 'list[V1TaskRunResult]',
        'retries_status': 'list[V1TaskRunStatus]',
        'sidecars': 'list[V1SidecarState]',
        'span_context': 'dict(str, str)',
        'start_time': 'V1Time',
        'steps': 'list[V1StepState]',
        'task_spec': 'V1TaskSpec'
    }

    attribute_map = {
        'annotations': 'annotations',
        'completion_time': 'completionTime',
        'conditions': 'conditions',
        'observed_generation': 'observedGeneration',
        'pod_name': 'podName',
        'provenance': 'provenance',
        'results': 'results',
        'retries_status': 'retriesStatus',
        'sidecars': 'sidecars',
        'span_context': 'spanContext',
        'start_time': 'startTime',
        'steps': 'steps',
        'task_spec': 'taskSpec'
    }

    def __init__(self, annotations=None, completion_time=None, conditions=None, observed_generation=None, pod_name='', provenance=None, results=None, retries_status=None, sidecars=None, span_context=None, start_time=None, steps=None, task_spec=None, local_vars_configuration=None):  # noqa: E501
        """V1TaskRunStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._completion_time = None
        self._conditions = None
        self._observed_generation = None
        self._pod_name = None
        self._provenance = None
        self._results = None
        self._retries_status = None
        self._sidecars = None
        self._span_context = None
        self._start_time = None
        self._steps = None
        self._task_spec = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if completion_time is not None:
            self.completion_time = completion_time
        if conditions is not None:
            self.conditions = conditions
        if observed_generation is not None:
            self.observed_generation = observed_generation
        self.pod_name = pod_name
        if provenance is not None:
            self.provenance = provenance
        if results is not None:
            self.results = results
        if retries_status is not None:
            self.retries_status = retries_status
        if sidecars is not None:
            self.sidecars = sidecars
        if span_context is not None:
            self.span_context = span_context
        if start_time is not None:
            self.start_time = start_time
        if steps is not None:
            self.steps = steps
        if task_spec is not None:
            self.task_spec = task_spec

    @property
    def annotations(self):
        """Gets the annotations of this V1TaskRunStatus.  # noqa: E501

        Annotations is additional Status fields for the Resource to save some additional State as well as convey more information to the user. This is roughly akin to Annotations on any k8s resource, just the reconciler conveying richer information outwards.  # noqa: E501

        :return: The annotations of this V1TaskRunStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this V1TaskRunStatus.

        Annotations is additional Status fields for the Resource to save some additional State as well as convey more information to the user. This is roughly akin to Annotations on any k8s resource, just the reconciler conveying richer information outwards.  # noqa: E501

        :param annotations: The annotations of this V1TaskRunStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def completion_time(self):
        """Gets the completion_time of this V1TaskRunStatus.  # noqa: E501


        :return: The completion_time of this V1TaskRunStatus.  # noqa: E501
        :rtype: V1Time
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """Sets the completion_time of this V1TaskRunStatus.


        :param completion_time: The completion_time of this V1TaskRunStatus.  # noqa: E501
        :type: V1Time
        """

        self._completion_time = completion_time

    @property
    def conditions(self):
        """Gets the conditions of this V1TaskRunStatus.  # noqa: E501

        Conditions the latest available observations of a resource's current state.  # noqa: E501

        :return: The conditions of this V1TaskRunStatus.  # noqa: E501
        :rtype: list[KnativeCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1TaskRunStatus.

        Conditions the latest available observations of a resource's current state.  # noqa: E501

        :param conditions: The conditions of this V1TaskRunStatus.  # noqa: E501
        :type: list[KnativeCondition]
        """

        self._conditions = conditions

    @property
    def observed_generation(self):
        """Gets the observed_generation of this V1TaskRunStatus.  # noqa: E501

        ObservedGeneration is the 'Generation' of the Service that was last processed by the controller.  # noqa: E501

        :return: The observed_generation of this V1TaskRunStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this V1TaskRunStatus.

        ObservedGeneration is the 'Generation' of the Service that was last processed by the controller.  # noqa: E501

        :param observed_generation: The observed_generation of this V1TaskRunStatus.  # noqa: E501
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def pod_name(self):
        """Gets the pod_name of this V1TaskRunStatus.  # noqa: E501

        PodName is the name of the pod responsible for executing this task's steps.  # noqa: E501

        :return: The pod_name of this V1TaskRunStatus.  # noqa: E501
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        """Sets the pod_name of this V1TaskRunStatus.

        PodName is the name of the pod responsible for executing this task's steps.  # noqa: E501

        :param pod_name: The pod_name of this V1TaskRunStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pod_name is None:  # noqa: E501
            raise ValueError("Invalid value for `pod_name`, must not be `None`")  # noqa: E501

        self._pod_name = pod_name

    @property
    def provenance(self):
        """Gets the provenance of this V1TaskRunStatus.  # noqa: E501


        :return: The provenance of this V1TaskRunStatus.  # noqa: E501
        :rtype: V1Provenance
        """
        return self._provenance

    @provenance.setter
    def provenance(self, provenance):
        """Sets the provenance of this V1TaskRunStatus.


        :param provenance: The provenance of this V1TaskRunStatus.  # noqa: E501
        :type: V1Provenance
        """

        self._provenance = provenance

    @property
    def results(self):
        """Gets the results of this V1TaskRunStatus.  # noqa: E501

        Results are the list of results written out by the task's containers  # noqa: E501

        :return: The results of this V1TaskRunStatus.  # noqa: E501
        :rtype: list[V1TaskRunResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this V1TaskRunStatus.

        Results are the list of results written out by the task's containers  # noqa: E501

        :param results: The results of this V1TaskRunStatus.  # noqa: E501
        :type: list[V1TaskRunResult]
        """

        self._results = results

    @property
    def retries_status(self):
        """Gets the retries_status of this V1TaskRunStatus.  # noqa: E501

        RetriesStatus contains the history of TaskRunStatus in case of a retry in order to keep record of failures. All TaskRunStatus stored in RetriesStatus will have no date within the RetriesStatus as is redundant.  # noqa: E501

        :return: The retries_status of this V1TaskRunStatus.  # noqa: E501
        :rtype: list[V1TaskRunStatus]
        """
        return self._retries_status

    @retries_status.setter
    def retries_status(self, retries_status):
        """Sets the retries_status of this V1TaskRunStatus.

        RetriesStatus contains the history of TaskRunStatus in case of a retry in order to keep record of failures. All TaskRunStatus stored in RetriesStatus will have no date within the RetriesStatus as is redundant.  # noqa: E501

        :param retries_status: The retries_status of this V1TaskRunStatus.  # noqa: E501
        :type: list[V1TaskRunStatus]
        """

        self._retries_status = retries_status

    @property
    def sidecars(self):
        """Gets the sidecars of this V1TaskRunStatus.  # noqa: E501

        The list has one entry per sidecar in the manifest. Each entry is represents the imageid of the corresponding sidecar.  # noqa: E501

        :return: The sidecars of this V1TaskRunStatus.  # noqa: E501
        :rtype: list[V1SidecarState]
        """
        return self._sidecars

    @sidecars.setter
    def sidecars(self, sidecars):
        """Sets the sidecars of this V1TaskRunStatus.

        The list has one entry per sidecar in the manifest. Each entry is represents the imageid of the corresponding sidecar.  # noqa: E501

        :param sidecars: The sidecars of this V1TaskRunStatus.  # noqa: E501
        :type: list[V1SidecarState]
        """

        self._sidecars = sidecars

    @property
    def span_context(self):
        """Gets the span_context of this V1TaskRunStatus.  # noqa: E501

        SpanContext contains tracing span context fields  # noqa: E501

        :return: The span_context of this V1TaskRunStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._span_context

    @span_context.setter
    def span_context(self, span_context):
        """Sets the span_context of this V1TaskRunStatus.

        SpanContext contains tracing span context fields  # noqa: E501

        :param span_context: The span_context of this V1TaskRunStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._span_context = span_context

    @property
    def start_time(self):
        """Gets the start_time of this V1TaskRunStatus.  # noqa: E501


        :return: The start_time of this V1TaskRunStatus.  # noqa: E501
        :rtype: V1Time
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this V1TaskRunStatus.


        :param start_time: The start_time of this V1TaskRunStatus.  # noqa: E501
        :type: V1Time
        """

        self._start_time = start_time

    @property
    def steps(self):
        """Gets the steps of this V1TaskRunStatus.  # noqa: E501

        Steps describes the state of each build step container.  # noqa: E501

        :return: The steps of this V1TaskRunStatus.  # noqa: E501
        :rtype: list[V1StepState]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this V1TaskRunStatus.

        Steps describes the state of each build step container.  # noqa: E501

        :param steps: The steps of this V1TaskRunStatus.  # noqa: E501
        :type: list[V1StepState]
        """

        self._steps = steps

    @property
    def task_spec(self):
        """Gets the task_spec of this V1TaskRunStatus.  # noqa: E501


        :return: The task_spec of this V1TaskRunStatus.  # noqa: E501
        :rtype: V1TaskSpec
        """
        return self._task_spec

    @task_spec.setter
    def task_spec(self, task_spec):
        """Sets the task_spec of this V1TaskRunStatus.


        :param task_spec: The task_spec of this V1TaskRunStatus.  # noqa: E501
        :type: V1TaskSpec
        """

        self._task_spec = task_spec

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
        if not isinstance(other, V1TaskRunStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1TaskRunStatus):
            return True

        return self.to_dict() != other.to_dict()
