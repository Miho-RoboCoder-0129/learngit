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
import sys
from rclpy.logging import get_logger
from rclpy.action import ActionClient
from base_interfaces_demo.action import Progress

# 3.自定义节点类;
class ProgressActionClient(Node):
    def __init__(self):
       super().__init__("progress_action_client_node_py")
       self.get_logger().info("这是一个action客户端")
       # 3-1.创建动作客户端对象
       self.client = ActionClient(self, Progress,"get_sum")
    # 3-2.发送目标请求
    def send_goal(self, num):
        #连接服务器
        self.client.wait_for_server()
        #发送目标请求   
        goal = Progress.Goal()
        goal.num = num
        self.future = self.client.send_goal_async(goal, self.fb_callback)
        self.future.add_done_callback(self.goal_response_callback)
    #3-3.目标响应回调函数
    def goal_response_callback(self, future):
        #获取目标句柄
        goal_handle = future.result()
        self.get_logger().info(goal_handle.__str__())

        #判断目标是否被接受
        if not goal_handle.accepted:
            self.get_logger().error("目标未被接受")
            return
        self.get_logger().info("目标被接受正在处理中...")

        #处理最终响应结果
        self.result_future = goal_handle.get_result_async()
        self.result_future.add_done_callback(self.get_result_callback)

    #3-5.最终结果回调函数
    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info("最终结果: %d" % result.sum)

    #3-4.连续反馈回调函数
    def fb_callback(self,fb_msg):
        progress = fb_msg.feedback.progress
        self.get_logger().info("连续反馈: %.2f" % progress)

def main():
    #2.初始化ros2客户端;
    if len(sys.argv) != 2:
        get_logger("rclpy").error("请提交一个整型数据")
        return
    rclpy.init()
    #4.调用spian函数，并传入节点对象;
    action_client = ProgressActionClient()
    action_client.send_goal(int(sys.argv[1]))
    rclpy.spin(action_client)
    #5.资源释放
    rclpy.shutdown()

if __name__ == ' __main__':
    main()