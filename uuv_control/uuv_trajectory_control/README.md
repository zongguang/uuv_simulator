# Write down what you have learned
# Current Status (only digging not modifying to tethered bluerov2); T-AUV related testing was modified in (https://github.com/zongguang/tauv_trajectory_control.git) 
In **uuv_simulator/uuv_trajectory_control/src/path_generator** folder, four types: linear, cubic, dubins & Linear interpolator with polynomial blend (lipb) are here.

**linear**: segment a **Linear Bezier curve** by 0.001 increment size which is a similar segmentation we used for self-developing trajectory controller. 

## Using different trajectory controller 
In the launch file **start_tutorial_dp_controller_demo.launch** change the controller 16-20 lines to the controller want to use. Currently changed to PID instead of default DP. 

The code below able to show a demo environment and send some waypoints to make it move and **change the trajectory type** in send_waypoints_file.launch interpolator arg to see different trajectory types
The speed.msg is defined and publishing node for speed was included in the demo.launch file. You should able to see the /speed and /ref_speed to topics publishing when you launch the demo. 
```
roslaunch uuv_tutorial_dp_controller start_tutorial_dp_controller_demo.launch
roslaunch uuv_control_utils send_waypoints_file.launch uuv_name:=rexrov
```
## plot Juggler "Super useful"
```
rosrun plotjuggler plotjuggler 
```
I attached the plot juggler formatting xml file to the package, which called **PID.xml**, you could import the file into the **layout** then the plot settings should be automatically set up. The only issue is for the xy and xz plot, you still need to drag data into the plot.

### general usage
Select streaming part to **ROS Topic Subscriber**, then press start, selecting the topics info you need then start recording. 

**Buffer** length need to be adjusted for long term visulization

**Data plotting** drag the specific data needed into the plot area (multiple are allowed)

**XY plot** if need xy xz plot, using ctrl to select multiple topics the same time and using **right click** to drag them into the plot

**Legend name change** bottom left add a custom series and drag the data you want into input timeseries, then give a new name (did not find other ways to change the lengend yet)

