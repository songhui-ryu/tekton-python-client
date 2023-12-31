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


from __future__ import absolute_import

import unittest
import datetime

import tekton_pipeline
from tekton_pipeline.models.v1_step import V1Step  # noqa: E501
from tekton_pipeline.rest import ApiException

class TestV1Step(unittest.TestCase):
    """V1Step unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1Step
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tekton_pipeline.models.v1_step.V1Step()  # noqa: E501
        if include_optional :
            return V1Step(
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
                name = '0', 
                on_error = '0', 
                script = '0', 
                security_context = None, 
                stderr_config = tekton_pipeline.models.v1/step_output_config.v1.StepOutputConfig(
                    path = '0', ), 
                stdout_config = tekton_pipeline.models.v1/step_output_config.v1.StepOutputConfig(
                    path = '0', ), 
                timeout = None, 
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
                    ]
            )
        else :
            return V1Step(
                name = '0',
        )

    def testV1Step(self):
        """Test V1Step"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
