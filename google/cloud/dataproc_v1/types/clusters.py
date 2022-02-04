# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.cloud.dataproc_v1.types import shared
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.dataproc.v1",
    manifest={
        "Cluster",
        "ClusterConfig",
        "GkeClusterConfig",
        "EndpointConfig",
        "AutoscalingConfig",
        "EncryptionConfig",
        "GceClusterConfig",
        "NodeGroupAffinity",
        "ShieldedInstanceConfig",
        "ConfidentialInstanceConfig",
        "InstanceGroupConfig",
        "ManagedGroupConfig",
        "AcceleratorConfig",
        "DiskConfig",
        "NodeInitializationAction",
        "ClusterStatus",
        "SecurityConfig",
        "KerberosConfig",
        "IdentityConfig",
        "SoftwareConfig",
        "LifecycleConfig",
        "MetastoreConfig",
        "ClusterMetrics",
        "CreateClusterRequest",
        "UpdateClusterRequest",
        "StopClusterRequest",
        "StartClusterRequest",
        "DeleteClusterRequest",
        "GetClusterRequest",
        "ListClustersRequest",
        "ListClustersResponse",
        "DiagnoseClusterRequest",
        "DiagnoseClusterResults",
        "ReservationAffinity",
    },
)


class Cluster(proto.Message):
    r"""Describes the identifying information, config, and status of
    a Dataproc cluster

    Attributes:
        project_id (str):
            Required. The Google Cloud Platform project
            ID that the cluster belongs to.
        cluster_name (str):
            Required. The cluster name. Cluster names
            within a project must be unique. Names of
            deleted clusters can be reused.
        config (google.cloud.dataproc_v1.types.ClusterConfig):
            Optional. The cluster config for a cluster of
            Compute Engine Instances. Note that Dataproc may
            set default values, and values may change when
            clusters are updated.
        labels (Sequence[google.cloud.dataproc_v1.types.Cluster.LabelsEntry]):
            Optional. The labels to associate with this cluster. Label
            **keys** must contain 1 to 63 characters, and must conform
            to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`__.
            Label **values** may be empty, but, if present, must contain
            1 to 63 characters, and must conform to `RFC
            1035 <https://www.ietf.org/rfc/rfc1035.txt>`__. No more than
            32 labels can be associated with a cluster.
        status (google.cloud.dataproc_v1.types.ClusterStatus):
            Output only. Cluster status.
        status_history (Sequence[google.cloud.dataproc_v1.types.ClusterStatus]):
            Output only. The previous cluster status.
        cluster_uuid (str):
            Output only. A cluster UUID (Unique Universal
            Identifier). Dataproc generates this value when
            it creates the cluster.
        metrics (google.cloud.dataproc_v1.types.ClusterMetrics):
            Output only. Contains cluster daemon metrics such as HDFS
            and YARN stats.

            **Beta Feature**: This report is available for testing
            purposes only. It may be changed before final release.
    """

    project_id = proto.Field(proto.STRING, number=1,)
    cluster_name = proto.Field(proto.STRING, number=2,)
    config = proto.Field(proto.MESSAGE, number=3, message="ClusterConfig",)
    labels = proto.MapField(proto.STRING, proto.STRING, number=8,)
    status = proto.Field(proto.MESSAGE, number=4, message="ClusterStatus",)
    status_history = proto.RepeatedField(
        proto.MESSAGE, number=7, message="ClusterStatus",
    )
    cluster_uuid = proto.Field(proto.STRING, number=6,)
    metrics = proto.Field(proto.MESSAGE, number=9, message="ClusterMetrics",)


