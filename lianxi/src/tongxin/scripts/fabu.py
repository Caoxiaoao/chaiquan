#! /usr/bin/env python
import rospy
from std_msgs.msg import String
if __name__=="__main__":
    rospy.init_node("talker")
    pub=rospy.Publisher("wei",String,queue_size=10)
    msg=String()
    msg.data="wocaonima"
    rate=rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(msg.data)
        rate.sleep()
        rospy.loginfo("正在发送数据：%s",msg.data)


