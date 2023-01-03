# hri-speech

Human Robot Interaction Using Speech

## Dependencies

depends on the follwing packages ros packages

```bash
    sudo apt install ros-noetic-turtlebot3-gazebo   #simulation env
    sudo apt install ros-noetic-turtlebot3-slam     #slam
    sudo apt install ros-noetic-turtlebot3-navigation #navigation stack
    sudo apt install ros-noetic-gmapping                #for mapping
    sudo apt install ros-noetic-dwa-local-planner       #for path planning
    sudo apt install ros-noetic-behaviortree-cpp-v3     #for task planning

```

depends on the follwing packages python packages

```bash
    pip3 install mediapipe  #gesture recognition

    #for using deepspeech
    pip3 install deepspeech #speech to text
    sudo apt-get install python3-pyaudio python3-pyaudio #

    # for using whisper
    pip install git+https://github.com/openai/whisper.git 
    pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
    # on Ubuntu or Debian
    sudo apt update && sudo apt install ffmpeg
    

```

## Usage

```bash
    cd <your_catkin_workspace>
    git clone git@github.com:brukg/hri_speech.git
    catkin build
    source devel/setup.bash or source devel/setup.zsh #depending on your shell
    export TURTLEBOT3_MODEL=waffle
    roscd hri_speech or cd <your_catkin_workspace>/src/hri_speech
    mkdir models
    cd models
    # makes sure to place/download the below files in the on the projects models directory
    wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
    wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer

    roslaunch hri_speech start_all.launch
```
