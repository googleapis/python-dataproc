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
# Snippet for UpdateJob
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dataproc


# [START dataproc_generated_dataproc_v1_JobController_UpdateJob_sync]
from google.cloud import dataproc_v1


def sample_update_job():
    # Create a client
    client = dataproc_v1.JobControllerClient()

    # Initialize request argument(s)
    job = dataproc_v1.Job()
    job.hadoop_job.main_jar_file_uri = "main_jar_file_uri_value"
    job.placement.cluster_name = "cluster_name_value"

    request = dataproc_v1.UpdateJobRequest(
        project_id="project_id_value",
        region="region_value",
        job_id="job_id_value",
        job=job,
    )

    # Make the request
    response = client.update_job(request=request)

    # Handle the response
    print(response)

# [END dataproc_generated_dataproc_v1_JobController_UpdateJob_sync]
