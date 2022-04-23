# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os
import uuid

import pytest


@pytest.fixture(scope="session")
def project_id() -> str:
    return os.environ["GOOGLE_CLOUD_PROJECT"]


@pytest.fixture(scope="session")
def region() -> str:
    return os.environ["DATAPROC_REGION"]


"""@pytest.fixture(scope="session")
def zone() -> str:
    return os.environ["DATAPROC_NODE_ZONE"]"""


@pytest.fixture(scope="session")
def dp_cluster_name() -> str:
    dp_cluster_name = "py-cgkec-test-{}".format(str(uuid.uuid4()))
    return dp_cluster_name


@pytest.fixture(scope="session")
def gke_cluster_name() -> str:
    return os.environ["DATAPROC_GKE_CLUSTER"]


@pytest.fixture(scope="session")
def node_pool() -> str:
    node_pool = "py-cgkec-test-{}".format(str(uuid.uuid4()))
    return node_pool


@pytest.fixture(scope="session")
def phs_cluster() -> str:
    return os.environ["DATAPROC_PHS_CLUSTER"]


@pytest.fixture(scope="session")
def bucket() -> str:
    staging_buckets = os.environ["DATAPROC_STAGING_BUCKET_OPTIONS"]
    bucket_options = json.loads(staging_buckets)
    print(bucket_options)
    return bucket_options[project_id]
