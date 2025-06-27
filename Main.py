import pygame
import sys
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Set up window
WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# Background color
PINK = (255, 192, 203)

# Load songs from folder
song_dir = "songs"
playlist = [file for file in os.listdir(song_dir) if file.endswith((".mp3", ".wav"))]
current_song_index = 0
paused = False

def load_song(index):
    global paused
    song_path = os.path.abspath(os.path.join(song_dir, playlist[index]))
    print("Loading song:", song_path)
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    paused = False
    print("Now playing:", playlist[index])

# Load images for buttons
def load_image(path, size):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, size)

button_size = (64, 64)
images = {
    "play": load_image("play_button.PNG", button_size),
    "pause": load_image("pause_button.PNG", button_size),
    "next": load_image("next.PNG", button_size),
    "prev": load_image("prev.PNG", button_size),
}

# Set button positions
button_positions = {
    "prev": {"default": (90, 200), "current": (90, 200), "pressed": False},
    "play": {"default": (170, 200), "current": (170, 200), "pressed": False},
    "pause": {"default": (250, 200), "current": (250, 200), "pressed": False},
    "next": {"default": (330, 200), "current": (330, 200), "pressed": False},
}

# Play first song at startup
if playlist:
    load_song(current_song_index)
else:
    print("⚠️ No songs found in the 'songs' folder!")

# Main loop
running = True
while running:
    screen.fill(PINK)

    # Draw buttons
    for key in button_positions:
        screen.blit(images[key], button_positions[key]["current"])

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for key, data in button_positions.items():
                x, y = data["current"]
                w, h = button_size
                if x <= mx <= x + w and y <= my <= y + h:
                    print(f"{key.capitalize()} button clicked")
                    data["current"] = (x, y + 3)
                    data["pressed"] = True

                    # Play button
                    if key == "play":
                        if paused:
                            pygame.mixer.music.unpause()
                            paused = False
                            print("Resumed")
                        elif not pygame.mixer.music.get_busy():
                            load_song(current_song_index)

                    #Pause button
                    elif key == "pause":
                        if pygame.mixer.music.get_busy() and not paused:
                            pygame.mixer.music.pause()
                            paused = True
                            print("Paused")

                    #Next button
                    elif key == "next":
                        current_song_index = (current_song_index + 1) % len(playlist)
                        load_song(current_song_index)

                    #Previous button
                    elif key == "prev":
                        current_song_index = (current_song_index - 1) % len(playlist)
                        load_song(current_song_index)

        elif event.type == pygame.MOUSEBUTTONUP:
            for data in button_positions.values():
                if data["pressed"]:
                    data["current"] = data["default"]
                    data["pressed"] = False

pygame.quit()
sys.exit()
