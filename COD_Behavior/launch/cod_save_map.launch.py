from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    nav_pose_yaml = PathJoinSubstitution([
        FindPackageShare("cod_behavior"),
        "launch",
        "cod_pose_tactical_front.yaml"
    ])

    save_map_tree = PathJoinSubstitution([
        FindPackageShare("cod_behavior"),
        "cod_bt",
        "save_map_tree.xml"
    ])

    serial_node = Node(
        package="rm_serial",
        executable="talker",
        name="rm_serial",
        output="screen",
        parameters=[{
            "port_name": "/dev/ttySLAM",
            "enable_downlink_receive": True
        }],
        arguments=["--ros-args", "--log-level", "info"]
    )

    behavior_node = Node(
        package="cod_behavior",
        executable="tree_1",
        name="cod_behavior",
        output="screen",
        parameters=[
            nav_pose_yaml,
            {"cod_bt_path": save_map_tree}
        ],
        arguments=["--ros-args", "--log-level", "warn"]
    )

    return LaunchDescription([
        # serial_node,
        behavior_node
    ])
