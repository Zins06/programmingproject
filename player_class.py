import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load individual frames for animation
        self.frames = [
            pygame.image.load("image_3-0.png").convert_alpha(),
            pygame.image.load("image_3-1.png").convert_alpha(),
            pygame.image.load("image_3-2.png").convert_alpha(),
            pygame.image.load("image_3-3.png").convert_alpha(),
            pygame.image.load("image_3-4.png").convert_alpha(),
            pygame.image.load("image_3-5.png").convert_alpha(),
            pygame.image.load("image_3-6.png").convert_alpha(),
            pygame.image.load("image_3-7.png").convert_alpha(),
        ]

        # Load idle frame (replace "idle.png" with the actual idle frame filename)
        self.idle_frame = pygame.image.load("image_3-0.png").convert_alpha()

        # Set the initial frame to the idle frame
        self.image = self.idle_frame

        # Set the size of the sprite
        self.width = 125
        self.height = 125
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  # Set the desired size
        self.frame_index = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)  # Set the initial position of the Player
        self.speed = 10  # Adjust the Player's movement speed as needed

        # Animation related variables
        self.animation_speed = 0.1  # Adjust the animation speed
        self.last_update = pygame.time.get_ticks()

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            # Only update frame if the Player is moving
            if self.rect.x != 0 or self.rect.y != 0:
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.image = pygame.transform.scale(self.frames[self.frame_index], (self.width, self.height))
            else:
                self.image = pygame.transform.scale(self.idle_frame, (self.width, self.height))

    def move(self, keys):
        # Handle Player movement based on WASD keys
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        self.rect.topleft = (self.rect.x, self.rect.y)

        # Call the animate method to update the sprite's image
        self.animate()
        # For debugging
        print("Player Position:", self.rect.x, self.rect.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)





