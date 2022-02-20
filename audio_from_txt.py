import pygame
pygame.init()
pygame.display.set_mode((200,100))

current_song = None
previous_song = None

clock = pygame.time.Clock()
clock.tick(10)
while True:
    pygame.event.poll()
    with open('D:\\song.txt') as f:
        current_song = f.readlines()[0]
        if current_song != previous_song:
            pygame.mixer.music.load(current_song)
            pygame.mixer.music.play(0)
            previous_song = current_song
        else:
            pass
    clock.tick(1)