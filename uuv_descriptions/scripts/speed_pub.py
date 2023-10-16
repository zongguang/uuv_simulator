#!/usr/bin/env python
import rospy
import numpy as np
from uuv_control_msgs.msg import Speed,TrajectoryPoint
from nav_msgs.msg import Odometry
real_linear_speed = 0.0  # Initialize linear speed
ref_linear_speed=0.0
def odom_callback(odom_msg):
    global real_linear_speed
    linear_x = odom_msg.twist.twist.linear.x
    linear_y = odom_msg.twist.twist.linear.y
    linear_z = odom_msg.twist.twist.linear.z
    real_linear_speed = np.linalg.norm([linear_x, linear_y, linear_z])
def cabk(traj_msg):
    global ref_linear_speed
    ref_vel_x=traj_msg.velocity.linear.x
    ref_vel_y=traj_msg.velocity.linear.y
    ref_vel_z=traj_msg.velocity.linear.z
    ref_linear_speed=np.linalg.norm([ref_vel_x,ref_vel_y,ref_vel_z])
def publish_speed():
    rospy.init_node('speed_publisher')
    pub = rospy.Publisher('speed', Speed, queue_size=1)
    rate = rospy.Rate(5)  # Adjust the publishing rate as needed (1 Hz in this example)
    rospy.Subscriber('/rexrov/pose_gt', Odometry, odom_callback)
    ref_pub=rospy.Publisher('ref_speed',Speed,queue_size=1)
    rospy.Subscriber('/rexrov/dp_controller/reference',TrajectoryPoint,cabk)
    while not rospy.is_shutdown():
        speed_msg = Speed()
        speed_msg.linear_speed = real_linear_speed
        pub.publish(speed_msg)
        ref_speed=Speed()
        ref_speed.linear_speed=ref_linear_speed
        ref_pub.publish(ref_speed)
        rate.sleep()
if __name__ == '__main__':
    try:
        publish_speed()
    except rospy.ROSInterruptException:
        pass
