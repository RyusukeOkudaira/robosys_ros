#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

if __name__ == "__main__":
	rospy.init_node("pub_led")
	pub1 = rospy.Publisher("led1",Bool,queue_size = 10)
	pub2 = rospy.Publisher("led2",Bool,queue_size = 10)
	pub3 = rospy.Publisher("led3",Bool,queue_size = 10)
	rate = rospy.Rate(10)

	pub1.publish(False)
	pub2.publish(False)
	pub3.publish(False)

	try:
		while not rospy.is_shutdown():
			pub1.publish(False)
			pub2.publish(False)
			pub3.publish(False)
			rate.sleep()
        	        pub1.publish(True)
          		pub2.publish(False)
               		pub3.publish(False)
               		rate.sleep()
                	pub1.publish(False)
	                pub2.publish(True)
        	        pub3.publish(False)
	                rate.sleep()
	                pub1.publish(False)
	                pub2.publish(False)
	                pub3.publish(True)
			rate.sleep()

	except rospy.KeybordInterrupt:
		pass
