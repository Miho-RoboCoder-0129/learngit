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
from rclpy.action import ActionServer
from base_interfaces_demo.action import Progress
import time

# 3.自定义节点类;
class ProgressActionServer(Node):
    def __init__(self):
       super().__init__("progress_action_server_node_py")
       self.get_logger().info("这是一个action服务器")
       # 3-1.创建动作服务器对象
       self.server = ActionServer(self, Progress, "get_sum", self.execute_callback)

    def execute_callback(self, goal_handle):
        #1.生成连续反馈
        num = goal_handle.request.num
        sum = 0
        for i in range(1,num + 1):
            sum += i
            feedback = Progress.Feedback()
            feedback.progress = i / sum
            goal_handle.publish_feedback(feedback)
            self.get_logger().info("连续反馈: %.2f" % feedback.progress)
            time.sleep(1.0)
        #2.相应最终结果
        goal_handle.succeed()
        result = Progress.Result()
        result.sum = sum

        self.get_logger().info("计算结果：%d" % result.sum)
        return result

def main():
    #2.初始化ros2客户端;
    rclpy.init()
    #4.调用spian函数，并传入节点对象;
    rclpy.spin(ProgressActionServer())
    #5.资源释放
    rclpy.shutdown()

if __name__ == ' __main__':
    main()