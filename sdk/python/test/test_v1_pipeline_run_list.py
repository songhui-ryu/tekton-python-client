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


from __future__ import absolute_import

import unittest
import datetime

import tekton_pipeline
from tekton_pipeline.models.v1_pipeline_run_list import V1PipelineRunList  # noqa: E501
from tekton_pipeline.rest import ApiException

class TestV1PipelineRunList(unittest.TestCase):
    """V1PipelineRunList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1PipelineRunList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tekton_pipeline.models.v1_pipeline_run_list.V1PipelineRunList()  # noqa: E501
        if include_optional :
            return V1PipelineRunList(
                api_version = '0', 
                items = [
                    tekton_pipeline.models.v1/pipeline_run.v1.PipelineRun(
                        api_version = '0', 
                        kind = '0', 
                        metadata = None, 
                        spec = tekton_pipeline.models.v1/pipeline_run_spec.v1.PipelineRunSpec(
                            params = [
                                tekton_pipeline.models.v1/param.v1.Param(
                                    name = '0', 
                                    value = tekton_pipeline.models.v1/param_value.v1.ParamValue(
                                        array_val = [
                                            '0'
                                            ], 
                                        object_val = {
                                            'key' : '0'
                                            }, 
                                        string_val = '0', 
                                        type = '0', ), )
                                ], 
                            pipeline_ref = tekton_pipeline.models.v1/pipeline_ref.v1.PipelineRef(
                                api_version = '0', 
                                name = '0', ), 
                            pipeline_spec = tekton_pipeline.models.v1/pipeline_spec.v1.PipelineSpec(
                                description = '0', 
                                display_name = '0', 
                                finally = [
                                    tekton_pipeline.models.v1/pipeline_task.v1.PipelineTask(
                                        description = '0', 
                                        display_name = '0', 
                                        matrix = tekton_pipeline.models.v1/matrix.v1.Matrix(
                                            include = [
                                                tekton_pipeline.models.v1/include_params.v1.IncludeParams(
                                                    name = '0', )
                                                ], ), 
                                        name = '0', 
                                        retries = 56, 
                                        run_after = [
                                            '0'
                                            ], 
                                        task_ref = tekton_pipeline.models.v1/task_ref.v1.TaskRef(
                                            api_version = '0', 
                                            kind = '0', 
                                            name = '0', ), 
                                        task_spec = tekton_pipeline.models.v1/embedded_task.v1.EmbeddedTask(
                                            api_version = '0', 
                                            description = '0', 
                                            display_name = '0', 
                                            kind = '0', 
                                            metadata = tekton_pipeline.models.v1/pipeline_task_metadata.v1.PipelineTaskMetadata(
                                                annotations = {
                                                    'key' : '0'
                                                    }, 
                                                labels = {
                                                    'key' : '0'
                                                    }, ), 
                                            results = [
                                                tekton_pipeline.models.v1/task_result.v1.TaskResult(
                                                    description = '0', 
                                                    name = '0', 
                                                    properties = {
                                                        'key' : tekton_pipeline.models.v1/property_spec.v1.PropertySpec(
                                                            type = '0', )
                                                        }, 
                                                    type = '0', )
                                                ], 
                                            sidecars = [
                                                tekton_pipeline.models.v1/sidecar.v1.Sidecar(
                                                    args = [
                                                        '0'
                                                        ], 
                                                    command = [
                                                        '0'
                                                        ], 
                                                    compute_resources = None, 
                                                    env = [
                                                        None
                                                        ], 
                                                    env_from = [
                                                        None
                                                        ], 
                                                    image = '0', 
                                                    image_pull_policy = '0', 
                                                    lifecycle = None, 
                                                    liveness_probe = None, 
                                                    name = '0', 
                                                    ports = [
                                                        None
                                                        ], 
                                                    readiness_probe = None, 
                                                    script = '0', 
                                                    security_context = None, 
                                                    startup_probe = None, 
                                                    stdin = True, 
                                                    stdin_once = True, 
                                                    termination_message_path = '0', 
                                                    termination_message_policy = '0', 
                                                    tty = True, 
                                                    volume_devices = [
                                                        None
                                                        ], 
                                                    volume_mounts = [
                                                        None
                                                        ], 
                                                    working_dir = '0', 
                                                    workspaces = [
                                                        tekton_pipeline.models.v1/workspace_usage.v1.WorkspaceUsage(
                                                            mount_path = '0', 
                                                            name = '0', )
                                                        ], )
                                                ], 
                                            step_template = tekton_pipeline.models.v1/step_template.v1.StepTemplate(
                                                compute_resources = None, 
                                                image = '0', 
                                                image_pull_policy = '0', 
                                                security_context = None, 
                                                working_dir = '0', ), 
                                            steps = [
                                                tekton_pipeline.models.v1/step.v1.Step(
                                                    compute_resources = None, 
                                                    image = '0', 
                                                    image_pull_policy = '0', 
                                                    name = '0', 
                                                    on_error = '0', 
                                                    script = '0', 
                                                    security_context = None, 
                                                    stderr_config = tekton_pipeline.models.v1/step_output_config.v1.StepOutputConfig(
                                                        path = '0', ), 
                                                    stdout_config = tekton_pipeline.models.v1/step_output_config.v1.StepOutputConfig(
                                                        path = '0', ), 
                                                    timeout = None, 
                                                    working_dir = '0', )
                                                ], 
                                            volumes = [
                                                None
                                                ], 
                                            workspaces = [
                                                tekton_pipeline.models.v1/workspace_declaration.v1.WorkspaceDeclaration(
                                                    description = '0', 
                                                    mount_path = '0', 
                                                    name = '0', 
                                                    optional = True, 
                                                    read_only = True, )
                                                ], ), 
                                        timeout = None, 
                                        when = [
                                            tekton_pipeline.models.v1/when_expression.v1.WhenExpression(
                                                input = '0', 
                                                operator = '0', 
                                                values = [
                                                    '0'
                                                    ], )
                                            ], 
                                        workspaces = [
                                            tekton_pipeline.models.v1/workspace_pipeline_task_binding.v1.WorkspacePipelineTaskBinding(
                                                name = '0', 
                                                sub_path = '0', 
                                                workspace = '0', )
                                            ], )
                                    ], 
                                results = [
                                    tekton_pipeline.models.v1/pipeline_result.v1.PipelineResult(
                                        description = '0', 
                                        name = '0', 
                                        type = '0', 
                                        value = tekton_pipeline.models.v1/param_value.v1.ParamValue(
                                            array_val = [
                                                '0'
                                                ], 
                                            object_val = {
                                                'key' : '0'
                                                }, 
                                            string_val = '0', 
                                            type = '0', ), )
                                    ], 
                                tasks = [
                                    tekton_pipeline.models.v1/pipeline_task.v1.PipelineTask(
                                        description = '0', 
                                        display_name = '0', 
                                        name = '0', 
                                        retries = 56, 
                                        timeout = None, )
                                    ], 
                                workspaces = [
                                    tekton_pipeline.models.v1/pipeline_workspace_declaration.v1.PipelineWorkspaceDeclaration(
                                        description = '0', 
                                        name = '0', 
                                        optional = True, )
                                    ], ), 
                            status = '0', 
                            task_run_specs = [
                                tekton_pipeline.models.v1/pipeline_task_run_spec.v1.PipelineTaskRunSpec(
                                    compute_resources = None, 
                                    pipeline_task_name = '0', 
                                    pod_template = tekton_pipeline.models.pod/template.pod.Template(
                                        affinity = None, 
                                        automount_service_account_token = True, 
                                        dns_config = None, 
                                        dns_policy = '0', 
                                        enable_service_links = True, 
                                        host_aliases = [
                                            None
                                            ], 
                                        host_network = True, 
                                        image_pull_secrets = [
                                            None
                                            ], 
                                        node_selector = {
                                            'key' : '0'
                                            }, 
                                        priority_class_name = '0', 
                                        runtime_class_name = '0', 
                                        scheduler_name = '0', 
                                        security_context = None, 
                                        tolerations = [
                                            None
                                            ], 
                                        topology_spread_constraints = [
                                            None
                                            ], ), 
                                    service_account_name = '0', 
                                    sidecar_specs = [
                                        tekton_pipeline.models.v1/task_run_sidecar_spec.v1.TaskRunSidecarSpec(
                                            compute_resources = None, 
                                            name = '0', )
                                        ], 
                                    step_specs = [
                                        tekton_pipeline.models.v1/task_run_step_spec.v1.TaskRunStepSpec(
                                            compute_resources = None, 
                                            name = '0', )
                                        ], )
                                ], 
                            task_run_template = tekton_pipeline.models.v1/pipeline_task_run_template.v1.PipelineTaskRunTemplate(
                                service_account_name = '0', ), 
                            timeouts = tekton_pipeline.models.v1/timeout_fields.v1.TimeoutFields(
                                pipeline = None, ), 
                            workspaces = [
                                tekton_pipeline.models.v1/workspace_binding.v1.WorkspaceBinding(
                                    config_map = None, 
                                    csi = None, 
                                    empty_dir = None, 
                                    name = '0', 
                                    persistent_volume_claim = None, 
                                    projected = None, 
                                    secret = None, 
                                    sub_path = '0', 
                                    volume_claim_template = None, )
                                ], ), 
                        status = tekton_pipeline.models.v1/pipeline_run_status.v1.PipelineRunStatus(
                            child_references = [
                                tekton_pipeline.models.v1/child_status_reference.v1.ChildStatusReference(
                                    api_version = '0', 
                                    kind = '0', 
                                    name = '0', 
                                    pipeline_task_name = '0', 
                                    when_expressions = [
                                        tekton_pipeline.models.v1/when_expression.v1.WhenExpression(
                                            input = '0', 
                                            operator = '0', 
                                            values = [
                                                '0'
                                                ], )
                                        ], )
                                ], 
                            completion_time = None, 
                            conditions = [
                                None
                                ], 
                            finally_start_time = None, 
                            observed_generation = 56, 
                            provenance = tekton_pipeline.models.v1/provenance.v1.Provenance(
                                feature_flags = None, 
                                ref_source = tekton_pipeline.models.v1/ref_source.v1.RefSource(
                                    digest = {
                                        'key' : '0'
                                        }, 
                                    entry_point = '0', 
                                    uri = '0', ), ), 
                            skipped_tasks = [
                                tekton_pipeline.models.v1/skipped_task.v1.SkippedTask(
                                    name = '0', 
                                    reason = '0', )
                                ], 
                            span_context = {
                                'key' : '0'
                                }, 
                            start_time = None, ), )
                    ], 
                kind = '0', 
                metadata = None
            )
        else :
            return V1PipelineRunList(
        )

    def testV1PipelineRunList(self):
        """Test V1PipelineRunList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
