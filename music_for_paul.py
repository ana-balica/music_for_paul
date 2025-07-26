import pygame
from gpiozero import Button
from signal import pause

pygame.mixer.pre_init(buffer=4096)
pygame.mixer.init()
print("mixer init")

button_song_map = {
  Button(18): pygame.mixer.Sound('/home/banana/abba_mamma_mia.mp3'),
  Button(23): pygame.mixer.Sound('/home/banana/bee_gees_stayin_alive.mp3'),
  Button(24): pygame.mixer.Sound('/home/banana/christina_perri_you_are_my_sunshine.mp3'),
  Button(25): pygame.mixer.Sound('/home/banana/louis_armstrong_what_a_wonderful_world.mp3'),
  Button(12): pygame.mixer.Sound('/home/banana/nutcracker.mp3'),
  Button(16): pygame.mixer.Sound('/home/banana/the_beatles_here_comes_the_sun.mp3'),
}
stop_button = Button(4)
print("buttons init")

def play_sound(button, song):
  pygame.mixer.stop()
  song.play()

stop_button.when_pressed = pygame.mixer.stop
for button, song in button_song_map.items():
  button.when_pressed = lambda button: play_sound(button, song)

pause()
