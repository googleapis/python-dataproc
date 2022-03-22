# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateWorkflowTemplate
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dataproc


# [START dataproc_generated_dataproc_v1_WorkflowTemplateService_CreateWorkflowTemplate_sync]
from google.cloud import dataproc_v1


def sample_create_workflow_template():
    # Create a client
    client = dataproc_v1.WorkflowTemplateServiceClient()

    # Initialize request argument(s)
    template = dataproc_v1.WorkflowTemplate()
    template.id = "id_value"
    template.placement.managed_cluster.cluster_name = "cluster_name_value"
    template.jobs.hadoop_job.main_jar_file_uri = "main_jar_file_uri_value"
    template.jobs.step_id = "step_id_value"

    request = dataproc_v1.CreateWorkflowTemplateRequest(
        parent="parent_value",
        template=template,
    )

    # Make the request
    response = client.create_workflow_template(request=request)

    # Handle the response
    print(response)

# [END dataproc_generated_dataproc_v1_WorkflowTemplateService_CreateWorkflowTemplate_sync]