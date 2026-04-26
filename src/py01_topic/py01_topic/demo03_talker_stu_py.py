# import rclpy
# from rclpy.node import Node
# from base_interfaces_demo.msg import Student

# class talkerstu(Node):
#     def __init__(self):
#         super().__init__("talkerstu_node_py")
#         self.count = 0
#         self.publisher = self.create_publisher(Student,"chatter_stu",10)
#         self.timer = self.create_timer(0.5,self.on_timer)

#     def on_timer(self):
#         stu = Student()
#         stu.name = "凹凸曼"
#         stu.age = self.count
#         stu.height = 1.40
#         self.publisher.publish(stu)

#         self.count += 1
#         self.get_logger().info("学生信息:%s,%d,%.2f" % (stu.name,stu.age,stu.height))
# def main():
#     rclpy.init()
#     rclpy.spin(talkerstu())
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

"""
     需求:
     流程:
         1.导包;
         2.初始化ros2客户端;
         3.自定义节点类; 
         4.调用spian函数，并传入节点对象;
         5.资源释放.


"""
#1.导包;
import rclpy
from rclpy.node import Node
from base_interfaces_demo.msg import Student

# 3.自定义节点类;
class TalkerStu(Node):
    def __init__(self):
       super().__init__("talkerstu_node_py")
       self.count = 0
       self.publisher = self.create_publisher(Student, "chatter_stu", 10)
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
    #2.初始化ros2客户端;
    rclpy.init()
    #4.调用spian函数，并传入节点对象;
    rclpy.spin(TalkerStu())
    #5.资源释放
    rclpy.shutdown()

if __name__ == ' __name__':
    main()