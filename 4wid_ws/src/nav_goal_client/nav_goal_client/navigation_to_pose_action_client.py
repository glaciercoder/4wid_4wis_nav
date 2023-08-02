import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from nav2_msgs.action import NavigateToPose
from std_msgs import PoseStamed


class NavigateToPoseActionClient(Node):

    def __init__(self):
        super().__init__('navigate_to_pose_action_client')
        self._action_client = ActionClient(self, NavigateToPose, 'NavigateToPose')

    def send_goal(self, order):
        goal_msg = NavigateToPose.Goal()
        goal_msg.order = order

        self._action_client.wait_for_server()

        return self._action_client.send_goal_async(goal_msg)


def main(args=None):
    rclpy.init(args=args)

    action_client = NavigateToPoseActionClient()

    future = action_client.send_goal(10)

    rclpy.spin_until_future_complete(action_client, future)


if __name__ == '__main__':
    main()