import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    gazebo_share = get_package_share_directory("gazebo_ros")
    gazebo_launch_file = os.path.join(gazebo_share,"launch","gazebo.launch.py")
    pkg_share = get_package_share_directory("robot_urdf")
    world_file = os.path.join(pkg_share,"worlds","house.world")
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch_file),
        launch_arguments={
            "world":world_file
        }.items()
        )
    
    rviz_file = os.path.join(pkg_share, "rviz","sim.rviz")
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        arguments=["-d",rviz_file]
    )
    
    spawn_entity = Node(
        package= "gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic","robot_description","-entity","ultron"]
    )

    spawn_entity_delayed = TimerAction(
        period=6.0,  # Adjust the delay time as necessary
        actions=[spawn_entity]
    )

    rsp_launch_file = os.path.join(pkg_share,"launch","rsp.launch.py")
    rsp_launch = IncludeLaunchDescription(rsp_launch_file)



    return LaunchDescription([rsp_launch,rviz, gazebo_launch, spawn_entity_delayed])