class ClusterConfig(proto.Message):
    r"""The cluster config.

    Attributes:
        config_bucket (str):
            Optional. A Cloud Storage bucket used to stage job
            dependencies, config files, and job driver console output.
            If you do not specify a staging bucket, Cloud Dataproc will
            determine a Cloud Storage location (US, ASIA, or EU) for
            your cluster's staging bucket according to the Compute
            Engine zone where your cluster is deployed, and then create
            and manage this project-level, per-location bucket (see
            `Dataproc staging and temp
            buckets <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket>`__).
            **This field requires a Cloud Storage bucket name, not a
            ``gs://...`` URI to a Cloud Storage bucket.**
        temp_bucket (str):
            Optional. A Cloud Storage bucket used to store ephemeral
            cluster and jobs data, such as Spark and MapReduce history
            files. If you do not specify a temp bucket, Dataproc will
            determine a Cloud Storage location (US, ASIA, or EU) for
            your cluster's temp bucket according to the Compute Engine
            zone where your cluster is deployed, and then create and
            manage this project-level, per-location bucket. The default
            bucket has a TTL of 90 days, but you can use any TTL (or
            none) if you specify a bucket (see `Dataproc staging and
            temp
            buckets <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket>`__).
            **This field requires a Cloud Storage bucket name, not a
            ``gs://...`` URI to a Cloud Storage bucket.**
        gce_cluster_config (google.cloud.dataproc_v1.types.GceClusterConfig):
            Optional. The shared Compute Engine config
            settings for all instances in a cluster.
        master_config (google.cloud.dataproc_v1.types.InstanceGroupConfig):
            Optional. The Compute Engine config settings
            for the cluster's master instance.
        worker_config (google.cloud.dataproc_v1.types.InstanceGroupConfig):
            Optional. The Compute Engine config settings
            for the cluster's worker instances.
        secondary_worker_config (google.cloud.dataproc_v1.types.InstanceGroupConfig):
            Optional. The Compute Engine config settings
            for a cluster's secondary worker instances
        software_config (google.cloud.dataproc_v1.types.SoftwareConfig):
            Optional. The config settings for cluster
            software.
        initialization_actions (Sequence[google.cloud.dataproc_v1.types.NodeInitializationAction]):
            Optional. Commands to execute on each node after config is
            completed. By default, executables are run on master and all
            worker nodes. You can test a node's ``role`` metadata to run
            an executable on a master or worker node, as shown below
            using ``curl`` (you can also use ``wget``):

            ::

                ROLE=$(curl -H Metadata-Flavor:Google
                http://metadata/computeMetadata/v1/instance/attributes/dataproc-role)
                if [[ "${ROLE}" == 'Master' ]]; then
                  ... master specific actions ...
                else
                  ... worker specific actions ...
                fi
        encryption_config (google.cloud.dataproc_v1.types.EncryptionConfig):
            Optional. Encryption settings for the
            cluster.
        autoscaling_config (google.cloud.dataproc_v1.types.AutoscalingConfig):
            Optional. Autoscaling config for the policy
            associated with the cluster. Cluster does not
            autoscale if this field is unset.
        security_config (google.cloud.dataproc_v1.types.SecurityConfig):
            Optional. Security settings for the cluster.
        lifecycle_config (google.cloud.dataproc_v1.types.LifecycleConfig):
            Optional. Lifecycle setting for the cluster.
        endpoint_config (google.cloud.dataproc_v1.types.EndpointConfig):
            Optional. Port/endpoint configuration for
            this cluster
        metastore_config (google.cloud.dataproc_v1.types.MetastoreConfig):
            Optional. Metastore configuration.
        gke_cluster_config (google.cloud.dataproc_v1.types.GkeClusterConfig):
            Optional. BETA. The Kubernetes Engine config for Dataproc
            clusters deployed to Kubernetes. Setting this is considered
            mutually exclusive with Compute Engine-based options such as
            ``gce_cluster_config``, ``master_config``,
            ``worker_config``, ``secondary_worker_config``, and
            ``autoscaling_config``.
    """

    config_bucket = proto.Field(proto.STRING, number=1,)
    temp_bucket = proto.Field(proto.STRING, number=2,)
    gce_cluster_config = proto.Field(
        proto.MESSAGE, number=8, message="GceClusterConfig",
    )
    master_config = proto.Field(proto.MESSAGE, number=9, message="InstanceGroupConfig",)
    worker_config = proto.Field(
        proto.MESSAGE, number=10, message="InstanceGroupConfig",
    )
    secondary_worker_config = proto.Field(
        proto.MESSAGE, number=12, message="InstanceGroupConfig",
    )
    software_config = proto.Field(proto.MESSAGE, number=13, message="SoftwareConfig",)
    initialization_actions = proto.RepeatedField(
        proto.MESSAGE, number=11, message="NodeInitializationAction",
    )
    encryption_config = proto.Field(
        proto.MESSAGE, number=15, message="EncryptionConfig",
    )
    autoscaling_config = proto.Field(
        proto.MESSAGE, number=18, message="AutoscalingConfig",
    )
    security_config = proto.Field(proto.MESSAGE, number=16, message="SecurityConfig",)
    lifecycle_config = proto.Field(proto.MESSAGE, number=17, message="LifecycleConfig",)
    endpoint_config = proto.Field(proto.MESSAGE, number=19, message="EndpointConfig",)
    metastore_config = proto.Field(proto.MESSAGE, number=20, message="MetastoreConfig",)
    gke_cluster_config = proto.Field(
        proto.MESSAGE, number=21, message="GkeClusterConfig",
    )


class GkeClusterConfig(proto.Message):
    r"""The GKE config for this cluster.

    Attributes:
        namespaced_gke_deployment_target (google.cloud.dataproc_v1.types.GkeClusterConfig.NamespacedGkeDeploymentTarget):
            Optional. A target for the deployment.
    """

    class NamespacedGkeDeploymentTarget(proto.Message):
        r"""A full, namespace-isolated deployment target for an existing
        GKE cluster.

        Attributes:
            target_gke_cluster (str):
                Optional. The target GKE cluster to deploy to. Format:
                'projects/{project}/locations/{location}/clusters/{cluster_id}'
            cluster_namespace (str):
                Optional. A namespace within the GKE cluster
                to deploy into.
        """

        target_gke_cluster = proto.Field(proto.STRING, number=1,)
        cluster_namespace = proto.Field(proto.STRING, number=2,)

    namespaced_gke_deployment_target = proto.Field(
        proto.MESSAGE, number=1, message=NamespacedGkeDeploymentTarget,
    )


class EndpointConfig(proto.Message):
    r"""Endpoint config for this cluster

    Attributes:
        http_ports (Sequence[google.cloud.dataproc_v1.types.EndpointConfig.HttpPortsEntry]):
            Output only. The map of port descriptions to URLs. Will only
            be populated if enable_http_port_access is true.
        enable_http_port_access (bool):
            Optional. If true, enable http access to
            specific ports on the cluster from external
            sources. Defaults to false.
    """

    http_ports = proto.MapField(proto.STRING, proto.STRING, number=1,)
    enable_http_port_access = proto.Field(proto.BOOL, number=2,)


class AutoscalingConfig(proto.Message):
    r"""Autoscaling Policy config associated with the cluster.

    Attributes:
        policy_uri (str):
            Optional. The autoscaling policy used by the cluster.

            Only resource names including projectid and location
            (region) are valid. Examples:

            -  ``https://www.googleapis.com/compute/v1/projects/[project_id]/locations/[dataproc_region]/autoscalingPolicies/[policy_id]``
            -  ``projects/[project_id]/locations/[dataproc_region]/autoscalingPolicies/[policy_id]``

            Note that the policy must be in the same project and
            Dataproc region.
    """

    policy_uri = proto.Field(proto.STRING, number=1,)


class EncryptionConfig(proto.Message):
    r"""Encryption settings for the cluster.

    Attributes:
        gce_pd_kms_key_name (str):
            Optional. The Cloud KMS key name to use for
            PD disk encryption for all instances in the
            cluster.
    """

    gce_pd_kms_key_name = proto.Field(proto.STRING, number=1,)


