#!/usr/bin/env python
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

# [START dataproc_update_cluster]
from google.cloud import dataproc_v1 as dataproc


def update_cluster(project_id, region, cluster_name):
    """Specify client with desired cluster"""
    client = dataproc.ClusterControllerClient(
        client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
    )
    # Get cluster
    cluster = client.get_cluster(
        project_id=project_id, region=region, cluster_name=cluster_name
    )
    # Update number of clusters

    new_num_instances = cluster.config.worker_config.num_instances * 2
    mask = {"paths": {"config.worker_config.num_instances": str(new_num_instances)}}
    # Update cluster config
    cluster.config.worker_config.num_instances = new_num_instances
    # Update cluster
    operation = client.update_cluster(
        project_id=project_id,
        region=region,
        cluster=cluster,
        cluster_name=cluster_name,
        update_mask=mask,
    )
    # Return result of operation
    updated_cluster = operation.result()
    print(f"result was: {updated_cluster}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit("python update_cluster.py project_id region cluster_name")

        project_id = sys.argv[1]
        region = sys.argv[2]
        cluster_name = sys.argv[3]
        update_cluster(project_id, region, cluster_name)
