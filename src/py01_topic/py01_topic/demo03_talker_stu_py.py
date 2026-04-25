import rclpy
from rclpy.node import Node
from base_interfaces_demo.msg import Student

class talkerstu(Node):
    def __init__(self):
        super().__init__("talkerstu_node_py")
        self.count = 0
        self.publisher = self.create_publisher(Student,"chatter_stu",10)
        self.timer = self.create_timer(0.5,self.on_timer)

    def on_timer(self):
        stu = Student()
        stu.name = "凹凸曼"
        stu.age = self.count
        stu.height = 1.40
        self.publisher.publish(stu)

        self.count += 1
        self.get_logger().info("学生信息:%s,%d,%.2f" % (stu.name,stu.age,stu.height))
def main():
    rclpy.init()
    rclpy.spin(talkerstu())
    rclpy.shutdown()

if __name__ == '__main__':
    main()