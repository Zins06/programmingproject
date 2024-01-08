import pygame
import sys
from player_class import Player
from tilemap_uti import load_tilemap_layout, create_tilemap, draw_tilemap, read_tilemap_layout


def main():
    pygame.init()  # Move the initialization of Pygame here

    # Gets the User's screen resolution
    info = pygame.display.Info()

    # Constants
    screen_width = info.current_w
    screen_height = info.current_h
    clock = pygame.time.Clock()

    # Load the tilemap layout
    tilemap_layout = load_tilemap_layout("Levels/level 1/level 1 tilemap layout.txt")

    # Define tile size
    tile_size = 49

    tile_mapping = {
        'T': pygame.image.load('ceiling/ceilingLTC.png'),
        'Y': pygame.image.load('ceiling/ceilingRTC.png'),
        'U': pygame.image.load('ceiling/ceilingLBC.png'),
        'I': pygame.image.load('ceiling/ceilingRBC.png'),
        'C': pygame.image.load('ceiling/ceilingH.png'),
        'V': pygame.image.load('ceiling/ceilingV.png'),
        'F': pygame.image.load('floors/floor.png'),
        'W': pygame.image.load('walls/wall.png'),
        'D': pygame.image.load('door/opendoor.png'),
    }

    tilemap_layout = read_tilemap_layout("Levels/level 1/level 1 tilemap layout.txt")

    # Create the tilemap
    tilemap = create_tilemap(tilemap_layout, tile_mapping)

    print("Tilemap Dimensions:", len(tilemap), "rows x", len(tilemap[0]), "columns")
    print("Screen Dimensions:", screen_width, "x", screen_height)

    # Create the game window
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Maze")

    player = Player()  # Create the Player instance after Pygame is initialized

    camera_offset = [0, 0]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate the offset to center the tilemap in the window
        offset_x = (screen_width - len(tilemap_layout[0]) * tile_size) // 2
        offset_y = (screen_height - len(tilemap_layout) * tile_size) // 2

        # Clear the screen
        screen.fill((255, 255, 255))

        # Update camera offset based on player position
        camera_offset[0] = max(0, min(player.rect.x - screen_width // 2,
                                      len(tilemap_layout[0]) * tile_size - screen_width))
        camera_offset[1] = max(0,
                               min(player.rect.y - screen_height // 2, len(tilemap_layout) * tile_size - screen_height))

        # Adjust the camera offset to keep the player centered
        camera_offset[0] -= offset_x
        camera_offset[1] -= offset_y

        # Print camera offset values
        print("Player Position:", player.rect.x, player.rect.y)
        print("Calculated Camera Offset:", camera_offset)
        print("Resulting Camera Position:", (camera_offset[0] - offset_x, camera_offset[1] - offset_y))

        # Draw the tilemap with the offset and camera_offset
        draw_tilemap(screen, tilemap, tile_mapping, tile_size, camera_offset)

        # Get the state of keyboard keys
        keys = pygame.key.get_pressed()

        # Update player's position based on keyboard input
        player.move(keys)

        # Print player position
        print("Player Position:", player.rect.x, player.rect.y)

        # Updates and draws the player
        player.draw(screen)

        # Updates the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)  # Adjust 60 to your desired frame rate

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
