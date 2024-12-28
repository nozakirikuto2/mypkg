import rclpy
from rclpy.node import Node
import math
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.subscription = self.create_subscription(
                String, "countup", self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f"Listen: {msg.data}")

def main():
    print("begin")
    rclpy.init()
    node = Listener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
    print("end")

if __name__ == "__main__":
    main()
