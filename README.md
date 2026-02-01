#AIG240 - Project1 README - Tatum Soward#

Assessment Questions:
1. What command did you use to create the ROS package?

   `catkin_create_pkg lab3_turtlesim rospy geometry_msgs`
3. Explain why and how you used ROS messages in your program. i.e., Which message and type?

   ROS messages are standardized data structures which allow for nodes to share information (communicate). In this project, the communication happens between our controller script and the TurtleSim node. This project used the message catagory `geometry_msgs` and type `Twist`, which is used for poses and velocities. `Twist` contains float64 data each of which is an element in a 3D vector (x,y,z). One vector describes linear motion, the other angular. 
5. Describe the steps to launch ROS, TurtleSim, and your ROS node simultaneously.
   1. In a terminal window enter the command `roscore`. This sets up the ROS server.
   2. In a seperate terminal, enter the command `rosrun turtlesim turtlesim_node`. A TurtleSim window should pop up.
   3. In another seperate terminal, enter the command `rosrun lab3_turtlesim turtle_teleop_mult_wasd.py` or `rosrun {package name} {program name}` to run your program.
6. How do you verify that your ROS node is publishing messages correctly? i.e., What command?

   `echo $ROS_PACKAGE_PATH`
   \n You should see: \n
   `/home/jetauto/{workspace}/src:/opt/ros/melodic/share`
