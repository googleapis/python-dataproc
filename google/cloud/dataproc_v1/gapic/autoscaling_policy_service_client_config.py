config = {
  "interfaces": {
    "google.cloud.dataproc.v1.AutoscalingPolicyService": {
      "retry_codes": {
        "retry_policy_4_codes": [
          "DEADLINE_EXCEEDED",
          "INTERNAL",
          "UNAVAILABLE"
        ],
        "retry_policy_1_codes": [
          "DEADLINE_EXCEEDED",
          "UNAVAILABLE"
        ],
        "retry_policy_6_codes": [
          "INTERNAL",
          "DEADLINE_EXCEEDED",
          "UNAVAILABLE"
        ],
        "no_retry_codes": [],
        "retry_policy_3_codes": [
          "UNAVAILABLE"
        ],
        "retry_policy_2_codes": [
          "DEADLINE_EXCEEDED",
          "INTERNAL",
          "UNAVAILABLE"
        ],
        "no_retry_1_codes": [],
        "retry_policy_5_codes": [
          "UNAVAILABLE"
        ],
        "retry_policy_7_codes": [
          "UNAVAILABLE"
        ]
      },
      "retry_params": {
        "retry_policy_1_params": {
          "initial_retry_delay_millis": 100,
          "retry_delay_multiplier": 1.3,
          "max_retry_delay_millis": 60000,
          "initial_rpc_timeout_millis": 600000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 600000,
          "total_timeout_millis": 600000
        },
        "retry_policy_3_params": {
          "initial_retry_delay_millis": 100,
          "retry_delay_multiplier": 1.3,
          "max_retry_delay_millis": 60000,
          "initial_rpc_timeout_millis": 600000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 600000,
          "total_timeout_millis": 600000
        },
        "retry_policy_2_params": {
          "initial_retry_delay_millis": 100,
          "retry_delay_multiplier": 1.3,
          "max_retry_delay_millis": 60000,
          "initial_rpc_timeout_millis": 900000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 900000,
          "total_timeout_millis": 900000
        },
        "retry_policy_6_params": {
          "initial_retry_delay_millis": 100,
          "retry_delay_multiplier": 1.3,
          "max_retry_delay_millis": 60000,
          "initial_rpc_timeout_millis": 300000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 300000,
          "total_timeout_millis": 300000
        },
        "retry_policy_7_params": {
          "initial_retry_delay_millis": 100,
          "retry_delay_multiplier": 1.3,
          "max_retry_delay_millis": 60000,
          "initial_rpc_timeout_millis": 900000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 900000,
          "total_timeout_millis": 900000
        },
        "retry_policy_5_params": {
          "initial_retry_delay_millis": 100,
          "retry_delay_multiplier": 1.3,
          "max_retry_delay_millis": 60000,
          "initial_rpc_timeout_millis": 300000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 300000,
          "total_timeout_millis": 300000
        },
        "retry_policy_4_params": {
          "initial_retry_delay_millis": 100,
          "retry_delay_multiplier": 1.3,
          "max_retry_delay_millis": 60000,
          "initial_rpc_timeout_millis": 600000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 600000,
          "total_timeout_millis": 600000
        },
        "no_retry_params": {
          "initial_retry_delay_millis": 0,
          "retry_delay_multiplier": 0.0,
          "max_retry_delay_millis": 0,
          "initial_rpc_timeout_millis": 0,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 0,
          "total_timeout_millis": 0
        },
        "no_retry_1_params": {
          "initial_retry_delay_millis": 0,
          "retry_delay_multiplier": 0.0,
          "max_retry_delay_millis": 0,
          "initial_rpc_timeout_millis": 600000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 600000,
          "total_timeout_millis": 600000
        }
      },
      "methods": {
        "CreateAutoscalingPolicy": {
          "timeout_millis": 600000,
          "retry_codes_name": "no_retry_1_codes",
          "retry_params_name": "no_retry_1_params"
        },
        "UpdateAutoscalingPolicy": {
          "timeout_millis": 600000,
          "retry_codes_name": "retry_policy_1_codes",
          "retry_params_name": "retry_policy_1_params"
        },
        "GetAutoscalingPolicy": {
          "timeout_millis": 600000,
          "retry_codes_name": "retry_policy_1_codes",
          "retry_params_name": "retry_policy_1_params"
        },
        "ListAutoscalingPolicies": {
          "timeout_millis": 600000,
          "retry_codes_name": "retry_policy_1_codes",
          "retry_params_name": "retry_policy_1_params"
        },
        "DeleteAutoscalingPolicy": {
          "timeout_millis": 600000,
          "retry_codes_name": "no_retry_1_codes",
          "retry_params_name": "no_retry_1_params"
        }
      }
    }
  }
}
