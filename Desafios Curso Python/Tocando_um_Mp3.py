# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame,time

pygame.mixer.init()# ← inicializa o mixer de áudio
pygame.mixer.music.load('KelLana.mp3')
pygame.mixer.music.play()

# Aguarda a música terminar de verdade
while pygame.mixer.music.get_busy():
    time.sleep(1)
