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

"""Accesses the google.cloud.dataproc.v1 WorkflowTemplateService API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.operation
import google.api_core.operations_v1
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.cloud.dataproc_v1.gapic import enums
from google.cloud.dataproc_v1.gapic import workflow_template_service_client_config
from google.cloud.dataproc_v1.gapic.transports import (
    workflow_template_service_grpc_transport,
)
from google.cloud.dataproc_v1.proto import autoscaling_policies_pb2
from google.cloud.dataproc_v1.proto import autoscaling_policies_pb2_grpc
from google.cloud.dataproc_v1.proto import clusters_pb2
from google.cloud.dataproc_v1.proto import clusters_pb2_grpc
from google.cloud.dataproc_v1.proto import jobs_pb2
from google.cloud.dataproc_v1.proto import jobs_pb2_grpc
from google.cloud.dataproc_v1.proto import operations_pb2 as proto_operations_pb2
from google.cloud.dataproc_v1.proto import workflow_templates_pb2
from google.cloud.dataproc_v1.proto import workflow_templates_pb2_grpc
from google.longrunning import operations_pb2 as longrunning_operations_pb2
from google.protobuf import duration_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution("google-cloud-dataproc").version


class WorkflowTemplateServiceClient(object):
    """
    The API interface for managing Workflow Templates in the
    Dataproc API.
    """

    SERVICE_ADDRESS = "dataproc.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.dataproc.v1.WorkflowTemplateService"

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
            WorkflowTemplateServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def location_path(cls, project, location):
        """Return a fully-qualified location string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}",
            project=project,
            location=location,
        )

    @classmethod
    def region_path(cls, project, region):
        """Return a fully-qualified region string."""
        return google.api_core.path_template.expand(
            "projects/{project}/regions/{region}", project=project, region=region
        )

    @classmethod
    def workflow_template_path(cls, project, region, workflow_template):
        """Return a fully-qualified workflow_template string."""
        return google.api_core.path_template.expand(
            "projects/{project}/regions/{region}/workflowTemplates/{workflow_template}",
            project=project,
            region=region,
            workflow_template=workflow_template,
        )

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
            transport (Union[~.WorkflowTemplateServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.WorkflowTemplateServiceGrpcTransport]): A transport
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
            client_config = workflow_template_service_client_config.config

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
                    default_class=workflow_template_service_grpc_transport.WorkflowTemplateServiceGrpcTransport,
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
            self.transport = workflow_template_service_grpc_transport.WorkflowTemplateServiceGrpcTransport(
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
    def create_workflow_template(
        self,
        parent,
        template,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates new workflow template.

        Example:
            >>> from google.cloud import dataproc_v1
            >>>
            >>> client = dataproc_v1.WorkflowTemplateServiceClient()
            >>>
            >>> parent = client.region_path('[PROJECT]', '[REGION]')
            >>>
            >>> # TODO: Initialize `template`:
            >>> template = {}
            >>>
            >>> response = client.create_workflow_template(parent, template)

        Args:
            parent (str): A URL/resource name that uniquely identifies the type of the
                serialized protocol buffer message. This string must contain at least
                one "/" character. The last segment of the URL's path must represent the
                fully qualified name of the type (as in
                ``path/google.protobuf.Duration``). The name should be in a canonical
                form (e.g., leading "." is not accepted).

                In practice, teams usually precompile into the binary all types that
                they expect it to use in the context of Any. However, for URLs which use
                the scheme ``http``, ``https``, or no scheme, one can optionally set up
                a type server that maps type URLs to message definitions as follows:

                -  If no scheme is provided, ``https`` is assumed.
                -  An HTTP GET on the URL must yield a ``google.protobuf.Type`` value in
                   binary format, or produce an error.
                -  Applications are allowed to cache lookup results based on the URL, or
                   have them precompiled into a binary to avoid any lookup. Therefore,
                   binary compatibility needs to be preserved on changes to types. (Use
                   versioned type names to manage breaking changes.)

                Note: this functionality is not currently available in the official
                protobuf release, and it is not used for type URLs beginning with
                type.googleapis.com.

                Schemes other than ``http``, ``https`` (or the empty scheme) might be
                used with implementation specific semantics.
            template (Union[dict, ~google.cloud.dataproc_v1.types.WorkflowTemplate]): Required. The Dataproc workflow template to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dataproc_v1.types.WorkflowTemplate`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dataproc_v1.types.WorkflowTemplate` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_workflow_template" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_workflow_template"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_workflow_template,
                default_retry=self._method_configs["CreateWorkflowTemplate"].retry,
                default_timeout=self._method_configs["CreateWorkflowTemplate"].timeout,
                client_info=self._client_info,
            )

        request = workflow_templates_pb2.CreateWorkflowTemplateRequest(
            parent=parent, template=template
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_workflow_template"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_workflow_template(
        self,
        name,
        version=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Retrieves the latest workflow template.

        Can retrieve previously instantiated template by specifying optional
        version parameter.

        Example:
            >>> from google.cloud import dataproc_v1
            >>>
            >>> client = dataproc_v1.WorkflowTemplateServiceClient()
            >>>
            >>> # TODO: Initialize `name`:
            >>> name = ''
            >>>
            >>> response = client.get_workflow_template(name)

        Args:
            name (str): Output only. The job status. Additional application-specific status
                information may be contained in the type_job and yarn_applications
                fields.
            version (int): Optional. The version of workflow template to retrieve. Only previously
                instantiated versions can be retrieved.

                If unspecified, retrieves the current version.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dataproc_v1.types.WorkflowTemplate` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_workflow_template" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_workflow_template"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_workflow_template,
                default_retry=self._method_configs["GetWorkflowTemplate"].retry,
                default_timeout=self._method_configs["GetWorkflowTemplate"].timeout,
                client_info=self._client_info,
            )

        request = workflow_templates_pb2.GetWorkflowTemplateRequest(
            name=name, version=version
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_workflow_template"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def instantiate_workflow_template(
        self,
        name,
        version=None,
        request_id=None,
        parameters=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Optional. Whether to continue executing queries if a query fails.
        The default value is ``false``. Setting to ``true`` can be useful when
        executing independent parallel queries.

        Example:
            >>> from google.cloud import dataproc_v1
            >>>
            >>> client = dataproc_v1.WorkflowTemplateServiceClient()
            >>>
            >>> # TODO: Initialize `name`:
            >>> name = ''
            >>>
            >>> response = client.instantiate_workflow_template(name)
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
            name (str): The Compute Engine metadata entries to add to all instances (see
                `Project and instance
                metadata <https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata>`__).
            version (int): Optional. The version of workflow template to instantiate. If specified,
                the workflow will be instantiated only if the current version of
                the workflow template has the supplied version.

                This option cannot be used to instantiate a previous version of
                workflow template.
            request_id (str): Signed fractions of a second at nanosecond resolution of the span of
                time. Durations less than one second are represented with a 0
                ``seconds`` field and a positive or negative ``nanos`` field. For
                durations of one second or more, a non-zero value for the ``nanos``
                field must be of the same sign as the ``seconds`` field. Must be from
                -999,999,999 to +999,999,999 inclusive.
            parameters (dict[str -> str]): Optional. Map from parameter names to values that should be used for those
                parameters. Values may not exceed 100 characters.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dataproc_v1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "instantiate_workflow_template" not in self._inner_api_calls:
            self._inner_api_calls[
                "instantiate_workflow_template"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.instantiate_workflow_template,
                default_retry=self._method_configs["InstantiateWorkflowTemplate"].retry,
                default_timeout=self._method_configs[
                    "InstantiateWorkflowTemplate"
                ].timeout,
                client_info=self._client_info,
            )

        request = workflow_templates_pb2.InstantiateWorkflowTemplateRequest(
            name=name, version=version, request_id=request_id, parameters=parameters
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["instantiate_workflow_template"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            empty_pb2.Empty,
            metadata_type=workflow_templates_pb2.WorkflowMetadata,
        )

    def instantiate_inline_workflow_template(
        self,
        parent,
        template,
        request_id=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Optional. The `Dataproc service
        account <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#service_accounts_in_cloud_dataproc>`__
        (also see `VM Data Plane
        identity <https://cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity>`__)
        used by Dataproc cluster VM instances to access Google Cloud Platform
        services.

        If not specified, the `Compute Engine default service
        account <https://cloud.google.com/compute/docs/access/service-accounts#default_service_account>`__
        is used.

        Example:
            >>> from google.cloud import dataproc_v1
            >>>
            >>> client = dataproc_v1.WorkflowTemplateServiceClient()
            >>>
            >>> parent = client.region_path('[PROJECT]', '[REGION]')
            >>>
            >>> # TODO: Initialize `template`:
            >>> template = {}
            >>>
            >>> response = client.instantiate_inline_workflow_template(parent, template)
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
            parent (str): Each of the definitions above may have "options" attached. These are
                just annotations which may cause code to be generated slightly
                differently or may contain hints for code that manipulates protocol
                messages.

                Clients may define custom options as extensions of the \*Options
                messages. These extensions may not yet be known at parsing time, so the
                parser cannot store the values in them. Instead it stores them in a
                field in the \*Options message called uninterpreted_option. This field
                must have the same name across all \*Options messages. We then use this
                field to populate the extensions when we build a descriptor, at which
                point all protos have been parsed and so all extensions are known.

                Extension numbers for custom options may be chosen as follows:

                -  For options which will only be used within a single application or
                   organization, or for experimental options, use field numbers 50000
                   through 99999. It is up to you to ensure that you do not use the same
                   number for multiple options.
                -  For options which will be published and used publicly by multiple
                   independent entities, e-mail
                   protobuf-global-extension-registry@google.com to reserve extension
                   numbers. Simply provide your project name (e.g. Objective-C plugin)
                   and your project website (if available) -- there's no need to explain
                   how you intend to use them. Usually you only need one extension
                   number. You can declare multiple options with only one extension
                   number by putting them in a sub-message. See the Custom Options
                   section of the docs for examples:
                   https://developers.google.com/protocol-buffers/docs/proto#options If
                   this turns out to be popular, a web service will be set up to
                   automatically assign option numbers.
            template (Union[dict, ~google.cloud.dataproc_v1.types.WorkflowTemplate]): Required. The workflow template to instantiate.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dataproc_v1.types.WorkflowTemplate`
            request_id (str): See ``HttpRule``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dataproc_v1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "instantiate_inline_workflow_template" not in self._inner_api_calls:
            self._inner_api_calls[
                "instantiate_inline_workflow_template"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.instantiate_inline_workflow_template,
                default_retry=self._method_configs[
                    "InstantiateInlineWorkflowTemplate"
                ].retry,
                default_timeout=self._method_configs[
                    "InstantiateInlineWorkflowTemplate"
                ].timeout,
                client_info=self._client_info,
            )

        request = workflow_templates_pb2.InstantiateInlineWorkflowTemplateRequest(
            parent=parent, template=template, request_id=request_id
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["instantiate_inline_workflow_template"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            empty_pb2.Empty,
            metadata_type=workflow_templates_pb2.WorkflowMetadata,
        )

    def update_workflow_template(
        self,
        template,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates (replaces) workflow template. The updated template
        must contain version that matches the current server version.

        Example:
            >>> from google.cloud import dataproc_v1
            >>>
            >>> client = dataproc_v1.WorkflowTemplateServiceClient()
            >>>
            >>> # TODO: Initialize `template`:
            >>> template = {}
            >>>
            >>> response = client.update_workflow_template(template)

        Args:
            template (Union[dict, ~google.cloud.dataproc_v1.types.WorkflowTemplate]): Optional. Whether to continue executing queries if a query fails.
                The default value is ``false``. Setting to ``true`` can be useful when
                executing independent parallel queries.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dataproc_v1.types.WorkflowTemplate`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dataproc_v1.types.WorkflowTemplate` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_workflow_template" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_workflow_template"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_workflow_template,
                default_retry=self._method_configs["UpdateWorkflowTemplate"].retry,
                default_timeout=self._method_configs["UpdateWorkflowTemplate"].timeout,
                client_info=self._client_info,
            )

        request = workflow_templates_pb2.UpdateWorkflowTemplateRequest(
            template=template
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("template.name", template.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_workflow_template"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_workflow_templates(
        self,
        parent,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists workflows that match the specified filter in the request.

        Example:
            >>> from google.cloud import dataproc_v1
            >>>
            >>> client = dataproc_v1.WorkflowTemplateServiceClient()
            >>>
            >>> parent = client.region_path('[PROJECT]', '[REGION]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_workflow_templates(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_workflow_templates(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): If set, all the classes from the .proto file are wrapped in a single
                outer class with the given name. This applies to both Proto1 (equivalent
                to the old "--one_java_file" option) and Proto2 (where a .proto always
                translates to a single class, but you may want to explicitly choose the
                class name).
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
            An iterable of :class:`~google.cloud.dataproc_v1.types.WorkflowTemplate` instances.
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
        if "list_workflow_templates" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_workflow_templates"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_workflow_templates,
                default_retry=self._method_configs["ListWorkflowTemplates"].retry,
                default_timeout=self._method_configs["ListWorkflowTemplates"].timeout,
                client_info=self._client_info,
            )

        request = workflow_templates_pb2.ListWorkflowTemplatesRequest(
            parent=parent, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_workflow_templates"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="templates",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def delete_workflow_template(
        self,
        name,
        version=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a workflow template. It does not cancel in-progress workflows.

        Example:
            >>> from google.cloud import dataproc_v1
            >>>
            >>> client = dataproc_v1.WorkflowTemplateServiceClient()
            >>>
            >>> # TODO: Initialize `name`:
            >>> name = ''
            >>>
            >>> client.delete_workflow_template(name)

        Args:
            name (str): Denotes a field as required. This indicates that the field **must**
                be provided as part of the request, and failure to do so will cause an
                error (usually ``INVALID_ARGUMENT``).
            version (int): Optional. The version of workflow template to delete. If specified,
                will only delete the template if the current server version matches
                specified version.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_workflow_template" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_workflow_template"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_workflow_template,
                default_retry=self._method_configs["DeleteWorkflowTemplate"].retry,
                default_timeout=self._method_configs["DeleteWorkflowTemplate"].timeout,
                client_info=self._client_info,
            )

        request = workflow_templates_pb2.DeleteWorkflowTemplateRequest(
            name=name, version=version
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_workflow_template"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
