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

"""Accesses the google.cloud.dataproc.v1beta2 WorkflowTemplateService API."""

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

from google.cloud.dataproc_v1beta2.gapic import enums
from google.cloud.dataproc_v1beta2.gapic import workflow_template_service_client_config
from google.cloud.dataproc_v1beta2.gapic.transports import (
    workflow_template_service_grpc_transport,
)
from google.cloud.dataproc_v1beta2.proto import autoscaling_policies_pb2
from google.cloud.dataproc_v1beta2.proto import autoscaling_policies_pb2_grpc
from google.cloud.dataproc_v1beta2.proto import clusters_pb2
from google.cloud.dataproc_v1beta2.proto import clusters_pb2_grpc
from google.cloud.dataproc_v1beta2.proto import jobs_pb2
from google.cloud.dataproc_v1beta2.proto import jobs_pb2_grpc
from google.cloud.dataproc_v1beta2.proto import operations_pb2 as proto_operations_pb2
from google.cloud.dataproc_v1beta2.proto import workflow_templates_pb2
from google.cloud.dataproc_v1beta2.proto import workflow_templates_pb2_grpc
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
    _INTERFACE_NAME = "google.cloud.dataproc.v1beta2.WorkflowTemplateService"

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
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.WorkflowTemplateServiceClient()
            >>>
            >>> parent = client.region_path('[PROJECT]', '[REGION]')
            >>>
            >>> # TODO: Initialize `template`:
            >>> template = {}
            >>>
            >>> response = client.create_workflow_template(parent, template)

        Args:
            parent (str): Optional. Mapping of query variable names to values (equivalent to
                the Pig command: ``name=[value]``).
            template (Union[dict, ~google.cloud.dataproc_v1beta2.types.WorkflowTemplate]): Required. The Dataproc workflow template to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dataproc_v1beta2.types.WorkflowTemplate`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dataproc_v1beta2.types.WorkflowTemplate` instance.

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
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.WorkflowTemplateServiceClient()
            >>>
            >>> # TODO: Initialize `name`:
            >>> name = ''
            >>>
            >>> response = client.get_workflow_template(name)

        Args:
            name (str): Optional. Specifies enumerated categories of jobs to list. (default
                = match ALL jobs).

                If ``filter`` is provided, ``jobStateMatcher`` will be ignored.
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
            A :class:`~google.cloud.dataproc_v1beta2.types.WorkflowTemplate` instance.

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
        instance_id=None,
        request_id=None,
        parameters=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Instantiates a template and begins execution.

        This method is equivalent to executing the sequence
        ``CreateWorkflowTemplate``, ``InstantiateWorkflowTemplate``,
        ``DeleteWorkflowTemplate``.

        The returned Operation can be used to track execution of workflow by
        polling ``operations.get``. The Operation will complete when entire
        workflow is finished.

        The running workflow can be aborted via ``operations.cancel``. This will
        cause any inflight jobs to be cancelled and workflow-owned clusters to
        be deleted.

        The ``Operation.metadata`` will be
        `WorkflowMetadata <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata>`__.
        Also see `Using
        WorkflowMetadata <https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata>`__.

        On successful completion, ``Operation.response`` will be ``Empty``.

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.WorkflowTemplateServiceClient()
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
            name (str): Protocol Buffers - Google's data interchange format Copyright 2008
                Google Inc. All rights reserved.
                https://developers.google.com/protocol-buffers/

                Redistribution and use in source and binary forms, with or without
                modification, are permitted provided that the following conditions are
                met:

                ::

                    * Redistributions of source code must retain the above copyright

                notice, this list of conditions and the following disclaimer. \*
                Redistributions in binary form must reproduce the above copyright
                notice, this list of conditions and the following disclaimer in the
                documentation and/or other materials provided with the distribution. \*
                Neither the name of Google Inc. nor the names of its contributors may be
                used to endorse or promote products derived from this software without
                specific prior written permission.

                THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
                IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
                TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
                PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
                OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
                EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
                PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
                PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
                LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
                NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
                SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
            version (int): Optional. The version of workflow template to instantiate. If specified,
                the workflow will be instantiated only if the current version of
                the workflow template has the supplied version.

                This option cannot be used to instantiate a previous version of
                workflow template.
            instance_id (str): The name of the driver's main class. The jar file containing the
                class must be in the default CLASSPATH or specified in
                ``jar_file_uris``.
            request_id (str): Each of the definitions above may have "options" attached. These are
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
            A :class:`~google.cloud.dataproc_v1beta2.types._OperationFuture` instance.

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
            name=name,
            version=version,
            instance_id=instance_id,
            request_id=request_id,
            parameters=parameters,
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
        instance_id=None,
        request_id=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Optional. The labels to associate with this cluster.

        Label keys must be between 1 and 63 characters long, and must conform to
        the following PCRE regular expression:
        [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}

        Label values must be between 1 and 63 characters long, and must conform
        to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63}

        No more than 32 labels can be associated with a given cluster.

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.WorkflowTemplateServiceClient()
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
            parent (str): Optional. A mapping of property names to values, used to configure
                Pig. Properties that conflict with values set by the Dataproc API may be
                overwritten. Can include properties set in /etc/hadoop/conf/*-site.xml,
                /etc/pig/conf/pig.properties, and classes in user code.
            template (Union[dict, ~google.cloud.dataproc_v1beta2.types.WorkflowTemplate]): Required. The workflow template to instantiate.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dataproc_v1beta2.types.WorkflowTemplate`
            instance_id (str): Optional. A filter constraining the jobs to list. Filters are
                case-sensitive and have the following syntax:

                [field = value] AND [field [= value]] ...

                where **field** is ``status.state`` or ``labels.[KEY]``, and ``[KEY]``
                is a label key. **value** can be ``*`` to match all values.
                ``status.state`` can be either ``ACTIVE`` or ``NON_ACTIVE``. Only the
                logical ``AND`` operator is supported; space-separated items are treated
                as having an implicit ``AND`` operator.

                Example filter:

                status.state = ACTIVE AND labels.env = staging AND labels.starred = \*
            request_id (str): Optional. The arguments to pass to the driver. Do not include
                arguments, such as ``-libjars`` or ``-Dfoo=bar``, that can be set as job
                properties, since a collision may occur that causes an incorrect job
                submission.
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
            parent=parent,
            template=template,
            instance_id=instance_id,
            request_id=request_id,
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
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.WorkflowTemplateServiceClient()
            >>>
            >>> # TODO: Initialize `template`:
            >>> template = {}
            >>>
            >>> response = client.update_workflow_template(template)

        Args:
            template (Union[dict, ~google.cloud.dataproc_v1beta2.types.WorkflowTemplate]): Denotes a field as required. This indicates that the field **must**
                be provided as part of the request, and failure to do so will cause an
                error (usually ``INVALID_ARGUMENT``).

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dataproc_v1beta2.types.WorkflowTemplate`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dataproc_v1beta2.types.WorkflowTemplate` instance.

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
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.WorkflowTemplateServiceClient()
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
            An iterable of :class:`~google.cloud.dataproc_v1beta2.types.WorkflowTemplate` instances.
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
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.WorkflowTemplateServiceClient()
            >>>
            >>> # TODO: Initialize `name`:
            >>> name = ''
            >>>
            >>> client.delete_workflow_template(name)

        Args:
            name (str): A Timestamp represents a point in time independent of any time zone
                or local calendar, encoded as a count of seconds and fractions of
                seconds at nanosecond resolution. The count is relative to an epoch at
                UTC midnight on January 1, 1970, in the proleptic Gregorian calendar
                which extends the Gregorian calendar backwards to year one.

                All minutes are 60 seconds long. Leap seconds are "smeared" so that no
                leap second table is needed for interpretation, using a `24-hour linear
                smear <https://developers.google.com/time/smear>`__.

                The range is from 0001-01-01T00:00:00Z to
                9999-12-31T23:59:59.999999999Z. By restricting to that range, we ensure
                that we can convert to and from `RFC
                3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ date strings.

                # Examples

                Example 1: Compute Timestamp from POSIX ``time()``.

                ::

                    Timestamp timestamp;
                    timestamp.set_seconds(time(NULL));
                    timestamp.set_nanos(0);

                Example 2: Compute Timestamp from POSIX ``gettimeofday()``.

                ::

                    struct timeval tv;
                    gettimeofday(&tv, NULL);

                    Timestamp timestamp;
                    timestamp.set_seconds(tv.tv_sec);
                    timestamp.set_nanos(tv.tv_usec * 1000);

                Example 3: Compute Timestamp from Win32 ``GetSystemTimeAsFileTime()``.

                ::

                    FILETIME ft;
                    GetSystemTimeAsFileTime(&ft);
                    UINT64 ticks = (((UINT64)ft.dwHighDateTime) << 32) | ft.dwLowDateTime;

                    // A Windows tick is 100 nanoseconds. Windows epoch 1601-01-01T00:00:00Z
                    // is 11644473600 seconds before Unix epoch 1970-01-01T00:00:00Z.
                    Timestamp timestamp;
                    timestamp.set_seconds((INT64) ((ticks / 10000000) - 11644473600LL));
                    timestamp.set_nanos((INT32) ((ticks % 10000000) * 100));

                Example 4: Compute Timestamp from Java ``System.currentTimeMillis()``.

                ::

                    long millis = System.currentTimeMillis();

                    Timestamp timestamp = Timestamp.newBuilder().setSeconds(millis / 1000)
                        .setNanos((int) ((millis % 1000) * 1000000)).build();

                Example 5: Compute Timestamp from current time in Python.

                ::

                    timestamp = Timestamp()
                    timestamp.GetCurrentTime()

                # JSON Mapping

                In JSON format, the Timestamp type is encoded as a string in the `RFC
                3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ format. That is, the
                format is "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z" where
                {year} is always expressed using four digits while {month}, {day},
                {hour}, {min}, and {sec} are zero-padded to two digits each. The
                fractional seconds, which can go up to 9 digits (i.e. up to 1 nanosecond
                resolution), are optional. The "Z" suffix indicates the timezone
                ("UTC"); the timezone is required. A proto3 JSON serializer should
                always use UTC (as indicated by "Z") when printing the Timestamp type
                and a proto3 JSON parser should be able to accept both UTC and other
                timezones (as indicated by an offset).

                For example, "2017-01-15T01:30:15.01Z" encodes 15.01 seconds past 01:30
                UTC on January 15, 2017.

                In JavaScript, one can convert a Date object to this format using the
                standard
                `toISOString() <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString>`__
                method. In Python, a standard ``datetime.datetime`` object can be
                converted to this format using
                ```strftime`` <https://docs.python.org/2/library/time.html#time.strftime>`__
                with the time format spec '%Y-%m-%dT%H:%M:%S.%fZ'. Likewise, in Java,
                one can use the Joda Time's
                ```ISODateTimeFormat.dateTime()`` <http://www.joda.org/joda-time/apidocs/org/joda/time/format/ISODateTimeFormat.html#dateTime%2D%2D>`__
                to obtain a formatter capable of generating timestamps in this format.
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
