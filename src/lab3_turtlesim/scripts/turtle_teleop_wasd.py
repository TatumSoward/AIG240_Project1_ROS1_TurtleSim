
#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

def getKey():
    # Helper function to get a single keypress
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def wasd_teleop():
    rospy.init_node('wasd_teleop', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    linear_vel = 2.0
    angular_vel = 1.5

    while not rospy.is_shutdown():
        key = getKey()
        twist = Twist()

        if key == 'w':
            twist.linear.x = linear_vel
        elif key == 's':
            twist.linear.x = -linear_vel
        elif key == 'a':
            twist.angular.z = angular_vel
        elif key == 'd':
            twist.angular.z = -angular_vel
        elif key == '':
            # Stop the turtle if no key is pressed (or key is released)
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        elif key == '\x03': # Ctrl+C to exit
            break
        
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin) # Save terminal settings
    try:
        wasd_teleop()
    except rospy.ROSInterruptException:
        pass
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings) # Restore terminal settings
