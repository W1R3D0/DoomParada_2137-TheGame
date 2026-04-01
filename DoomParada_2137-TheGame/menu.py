import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1366, 768))  # Adjust to your resolution
pygame.display.set_caption("DOOM - Main Menu")

font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()

# Load the background image
background_image = pygame.image.load('resources/Menu/background.png')  # Replace with your actual background file

# Initialize the music
#pygame.mixer.music.load('title_screen_music.mp3')  # Replace with your music file
#pygame.mixer.music.set_volume(0.5)  # Set volume (optional)
#pygame.mixer.music.play(-1, 0.0)  # Loop music (-1 means infinite loop)

def draw_start_screen():
    screen.blit(background_image, (0, 0))  # Draw the background
    start_text = font.render("Press ENTER to Start", True, (255, 255, 255))

    #screen.blit(title_text, (320, 200))
    screen.blit(start_text, (240, 300))

    pygame.display.flip()

def show_start_screen():
    while True:  # Fixed typo: removed the stray "m"
        draw_start_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Exit the start screen and launch the game

        clock.tick(60)

def start_doom_game():
    # Print to confirm game startup
    print("Starting DOOM game...")
    # This will launch your main game (change 'main.py' to your actual game script)
    subprocess.Popen(["python3", "main.py"])

def main():
    show_start_screen()  # Display the start screen
    start_doom_game()  # Launch the main game

if __name__ == "__main__":
    main()
