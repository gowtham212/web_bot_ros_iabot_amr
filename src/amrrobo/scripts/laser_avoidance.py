#! /usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan
# from geometry_msgs.msg import Twist
from std_msgs.msg import String
pub = None

def clbk_laser(msg):
    '''
        We need to provide a callback function 
        to the Subscriber defined in main, 
        for this purpose we have this function. 
        It receives laser scan data comprising 
        of 720 readings and converts it into 5 readings 
    '''
    regions = {
        'right':  min(min(msg.ranges[716:1209]), 10)
        # 'fright': min(min(msg.ranges[144:287]), 10),
        # 'front':  min(min(msg.ranges[288:431]), 10),
        # 'fleft':  min(min(msg.ranges[432:575]), 10),
        # 'left':   min(min(msg.ranges[576:719]), 10),
    }
    
    take_action(regions)
    
def take_action(regions):
    '''
        This function implements the obstacle avoidance logic. 
        Based on the distances sensed in the five region 
        (left, center-left, center, center-right, right). 
        We consider possible combinations for obstacles, 
        once we identify the obstacle configuration 
        we steer the robot away from obstacle.
    '''
    msg = String()
    # linear_x = 0
    # angular_z = 0
    
    state_description = ''
    
    if regions['right'] > 1 :
        state_description = 'case 1 - nothing'
    if regions['right'] < 1 :
        state_description = 'case 2 - thing'
        datas="2"
        msg.data=datas
#        rospy.loginfo(regions)
    # rospy.loginfo(state_description)
    
    pub.publish(msg)

def main():
    '''
        This is the entry point of the file. 
        This function sets up a Subscriber 
        to the laser scan topic /m2wr/laser/scan 
        and a Publisher to /cmd_vel topic.
    '''
    global pub
    
    rospy.init_node('reading_laser')
    
    pub = rospy.Publisher('status_led', String, queue_size=1)
    
    sub = rospy.Subscriber('/scan_frontend', LaserScan, clbk_laser)
    
    rospy.spin()

if __name__ == '__main__':
    main()
