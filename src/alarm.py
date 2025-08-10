import os
import pygame

class AlarmPlayer:
    def __init__(self, audio_file):
        self.audio_path = os.path.join(os.path.dirname(__file__), "..", "audio", audio_file)
        pygame.mixer.init()
        if os.path.exists(self.audio_path):
            pygame.mixer.music.load(self.audio_path)
        else:
            print(f"[WARNING] Audio file not found: {self.audio_path}")

    def play_alarm(self):
        if pygame.mixer.music.get_busy():
            return
        pygame.mixer.music.play()

    def stop_alarm(self):
        pygame.mixer.music.stop()
