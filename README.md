# hri-speech

Human Robot Interaction Using Speech

## Dependencies

this project depends on the follwing packages

```bash
    sudo apt install ros-noetic-turtlebot3-gazebo
    sudo apt install ros-noetic-turtlebot3-slam
    sudo apt install ros-noetic-turtlebot3-navigation
```
## Usage

```bash
    cd <your_catkin_workspace>
    catkin build
    source devel/setup.bash or source devel/setup.zsh #depending on your shell
    export TURTLEBOT3_MODEL=waffle
    roslaunch hri_speech start_all.launch
```
