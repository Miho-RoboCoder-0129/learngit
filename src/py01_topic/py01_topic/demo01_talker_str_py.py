#无修改
#1.导包；
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#3.自定义节点类；
class Talker(Node):
    def __init__(self):
        super().__init__("talker_node_py")
        self.get_logger().info("发布方创建了(python)!")
        self.count = 0
        self.publisher = self.create_publisher(String,"chatter",10)
        self.timer = self.create_timer(1.0,self.on_timer)
    def on_timer(self):
        message = String()
        message.data = "hello world(python)!" + str(self.count)
        self.publisher.publish(message)
        self.count += 1
        self.get_logger().info("发布的数据：%s" % message.data)

def main():
    #2.初始化ROS2客户端；
    rclpy.init()
    #4.调用spin函数，传入自定义类对象；
    rclpy.spin(Talker())
    #5.释放资源
    rclpy.shutdown()


if __name__ == '__main__':
    main()
