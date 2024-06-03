import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch.actions import IncludeLaunchDescription

def generate_launch_description():
    pkg_share = get_package_share_directory("robot_urdf")
    rsp_launch_file = os.path.join(pkg_share,"launch","rsp.launch.py")
    rsp_launch = IncludeLaunchDescription(rsp_launch_file)
    rviz_file = os.path.join(pkg_share, "rviz","display_model.rviz")
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        arguments=["-d",rviz_file]
    )

    jsp_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        output="screen"
    )

    return LaunchDescription([rsp_launch,rviz,jsp_gui])
