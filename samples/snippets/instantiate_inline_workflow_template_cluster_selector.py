# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This sample walks a user through instantiating an inline
# workflow using a cluster selector for Cloud Dataproc using the Python client library.
#
# This script can be run on its own:
#   python instantiate_inline_workflow_template_cluster_selector.py ${PROJECT_ID} ${REGION} ${CLUSTER_LABEL}


import sys

# [START instantiate_inline_workflow_template_cluster_selector]
from google.cloud import dataproc_v1 as dataproc


def instantiate_inline_workflow_template_cluster_selector(project_id, region, label):
    """This sample walks a user through submitting a workflow
    for a Cloud Dataproc using the Python client library.
    Args:
        project_id (string): Project to use for running the workflow.
        region (string): Region where the workflow resources should live.
        label (string): The label corresponding to the cluster pool where the job needs to be submitted
    """

    # Create a client with the endpoint set to the desired region.
    workflow_template_client = dataproc.WorkflowTemplateServiceClient(
        client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
    )

    parent = "projects/{}/regions/{}".format(project_id, region)

    template = \
                {
                "id": "clusterpool",
                "placement": 
                    {
                        "cluster_selector": {
                            "zone": "us-central1-a",
                            "cluster_labels": {"cluster-pool": label}
                        }
                    }
                ,
                "jobs": [
                    {
                        "step_id": "test-job-1",
                        "spark_job": 
                            {
                                "main_jar_file_uri": "file:///usr/lib/spark/examples/jars/spark-examples.jar"
                            }
                        ,
                    }
                ],
            }

   

    # Submit the request to instantiate the workflow from an inline template.
    operation = workflow_template_client.instantiate_inline_workflow_template(
        request={"parent": parent, "template": template}
    )
    operation.result()

    # Output a success message.
    print("Workflow ran successfully.")
    # [END instantiate_inline_workflow_template_cluster_selector]


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(
            "python instantiate_inline_workflow_template_cluster_selector.py " + "project_id region"
        )

    project_id = sys.argv[1]
    region = sys.argv[2]
    label = sys.argv[3]
    instantiate_inline_workflow_template_cluster_selector(project_id, region, label)
