import pygame
from gpiozero import Button
from signal import pause

pygame.mixer.pre_init(buffer=4096)
pygame.mixer.init()
print("mixer init")

button_song_map = {
  Button(18): pygame.mixer.Sound('/home/banana/Music/abba_mamma_mia.mp3'),
  Button(23): pygame.mixer.Sound('/home/banana/Music/bee_gees_stayin_alive.mp3'),
  Button(21): pygame.mixer.Sound('/home/banana/Music/christina_perri_you_are_my_sunshine.mp3'),
  Button(16): pygame.mixer.Sound('/home/banana/Music/louis_armstrong_what_a_wonderful_world.mp3'),
  Button(12): pygame.mixer.Sound('/home/banana/Music/nutcracker.mp3'),
  Button(5): pygame.mixer.Sound('/home/banana/Music/the_beatles_here_comes_the_sun.mp3'),
}
stop_button = Button(4)
print("buttons init")

def play_sound(button, song):
  pygame.mixer.stop()
  song.play()

stop_button.when_pressed = pygame.mixer.stop
for button, song in button_song_map.items():
  button.when_pressed = lambda b=button, s=song: play_sound(b, s)

pause()
