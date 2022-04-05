
#!/usr/bin/env python

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

# This sample walks a user through creating a Cloud Dataproc cluster using
# the Python client library.
#
# This script can be run on its own:
#   python create_cluster.py ${PROJECT_ID} ${REGION} ${DP_CLUSTER_NAME}


import sys
from typing import Dict
# from urllib import response

# [START dataproc_create_cluster_on_gke]

from google.cloud import dataproc_v1 as dataproc
# from google.cloud import dataproc_v1.types as dataproc_types

# Developer (TODO): Replace with your project_id.
project_id = "your project_id"
# Developer (TODO): Replace with the region you are using.
region = "your region"
# Developer (TODO): Replace with the cluster_name of the Dataproc cluster on which you want to run a virtual cluster on GKE.
dp_cluster_name = "your_dp_cluster_name"
# Developer (TODO): You may find it helpful to create a Dict object with other needed pieces of information.
dp_on_gke_params = {
    # Developer (TODO): Replace with gke_cluster_name for the virtual cluster you will run on GKE.
    "gke_cluster_name" (str): "your_gke_cluster_name",
    # Developer (TODO): Replace with your desired node_pool. If unspecified, Dataproc will use your default node_pool.
    "node_pool" (str): "your_node_pool",
    # Developer (TODO): Replace with your phs_cluster name if you plan to run a Spark job.
    "phs_cluster" (str): "your phs_cluster",
    # Developer (TODO): Replace with your gcs_bucket_name for staging.
    "bucket" (str): "your_gcs_ bucket_name"
}
# Create a Kubernetes cluster config for GKE set up to use Spark.
def kubernetes_cluster_config(project_id: str, region: str, dp_on_gke_params: Dict) -> dataproc.types.KubernetesClusterConfig:
    gke_cluster_name = dp_on_gke_params.gke_cluster_name
    node_pool = dp_on_gke_params.node_pool

    kubernetes_cluster_config = dataproc.KubernetesClusterConfig({
        "gkeClusterConfig": {
        "gkeClusterTarget": f"projects/{project_id}/locations/{region}/clusters/{gke_cluster_name}",
        "nodePoolTarget": [
          {
            "nodePool": f"projects/{project_id}/locations/{region}/clusters/{gke_cluster_name}/nodePools/{node_pool}",
            "roles":[
              "DEFAULT"
            ]
          }
        ]
      },
      "kubernetesSoftwareConfig":{
        "componentVersion":{
          "SPARK":"3"
        }
      }
    },
        )
    return kubernetes_cluster_config

# Create an auxiliary services config for GKE in order to submit Spark jobs.
def auxiliary_services_config(project_id: str, region: str, dp_on_gke_params: Dict) -> dataproc.types.AuxiliaryServicesConfig =
    phs_cluster = dp_on_gke_params.phs_cluster

    auxiliary_services_config = {
      "sparkHistoryServerConfig":{
        "dataprocCluster": f"projects/{project_id}/regions/{region}/clusters/{phs_cluster}"
      }
    }
    return auxiliary_services_config

# Create a virtual cluster config for GKE using your Kubernetes and auxiliary services configs.
def virtual_cluster_config(kubernetes_cluster_config: dataproc.types.KubernetesClusterConfig, auxiliary_services_config: dataproc.types.AuxiliaryServicesConfig, dp_on_gke_params: Dict) -> dataproc.types.VirtualClusterConfig:
    staging_bucket = dp_on_gke_params.staging_bucket
    virtual_cluster_config = dataproc.VirtualClusterConfig({
        "staging_bucket": staging_bucket,
        "kubernetes_cluster_config": kubernetes_cluster_config,
        "auxiliary_services_config": auxiliary_services_config
    })
    return virtual_cluster_config


def create_cluster_on_gke(project_id: str, region: str, dp_cluster_name: str, dp_on_gke_params: Dict) -> None:
    # Create a client with the endpoint set to the desired cluster region. Check if same: TODO
    cluster_client = dataproc.ClusterControllerClient(
        client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
    )
    
    # Create configs specific to adding a GKE cluster on Dataproc.
    kubernetes_cluster_config = kubernetes_cluster_config(project_id, region, dp_on_gke_params)
    auxiliary_services_config = auxiliary_services_config(project_id, region, dp_on_gke_params)
    virtual_cluster_config = virtual_cluster_config(kubernetes_cluster_config, auxiliary_services_config, dp_on_gke_params)

    # Create a GKE cluster to add to your project.
    gke_cluster = dataproc.Cluster({
        "project_id": project_id,
        "cluster_name": dp_cluster_name,
        "virtual_cluster_config": virtual_cluster_config,
    })

    # Add the cluster to your project.
    operation = cluster_client.create_cluster(
        request={"project_id": project_id, "region": region, "cluster": gke_cluster}
    )
    response = operation.result(60)

    # Output a success message.
    print(f"Cluster created successfully: {response.dp_cluster_name}")
    
    # [END dataproc_create_cluster_on_gke]


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit("python create_cluster_on_gke.py project_id region cluster_name")

    project_id = sys.argv[1]
    region = sys.argv[2]
    gke_cluster_name = sys.argv[3]
    create_cluster_on_gke(project_id, region, dp_cluster_name, dp_on_gke_params)

