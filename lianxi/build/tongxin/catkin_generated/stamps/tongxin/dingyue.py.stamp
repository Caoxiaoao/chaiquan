#! usr/bin/env python
import rospy
from std_msgs.msg import String
def fun(xiaoxi):
    rospy.loginfo("接受的消息为：%s",xiaoxi.date)
if __name__=="__main__":
    rospy.init_node("linser")
    sub=rospy.Subscriber("wei",String,fun,queue_size=10)
    rospy.spin()