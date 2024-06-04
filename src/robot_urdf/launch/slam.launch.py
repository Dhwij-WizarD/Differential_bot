import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription 
from ament_index_python import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_share = get_package_share_directory("robot_urdf")
    sim_launch_file = os.path.join(pkg_share , "launch","sim.launch.py")
    sim_launch = IncludeLaunchDescription(sim_launch_file)

    slam_share = get_package_share_directory("slam_toolbox")
    slam_launch_file = os.path.join(slam_share,"launch", "online_async_launch.py")
    params_file = os.path.join(pkg_share,"config","mapper_params_online_async.yaml")
    slam_arguments = {"params_file": params_file, "use_sim_time":"true"}
    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            slam_launch_file
        ),
        launch_arguments=slam_arguments.items()
    )


    return LaunchDescription([sim_launch,slam_launch])