class GceClusterConfig(proto.Message):
    r"""Common config settings for resources of Compute Engine
    cluster instances, applicable to all instances in the cluster.

    Attributes:
        zone_uri (str):
            Optional. The zone where the Compute Engine cluster will be
            located. On a create request, it is required in the "global"
            region. If omitted in a non-global Dataproc region, the
            service will pick a zone in the corresponding Compute Engine
            region. On a get request, zone will always be present.

            A full URL, partial URI, or short name are valid. Examples:

            -  ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/[zone]``
            -  ``projects/[project_id]/zones/[zone]``
            -  ``us-central1-f``
        network_uri (str):
            Optional. The Compute Engine network to be used for machine
            communications. Cannot be specified with subnetwork_uri. If
            neither ``network_uri`` nor ``subnetwork_uri`` is specified,
            the "default" network of the project is used, if it exists.
            Cannot be a "Custom Subnet Network" (see `Using
            Subnetworks <https://cloud.google.com/compute/docs/subnetworks>`__
            for more information).

            A full URL, partial URI, or short name are valid. Examples:

            -  ``https://www.googleapis.com/compute/v1/projects/[project_id]/regions/global/default``
            -  ``projects/[project_id]/regions/global/default``
            -  ``default``
        subnetwork_uri (str):
            Optional. The Compute Engine subnetwork to be used for
            machine communications. Cannot be specified with
            network_uri.

            A full URL, partial URI, or short name are valid. Examples:

            -  ``https://www.googleapis.com/compute/v1/projects/[project_id]/regions/us-east1/subnetworks/sub0``
            -  ``projects/[project_id]/regions/us-east1/subnetworks/sub0``
            -  ``sub0``
        internal_ip_only (bool):
            Optional. If true, all instances in the cluster will only
            have internal IP addresses. By default, clusters are not
            restricted to internal IP addresses, and will have ephemeral
            external IP addresses assigned to each instance. This
            ``internal_ip_only`` restriction can only be enabled for
            subnetwork enabled networks, and all off-cluster
            dependencies must be configured to be accessible without
            external IP addresses.
        private_ipv6_google_access (google.cloud.dataproc_v1.types.GceClusterConfig.PrivateIpv6GoogleAccess):
            Optional. The type of IPv6 access for a
            cluster.
        service_account (str):
            Optional. The `Dataproc service
            account <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#service_accounts_in_dataproc>`__
            (also see `VM Data Plane
            identity <https://cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity>`__)
            used by Dataproc cluster VM instances to access Google Cloud
            Platform services.

            If not specified, the `Compute Engine default service
            account <https://cloud.google.com/compute/docs/access/service-accounts#default_service_account>`__
            is used.
        service_account_scopes (Sequence[str]):
            Optional. The URIs of service account scopes to be included
            in Compute Engine instances. The following base set of
            scopes is always included:

            -  https://www.googleapis.com/auth/cloud.useraccounts.readonly
            -  https://www.googleapis.com/auth/devstorage.read_write
            -  https://www.googleapis.com/auth/logging.write

            If no scopes are specified, the following defaults are also
            provided:

            -  https://www.googleapis.com/auth/bigquery
            -  https://www.googleapis.com/auth/bigtable.admin.table
            -  https://www.googleapis.com/auth/bigtable.data
            -  https://www.googleapis.com/auth/devstorage.full_control
        tags (Sequence[str]):
            The Compute Engine tags to add to all instances (see
            `Tagging
            instances <https://cloud.google.com/compute/docs/label-or-tag-resources#tags>`__).
        metadata (Sequence[google.cloud.dataproc_v1.types.GceClusterConfig.MetadataEntry]):
            The Compute Engine metadata entries to add to all instances
            (see `Project and instance
            metadata <https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata>`__).
        reservation_affinity (google.cloud.dataproc_v1.types.ReservationAffinity):
            Optional. Reservation Affinity for consuming
            Zonal reservation.
        node_group_affinity (google.cloud.dataproc_v1.types.NodeGroupAffinity):
            Optional. Node Group Affinity for sole-tenant
            clusters.
        shielded_instance_config (google.cloud.dataproc_v1.types.ShieldedInstanceConfig):
            Optional. Shielded Instance Config for clusters using
            `Compute Engine Shielded
            VMs <https://cloud.google.com/security/shielded-cloud/shielded-vm>`__.
        confidential_instance_config (google.cloud.dataproc_v1.types.ConfidentialInstanceConfig):
            Optional. Confidential Instance Config for clusters using
            `Confidential
            VMs <https://cloud.google.com/compute/confidential-vm/docs>`__.
    """

    class PrivateIpv6GoogleAccess(proto.Enum):
        r"""``PrivateIpv6GoogleAccess`` controls whether and how Dataproc
        cluster nodes can communicate with Google Services through gRPC over
        IPv6. These values are directly mapped to corresponding values in
        the `Compute Engine Instance
        fields <https://cloud.google.com/compute/docs/reference/rest/v1/instances>`__.
        """
        PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED = 0
        INHERIT_FROM_SUBNETWORK = 1
        OUTBOUND = 2
        BIDIRECTIONAL = 3

    zone_uri = proto.Field(proto.STRING, number=1,)
    network_uri = proto.Field(proto.STRING, number=2,)
    subnetwork_uri = proto.Field(proto.STRING, number=6,)
    internal_ip_only = proto.Field(proto.BOOL, number=7,)
    private_ipv6_google_access = proto.Field(
        proto.ENUM, number=12, enum=PrivateIpv6GoogleAccess,
    )
    service_account = proto.Field(proto.STRING, number=8,)
    service_account_scopes = proto.RepeatedField(proto.STRING, number=3,)
    tags = proto.RepeatedField(proto.STRING, number=4,)
    metadata = proto.MapField(proto.STRING, proto.STRING, number=5,)
    reservation_affinity = proto.Field(
        proto.MESSAGE, number=11, message="ReservationAffinity",
    )
    node_group_affinity = proto.Field(
        proto.MESSAGE, number=13, message="NodeGroupAffinity",
    )
    shielded_instance_config = proto.Field(
        proto.MESSAGE, number=14, message="ShieldedInstanceConfig",
    )
    confidential_instance_config = proto.Field(
        proto.MESSAGE, number=15, message="ConfidentialInstanceConfig",
    )


class NodeGroupAffinity(proto.Message):
    r"""Node Group Affinity for clusters using sole-tenant node
    groups.

    Attributes:
        node_group_uri (str):
            Required. The URI of a sole-tenant `node group
            resource <https://cloud.google.com/compute/docs/reference/rest/v1/nodeGroups>`__
            that the cluster will be created on.

            A full URL, partial URI, or node group name are valid.
            Examples:

            -  ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-central1-a/nodeGroups/node-group-1``
            -  ``projects/[project_id]/zones/us-central1-a/nodeGroups/node-group-1``
            -  ``node-group-1``
    """

    node_group_uri = proto.Field(proto.STRING, number=1,)


