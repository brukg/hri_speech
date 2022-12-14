# hri-speech

Human Robot Interaction Using Speech

## Dependencies

depends on the follwing packages ros packages

```bash
    sudo apt install ros-noetic-turtlebot3-gazebo
    sudo apt install ros-noetic-turtlebot3-slam
    sudo apt install ros-noetic-turtlebot3-navigation
    sudo apt install ros-noetic-behaviortree-cpp-v3

```

depends on the follwing packages ros packages

```bash
    pip3 install deepspeech
    pip3 install mediapipe
    wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
    wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
    # after downloading the model makes sure to place them on the projects models directory
    mv deepspeech-0.9.3-models.pbmm models/
    mv deepspeech-0.9.3-models.scorer models/

```

## Usage

```bash
    cd <your_catkin_workspace>
    catkin build
    source devel/setup.bash or source devel/setup.zsh #depending on your shell
    export TURTLEBOT3_MODEL=waffle
    roslaunch hri_speech start_all.launch
```
