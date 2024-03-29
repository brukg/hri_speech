# Speech-Based Human Robot Interaction and Task Assignment

The motivation for this project is to communicate with robots through natural speech. For this we are using an open-source Speech-to-Text engine named [DeepSpeech](https://github.com/mozilla/DeepSpeech), developed by [Mozila](https://github.com/mozilla).

## Getting Started

To get started, first install the following **Dependencies**

## Dependencies

_ROS-Noetic_

```bash
    sudo apt install ros-noetic-turtlebot3-gazebo   #simulation env
    sudo apt install ros-noetic-turtlebot3-slam     #slam
    sudo apt install ros-noetic-turtlebot3-navigation #navigation stack
    sudo apt install ros-noetic-gmapping                #for mapping
    sudo apt install ros-noetic-dwa-local-planner       #dynamic windowing approach controller
    sudo apt install ros-noetic-behaviortree-cpp-v3     #for task planning

```

install the following python packages

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
    #for text to speech
    sudo apt install libespeak-dev
    pip install pyttsx3

    

```

## How to run the project

After installing all the dependencies, go to your ros workspace and clone this repository.

```bash
    cd <your_catkin_workspace>
    git clone git@github.com:brukg/hri_speech.git
```

Then build the project using the following command and source it your workspace.

```bash
    catkin build
    source devel/setup.bash or source devel/setup.zsh #depending on your shell
```

Next go to project directory and create a folder named **models**.

```bash
    export TURTLEBOT3_MODEL=waffle
    roscd hri_speech or cd <your_catkin_workspace>/src/hri_speech
    mkdir models
```

Go inside the **models** folder and download two deepspeech models.

```bash
    cd models
    # makes sure to place/download the below files in the on the projects models directory
    wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
    wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
```

openai davinci model is used to extract semantic meaning from text for this you have to setup openai key [here](https://beta.openai.com/account/api-keys) and export it before running the project replace the string in the below command with your key

```bash
export OPENAI_API_KEY="key obtained from openai account"
```


Finally run the project using the following command.

```bash
    roslaunch hri_speech start_all.launch
```
