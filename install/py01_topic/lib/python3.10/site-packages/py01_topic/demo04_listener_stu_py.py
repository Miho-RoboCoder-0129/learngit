import rclpy
from rclpy.node import Node
from base_interfaces_demo import Student

class Listenerstu(Node):
    def __init__(self):
        super().__init__("listenerstu_node_py")
        self.subscription = self.create_subscription(Student,"chatter_stu",self.do_cb,10)
    def do_cb(self,stu):
        self.get_logger().info("订阅到的学生信息:name = %s,age = %d,height = %.2f" % (stu.name,stu.age,stu.height))
def main():
    rclpy.init()
    rclpy.spin(Listenerstu())
    rclpy.shutdown()

if __name__ == '__main__':
    main()