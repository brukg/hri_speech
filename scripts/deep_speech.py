import deepspeech
import numpy as np
# import pyaudio
import rospy


class DeepSpeech:
    def __init__(self, model, scorer):
        self.model = deepspeech.Model(model)
        self.model.enableExternalScorer(scorer)
        # self.p = pyaudio.PyAudio()
        # self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
        # self.stream.start_stream()
        self.timer = rospy.Timer(rospy.Duration(1), self.timer_callback)
        print("DeepSpeech initialized")

    def timer_callback(self, event):
        # data = self.stream.read(1024)
        # data16 = np.frombuffer(data, dtype=np.int16)
        # print(self.model.stt(data16))
        pass