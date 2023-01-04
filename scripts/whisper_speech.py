import io
from pydub import AudioSegment
import speech_recognition as sr
import whisper
import queue
import tempfile
import os
import threading
# import click
import torch
import numpy as np
from task import text2task
class WhisperSpeech:
    def __init__(self, robot, model= "base", english=True, verbose=False, energy=300, pause=0.8, dynamic_energy=False, save_file=False):
        """
        :param model: Model to use
        :param english: Whether to use English model
        :param verbose: Whether to print verbose output
        :param energy: Energy level for mic to detect
        :param pause: Pause time before entry ends
        :param dynamic_energy: Flag to enable dynamic engergy
        :param save_file: Flag to save file
        """
        self.model = model
        self.english = english
        self.verbose = verbose
        self.energy = energy
        self.pause = pause
        self.dynamic_energy = dynamic_energy
        self.save_file = save_file

        self.robot = robot

        
    # def main(self):
        temp_dir = tempfile.mkdtemp() if self.save_file else None
        #there are no english models for large
        if self.model != "large" and self.english:
            self.model = self.model + ".en"
        audio_model = whisper.load_model(self.model)
        audio_queue = queue.Queue()
        result_queue = queue.Queue()
        threading.Thread(target=self.record_audio,
                        args=(audio_queue, self.energy, self.pause, self.dynamic_energy, self.save_file, temp_dir)).start()
        threading.Thread(target=self.transcribe_forever,
                        args=(audio_queue, result_queue, audio_model, self.english, self.verbose, self.save_file)).start()

        while True:
            print(result_queue.get())


    def record_audio(self, audio_queue, energy, pause, dynamic_energy, save_file, temp_dir):
        #load the speech recognizer and set the initial energy threshold and pause threshold
        r = sr.Recognizer()
        r.energy_threshold = energy
        r.pause_threshold = pause
        r.dynamic_energy_threshold = dynamic_energy

        with sr.Microphone(sample_rate=16000) as source:
            print("Say something!")
            i = 0
            while True:
                #get and save audio to wav file
                audio = r.listen(source)
                if save_file:
                    data = io.BytesIO(audio.get_wav_data())
                    audio_clip = AudioSegment.from_file(data)
                    filename = os.path.join(temp_dir, f"temp{i}.wav")
                    audio_clip.export(filename, format="wav")
                    audio_data = filename
                else:
                    torch_audio = torch.from_numpy(np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)
                    audio_data = torch_audio

                audio_queue.put_nowait(audio_data)
                i += 1


    def transcribe_forever(self, audio_queue, result_queue, audio_model, english, verbose, save_file):
        while True:
            audio_data = audio_queue.get()
            if english:
                result = audio_model.transcribe(audio_data,language='english')
            else:
                result = audio_model.transcribe(audio_data)

            if not verbose:
                predicted_text = result["text"]
                
                result_queue.put_nowait("You said: " + predicted_text)
                if len(predicted_text) > 0:
                    task = text2task(predicted_text.lower())
                    if task is not None:
                        self.robot.goto(task)
            else:
                result_queue.put_nowait(result)

            if save_file:
                os.remove(audio_data)

# if __name__ == "__main__":
    # wspr = WhisperSpeech()
    # wspr.main()