class ShieldedInstanceConfig(proto.Message):
    r"""Shielded Instance Config for clusters using `Compute Engine Shielded
    VMs <https://cloud.google.com/security/shielded-cloud/shielded-vm>`__.

    Attributes:
        enable_secure_boot (bool):
            Optional. Defines whether instances have
            Secure Boot enabled.
        enable_vtpm (bool):
            Optional. Defines whether instances have the
            vTPM enabled.
        enable_integrity_monitoring (bool):
            Optional. Defines whether instances have
            integrity monitoring enabled.
    """

    enable_secure_boot = proto.Field(proto.BOOL, number=1,)
    enable_vtpm = proto.Field(proto.BOOL, number=2,)
    enable_integrity_monitoring = proto.Field(proto.BOOL, number=3,)


class ConfidentialInstanceConfig(proto.Message):
    r"""Confidential Instance Config for clusters using `Confidential
    VMs <https://cloud.google.com/compute/confidential-vm/docs>`__

    Attributes:
        enable_confidential_compute (bool):
            Optional. Defines whether the instance should
            have confidential compute enabled.
    """

    enable_confidential_compute = proto.Field(proto.BOOL, number=1,)


class InstanceGroupConfig(proto.Message):
    r"""The config settings for Compute Engine resources in
    an instance group, such as a master or worker group.

    Attributes:
        num_instances (int):
            Optional. The number of VM instances in the instance group.
            For `HA
            cluster </dataproc/docs/concepts/configuring-clusters/high-availability>`__
            `master_config <#FIELDS.master_config>`__ groups, **must be
            set to 3**. For standard cluster
            `master_config <#FIELDS.master_config>`__ groups, **must be
            set to 1**.
        instance_names (Sequence[str]):
            Output only. The list of instance names. Dataproc derives
            the names from ``cluster_name``, ``num_instances``, and the
            instance group.
        image_uri (str):
            Optional. The Compute Engine image resource used for cluster
            instances.

            The URI can represent an image or image family.

            Image examples:

            -  ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/[image-id]``
            -  ``projects/[project_id]/global/images/[image-id]``
            -  ``image-id``

            Image family examples. Dataproc will use the most recent
            image from the family:

            -  ``https://www.googleapis.com/compute/beta/projects/[project_id]/global/images/family/[custom-image-family-name]``
            -  ``projects/[project_id]/global/images/family/[custom-image-family-name]``

            If the URI is unspecified, it will be inferred from
            ``SoftwareConfig.image_version`` or the system default.
        machine_type_uri (str):
            Optional. The Compute Engine machine type used for cluster
            instances.

            A full URL, partial URI, or short name are valid. Examples:

            -  ``https://www.googleapis.com/compute/v1/projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2``
            -  ``projects/[project_id]/zones/us-east1-a/machineTypes/n1-standard-2``
            -  ``n1-standard-2``

            **Auto Zone Exception**: If you are using the Dataproc `Auto
            Zone
            Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`__
            feature, you must use the short name of the machine type
            resource, for example, ``n1-standard-2``.
        disk_config (google.cloud.dataproc_v1.types.DiskConfig):
            Optional. Disk option config settings.
        is_preemptible (bool):
            Output only. Specifies that this instance
            group contains preemptible instances.
        preemptibility (google.cloud.dataproc_v1.types.InstanceGroupConfig.Preemptibility):
            Optional. Specifies the preemptibility of the instance
            group.

            The default value for master and worker groups is
            ``NON_PREEMPTIBLE``. This default cannot be changed.

            The default value for secondary instances is
            ``PREEMPTIBLE``.
        managed_group_config (google.cloud.dataproc_v1.types.ManagedGroupConfig):
            Output only. The config for Compute Engine
            Instance Group Manager that manages this group.
            This is only used for preemptible instance
            groups.
        accelerators (Sequence[google.cloud.dataproc_v1.types.AcceleratorConfig]):
            Optional. The Compute Engine accelerator
            configuration for these instances.
        min_cpu_platform (str):
            Optional. Specifies the minimum cpu platform for the
            Instance Group. See `Dataproc -> Minimum CPU
            Platform <https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu>`__.
    """

    class Preemptibility(proto.Enum):
        r"""Controls the use of [preemptible instances]
        (https://cloud.google.com/compute/docs/instances/preemptible) within
        the group.
        """
        PREEMPTIBILITY_UNSPECIFIED = 0
        NON_PREEMPTIBLE = 1
        PREEMPTIBLE = 2

    num_instances = proto.Field(proto.INT32, number=1,)
    instance_names = proto.RepeatedField(proto.STRING, number=2,)
    image_uri = proto.Field(proto.STRING, number=3,)
    machine_type_uri = proto.Field(proto.STRING, number=4,)
    disk_config = proto.Field(proto.MESSAGE, number=5, message="DiskConfig",)
    is_preemptible = proto.Field(proto.BOOL, number=6,)
    preemptibility = proto.Field(proto.ENUM, number=10, enum=Preemptibility,)
    managed_group_config = proto.Field(
        proto.MESSAGE, number=7, message="ManagedGroupConfig",
    )
    accelerators = proto.RepeatedField(
        proto.MESSAGE, number=8, message="AcceleratorConfig",
    )
    min_cpu_platform = proto.Field(proto.STRING, number=9,)


class ManagedGroupConfig(proto.Message):
    r"""Specifies the resources used to actively manage an instance
    group.

    Attributes:
        instance_template_name (str):
            Output only. The name of the Instance
            Template used for the Managed Instance Group.
        instance_group_manager_name (str):
            Output only. The name of the Instance Group
            Manager for this group.
    """

    instance_template_name = proto.Field(proto.STRING, number=1,)
    instance_group_manager_name = proto.Field(proto.STRING, number=2,)


