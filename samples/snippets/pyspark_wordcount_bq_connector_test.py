#!/usr/bin/env python

# Copyright 2021 Google LLC
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

# TODO(coleleah): imports
import pytest
import uuid

import submit_job_to_cluster

from google.api_core.exceptions import NotFound
from google.cloud import dataproc_v1 as dataproc
from google.cloud import storage


# PROJECT_ID = os.environ["GOOGLE_CLOUD_PROJECT"]
PROJECT_ID = "leah-playground"

REGION = "us-west1"
ZONE = "us-west1-b"
CLUSTER_NAME = "pyspark-wordcount-bq-connector-test-{}".format(str(uuid.uuid4())[0:10]) #only use part of UUID to get around length limits for name
CLUSTER = {
    "project_id": PROJECT_ID,
    "cluster_name": CLUSTER_NAME,
    "config": {
        "master_config": {"num_instances": 1, "machine_type_uri": "n1-standard-2"},
        "worker_config": {"num_instances": 2, "machine_type_uri": "n1-standard-2"},
    },
}

# TODO(coleleah): fixture for bucket
@pytest.fixture(scope="module")
def test_bucket():
    """Yields a bucket that is deleted after the test completes."""
    bucket = None
    while bucket is None or bucket.exists():
        bucket_name = "pyspark-wordcount-bq-connector-test-{}".format(str(uuid.uuid4())[0:10]) # maek name conform to length requirements
        bucket = storage.Client().bucket(bucket_name)
    bucket = storage.Client().create_bucket(bucket.name)
    yield bucket.name
    bucket.delete(force=True)

# TODO(coleleah): fixture for bq dataset
@pytest.fixture(scope="module")
def temp_dataset():
    try:
        from google.cloud import bigquery

        client = bigquery.Client()
        dataset_id = "pyspark-wordcount-bq-connector-test-{}".format(str(uuid.uuid4())[0:10])
        dataset_ref = bigquery.DatasetReference(client.project, dataset_id)
        dataset = client.create_dataset(bigquery.Dataset(dataset_ref))
        yield dataset
    finally:
        try:
            client.delete_dataset(dataset, delete_contents=True)
        except NotFound: 
            print("Dataset already deleted or doesn't exist")
# TODO(coleleah): fixture for dataproc cluster

@pytest.fixture(scope="module")
def test_cluster():
    try:
        cluster_client = dataproc.ClusterControllerClient(
            client_options={"api_endpoint": "{}-dataproc.googleapis.com:443".format(REGION)}
        )

        # Create the cluster.
        operation = cluster_client.create_cluster(
            request={"project_id": PROJECT_ID, "region": REGION, "cluster": CLUSTER}
        )
        operation.result()

        yield
    finally:
        try:
            cluster_client.delete_cluster(
                request={
                    "project_id": PROJECT_ID,
                    "region": REGION,
                    "cluster_name": CLUSTER_NAME,
                }
            )
        except NotFound as e:
            print(f"Cluster already deleted {e}")

# TODO(coleleah): test that job gets submitted successfully and we can see output

def test_pyspark_wordcount_job(test_cluster, test_bucket):
    submit_job_to_cluster.main(
    PROJECT_ID, 
    ZONE,
    CLUSTER_NAME,
    test_bucket,
    pyspark_file="pyspark_wordcount_bq_connector.py",
    create_new_cluster=False,
    global_region=True,
)
    # TODO(coleleah): assert table exists
    # TODO(coleleah): assert expected in output
# # Helper function
# def submit_job(project_id, region, cluster_name):
#     # Create the job client.
#     job_client = dataproc.JobControllerClient(
#         client_options={"api_endpoint": "{}-dataproc.googleapis.com:443".format(region)}
#     )

#     # Create the job config. 'main_jar_file_uri' can also be a
#     # Google Cloud Storage URL.
#     PYSPARK_JOB = {
#         "reference": {"project_id": PROJECT_ID},
#         "placement": {"cluster_name": CLUSTER_NAME},
#         "pyspark_job": {"main_python_file_uri": TEST_BUCKET, "jar_file_uris": ["gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar"]},
#     }

#     operation = job_client.submit_job_as_operation(
#         request={"project_id": project_id, "region": region, "job": PYSPARK_JOB}
#     )
#     response = operation.result()

#     # Dataproc job output gets saved to the Google Cloud Storage bucket
#     # allocated to the job. Use a regex to obtain the bucket and blob info.
#     matches = re.match("gs://(.*?)/(.*)", response.driver_output_resource_uri)

#     output = (
#         storage.Client()
#         .get_bucket(matches.group(1))
#         .blob(f"{matches.group(2)}.000000000")
#         .download_as_string()
#     )

#     print(f"Job finished successfully: {output}")


# # [END dataproc_submit_job]


# if __name__ == "__main__":
#     if len(sys.argv) < 3:
#         sys.exit("python submit_job.py project_id region cluster_name")

#     project_id = sys.argv[1]
#     region = sys.argv[2]
#     cluster_name = sys.argv[3]
#     submit_job(project_id, region, cluster_name)
