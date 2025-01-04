import rclpy
from rclpy.node import Node
import math
from std_msgs.msg import String

class SinPublisher(Node):
    def __init__(self):
        super().__init__("sin_publisher")
        self.pub = self.create_publisher(String, "countup", 10)
        self.create_timer(0.5, self.publish_sin)
        self.angle = 0
        

    def publish_sin(self):
        rad = math.radians(self.angle)
        sin = math.sin(rad)
        ans = round(sin, 5)
        mes = f"{self.angle}, {ans}"
        msg =String()
        msg.data = mes
        self.pub.publish(msg)
        self.angle = (self.angle + 1) % 361

def main():
    rclpy.init()
    node = SinPublisher()
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