class AcceleratorConfig(proto.Message):
    r"""Specifies the type and number of accelerator cards attached to the
    instances of an instance. See `GPUs on Compute
    Engine <https://cloud.google.com/compute/docs/gpus/>`__.

    Attributes:
        accelerator_type_uri (str):
            Full URL, partial URI, or short name of the accelerator type
            resource to expose to this instance. See `Compute Engine
            AcceleratorTypes <https://cloud.google.com/compute/docs/reference/beta/acceleratorTypes>`__.

            Examples:

            -  ``https://www.googleapis.com/compute/beta/projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80``
            -  ``projects/[project_id]/zones/us-east1-a/acceleratorTypes/nvidia-tesla-k80``
            -  ``nvidia-tesla-k80``

            **Auto Zone Exception**: If you are using the Dataproc `Auto
            Zone
            Placement <https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement>`__
            feature, you must use the short name of the accelerator type
            resource, for example, ``nvidia-tesla-k80``.
        accelerator_count (int):
            The number of the accelerator cards of this
            type exposed to this instance.
    """

    accelerator_type_uri = proto.Field(proto.STRING, number=1,)
    accelerator_count = proto.Field(proto.INT32, number=2,)


class DiskConfig(proto.Message):
    r"""Specifies the config of disk options for a group of VM
    instances.

    Attributes:
        boot_disk_type (str):
            Optional. Type of the boot disk (default is "pd-standard").
            Valid values: "pd-balanced" (Persistent Disk Balanced Solid
            State Drive), "pd-ssd" (Persistent Disk Solid State Drive),
            or "pd-standard" (Persistent Disk Hard Disk Drive). See
            `Disk
            types <https://cloud.google.com/compute/docs/disks#disk-types>`__.
        boot_disk_size_gb (int):
            Optional. Size in GB of the boot disk
            (default is 500GB).
        num_local_ssds (int):
            Optional. Number of attached SSDs, from 0 to 4 (default is
            0). If SSDs are not attached, the boot disk is used to store
            runtime logs and
            `HDFS <https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html>`__
            data. If one or more SSDs are attached, this runtime bulk
            data is spread across them, and the boot disk contains only
            basic config and installed binaries.
        local_ssd_interface (str):
            Optional. Interface type of local SSDs (default is "scsi").
            Valid values: "scsi" (Small Computer System Interface),
            "nvme" (Non-Volatile Memory Express). See `SSD Interface
            types <https://cloud.google.com/compute/docs/disks/local-ssd#performance>`__.
    """

    boot_disk_type = proto.Field(proto.STRING, number=3,)
    boot_disk_size_gb = proto.Field(proto.INT32, number=1,)
    num_local_ssds = proto.Field(proto.INT32, number=2,)
    local_ssd_interface = proto.Field(proto.STRING, number=4,)


class NodeInitializationAction(proto.Message):
    r"""Specifies an executable to run on a fully configured node and
    a timeout period for executable completion.

    Attributes:
        executable_file (str):
            Required. Cloud Storage URI of executable
            file.
        execution_timeout (google.protobuf.duration_pb2.Duration):
            Optional. Amount of time executable has to complete. Default
            is 10 minutes (see JSON representation of
            `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).

            Cluster creation fails with an explanatory error message
            (the name of the executable that caused the error and the
            exceeded timeout period) if the executable is not completed
            at end of the timeout period.
    """

    executable_file = proto.Field(proto.STRING, number=1,)
    execution_timeout = proto.Field(
        proto.MESSAGE, number=2, message=duration_pb2.Duration,
    )


class ClusterStatus(proto.Message):
    r"""The status of a cluster and its instances.

    Attributes:
        state (google.cloud.dataproc_v1.types.ClusterStatus.State):
            Output only. The cluster's state.
        detail (str):
            Optional. Output only. Details of cluster's
            state.
        state_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this state was entered (see JSON
            representation of
            `Timestamp <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).
        substate (google.cloud.dataproc_v1.types.ClusterStatus.Substate):
            Output only. Additional state information
            that includes status reported by the agent.
    """

    class State(proto.Enum):
        r"""The cluster state."""
        UNKNOWN = 0
        CREATING = 1
        RUNNING = 2
        ERROR = 3
        ERROR_DUE_TO_UPDATE = 9
        DELETING = 4
        UPDATING = 5
        STOPPING = 6
        STOPPED = 7
        STARTING = 8

    class Substate(proto.Enum):
        r"""The cluster substate."""
        UNSPECIFIED = 0
        UNHEALTHY = 1
        STALE_STATUS = 2

    state = proto.Field(proto.ENUM, number=1, enum=State,)
    detail = proto.Field(proto.STRING, number=2,)
    state_start_time = proto.Field(
        proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,
    )
    substate = proto.Field(proto.ENUM, number=4, enum=Substate,)


class SecurityConfig(proto.Message):
    r"""Security related configuration, including encryption,
    Kerberos, etc.

    Attributes:
        kerberos_config (google.cloud.dataproc_v1.types.KerberosConfig):
            Optional. Kerberos related configuration.
        identity_config (google.cloud.dataproc_v1.types.IdentityConfig):
            Optional. Identity related configuration,
            including service account based secure
            multi-tenancy user mappings.
    """

    kerberos_config = proto.Field(proto.MESSAGE, number=1, message="KerberosConfig",)
    identity_config = proto.Field(proto.MESSAGE, number=2, message="IdentityConfig",)


