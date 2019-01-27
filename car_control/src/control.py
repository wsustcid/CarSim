#!/usr/bin/env python

import rospy
from prius_msgs.msg import Control

def control_test():
    pub = rospy.Publisher("/prius", Control, queue_size=1)
    rospy.init_node('sim_control', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    command = Control()
    command.header.stamp = rospy.Time.now()
    command.throttle = 0.2
    command.brake = 0
    command.steer = 0.0
    command.shift_gears = Control.NO_COMMAND   
    
   # while not rospy.is_shutdown():
    for i in range(10):
        pub.publish(command)
        rate.sleep()
    
    for i in range(10):
        command.brake = 0.5
        pub.publish(command)
        rate.sleep()

if __name__ == '__main__':
    try:
        control_test()
    except rospy.ROSInterruptException:
        pass 
