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

"""Accesses the google.cloud.dataproc.v1beta2 ClusterController API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.grpc_helpers
import google.api_core.operation
import google.api_core.operations_v1
import google.api_core.page_iterator
import grpc

from google.cloud.dataproc_v1beta2.gapic import cluster_controller_client_config
from google.cloud.dataproc_v1beta2.gapic import enums
from google.cloud.dataproc_v1beta2.gapic.transports import (
    cluster_controller_grpc_transport,
)
from google.cloud.dataproc_v1beta2.proto import autoscaling_policies_pb2
from google.cloud.dataproc_v1beta2.proto import autoscaling_policies_pb2_grpc
from google.cloud.dataproc_v1beta2.proto import clusters_pb2
from google.cloud.dataproc_v1beta2.proto import clusters_pb2_grpc
from google.cloud.dataproc_v1beta2.proto import operations_pb2 as proto_operations_pb2
from google.longrunning import operations_pb2 as longrunning_operations_pb2
from google.protobuf import duration_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution("google-cloud-dataproc").version


class ClusterControllerClient(object):
    """
    The ClusterControllerService provides methods to manage clusters
    of Compute Engine instances.
    """

    SERVICE_ADDRESS = "dataproc.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.dataproc.v1beta2.ClusterController"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ClusterControllerClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.ClusterControllerGrpcTransport,
                    Callable[[~.Credentials, type], ~.ClusterControllerGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = cluster_controller_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=cluster_controller_grpc_transport.ClusterControllerGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = cluster_controller_grpc_transport.ClusterControllerGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def create_cluster(
        self,
        project_id,
        region,
        cluster,
        request_id=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Required. The "resource name" of the region or location, as
        described in https://cloud.google.com/apis/design/resource_names.

        -  For ``projects.regions.autoscalingPolicies.create``, the resource
           name has the following format:
           ``projects/{project_id}/regions/{region}``

        -  For ``projects.locations.autoscalingPolicies.create``, the resource
           name has the following format:
           ``projects/{project_id}/locations/{location}``

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.ClusterControllerClient()
            >>>
            >>> # TODO: Initialize `project_id`:
            >>> project_id = ''
            >>>
            >>> # TODO: Initialize `region`:
            >>> region = ''
            >>>
            >>> # TODO: Initialize `cluster`:
            >>> cluster = {}
            >>>
            >>> response = client.create_cluster(project_id, region, cluster)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            project_id (str): Required. The ID of the Google Cloud Platform project that the cluster
                belongs to.
            region (str): Required. The Dataproc region in which to handle the request.
            cluster (Union[dict, ~google.cloud.dataproc_v1beta2.types.Cluster]): Required. The cluster to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dataproc_v1beta2.types.Cluster`
            request_id (str): The response message for ``Operations.ListOperations``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dataproc_v1beta2.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_cluster" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_cluster"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_cluster,
                default_retry=self._method_configs["CreateCluster"].retry,
                default_timeout=self._method_configs["CreateCluster"].timeout,
                client_info=self._client_info,
            )

        request = clusters_pb2.CreateClusterRequest(
            project_id=project_id, region=region, cluster=cluster, request_id=request_id
        )
        operation = self._inner_api_calls["create_cluster"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            clusters_pb2.Cluster,
            metadata_type=proto_operations_pb2.ClusterOperationMetadata,
        )

    def update_cluster(
        self,
        project_id,
        region,
        cluster_name,
        cluster,
        update_mask,
        graceful_decommission_timeout=None,
        request_id=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        JSON name of this field. The value is set by protocol compiler. If
        the user has set a "json_name" option on this field, that option's value
        will be used. Otherwise, it's deduced from the field's name by
        converting it to camelCase.

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.ClusterControllerClient()
            >>>
            >>> # TODO: Initialize `project_id`:
            >>> project_id = ''
            >>>
            >>> # TODO: Initialize `region`:
            >>> region = ''
            >>>
            >>> # TODO: Initialize `cluster_name`:
            >>> cluster_name = ''
            >>>
            >>> # TODO: Initialize `cluster`:
            >>> cluster = {}
            >>>
            >>> # TODO: Initialize `update_mask`:
            >>> update_mask = {}
            >>>
            >>> response = client.update_cluster(project_id, region, cluster_name, cluster, update_mask)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            project_id (str): Required. The ID of the Google Cloud Platform project the
                cluster belongs to.
            region (str): Required. The Dataproc region in which to handle the request.
            cluster_name (str): Required. The cluster name.
            cluster (Union[dict, ~google.cloud.dataproc_v1beta2.types.Cluster]): Required. The changes to the cluster.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dataproc_v1beta2.types.Cluster`
            update_mask (Union[dict, ~google.cloud.dataproc_v1beta2.types.FieldMask]): Optional. Whether to continue executing queries if a query fails.
                The default value is ``false``. Setting to ``true`` can be useful when
                executing independent parallel queries.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dataproc_v1beta2.types.FieldMask`
            graceful_decommission_timeout (Union[dict, ~google.cloud.dataproc_v1beta2.types.Duration]): Number of attached SSDs, from 0 to 4 (default is 0). If SSDs are not
                attached, the boot disk is used to store runtime logs and
                `HDFS <https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html>`__
                data. If one or more SSDs are attached, this runtime bulk data is spread
                across them, and the boot disk contains only basic config and installed
                binaries.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dataproc_v1beta2.types.Duration`
            request_id (str): The ``Status`` type defines a logical error model that is suitable
                for different programming environments, including REST APIs and RPC
                APIs. It is used by `gRPC <https://github.com/grpc>`__. Each ``Status``
                message contains three pieces of data: error code, error message, and
                error details.

                You can find out more about this error model and how to work with it in
                the `API Design Guide <https://cloud.google.com/apis/design/errors>`__.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dataproc_v1beta2.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_cluster" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_cluster"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_cluster,
                default_retry=self._method_configs["UpdateCluster"].retry,
                default_timeout=self._method_configs["UpdateCluster"].timeout,
                client_info=self._client_info,
            )

        request = clusters_pb2.UpdateClusterRequest(
            project_id=project_id,
            region=region,
            cluster_name=cluster_name,
            cluster=cluster,
            update_mask=update_mask,
            graceful_decommission_timeout=graceful_decommission_timeout,
            request_id=request_id,
        )
        operation = self._inner_api_calls["update_cluster"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            clusters_pb2.Cluster,
            metadata_type=proto_operations_pb2.ClusterOperationMetadata,
        )

    def delete_cluster(
        self,
        project_id,
        region,
        cluster_name,
        cluster_uuid=None,
        request_id=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        The name of the uninterpreted option. Each string represents a
        segment in a dot-separated name. is_extension is true iff a segment
        represents an extension (denoted with parentheses in options specs in
        .proto files). E.g.,{ ["foo", false], ["bar.baz", true], ["qux", false]
        } represents "foo.(bar.baz).qux".

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.ClusterControllerClient()
            >>>
            >>> # TODO: Initialize `project_id`:
            >>> project_id = ''
            >>>
            >>> # TODO: Initialize `region`:
            >>> region = ''
            >>>
            >>> # TODO: Initialize `cluster_name`:
            >>> cluster_name = ''
            >>>
            >>> response = client.delete_cluster(project_id, region, cluster_name)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            project_id (str): Required. The ID of the Google Cloud Platform project that the cluster
                belongs to.
            region (str): Required. The Dataproc region in which to handle the request.
            cluster_name (str): Required. The cluster name.
            cluster_uuid (str): A Location identifies a piece of source code in a .proto file which
                corresponds to a particular definition. This information is intended to
                be useful to IDEs, code indexers, documentation generators, and similar
                tools.

                For example, say we have a file like: message Foo { optional string foo
                = 1; } Let's look at just the field definition: optional string foo = 1;
                ^ ^^ ^^ ^ ^^^ a bc de f ghi We have the following locations: span path
                represents [a,i) [ 4, 0, 2, 0 ] The whole field definition. [a,b) [ 4,
                0, 2, 0, 4 ] The label (optional). [c,d) [ 4, 0, 2, 0, 5 ] The type
                (string). [e,f) [ 4, 0, 2, 0, 1 ] The name (foo). [g,h) [ 4, 0, 2, 0, 3
                ] The number (1).

                Notes:

                -  A location may refer to a repeated field itself (i.e. not to any
                   particular index within it). This is used whenever a set of elements
                   are logically enclosed in a single code segment. For example, an
                   entire extend block (possibly containing multiple extension
                   definitions) will have an outer location whose path refers to the
                   "extensions" repeated field without an index.
                -  Multiple locations may have the same path. This happens when a single
                   logical declaration is spread out across multiple places. The most
                   obvious example is the "extend" block again -- there may be multiple
                   extend blocks in the same scope, each of which will have the same
                   path.
                -  A location's span is not always a subset of its parent's span. For
                   example, the "extendee" of an extension declaration appears at the
                   beginning of the "extend" block and is shared by all extensions
                   within the block.
                -  Just because a location's span is a subset of some other location's
                   span does not mean that it is a descendant. For example, a "group"
                   defines both a type and a field in a single declaration. Thus, the
                   locations corresponding to the type and field and their components
                   will overlap.
                -  Code which tries to interpret locations should probably be designed
                   to ignore those that it doesn't understand, as more types of
                   locations could be recorded in the future.
            request_id (str): Optional. The duration to keep the cluster alive while idling (when
                no jobs are running). Passing this threshold will cause the cluster to
                be deleted. Minimum value is 10 minutes; maximum value is 14 days (see
                JSON representation of
                `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dataproc_v1beta2.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_cluster" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_cluster"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_cluster,
                default_retry=self._method_configs["DeleteCluster"].retry,
                default_timeout=self._method_configs["DeleteCluster"].timeout,
                client_info=self._client_info,
            )

        request = clusters_pb2.DeleteClusterRequest(
            project_id=project_id,
            region=region,
            cluster_name=cluster_name,
            cluster_uuid=cluster_uuid,
            request_id=request_id,
        )
        operation = self._inner_api_calls["delete_cluster"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            empty_pb2.Empty,
            metadata_type=proto_operations_pb2.ClusterOperationMetadata,
        )

    def get_cluster(
        self,
        project_id,
        region,
        cluster_name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets the resource representation for a cluster in a project.

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.ClusterControllerClient()
            >>>
            >>> # TODO: Initialize `project_id`:
            >>> project_id = ''
            >>>
            >>> # TODO: Initialize `region`:
            >>> region = ''
            >>>
            >>> # TODO: Initialize `cluster_name`:
            >>> cluster_name = ''
            >>>
            >>> response = client.get_cluster(project_id, region, cluster_name)

        Args:
            project_id (str): Required. The ID of the Google Cloud Platform project that the cluster
                belongs to.
            region (str): Required. The Dataproc region in which to handle the request.
            cluster_name (str): Required. The cluster name.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dataproc_v1beta2.types.Cluster` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_cluster" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_cluster"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_cluster,
                default_retry=self._method_configs["GetCluster"].retry,
                default_timeout=self._method_configs["GetCluster"].timeout,
                client_info=self._client_info,
            )

        request = clusters_pb2.GetClusterRequest(
            project_id=project_id, region=region, cluster_name=cluster_name
        )
        return self._inner_api_calls["get_cluster"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_clusters(
        self,
        project_id,
        region,
        filter_=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists all regions/{region}/clusters in a project alphabetically.

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.ClusterControllerClient()
            >>>
            >>> # TODO: Initialize `project_id`:
            >>> project_id = ''
            >>>
            >>> # TODO: Initialize `region`:
            >>> region = ''
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_clusters(project_id, region):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_clusters(project_id, region).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            project_id (str): Required. The ID of the Google Cloud Platform project that the cluster
                belongs to.
            region (str): Required. The Dataproc region in which to handle the request.
            filter_ (str): Optional. Mapping of query variable names to values (equivalent to
                the Hive command: ``SET name="value";``).
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.dataproc_v1beta2.types.Cluster` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_clusters" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_clusters"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_clusters,
                default_retry=self._method_configs["ListClusters"].retry,
                default_timeout=self._method_configs["ListClusters"].timeout,
                client_info=self._client_info,
            )

        request = clusters_pb2.ListClustersRequest(
            project_id=project_id, region=region, filter=filter_, page_size=page_size
        )
        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_clusters"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="clusters",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def diagnose_cluster(
        self,
        project_id,
        region,
        cluster_name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        The resource has one pattern, but the API owner expects to add more
        later. (This is the inverse of ORIGINALLY_SINGLE_PATTERN, and prevents
        that from being necessary once there are multiple patterns.)

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.ClusterControllerClient()
            >>>
            >>> # TODO: Initialize `project_id`:
            >>> project_id = ''
            >>>
            >>> # TODO: Initialize `region`:
            >>> region = ''
            >>>
            >>> # TODO: Initialize `cluster_name`:
            >>> cluster_name = ''
            >>>
            >>> response = client.diagnose_cluster(project_id, region, cluster_name)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            project_id (str): Required. The ID of the Google Cloud Platform project that the cluster
                belongs to.
            region (str): Required. The Dataproc region in which to handle the request.
            cluster_name (str): Required. The cluster name.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dataproc_v1beta2.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "diagnose_cluster" not in self._inner_api_calls:
            self._inner_api_calls[
                "diagnose_cluster"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.diagnose_cluster,
                default_retry=self._method_configs["DiagnoseCluster"].retry,
                default_timeout=self._method_configs["DiagnoseCluster"].timeout,
                client_info=self._client_info,
            )

        request = clusters_pb2.DiagnoseClusterRequest(
            project_id=project_id, region=region, cluster_name=cluster_name
        )
        operation = self._inner_api_calls["diagnose_cluster"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            empty_pb2.Empty,
            metadata_type=proto_operations_pb2.ClusterOperationMetadata,
        )
