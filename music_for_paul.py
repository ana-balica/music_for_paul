import pygame
from gpiozero import Button
from signal import pause

pygame.mixer.pre_init(buffer=4096)
pygame.mixer.init()
print("mixer init")

button_song_map = {
  Button(23): '/home/banana/song1.wav',
  Button(24): '/home/banana/song2.wav',
}
print("button init")

def play_sound(button, song):
  pygame.mixer.stop()
  song.play()

for button, song in button_song_map.items():
  button.when_pressed = lambda button: play_sound(button, song)

pause()