class KerberosConfig(proto.Message):
    r"""Specifies Kerberos related configuration.

    Attributes:
        enable_kerberos (bool):
            Optional. Flag to indicate whether to
            Kerberize the cluster (default: false). Set this
            field to true to enable Kerberos on a cluster.
        root_principal_password_uri (str):
            Optional. The Cloud Storage URI of a KMS
            encrypted file containing the root principal
            password.
        kms_key_uri (str):
            Optional. The uri of the KMS key used to
            encrypt various sensitive files.
        keystore_uri (str):
            Optional. The Cloud Storage URI of the
            keystore file used for SSL encryption. If not
            provided, Dataproc will provide a self-signed
            certificate.
        truststore_uri (str):
            Optional. The Cloud Storage URI of the
            truststore file used for SSL encryption. If not
            provided, Dataproc will provide a self-signed
            certificate.
        keystore_password_uri (str):
            Optional. The Cloud Storage URI of a KMS
            encrypted file containing the password to the
            user provided keystore. For the self-signed
            certificate, this password is generated by
            Dataproc.
        key_password_uri (str):
            Optional. The Cloud Storage URI of a KMS
            encrypted file containing the password to the
            user provided key. For the self-signed
            certificate, this password is generated by
            Dataproc.
        truststore_password_uri (str):
            Optional. The Cloud Storage URI of a KMS
            encrypted file containing the password to the
            user provided truststore. For the self-signed
            certificate, this password is generated by
            Dataproc.
        cross_realm_trust_realm (str):
            Optional. The remote realm the Dataproc
            on-cluster KDC will trust, should the user
            enable cross realm trust.
        cross_realm_trust_kdc (str):
            Optional. The KDC (IP or hostname) for the
            remote trusted realm in a cross realm trust
            relationship.
        cross_realm_trust_admin_server (str):
            Optional. The admin server (IP or hostname)
            for the remote trusted realm in a cross realm
            trust relationship.
        cross_realm_trust_shared_password_uri (str):
            Optional. The Cloud Storage URI of a KMS
            encrypted file containing the shared password
            between the on-cluster Kerberos realm and the
            remote trusted realm, in a cross realm trust
            relationship.
        kdc_db_key_uri (str):
            Optional. The Cloud Storage URI of a KMS
            encrypted file containing the master key of the
            KDC database.
        tgt_lifetime_hours (int):
            Optional. The lifetime of the ticket granting
            ticket, in hours. If not specified, or user
            specifies 0, then default value 10 will be used.
        realm (str):
            Optional. The name of the on-cluster Kerberos
            realm. If not specified, the uppercased domain
            of hostnames will be the realm.
    """

    enable_kerberos = proto.Field(proto.BOOL, number=1,)
    root_principal_password_uri = proto.Field(proto.STRING, number=2,)
    kms_key_uri = proto.Field(proto.STRING, number=3,)
    keystore_uri = proto.Field(proto.STRING, number=4,)
    truststore_uri = proto.Field(proto.STRING, number=5,)
    keystore_password_uri = proto.Field(proto.STRING, number=6,)
    key_password_uri = proto.Field(proto.STRING, number=7,)
    truststore_password_uri = proto.Field(proto.STRING, number=8,)
    cross_realm_trust_realm = proto.Field(proto.STRING, number=9,)
    cross_realm_trust_kdc = proto.Field(proto.STRING, number=10,)
    cross_realm_trust_admin_server = proto.Field(proto.STRING, number=11,)
    cross_realm_trust_shared_password_uri = proto.Field(proto.STRING, number=12,)
    kdc_db_key_uri = proto.Field(proto.STRING, number=13,)
    tgt_lifetime_hours = proto.Field(proto.INT32, number=14,)
    realm = proto.Field(proto.STRING, number=15,)


class IdentityConfig(proto.Message):
    r"""Identity related configuration, including service account
    based secure multi-tenancy user mappings.

    Attributes:
        user_service_account_mapping (Sequence[google.cloud.dataproc_v1.types.IdentityConfig.UserServiceAccountMappingEntry]):
            Required. Map of user to service account.
    """

    user_service_account_mapping = proto.MapField(proto.STRING, proto.STRING, number=1,)


class SoftwareConfig(proto.Message):
    r"""Specifies the selection and config of software inside the
    cluster.

    Attributes:
        image_version (str):
            Optional. The version of software inside the cluster. It
            must be one of the supported `Dataproc
            Versions <https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported_dataproc_versions>`__,
            such as "1.2" (including a subminor version, such as
            "1.2.29"), or the `"preview"
            version <https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#other_versions>`__.
            If unspecified, it defaults to the latest Debian version.
        properties (Sequence[google.cloud.dataproc_v1.types.SoftwareConfig.PropertiesEntry]):
            Optional. The properties to set on daemon config files.

            Property keys are specified in ``prefix:property`` format,
            for example ``core:hadoop.tmp.dir``. The following are
            supported prefixes and their mappings:

            -  capacity-scheduler: ``capacity-scheduler.xml``
            -  core: ``core-site.xml``
            -  distcp: ``distcp-default.xml``
            -  hdfs: ``hdfs-site.xml``
            -  hive: ``hive-site.xml``
            -  mapred: ``mapred-site.xml``
            -  pig: ``pig.properties``
            -  spark: ``spark-defaults.conf``
            -  yarn: ``yarn-site.xml``

            For more information, see `Cluster
            properties <https://cloud.google.com/dataproc/docs/concepts/cluster-properties>`__.
        optional_components (Sequence[google.cloud.dataproc_v1.types.Component]):
            Optional. The set of components to activate
            on the cluster.
    """

    image_version = proto.Field(proto.STRING, number=1,)
    properties = proto.MapField(proto.STRING, proto.STRING, number=2,)
    optional_components = proto.RepeatedField(
        proto.ENUM, number=3, enum=shared.Component,
    )


class LifecycleConfig(proto.Message):
    r"""Specifies the cluster auto-delete schedule configuration.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        idle_delete_ttl (google.protobuf.duration_pb2.Duration):
            Optional. The duration to keep the cluster alive while
            idling (when no jobs are running). Passing this threshold
            will cause the cluster to be deleted. Minimum value is 5
            minutes; maximum value is 14 days (see JSON representation
            of
            `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).
        auto_delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The time when cluster will be auto-deleted (see
            JSON representation of
            `Timestamp <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).

            This field is a member of `oneof`_ ``ttl``.
        auto_delete_ttl (google.protobuf.duration_pb2.Duration):
            Optional. The lifetime duration of cluster. The cluster will
            be auto-deleted at the end of this period. Minimum value is
            10 minutes; maximum value is 14 days (see JSON
            representation of
            `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).

            This field is a member of `oneof`_ ``ttl``.
        idle_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when cluster became idle (most recent
            job finished) and became eligible for deletion due to
            idleness (see JSON representation of
            `Timestamp <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).
    """

    idle_delete_ttl = proto.Field(
        proto.MESSAGE, number=1, message=duration_pb2.Duration,
    )
    auto_delete_time = proto.Field(
        proto.MESSAGE, number=2, oneof="ttl", message=timestamp_pb2.Timestamp,
    )
    auto_delete_ttl = proto.Field(
        proto.MESSAGE, number=3, oneof="ttl", message=duration_pb2.Duration,
    )
    idle_start_time = proto.Field(
        proto.MESSAGE, number=4, message=timestamp_pb2.Timestamp,
    )


