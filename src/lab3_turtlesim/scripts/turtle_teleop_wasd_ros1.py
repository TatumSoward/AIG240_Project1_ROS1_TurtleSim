#!/usr/bin/env python3
"""
This code was made using the assistance of Google Gemini Gen AI
"""

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

# Function to get key presses (for ROS1 Indigo/Noetic)
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def wasd_teleop():
    rospy.init_node('wasd_teleop', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10 Hz

    # Define movement parameters (adjust as needed)
    linear_speed = 1.0  # Forward/Backward speed
    angular_speed = 1.0 # Turning speed

    while not rospy.is_shutdown():
        ch = getch() # Get a single character input

        twist_msg = Twist() # Create a new Twist message

        if ch == 'w':
            twist_msg.linear.x = linear_speed # Move forward
        elif ch == 's':
            twist_msg.linear.x = -linear_speed # Move backward
        elif ch == 'a':
            twist_msg.angular.z = angular_speed # Turn left (counter-clockwise)
        elif ch == 'd':
            twist_msg.angular.z = -angular_speed # Turn right (clockwise)
        elif ch == 'q': # Quit
            break

        pub.publish(twist_msg) # Publish the command
        rate.sleep() # Sleep for a short duration

if __name__ == '__main__':
    try:
        wasd_teleop()
    except rospy.ROSInterruptException:
        pass

