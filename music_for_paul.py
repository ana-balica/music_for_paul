import pygame
from gpiozero import Button
from signal import pause

button_song_map = {
  23: '/home/banana/song1.wav"
}

blue_button = Button(23)
print("button init")

pygame.mixer.pre_init(buffer=4096)
pygame.mixer.init()

def play_sound(filepath):
  sound = pygame.mixer.Sound(filepath)
  playing = sound.play()
  while playing.get_busy():
    pygame.time.delay(100)

blue_button.when_pressed = lambda: play_sound('/home/banana/song1.wav")
