# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
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


import google.api_core.grpc_helpers
import google.api_core.operations_v1

from google.cloud.dataproc_v1.proto import workflow_templates_pb2_grpc


class WorkflowTemplateServiceGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.dataproc.v1 WorkflowTemplateService API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self, channel=None, credentials=None, address="dataproc.googleapis.com:443"
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive."
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "workflow_template_service_stub": workflow_templates_pb2_grpc.WorkflowTemplateServiceStub(
                channel
            )
        }

        # Because this API includes a method that returns a
        # long-running operation (proto: google.longrunning.Operation),
        # instantiate an LRO client.
        self._operations_client = google.api_core.operations_v1.OperationsClient(
            channel
        )

    @classmethod
    def create_channel(
        cls, address="dataproc.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def create_workflow_template(self):
        """Return the gRPC stub for :meth:`WorkflowTemplateServiceClient.create_workflow_template`.

        Creates new workflow template.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["workflow_template_service_stub"].CreateWorkflowTemplate

    @property
    def get_workflow_template(self):
        """Return the gRPC stub for :meth:`WorkflowTemplateServiceClient.get_workflow_template`.

        Retrieves the latest workflow template.

        Can retrieve previously instantiated template by specifying optional
        version parameter.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["workflow_template_service_stub"].GetWorkflowTemplate

    @property
    def instantiate_workflow_template(self):
        """Return the gRPC stub for :meth:`WorkflowTemplateServiceClient.instantiate_workflow_template`.

        Optional. Whether to continue executing queries if a query fails.
        The default value is ``false``. Setting to ``true`` can be useful when
        executing independent parallel queries.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["workflow_template_service_stub"].InstantiateWorkflowTemplate

    @property
    def instantiate_inline_workflow_template(self):
        """Return the gRPC stub for :meth:`WorkflowTemplateServiceClient.instantiate_inline_workflow_template`.

        Optional. The `Dataproc service
        account <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#service_accounts_in_cloud_dataproc>`__
        (also see `VM Data Plane
        identity <https://cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity>`__)
        used by Dataproc cluster VM instances to access Google Cloud Platform
        services.

        If not specified, the `Compute Engine default service
        account <https://cloud.google.com/compute/docs/access/service-accounts#default_service_account>`__
        is used.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs[
            "workflow_template_service_stub"
        ].InstantiateInlineWorkflowTemplate

    @property
    def update_workflow_template(self):
        """Return the gRPC stub for :meth:`WorkflowTemplateServiceClient.update_workflow_template`.

        Updates (replaces) workflow template. The updated template
        must contain version that matches the current server version.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["workflow_template_service_stub"].UpdateWorkflowTemplate

    @property
    def list_workflow_templates(self):
        """Return the gRPC stub for :meth:`WorkflowTemplateServiceClient.list_workflow_templates`.

        Lists workflows that match the specified filter in the request.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["workflow_template_service_stub"].ListWorkflowTemplates

    @property
    def delete_workflow_template(self):
        """Return the gRPC stub for :meth:`WorkflowTemplateServiceClient.delete_workflow_template`.

        Deletes a workflow template. It does not cancel in-progress workflows.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["workflow_template_service_stub"].DeleteWorkflowTemplate
