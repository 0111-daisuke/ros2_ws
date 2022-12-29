import rclpy
from rclpy.node import Node
from person_msgs.msg import Int16

class Talker():
    def _init_(self):
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
        node.create_timer(0.5, self.cb)
        rclpy.init()
        node = Node("talker")
        talker = Talker

        def cb(self):
            msg = Int16()
            msg.data = self.n
            talker.pub.publish(msg)
            talker.n += 1

node.create_timer(0.5, cb)
rclpy.init()
node = Node("talker")
talker = Talker(node)
rclpy.spin(node)
