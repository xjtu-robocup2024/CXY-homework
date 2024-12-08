#!/usr/bin/env python3
import rospy
from turtlesim.srv import Spawn
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import tf
import math

# 第二只小乌龟的运动控制节点
class TurtleFollower:
    def __init__(self):
        rospy.init_node('turtle_follower', anonymous=True)

        # 发布速度指令到第二只小乌龟
        self.vel_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

        # 订阅第一只小乌龟的位置信息
        self.turtle1_pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.update_turtle1_pose)
        
        # 订阅第二只小乌龟的位置信息
        self.turtle2_pose_sub = rospy.Subscriber('/turtle2/pose', Pose, self.update_turtle2_pose)

        # 初始化两只小乌龟的位置
        self.turtle1_pose = None
        self.turtle2_pose = None

        # 频率设置
        self.rate = rospy.Rate(10)

    def update_turtle1_pose(self, msg):
        self.turtle1_pose = msg

    def update_turtle2_pose(self, msg):
        self.turtle2_pose = msg

    def compute_velocity(self):
        if not self.turtle1_pose or not self.turtle2_pose:
            return None

        # 计算相对距离和角度
        dx = self.turtle1_pose.x - self.turtle2_pose.x
        dy = self.turtle1_pose.y - self.turtle2_pose.y
        distance = math.sqrt(dx**2 + dy**2)
        angle_to_target = math.atan2(dy, dx)

        # 计算速度指令
        twist = Twist()
        twist.linear.x = 1.5 * distance
        twist.angular.z = 4.0 * (angle_to_target - self.turtle2_pose.theta)

        return twist

    def run(self):
        while not rospy.is_shutdown():
            velocity = self.compute_velocity()
            if velocity:
                self.vel_pub.publish(velocity)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        # 启动 turtlesim_node
        rospy.init_node('turtle_controller', anonymous=True)

        # 调用 spawn 服务生成第二只小乌龟
        rospy.wait_for_service('/spawn')
        spawn_turtle = rospy.ServiceProxy('/spawn', Spawn)
        spawn_turtle(5.0, 5.0, 0, 'turtle2')

        # 启动跟踪节点
        follower = TurtleFollower()
        follower.run()

    except rospy.ROSInterruptException:
        pass
