import xacro
import os

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    use_sim_time = LaunchConfiguration("use_sim_time", default=True)
    pkg_share = get_package_share_directory("robot_urdf")
    robot_description_file = os.path.join(pkg_share , "urdf","robot.urdf.xacro")
    robot_description = xacro.process_file(robot_description_file).toxml()
    params = {"robot_description":robot_description,"use_sim_time": use_sim_time}

    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output = "screen",
        parameters= [params]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "use_sim_time",
            default_value="true",
            description="use_sim_time if true"
        ),
        rsp
    ])