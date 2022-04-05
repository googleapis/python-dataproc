
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


from typing import Dict
from venv import create
# from urllib import response

# [START dataproc_create_cluster_on_gke]

from google.cloud import dataproc_v1 as dataproc
# from google.cloud import dataproc_v1.types as dataproc_types

def main() -> None:
  # Developer (TODO): Replace with your project_id.
  project_id = "your project_id"
  # Developer (TODO): Replace with the region you are using.
  region = "your region"
  # Developer (TODO): Replace with the cluster_name of the Dataproc cluster on which you want to run a virtual cluster on GKE.
  dp_cluster_name = "your_dp_cluster_name"
  # Developer (TODO): You may find it helpful to create a Dict object with other needed pieces of information.
  # Developer (TODO): Replace with gke_cluster_name for the virtual cluster you will run on GKE.
  gke_cluster_name = "your_gke_cluster_name"
  # Developer (TODO): Replace with your desired node_pool. If unspecified, Dataproc will use your default node_pool.
  node_pool = "your_node_pool"
  # Developer (TODO): Replace with your phs_cluster name if you plan to run a Spark job.
  phs_cluster = "your phs_cluster"
  # Developer (TODO): Replace with your gcs_bucket_name for staging.
  bucket = "your_gcs_ bucket_name"

  # Create a Kubernetes cluster config for GKE set up to use Spark.
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

  # Create an auxiliary services config for GKE in order to submit Spark jobs.
  auxiliary_services_config = dataproc.AuxiliaryServicesConfig({
    "sparkHistoryServerConfig":{
      "dataprocCluster": f"projects/{project_id}/regions/{region}/clusters/{phs_cluster}"
     }
  })

  # Create a virtual cluster config for GKE using your Kubernetes and auxiliary services configs.
  virtual_cluster_config = dataproc.VirtualClusterConfig({
        "staging_bucket": bucket,
        "kubernetes_cluster_config": kubernetes_cluster_config,
        "auxiliary_services_config": auxiliary_services_config
    })
  create_cluster_on_gke(project_id=project_id, region=region, dp_cluster_name=dp_cluster_name, virtual_cluster_config=virtual_cluster_config)

def create_cluster_on_gke(project_id: str, region: str, dp_cluster_name: str, virtual_cluster_config: dataproc.VirtualClusterConfig) -> None:
  # Create a client with the endpoint set to the desired cluster region. Check if same: TODO
  cluster_client = dataproc.ClusterControllerClient(
      client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
  )
    
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