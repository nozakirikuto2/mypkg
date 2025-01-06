# SPDX-FileCopyrightText: 2025 Rikuto Nozaki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
import math
from std_msgs.msg import String

class Sub(Node):
    def __init__(self):
        super().__init__("sub")
        self.subscription = self.create_subscription(
                String, "countup", self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f"{msg.data}")

def main():
    print("begin")
    rclpy.init()
    node = Sub()
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
