#!/bin/bash

while true; do
    ros2 action send_goal -f /MoveJ ros2_data/action/MoveJ "{goal: {joint1: 360.0, joint2: -90.0, joint3: 50.0, joint4: -0.5, joint5: 50.0, joint6: 0.0}, speed: 0.8}"
    ros2 action send_goal -f /MoveJ ros2_data/action/MoveJ "{goal: {joint1: 0.0, joint2: -90.0, joint3: 50.0, joint4: -0.5, joint5: 50.0, joint6: 0.0}, speed: 0.8}"
done

