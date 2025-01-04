import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

      sin_publisher = launch_ros.actions.Node(
          package='mypkg',
          executable='sin_publisher',
          )
      sub = launch_ros.actions.Node(
          package='mypkg',
          executable='sub',
          output='screen'
          )

      return launch.LaunchDescription([sin_publisher, sub])
