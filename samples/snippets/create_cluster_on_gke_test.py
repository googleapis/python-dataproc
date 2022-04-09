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

from conftest import (
    bucket,
    dp_cluster_name,
    gke_cluster_name,
    node_pool,
    phs_cluster,
    project_id,
    region,
)
import create_cluster_on_gke

test_project_id = project_id
test_region = region
test_dp_cluster_name = dp_cluster_name
test_gke_cluster_name = gke_cluster_name
test_node_pool = node_pool
test_phs_cluster = phs_cluster
test_bucket = bucket


@pytest.fixture(autouse=True)
def teardown() -> None:
    yield

    cluster_client = dataproc.ClusterControllerClient(
        client_options={"api_endpoint": f"{test_region}-dataproc.googleapis.com:443"}
    )
    # Client library function to delete cluster.
    try:
        operation = cluster_client.delete_cluster(
            request={
                "project_id": test_project_id,
                "region": test_region,
                "cluster_name": test_dp_cluster_name,
            }
        )
        # Wait for cluster to delete
        operation.result()
    except NotFound:
        print("Cluster already deleted")


def test_cluster_create_on_gke(capsys) -> None:
    kubernetes_cluster_config = dataproc.KubernetesClusterConfig(
        {
            "gkeClusterConfig": {
                "gkeClusterTarget": f"projects/{test_project_id}/locations/{test_region}/clusters/{test_gke_cluster_name}",
                "nodePoolTarget": [
                    {
                        "nodePool": f"projects/{test_project_id}/locations/{test_region}/clusters/{test_gke_cluster_name}/nodePools/{test_node_pool}",
                        "roles": ["DEFAULT"],
                    }
                ],
            },
            "kubernetesSoftwareConfig": {"componentVersion": {"SPARK": "3"}},
        },
    )

    auxiliary_services_config = dataproc.AuxiliaryServicesConfig(
        {
            "sparkHistoryServerConfig": {
                "dataprocCluster": f"projects/{test_project_id}/regions/{test_region}/clusters/{test_phs_cluster}"
            }
        }
    )

    test_virtual_cluster_config = dataproc.VirtualClusterConfig(
        {
            "staging_bucket": test_bucket,
            "kubernetes_cluster_config": kubernetes_cluster_config,
            "auxiliary_services_config": auxiliary_services_config,
        }
    )
    # Wrapper function for client library function
    create_cluster_on_gke(test_project_id, test_region, test_virtual_cluster_config)

    out, _ = capsys.readouterr()
    assert test_dp_cluster_name in out
