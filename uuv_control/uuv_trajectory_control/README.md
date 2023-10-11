# Write down what you have learned
# Current Status (only digging not modifying to tethered bluerov2)
In **uuv_simulator/uuv_trajectory_control/src/path_generator** folder, four types: linear, cubic, dubins & Linear interpolator with polynomial blend (lipb) are here.

**linear**: segment a **Linear Bezier curve** by 0.001 increment size which is a similar segmentation we used for self-developing trajectory controller. 

## Using different trajectory controller 
In the launch file **start_tutorial_dp_controller_demo.launch** change the controller 16-20 lines to the controller want to use. Currently changed to PID instead of default DP. 

The code below able to show a demo environment and send some waypoints to make it move and **change the trajectory type** in send_waypoints_file.launch interpolator arg to see different trajectory types

```
roslaunch uuv_tutorial_dp_controller start_tutorial_dp_controller_demo.launch
roslaunch uuv_control_utils send_waypoints_file.launch uuv_name:=rexrov
```
