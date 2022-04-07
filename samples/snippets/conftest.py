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

import os
import uuid

import pytest


@pytest.fixture(scope="session")
def project_id() -> str:
    return os.environ["PROJECT_ID"]

@pytest.fixture(scope="session")
def region() -> str:
    return os.environ["REGION"]

@pytest.fixture(scope="session")
def dp_cluster_name() -> str:
    dp_cluster_name = "py-cgkec-test-{}".format(str(uuid.uuid4()))
    return dp_cluster_name

@pytest.fixture(scope="session")
def gke_cluster_name() -> str:
    gke_cluster_name = "py-cgkec-test-{}".format(str(uuid.uuid4()))
    return gke_cluster_name

@pytest.fixture(scope="session")
def node_pool() -> str:
    return os.environ["NODE_POOL"]

"""@pytest.fixture(scope="session")
def phs_cluster() -> str:
    return os.environ["PHS_CLUSTER"]"""

@pytest.fixture(scope="session")
def bucket() -> str:
    return os.environ["BUCKET"]