class MetastoreConfig(proto.Message):
    r"""Specifies a Metastore configuration.

    Attributes:
        dataproc_metastore_service (str):
            Required. Resource name of an existing Dataproc Metastore
            service.

            Example:

            -  ``projects/[project_id]/locations/[dataproc_region]/services/[service-name]``
    """

    dataproc_metastore_service = proto.Field(proto.STRING, number=1,)


class ClusterMetrics(proto.Message):
    r"""Contains cluster daemon metrics, such as HDFS and YARN stats.

    **Beta Feature**: This report is available for testing purposes
    only. It may be changed before final release.

    Attributes:
        hdfs_metrics (Sequence[google.cloud.dataproc_v1.types.ClusterMetrics.HdfsMetricsEntry]):
            The HDFS metrics.
        yarn_metrics (Sequence[google.cloud.dataproc_v1.types.ClusterMetrics.YarnMetricsEntry]):
            The YARN metrics.
    """

    hdfs_metrics = proto.MapField(proto.STRING, proto.INT64, number=1,)
    yarn_metrics = proto.MapField(proto.STRING, proto.INT64, number=2,)


class CreateClusterRequest(proto.Message):
    r"""A request to create a cluster.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster (google.cloud.dataproc_v1.types.Cluster):
            Required. The cluster to create.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two
            `CreateClusterRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.CreateClusterRequest>`__\ s
            with the same id, then the second request will be ignored
            and the first
            [google.longrunning.Operation][google.longrunning.Operation]
            created and stored in the backend is returned.

            It is recommended to always set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (_), and hyphens (-). The maximum length is 40
            characters.
        action_on_failed_primary_workers (google.cloud.dataproc_v1.types.FailureAction):
            Optional. Failure action when primary worker
            creation fails.
    """

    project_id = proto.Field(proto.STRING, number=1,)
    region = proto.Field(proto.STRING, number=3,)
    cluster = proto.Field(proto.MESSAGE, number=2, message="Cluster",)
    request_id = proto.Field(proto.STRING, number=4,)
    action_on_failed_primary_workers = proto.Field(
        proto.ENUM, number=5, enum=shared.FailureAction,
    )


class UpdateClusterRequest(proto.Message):
    r"""A request to update a cluster.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster_name (str):
            Required. The cluster name.
        cluster (google.cloud.dataproc_v1.types.Cluster):
            Required. The changes to the cluster.
        graceful_decommission_timeout (google.protobuf.duration_pb2.Duration):
            Optional. Timeout for graceful YARN decomissioning. Graceful
            decommissioning allows removing nodes from the cluster
            without interrupting jobs in progress. Timeout specifies how
            long to wait for jobs in progress to finish before
            forcefully removing nodes (and potentially interrupting
            jobs). Default timeout is 0 (for forceful decommission), and
            the maximum allowed timeout is 1 day. (see JSON
            representation of
            `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).

            Only supported on Dataproc image versions 1.2 and higher.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Specifies the path, relative to ``Cluster``, of
            the field to update. For example, to change the number of
            workers in a cluster to 5, the ``update_mask`` parameter
            would be specified as
            ``config.worker_config.num_instances``, and the ``PATCH``
            request body would specify the new value, as follows:

            ::

                {
                  "config":{
                    "workerConfig":{
                      "numInstances":"5"
                    }
                  }
                }

            Similarly, to change the number of preemptible workers in a
            cluster to 5, the ``update_mask`` parameter would be
            ``config.secondary_worker_config.num_instances``, and the
            ``PATCH`` request body would be set as follows:

            ::

                {
                  "config":{
                    "secondaryWorkerConfig":{
                      "numInstances":"5"
                    }
                  }
                }

            Note: Currently, only the following fields can be updated:

            .. raw:: html

                 <table>
                 <tbody>
                 <tr>
                 <td><strong>Mask</strong></td>
                 <td><strong>Purpose</strong></td>
                 </tr>
                 <tr>
                 <td><strong><em>labels</em></strong></td>
                 <td>Update labels</td>
                 </tr>
                 <tr>
                 <td><strong><em>config.worker_config.num_instances</em></strong></td>
                 <td>Resize primary worker group</td>
                 </tr>
                 <tr>
                 <td><strong><em>config.secondary_worker_config.num_instances</em></strong></td>
                 <td>Resize secondary worker group</td>
                 </tr>
                 <tr>
                 <td>config.autoscaling_config.policy_uri</td><td>Use, stop using, or
                 change autoscaling policies</td>
                 </tr>
                 </tbody>
                 </table>
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two
            `UpdateClusterRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.UpdateClusterRequest>`__\ s
            with the same id, then the second request will be ignored
            and the first
            [google.longrunning.Operation][google.longrunning.Operation]
            created and stored in the backend is returned.

            It is recommended to always set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (_), and hyphens (-). The maximum length is 40
            characters.
    """

    project_id = proto.Field(proto.STRING, number=1,)
    region = proto.Field(proto.STRING, number=5,)
    cluster_name = proto.Field(proto.STRING, number=2,)
    cluster = proto.Field(proto.MESSAGE, number=3, message="Cluster",)
    graceful_decommission_timeout = proto.Field(
        proto.MESSAGE, number=6, message=duration_pb2.Duration,
    )
    update_mask = proto.Field(
        proto.MESSAGE, number=4, message=field_mask_pb2.FieldMask,
    )
    request_id = proto.Field(proto.STRING, number=7,)


class StopClusterRequest(proto.Message):
    r"""A request to stop a cluster.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster_name (str):
            Required. The cluster name.
        cluster_uuid (str):
            Optional. Specifying the ``cluster_uuid`` means the RPC will
            fail (with error NOT_FOUND) if a cluster with the specified
            UUID does not exist.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two
            `StopClusterRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.StopClusterRequest>`__\ s
            with the same id, then the second request will be ignored
            and the first
            [google.longrunning.Operation][google.longrunning.Operation]
            created and stored in the backend is returned.

            Recommendation: Set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (_), and hyphens (-). The maximum length is 40
            characters.
    """

    project_id = proto.Field(proto.STRING, number=1,)
    region = proto.Field(proto.STRING, number=2,)
    cluster_name = proto.Field(proto.STRING, number=3,)
    cluster_uuid = proto.Field(proto.STRING, number=4,)
    request_id = proto.Field(proto.STRING, number=5,)


