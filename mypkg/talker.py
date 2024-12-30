import rclpy
from rclpy.node import Node
import math
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(String, "countup", 10)
        self.create_timer(0.5, self.cb)
        self.angle = 0
        self.get_logger().set_level(rclpy.logging.LoggingSeverity.WARN)

    def cb(self):
        rad = math.radians(self.angle)
        sin = math.sin(rad)
        ans = round(sin, 5)
        mes = f"{self.angle}, {ans}"
        msg =String()
        msg.data = mes
        self.pub.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")
        self.angle = (self.angle + 1)

def main():
    rclpy.init()
    node = Talker()
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
