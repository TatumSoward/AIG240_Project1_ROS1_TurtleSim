#!/usr/bin/env python3
# This code was made with the assistance of Google Gemini Gen AI
import rospy
from geometry_msgs.msg import Twist
from pynput import keyboard

class TeleopNode:
    def __init__(self):
        rospy.init_node('multi_key_teleop')
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        
        # Movement settings
        self.linear_speed = 1.0
        self.angular_speed = 1.0
        
        # Track which keys are currently held down
        self.pressed_keys = set()
        
        # Start the keyboard listener in the background
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        
        rospy.loginfo("Teleop Control Ready. Use WASD. Press ESC to quit.")

    def on_press(self, key):
        try:
            # Store the character of the key pressed
            if hasattr(key, 'char'):
                self.pressed_keys.add(key.char)
        except AttributeError:
            pass

    def on_release(self, key):
        try:
            if hasattr(key, 'char') and key.char in self.pressed_keys:
                self.pressed_keys.remove(key.char)
        except AttributeError:
            pass
        if key == keyboard.Key.esc:
            rospy.signal_shutdown("User quit")
            return False

    def run(self):
        rate = rospy.Rate(10) # 10Hz
        while not rospy.is_shutdown():
            twist = Twist()
            
            # Combine inputs for fluid movement
            # Forward/Backward
            if 'w' in self.pressed_keys:
                twist.linear.x += self.linear_speed
            if 's' in self.pressed_keys:
                twist.linear.x -= self.linear_speed
                
            # Left/Right
            if 'a' in self.pressed_keys:
                twist.angular.z += self.angular_speed
            if 'd' in self.pressed_keys:
                twist.angular.z -= self.angular_speed

            # Circular motion shortcuts (Done by me)
            if 'q' in self.pressed_keys:
                twist.linear.x += self.linear_speed
                twist.angular.z += self.angular_speed
            if 'z' in self.pressed_keys:
                twist.linear.x -= self.linear_speed
                twist.angular.z += self.angular_speed
            if 'c' in self.pressed_keys:
                twist.linear.x -= self.linear_speed
                twist.angular.z -= self.angular_speed
            if 'e' in self.pressed_keys:
                twist.linear.x += self.linear_speed
                twist.angular.z -= self.angular_speed

            self.pub.publish(twist)
            rate.sleep()

if __name__ == '__main__':
    try:
        node = TeleopNode()
        node.run()
    except rospy.ROSInterruptException:
        pass
