# DO NOT skip the next commented line
#!/usr/bin/env python

import rospy
# Brings in the SimpleActionClient
import actionlib *
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal,GoalStatusArray


def callback(data):
	
	# print the actual message in its raw format
	rospy.loginfo("Here's what was subscribed: %s", data.GoalStatus)
	
def main():
	
	# initialize a node by the name 'listener'.
	# you may choose to name it however you like,
	# since you don't have to use it ahead
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("move_base/status", GoalStatusArray, callback)
	
	# spin() simply keeps python from
	# exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	
	# you could name this function
	try:
		main()
	except rospy.ROSInterruptException:
		pass
