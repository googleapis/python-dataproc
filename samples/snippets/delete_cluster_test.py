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

from google.api_core.exceptions import NotFound
from google.cloud import dataproc_v1 as dataproc
import pytest

import create_cluster
import delete_cluster


@pytest.fixture(autouse=True)
def teardown(region: str, project_id: str, dp_cluster_name: str) -> None:
    # The test itself should delete the created cluster, but if it doesn't, it will be caught in teardown.
    yield

    cluster_client = dataproc.ClusterControllerClient(
        client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
    )
    # Client library function
    try:
        operation = cluster_client.delete_cluster(
            request={
                "project_id": project_id,
                "region": region,
                "cluster_name": dp_cluster_name,
            }
        )
        # Wait for cluster to delete
        operation.result()

    except NotFound:
        print("Cluster already deleted")


def test_cluster_delete(
    capsys: pytest.CaptureFixture, project_id: str, region: str, dp_cluster_name: str
) -> None:
    # Wrapper function for client library function
    create_cluster.create_cluster(project_id, region, dp_cluster_name)
    delete_cluster.delete_cluster(project_id, region, dp_cluster_name)

    out, _ = capsys.readouterr()
    assert dp_cluster_name in out
    assert "Cluster created successfully" in out
    assert "successfully deleted" in out
