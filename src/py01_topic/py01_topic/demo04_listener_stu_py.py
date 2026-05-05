# import rclpy
# from rclpy.node import Node
# from base_interfaces_demo.msg import Student

# class Listenerstu(Node):
#     def __init__(self):
#         super().__init__("listenerstu_node_py")
#         self.subscription = self.create_subscription(Student,"chatter_stu",self.do_cb,10)
#     def do_cb(self,stu):
#         self.get_logger().info("订阅到的学生信息:name = %s,age = %d,height = %.2f" % (stu.name,stu.age,stu.height))
# def main():
#     rclpy.init()
#     rclpy.spin(Listenerstu())
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

"""
     需求:
     流程:
         1.导包;
         2.初始化ros2客户端;
         3.自定义节点类;
                         
         4.调用spian函数,并传入节点对象;
         5.资源释放.


"""
#1.导包;
import rclpy
from rclpy.node import Node
from base_interfaces_demo.msg import Student

# 3.自定义节点类;
class ListenerStu(Node):
    def __init__(self):
       super().__init__("listenerstu_node_py")
       self.subscription = self.create_subscription(Student,"chatter_stu",self.do_cb,10)

    def do_cb(self, stu):
        self.get_logger().info("订阅到的学生信息:name = %s,age = %d,height = %.2f" % (stu.name,stu.age,stu.height))

def main():
    #2.初始化ros2客户端;
    rclpy.init()
    #4.调用spian函数，并传入节点对象;
    rclpy.spin(ListenerStu())
    #5.资源释放
    rclpy.shutdown()

if __name__ == ' __name__':
    main()