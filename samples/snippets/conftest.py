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
    py_project = os.envrion["DATAPROC_PY_PROJECT"]
    py_project_bucket = os.environ["DATAPROC_PY_PROJECT_BUCKET"]
    py_project37 = os.environ["DATAPROC_PY_PROJECT37"]
    py_project37_bucket = os.environ["DATAPROC_PY_PROJECT37_BUCKET"]
    py_project38 = os.environ["DATAPROC_PY_PROJECT38"]
    py_project38_bucket = os.environ["DATAPROC_PY_PROJECT38_BUCKET"]
    py_project39 = os.environ["DATAPROC_PY_PROJECT39"]
    py_project39_bucket = os.environ["DATAPROC_PY_PROJECT39_BUCKET"]
    py_project310 = os.environ["DATAPROC_PY_PROJECT310"]
    py_project310_bucket = os.environ["DATAPROC_PY_PROJECT310_BUCKET"]
    staging_bucket_options = {
        py_project: py_project_bucket,
        py_project37: py_project37_bucket,
        py_project38: py_project38_bucket,
        py_project39: py_project39_bucket,
        py_project310: py_project310_bucket
    }
    return staging_bucket_options[project_id]
