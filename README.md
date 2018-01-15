# robosys_ros
課題１で製作したLEDのデバイスドライバ([robosys-device-driver](https://github.com/RyusukeOkudaira/robosys-device-driver))を少し改造し，ROSを用いて光らせるパッケージです。

# Demo
[ROS for Light the three LED](https://www.youtube.com/watch?v=-X8fsAv6zqY)

# Requirements
- Raspberry Pi 3
- Ubuntu 16.04
- ROS Kinetic
- LED

# Instaallation
- download repository 
```
$ cd ~/catkin_ws/src
$ git clone git clone https://github.com/RyusukeOkudaira/robosys_ros.git
```
- set up
```
$ cd ~/catkin_ws
$ catkin_make
$ cd ~/catkin_ws/src/robosys_ros/led_driver
$ chmod +x setupfile.sh
$ ./setup.sh
```

# Usage
- comand for execution this package
```
$ cd ~/catkin_ws/src/robosys_ros/script
$ roscore &
$ rosrun robosys_ros sub_led.py &
$ rosrun robosys_ros pub_led.py
```

# License
This repository is licensed under the MIT license, see [LICENSE](https://github.com/RyusukeOkudaira/robosys_ros/blob/master/LICENSE)
