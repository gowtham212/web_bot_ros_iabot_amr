#!/usr/bin/env python
import rospy
import roslib;
from actionlib_msgs.msg import GoalStatusArray
# //uint8 PENDING         = 0  
#     //uint8 ACTIVE          = 1 
#     //uint8 PREEMPTED       = 2
#     //uint8 SUCCEEDED       = 3
#     //uint8 ABORTED         = 4
#     //uint8 REJECTED        = 5
#     //uint8 PREEMPTING      = 6
#     //uint8 RECALLING       = 7
#     //uint8 RECALLED        = 8
#     //uint8 LOST            = 9
from std_msgs.msg import String
pub = None
 
def callback(data12):
    msg = String()
    status_id=0
    status_id =(data12.status_list[0].status)
    if(status_id ==[]):
        print("not")
    else:
        print(status_id)
        if(status_id == 1):
            print("active") 
            datas="1"
            msg.data=datas
        if(status_id == 4):
            print("aborted")
            datas="2"
            msg.data=datas 
        if(status_id ==3):
            print("reached")
            datas="3"
            msg.data=datas 
    pub.publish(msg)

      
def listener1():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener1', anonymous=True)
    global pub
    pub = rospy.Publisher('status_led', String, queue_size=1)
    rospy.Subscriber("/move_base/status", GoalStatusArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener1()