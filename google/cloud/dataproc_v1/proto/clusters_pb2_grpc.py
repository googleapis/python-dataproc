# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.cloud.dataproc_v1.proto import (
    clusters_pb2 as google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)


class ClusterControllerStub(object):
    """The ClusterControllerService provides methods to manage clusters
    of Compute Engine instances.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateCluster = channel.unary_unary(
            "/google.cloud.dataproc.v1.ClusterController/CreateCluster",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.CreateClusterRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.UpdateCluster = channel.unary_unary(
            "/google.cloud.dataproc.v1.ClusterController/UpdateCluster",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.UpdateClusterRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.DeleteCluster = channel.unary_unary(
            "/google.cloud.dataproc.v1.ClusterController/DeleteCluster",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.DeleteClusterRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.GetCluster = channel.unary_unary(
            "/google.cloud.dataproc.v1.ClusterController/GetCluster",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.GetClusterRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.Cluster.FromString,
        )
        self.ListClusters = channel.unary_unary(
            "/google.cloud.dataproc.v1.ClusterController/ListClusters",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.ListClustersRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.ListClustersResponse.FromString,
        )
        self.DiagnoseCluster = channel.unary_unary(
            "/google.cloud.dataproc.v1.ClusterController/DiagnoseCluster",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.DiagnoseClusterRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class ClusterControllerServicer(object):
    """The ClusterControllerService provides methods to manage clusters
    of Compute Engine instances.
    """

    def CreateCluster(self, request, context):
        """Creates a cluster in a project. The returned
        [Operation.metadata][google.longrunning.Operation.metadata] will be
        [ClusterOperationMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateCluster(self, request, context):
        """Updates a cluster in a project. The returned
        [Operation.metadata][google.longrunning.Operation.metadata] will be
        [ClusterOperationMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteCluster(self, request, context):
        """Deletes a cluster in a project. The returned
        [Operation.metadata][google.longrunning.Operation.metadata] will be
        [ClusterOperationMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetCluster(self, request, context):
        """Gets the resource representation for a cluster in a project."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListClusters(self, request, context):
        """Lists all regions/{region}/clusters in a project alphabetically."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DiagnoseCluster(self, request, context):
        """Gets cluster diagnostic information. The returned
        [Operation.metadata][google.longrunning.Operation.metadata] will be
        [ClusterOperationMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata).
        After the operation completes,
        [Operation.response][google.longrunning.Operation.response]
        contains
        [DiagnoseClusterResults](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#diagnoseclusterresults).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ClusterControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateCluster": grpc.unary_unary_rpc_method_handler(
            servicer.CreateCluster,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.CreateClusterRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "UpdateCluster": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateCluster,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.UpdateClusterRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "DeleteCluster": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteCluster,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.DeleteClusterRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "GetCluster": grpc.unary_unary_rpc_method_handler(
            servicer.GetCluster,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.GetClusterRequest.FromString,
            response_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.Cluster.SerializeToString,
        ),
        "ListClusters": grpc.unary_unary_rpc_method_handler(
            servicer.ListClusters,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.ListClustersRequest.FromString,
            response_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.ListClustersResponse.SerializeToString,
        ),
        "DiagnoseCluster": grpc.unary_unary_rpc_method_handler(
            servicer.DiagnoseCluster,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.DiagnoseClusterRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.dataproc.v1.ClusterController", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ClusterController(object):
    """The ClusterControllerService provides methods to manage clusters
    of Compute Engine instances.
    """

    @staticmethod
    def CreateCluster(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dataproc.v1.ClusterController/CreateCluster",
            google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.CreateClusterRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateCluster(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dataproc.v1.ClusterController/UpdateCluster",
            google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.UpdateClusterRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteCluster(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dataproc.v1.ClusterController/DeleteCluster",
            google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.DeleteClusterRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetCluster(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dataproc.v1.ClusterController/GetCluster",
            google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.GetClusterRequest.SerializeToString,
            google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.Cluster.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListClusters(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dataproc.v1.ClusterController/ListClusters",
            google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.ListClustersRequest.SerializeToString,
            google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.ListClustersResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DiagnoseCluster(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dataproc.v1.ClusterController/DiagnoseCluster",
            google_dot_cloud_dot_dataproc__v1_dot_proto_dot_clusters__pb2.DiagnoseClusterRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