class StartClusterRequest(proto.Message):
    r"""A request to start a cluster.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster_name (str):
            Required. The cluster name.
        cluster_uuid (str):
            Optional. Specifying the ``cluster_uuid`` means the RPC will
            fail (with error NOT_FOUND) if a cluster with the specified
            UUID does not exist.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two
            `StartClusterRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.StartClusterRequest>`__\ s
            with the same id, then the second request will be ignored
            and the first
            [google.longrunning.Operation][google.longrunning.Operation]
            created and stored in the backend is returned.

            Recommendation: Set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (_), and hyphens (-). The maximum length is 40
            characters.
    """

    project_id = proto.Field(proto.STRING, number=1,)
    region = proto.Field(proto.STRING, number=2,)
    cluster_name = proto.Field(proto.STRING, number=3,)
    cluster_uuid = proto.Field(proto.STRING, number=4,)
    request_id = proto.Field(proto.STRING, number=5,)


class DeleteClusterRequest(proto.Message):
    r"""A request to delete a cluster.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster_name (str):
            Required. The cluster name.
        cluster_uuid (str):
            Optional. Specifying the ``cluster_uuid`` means the RPC
            should fail (with error NOT_FOUND) if cluster with specified
            UUID does not exist.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two
            `DeleteClusterRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.DeleteClusterRequest>`__\ s
            with the same id, then the second request will be ignored
            and the first
            [google.longrunning.Operation][google.longrunning.Operation]
            created and stored in the backend is returned.

            It is recommended to always set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (_), and hyphens (-). The maximum length is 40
            characters.
    """

    project_id = proto.Field(proto.STRING, number=1,)
    region = proto.Field(proto.STRING, number=3,)
    cluster_name = proto.Field(proto.STRING, number=2,)
    cluster_uuid = proto.Field(proto.STRING, number=4,)
    request_id = proto.Field(proto.STRING, number=5,)


class GetClusterRequest(proto.Message):
    r"""Request to get the resource representation for a cluster in a
    project.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster_name (str):
            Required. The cluster name.
    """

    project_id = proto.Field(proto.STRING, number=1,)
    region = proto.Field(proto.STRING, number=3,)
    cluster_name = proto.Field(proto.STRING, number=2,)


class ListClustersRequest(proto.Message):
    r"""A request to list the clusters in a project.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        filter (str):
            Optional. A filter constraining the clusters to list.
            Filters are case-sensitive and have the following syntax:

            field = value [AND [field = value]] ...

            where **field** is one of ``status.state``, ``clusterName``,
            or ``labels.[KEY]``, and ``[KEY]`` is a label key. **value**
            can be ``*`` to match all values. ``status.state`` can be
            one of the following: ``ACTIVE``, ``INACTIVE``,
            ``CREATING``, ``RUNNING``, ``ERROR``, ``DELETING``, or
            ``UPDATING``. ``ACTIVE`` contains the ``CREATING``,
            ``UPDATING``, and ``RUNNING`` states. ``INACTIVE`` contains
            the ``DELETING`` and ``ERROR`` states. ``clusterName`` is
            the name of the cluster provided at creation time. Only the
            logical ``AND`` operator is supported; space-separated items
            are treated as having an implicit ``AND`` operator.

            Example filter:

            status.state = ACTIVE AND clusterName = mycluster AND
            labels.env = staging AND labels.starred = \*
        page_size (int):
            Optional. The standard List page size.
        page_token (str):
            Optional. The standard List page token.
    """

    project_id = proto.Field(proto.STRING, number=1,)
    region = proto.Field(proto.STRING, number=4,)
    filter = proto.Field(proto.STRING, number=5,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)


class ListClustersResponse(proto.Message):
    r"""The list of all clusters in a project.

    Attributes:
        clusters (Sequence[google.cloud.dataproc_v1.types.Cluster]):
            Output only. The clusters in the project.
        next_page_token (str):
            Output only. This token is included in the response if there
            are more results to fetch. To fetch additional results,
            provide this value as the ``page_token`` in a subsequent
            ``ListClustersRequest``.
    """

    @property
    def raw_page(self):
        return self

    clusters = proto.RepeatedField(proto.MESSAGE, number=1, message="Cluster",)
    next_page_token = proto.Field(proto.STRING, number=2,)


class DiagnoseClusterRequest(proto.Message):
    r"""A request to collect cluster diagnostic information.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the cluster belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        cluster_name (str):
            Required. The cluster name.
    """

    project_id = proto.Field(proto.STRING, number=1,)
    region = proto.Field(proto.STRING, number=3,)
    cluster_name = proto.Field(proto.STRING, number=2,)


class DiagnoseClusterResults(proto.Message):
    r"""The location of diagnostic output.

    Attributes:
        output_uri (str):
            Output only. The Cloud Storage URI of the
            diagnostic output. The output report is a plain
            text file with a summary of collected
            diagnostics.
    """

    output_uri = proto.Field(proto.STRING, number=1,)


class ReservationAffinity(proto.Message):
    r"""Reservation Affinity for consuming Zonal reservation.

    Attributes:
        consume_reservation_type (google.cloud.dataproc_v1.types.ReservationAffinity.Type):
            Optional. Type of reservation to consume
        key (str):
            Optional. Corresponds to the label key of
            reservation resource.
        values (Sequence[str]):
            Optional. Corresponds to the label values of
            reservation resource.
    """

    class Type(proto.Enum):
        r"""Indicates whether to consume capacity from an reservation or
        not.
        """
        TYPE_UNSPECIFIED = 0
        NO_RESERVATION = 1
        ANY_RESERVATION = 2
        SPECIFIC_RESERVATION = 3

    consume_reservation_type = proto.Field(proto.ENUM, number=1, enum=Type,)
    key = proto.Field(proto.STRING, number=2,)
    values = proto.RepeatedField(proto.STRING, number=3,)


__all__ = tuple(sorted(__protobuf__.manifest))
