import pygame
import sys

pygame.init()


# Define a Class for Settings
class Settings:

    # Define the initiative numbers
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (0, 230, 230)
        self.fullscreen = False
        self.caption = "Draw your Way"

    # Define Function to change the screen size
    def set_screen_size(self, width, height):
        self.screen_width = width
        self.screen_height = height

    # Define function to set a basic Background color
    def set_bg_color(self, color):
        self.bg_color = color

    # Define Function to set Fullscreen
    def set_fullscreen(self, fullscreen):
        self.fullscreen = fullscreen

    # Define Function to set caption
    def set_caption(self, caption):
        self.caption = caption


# Define a Class for the in game Settings
class GameSettings:
    def __init__(self, setting):
        self.settings = setting
        self.screen = None
        self.font = None
        self.room_number = 0
        self.square_width = 0
        self.square_size = (50, 50)
        self.square_direction = 'stay'
        self.default_ground_height = 100
        self.square_height = self.default_ground_height
        self.square_pos = (50 - self.square_width, self.settings.screen_height - self.square_height)
        self.square_velocity = 0
        self.gravity = 0.1
        self.jumping = bool(False)
        self.square_speed = 1.5
        self.square_speed_y = 0
        self.ground_pos = (0, 0)
        self.square_rect = pygame.Rect(self.square_pos[0], self.square_pos[1], self.square_size[0], self.square_size[1])
        self.jumps = 1
        self.unlock_boost = False
        self.unlock_jump = False
        self.use_boost = False

    def reset_game_settings(self):
        self.square_direction = 'stay'
        self.default_ground_height = 100
        self.square_height = self.default_ground_height
        self.square_pos = (50 - self.square_width, self.settings.screen_height - self.square_height)
        self.square_velocity = 0
        self.jumping = bool(False)
        self.square_speed = 1.5
        self.square_speed_y = 0
        self.ground_pos = (0, 0)
        self.square_rect = pygame.Rect(self.square_pos[0], self.square_pos[1],
                                       self.square_size[0], self.square_size[1])
        self.jumps = 1
        self.unlock_boost = False
        self.unlock_jump = False
        self.use_boost = False
    
    # Define a Function to place the player
    def place_square(self):
        self.square_pos = (50 - self.square_width, self.settings.screen_height - self.square_height
                           - self.square_size[1])
        self.square_rect = pygame.Rect(self.square_pos[0], self.square_pos[1], self.square_size[0]+1,
                                       self.square_size[1])
        pygame.draw.rect(self.screen, (255, 0, 0), (self.square_pos[0], self.square_pos[1],
                                                    self.square_size[0], self.square_size[1]))

        # check if the player is within the boundaries of the screen
        if -200 <= self.square_pos[0] <= self.settings.screen_width - self.square_size[0] + 200 and -100 <= \
                self.square_pos[1] <= self.settings.screen_height - self.square_size[1] + 100:
            self.square_rect = pygame.Rect(self.square_pos[0], self.square_pos[1], self.square_size[0] + 1,
                                           self.square_size[1])
            pygame.draw.rect(self.screen, (200, 0, 100), (self.square_pos[0], self.square_pos[1],
                                                          self.square_size[0], self.square_size[1]))
        else:
            # player is not on the screen, call gameover function
            self.gameover_screen()

    # Define a Function to change the jump height
    def jump(self):
        self.square_velocity = - 8

    def un_jump(self):
        if self.room_number == 1:
            self.unlock_jump = True

    def boost(self):
        self.square_speed = 4.5

    def un_boost(self):
        if self.room_number == 3:
            self.unlock_boost = True

    # Define a Funktion to display a Start screen
    def start_screen(self):
        # Initialize the font
        self.font = pygame.font.Font(None, 72)
        # Create the start text
        start_text = self.font.render("Press SPACE to start", True, (255, 255, 255))
        # Get the size of the start text
        text_rect = start_text.get_rect()
        # Center the text on the screen
        text_rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2)
        waiting = True
        while waiting:
            # Clear the screen
            self.screen.fill((0, 0, 0))
            text_rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2)
            # Draw the start text
            self.screen.blit(start_text, text_rect)
            # Update the display
            pygame.display.update()
            # Check for events
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_SPACE:
                        waiting = False

    def gameover_screen(self):
        # Initialize the font
        self.font = pygame.font.Font(None, 72)
        # Create the gameover text
        gameover_text = self.font.render("Game Over", True, (255, 255, 255))
        # Get the size of the gameover text
        text_rect = gameover_text.get_rect()
        # Center the text on the screen
        text_rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2)
        waiting = True
        while waiting:
            # Clear the screen
            self.screen.fill((0, 0, 0))
            text_rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2)
            # Draw the gameover text
            self.screen.blit(gameover_text, text_rect)
            # Update the display
            pygame.display.update()
            # Check for events
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_SPACE:
                        waiting = False

    # Define a Function to choose between Fullscreen or Windowed mode
    def start(self):
        if self.settings.fullscreen:
            settings.set_screen_size(1920, 1080)
            self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        else:
            settings.set_screen_size(1920, 1080)
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.start_screen()


class GlitchRoom:
    # Define the Setting for the room
    def __init__(self, setting):
        self.settings = setting
        self.games = game
        self.ground_height = 100
        self.ground_pos = (0, self.settings.screen_height)
        self.ground_rect = pygame.Rect(self.ground_pos[0], self.ground_pos[1] - self.ground_height,
                                       self.settings.screen_width, self.ground_height)
        # Initialize the font
        self.font = pygame.font.Font(None, 80)

    def display_text_room_glitch(self):
        # Create the text to display in room 1 (split into two lines)
        line1 = "No You should not be here!"
        line2 = "Other way!"
        text1 = self.font.render(line1, True, (0, 125, 0))
        text2 = self.font.render(line2, True, (0, 125, 0))

        # Calculate the center position of the screen
        center_x = self.settings.screen_width // 2
        pos_y = self.settings.screen_height // 2 - 300

        # Calculate the position of the first line of text
        text1_x = center_x - text1.get_rect().width // 2
        text1_y = pos_y - text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Calculate the position of the second line of text
        text2_x = center_x - text2.get_rect().width // 2
        text2_y = pos_y + text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Draw the text (each line at a different position)
        game.screen.blit(text1, (text1_x, text1_y))
        game.screen.blit(text2, (text2_x, text2_y))

    # Define the Ground of Room 1
    def glitch_room_ground(self):
        self.ground_pos = (0, self.settings.screen_height)
        pygame.draw.rect(game.screen, (255, 255, 0), (self.ground_pos[0], self.ground_pos[1] - self.ground_height,
                                                      self.settings.screen_width, self.ground_height))
        self.ground_rect = pygame.Rect(self.ground_pos[0], self.ground_pos[1] - self.ground_height,
                                       self.settings.screen_width, self.ground_height)


# Define the first Room you spawn in
class Room1:
    # Define the Setting for the room
    def __init__(self, setting):
        self.settings = setting
        self.games = game
        self.ground_height = 100
        self.ground_pos = (0, self.settings.screen_height)
        self.ground_rect = pygame.Rect(self.ground_pos[0], self.ground_pos[1] - self.ground_height,
                                       self.settings.screen_width, self.ground_height)
        # Initialize the font
        self.font = pygame.font.Font(None, 80)

    def display_text_room1(self):
        # Create the text to display in room 1 (split into two lines)
        line1 = "Welcome to [insert game name]"
        line2 = "Move with the A or D buttons"
        text1 = self.font.render(line1, True, (0, 125, 0))
        text2 = self.font.render(line2, True, (0, 125, 0))

        # Calculate the center position of the screen
        center_x = self.settings.screen_width // 2
        pos_y = self.settings.screen_height // 2 - 300

        # Calculate the position of the first line of text
        text1_x = center_x - text1.get_rect().width // 2
        text1_y = pos_y - text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Calculate the position of the second line of text
        text2_x = center_x - text2.get_rect().width // 2
        text2_y = pos_y + text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Draw the text (each line at a different position)
        game.screen.blit(text1, (text1_x, text1_y))
        game.screen.blit(text2, (text2_x, text2_y))

    # Define the Ground of Room 1
    def room1_ground(self):
        self.ground_pos = (0, self.settings.screen_height)
        pygame.draw.rect(game.screen, (255, 255, 0), (self.ground_pos[0], self.ground_pos[1] - self.ground_height,
                                                      self.settings.screen_width, self.ground_height))
        self.ground_rect = pygame.Rect(self.ground_pos[0], self.ground_pos[1] - self.ground_height,
                                       self.settings.screen_width, self.ground_height)


# Define the bonus Room
class Room0:
    # Define the Setting for the room
    def __init__(self, setting):
        self.settings = setting
        self.ground0_height = 100
        self.ground0_pos = (0, self.settings.screen_height)
        self.ground0_rect = pygame.Rect(self.ground0_pos[0], self.ground0_pos[1] - self.ground0_height,
                                        self.settings.screen_width, self.ground0_height)
        self.font = pygame.font.Font(None, 80)

    # Define the Ground of Room 0
    def room0_ground(self):
        self.ground0_pos = (0, self.settings.screen_height)
        pygame.draw.rect(game.screen, (255, 255, 0), (self.ground0_pos[0], self.ground0_pos[1] - self.ground0_height,
                                                      self.settings.screen_width, self.ground0_height))
        self.ground0_rect = pygame.Rect(self.ground0_pos[0], self.ground0_pos[1] - self.ground0_height,
                                        self.settings.screen_width, self.ground0_height)

    def display_text_room0(self):
        line1 = "Congrats... You found a Secret room"
        line2 = "Now go the other direction!"
        text1 = self.font.render(line1, True, (0, 125, 0))
        text2 = self.font.render(line2, True, (0, 125, 0))

        # Calculate the center position of the screen
        center_x = self.settings.screen_width // 2
        pos_y = self.settings.screen_height // 2 - 300

        # Calculate the position of the first line of text
        text1_x = center_x - text1.get_rect().width // 2
        text1_y = pos_y - text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Calculate the position of the second line of text
        text2_x = center_x - text2.get_rect().width // 2
        text2_y = pos_y + text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Draw the text (each line at a different position)
        game.screen.blit(text1, (text1_x, text1_y))
        game.screen.blit(text2, (text2_x, text2_y))


# Define the 2 Room you spawn in
class Room2:
    # Define the Setting for the room
    def __init__(self, setting):
        self.settings = setting
        self.games = game
        self.ground2_height = 100
        self.ground2_pos = (0, self.settings.screen_height)
        self.ground2_rect = pygame.Rect(self.ground2_pos[0], self.ground2_pos[1] - self.ground2_height,
                                        self.settings.screen_width, self.ground2_height)
        self.object2_pos = (300, 0)
        self.object2_size = (100, 50)
        self.object2_rect = pygame.Rect(self.object2_pos[0], self.object2_pos[1],
                                        self.object2_size[0], self.object2_size[1])
        self.object2_size2 = (300, 150)
        self.object2_pos2 = (300, 0)
        self.object2_rect2 = pygame.Rect(self.object2_pos2[0], self.ground2_pos[1] - self.ground2_height
                                         - self.object2_size2[1], self.object2_size2[0], self.object2_size2[1])
        self.font = pygame.font.Font(None, 80)

    def display_text_room2(self):
        line1 = "Very good, now jump over the boxes"
        line2 = "You can jump with the SPACE bar!"
        text1 = self.font.render(line1, True, (0, 125, 0))
        text2 = self.font.render(line2, True, (0, 125, 0))

        # Calculate the center position of the screen
        center_x = self.settings.screen_width // 2
        pos_y = self.settings.screen_height // 2 - 300

        # Calculate the position of the first line of text
        text1_x = center_x - text1.get_rect().width // 2
        text1_y = pos_y - text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Calculate the position of the second line of text
        text2_x = center_x - text2.get_rect().width // 2
        text2_y = pos_y + text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Draw the text (each line at a different position)
        game.screen.blit(text1, (text1_x, text1_y))
        game.screen.blit(text2, (text2_x, text2_y))

    # Define the Ground of Room 1
    def room2_ground(self):
        self.ground2_pos = (0, self.settings.screen_height)
        pygame.draw.rect(game.screen, (255, 255, 0), (self.ground2_pos[0], self.ground2_pos[1] - self.ground2_height,
                                                      self.settings.screen_width, self.ground2_height))
        self.ground2_rect = pygame.Rect(self.ground2_pos[0], self.ground2_pos[1] - self.ground2_height,
                                        self.settings.screen_width, self.ground2_height)

    def room2_object(self):
        self.object2_size = (300, 150)
        self.object2_pos = (300, 0)
        self.object2_rect = pygame.Rect(self.object2_pos[0], self.ground2_pos[1] - self.ground2_height
                                        - self.object2_size[1], self.object2_size[0], self.object2_size[1])
        pygame.draw.rect(game.screen, (255, 255, 0), (self.object2_pos[0], self.ground2_pos[1] - self.ground2_height -
                                                      self.object2_size[1], self.object2_size[0], self.object2_size[1]))

    def room2_object2(self):
        self.object2_size2 = (200, 250)
        self.object2_pos2 = (1300, 0)
        self.object2_rect2 = pygame.Rect(self.object2_pos2[0], self.ground2_pos[1] - self.ground2_height -
                                         self.object2_size2[1] - self.object2_pos2[1],
                                         self.object2_size2[0], self.object2_size2[1])
        pygame.draw.rect(game.screen, (255, 255, 0), (self.object2_pos2[0], self.ground2_pos[1] - self.ground2_height -
                                                      self.object2_size2[1] - self.object2_pos2[1],
                                                      self.object2_size2[0], self.object2_size2[1]))


class Room3:
    # Define the Setting for the room
    def __init__(self, setting):
        self.settings = setting
        self.games = game
        self.ground3_height = 100
        self.ground3_pos = (0, self.settings.screen_height)
        self.ground3_rect = pygame.Rect(self.ground3_pos[0], self.ground3_pos[1] - self.ground3_height,
                                        self.settings.screen_width, self.ground3_height)
        self.object3_pos = (300, 0)
        self.object3_size = (100, 50)
        self.object3_rect = pygame.Rect(self.object3_pos[0], self.object3_pos[1],
                                        self.object3_size[0], self.object3_size[1])
        self.object3_size2 = (300, 150)
        self.object3_pos2 = (300, 0)
        self.object3_rect2 = pygame.Rect(self.object3_pos2[0], self.ground3_pos[1] - self.ground3_height
                                         - self.object3_size2[1], self.object3_size2[0], self.object3_size2[1])
        self.font = pygame.font.Font(None, 80)

    # Define the Ground of Room 1
    def room3_ground(self):
        self.ground3_pos = (0, self.settings.screen_height)
        pygame.draw.rect(game.screen, (255, 255, 0), (self.ground3_pos[0], self.ground3_pos[1] - self.ground3_height,
                                                      self.settings.screen_width, self.ground3_height))
        self.ground3_rect = pygame.Rect(self.ground3_pos[0], self.ground3_pos[1] - self.ground3_height,
                                        self.settings.screen_width, self.ground3_height)

    def room3_object(self):
        self.object3_size = (300, 150)
        self.object3_pos = (300, 0)
        self.object3_rect = pygame.Rect(self.object3_pos[0], self.ground3_pos[1] - self.ground3_height
                                        - self.object3_size[1], self.object3_size[0], self.object3_size[1])
        pygame.draw.rect(game.screen, (255, 255, 0), (self.object3_pos[0], self.ground3_pos[1] - self.ground3_height -
                                                      self.object3_size[1],
                                                      self.object3_size[0], self.object3_size[1]))

    def room3_object2(self):
        self.object3_size2 = (200, 350)
        self.object3_pos2 = (900, 0)
        self.object3_rect2 = pygame.Rect(self.object3_pos2[0], self.ground3_pos[1] - self.ground3_height -
                                         self.object3_size2[1] - self.object3_pos2[1],
                                         self.object3_size2[0], self.object3_size2[1])
        pygame.draw.rect(game.screen, (255, 255, 0), (self.object3_pos2[0], self.ground3_pos[1] -
                                                      self.ground3_height -
                                                      self.object3_size2[1] - self.object3_pos2[1],
                                                      self.object3_size2[0], self.object3_size2[1]))

    def display_text_room3(self):
        line1 = "This jump looks hard..."
        line2 = "But you will find a way!"
        text1 = self.font.render(line1, True, (0, 125, 0))
        text2 = self.font.render(line2, True, (0, 125, 0))

        # Calculate the center position of the screen
        center_x = self.settings.screen_width // 2
        pos_y = self.settings.screen_height // 2 - 300

        # Calculate the position of the first line of text
        text1_x = center_x - text1.get_rect().width // 2
        text1_y = pos_y - text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Calculate the position of the second line of text
        text2_x = center_x - text2.get_rect().width // 2
        text2_y = pos_y + text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Draw the text (each line at a different position)
        game.screen.blit(text1, (text1_x, text1_y))
        game.screen.blit(text2, (text2_x, text2_y))


class Room4:
    # Define the Setting for the room
    def __init__(self, setting):
        self.settings = setting
        self.games = game
        self.ground4_height = 100
        self.ground4_pos = (0, self.settings.screen_height)
        self.ground4_rect = pygame.Rect(self.ground4_pos[0], self.ground4_pos[1] - self.ground4_height,
                                        self.settings.screen_width, self.ground4_height)
        self.object4_pos = (300, 0)
        self.object4_size = (100, 50)
        self.object4_rect = pygame.Rect(self.object4_pos[0], self.object4_pos[1],
                                        self.object4_size[0], self.object4_size[1])
        self.object4_size2 = (300, 150)
        self.object4_pos2 = (300, 0)
        self.object4_rect2 = pygame.Rect(self.object4_pos2[0], self.ground4_pos[1] - self.ground4_height
                                         - self.object4_size2[1], self.object4_size2[0], self.object4_size2[1])
        self.font = pygame.font.Font(None, 80)

    # Define the Ground of Room 1
    def room4_ground(self):
        self.ground4_pos = (0, self.settings.screen_height)
        pygame.draw.rect(game.screen, (255, 255, 0), (self.ground4_pos[0], self.ground4_pos[1] - self.ground4_height,
                                                      self.settings.screen_width, self.ground4_height))
        self.ground4_rect = pygame.Rect(self.ground4_pos[0], self.ground4_pos[1] - self.ground4_height,
                                        self.settings.screen_width, self.ground4_height)

    def room4_object(self):
        self.object4_size = (300, 150)
        self.object4_pos = (300, 0)
        self.object4_rect = pygame.Rect(self.object4_pos[0], self.ground4_pos[1] - self.ground4_height
                                        - self.object4_size[1], self.object4_size[0], self.object4_size[1])
        pygame.draw.rect(game.screen, (255, 255, 0), (self.object4_pos[0], self.ground4_pos[1] - self.ground4_height -
                                                      self.object4_size[1],
                                                      self.object4_size[0], self.object4_size[1]))

    def room4_object2(self):
        self.object4_size2 = (250, 400)
        self.object4_pos2 = (1000, 0)
        self.object4_rect2 = pygame.Rect(self.object4_pos2[0], self.ground4_pos[1] - self.ground4_height -
                                         self.object4_size2[1] - self.object4_pos2[1],
                                         self.object4_size2[0], self.object4_size2[1])
        pygame.draw.rect(game.screen, (255, 255, 0), (self.object4_pos2[0], self.ground4_pos[1] -
                                                      self.ground4_height -
                                                      self.object4_size2[1] - self.object4_pos2[1],
                                                      self.object4_size2[0], self.object4_size2[1]))

    def display_text_room4(self):
        line1 = "Impressive! And I even forgot to tell you something"
        line2 = "You can get a boost if you press LSHIFT with A or D"
        text1 = self.font.render(line1, True, (0, 125, 0))
        text2 = self.font.render(line2, True, (0, 125, 0))

        # Calculate the center position of the screen
        center_x = self.settings.screen_width // 2
        pos_y = self.settings.screen_height // 2 - 300

        # Calculate the position of the first line of text
        text1_x = center_x - text1.get_rect().width // 2
        text1_y = pos_y - text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Calculate the position of the second line of text
        text2_x = center_x - text2.get_rect().width // 2
        text2_y = pos_y + text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Draw the text (each line at a different position)
        game.screen.blit(text1, (text1_x, text1_y))
        game.screen.blit(text2, (text2_x, text2_y))


class Room5:
    # Define the Setting for the room
    def __init__(self, setting):
        self.settings = setting
        self.ground5_height = 100
        self.ground5_pos = (0, self.settings.screen_height)
        self.ground5_rect = pygame.Rect(self.ground5_pos[0], self.ground5_pos[1] - self.ground5_height,
                                        self.settings.screen_width, self.ground5_height)
        self.object5_pos = (300, 0)
        self.object5_size = (100, 50)
        self.object5_rect = pygame.Rect(self.object5_pos[0], self.object5_pos[1],
                                        self.object5_size[0], self.object5_size[1])
        self.object5_size2 = (250, 100)
        self.object5_pos2 = (400, self.ground5_pos[1] - self.ground5_height - 250)
        self.object5_rect2 = pygame.Rect(self.object5_pos2[0], self.object5_pos2[1],
                                         self.object5_size2[0], self.object5_size2[1])
        self.object5_size3 = (250, 100)
        self.object5_pos3 = (800, self.ground5_pos[1] - self.ground5_height - 0)
        self.object5_rect3 = pygame.Rect(self.object5_pos3[0], self.object5_pos3[1],
                                         self.object5_size3[0], self.object5_size3[1])
        self.object5_size4 = (100, 700)
        self.object5_pos4 = (1400, self.ground5_pos[1] - self.ground5_height - self.object5_size4[1])
        self.object5_rect4 = pygame.Rect(self.object5_pos4[0], self.object5_pos4[1],
                                         self.object5_size4[0], self.object5_size4[1])

    # Define the Ground of Room 5
    def room5_ground(self):
        self.ground5_pos = (0, self.settings.screen_height)
        pygame.draw.rect(game.screen, (255, 255, 0), (self.ground5_pos[0], self.ground5_pos[1] - self.ground5_height,
                                                      self.settings.screen_width, self.ground5_height))
        self.ground5_rect = pygame.Rect(self.ground5_pos[0], self.ground5_pos[1] - self.ground5_height,
                                        self.settings.screen_width, self.ground5_height)

    def room5_object(self):
        self.object5_size = (200, 100)
        self.object5_pos = (400, self.ground5_pos[1] - self.ground5_height - 250)
        self.object5_rect = pygame.Rect(self.object5_pos[0], self.object5_pos[1],
                                        self.object5_size[0], self.object5_size[1])
        pygame.draw.rect(game.screen, (255, 255, 0), (self.object5_pos[0], self.object5_pos[1],
                                                      self.object5_size[0], self.object5_size[1]))

    def room5_object2(self):
        self.object5_size2 = (250, 100)
        self.object5_pos2 = (800, self.ground5_pos[1] - self.ground5_height - 450)
        self.object5_rect2 = pygame.Rect(self.object5_pos2[0], self.object5_pos2[1],
                                         self.object5_size2[0], self.object5_size2[1])
        pygame.draw.rect(game.screen, (255, 255, 0), (self.object5_pos2[0], self.object5_pos2[1],
                                                      self.object5_size2[0], self.object5_size2[1]))

    def room5_object3(self):
        self.object5_size3 = (100, 400)
        self.object5_pos3 = (1500, self.ground5_pos[1] - self.ground5_height - self.object5_size3[1])
        self.object5_rect3 = pygame.Rect(self.object5_pos3[0], self.object5_pos3[1],
                                         self.object5_size3[0], self.object5_size3[1])
        pygame.draw.rect(game.screen, (255, 255, 0), (self.object5_pos3[0], self.object5_pos3[1],
                                                      self.object5_size3[0], self.object5_size3[1]))

    def room5_object4(self):
        self.object5_size4 = (100, 450)
        self.object5_pos4 = (1500, 0)
        self.object5_rect4 = pygame.Rect(self.object5_pos4[0], self.object5_pos4[1],
                                         self.object5_size4[0], self.object5_size4[1])
        pygame.draw.rect(game.screen, (255, 255, 0), (self.object5_pos4[0], self.object5_pos4[1],
                                                      self.object5_size4[0], self.object5_size4[1]))


class Room6:
    # Define the Setting for the room
    def __init__(self, setting):
        self.settings = setting
        self.ground6_height = 100
        self.ground6_pos = (0, self.settings.screen_height)
        self.ground6_rect = pygame.Rect(self.ground6_pos[0], self.ground6_pos[1] - self.ground6_height,
                                        self.settings.screen_width, self.ground6_height)
        self.object6_pos = (300, 0)
        self.object6_size = (100, 50)
        self.object6_rect = pygame.Rect(self.object6_pos[0], self.object6_pos[1],
                                        self.object6_size[0], self.object6_size[1])
        self.object6_size1 = (250, 100)
        self.object6_pos1 = (400, self.ground6_pos[1] - self.ground6_height)
        self.object6_rect1 = pygame.Rect(self.object6_pos1[0], self.object6_pos1[1],
                                         self.object6_size1[0], self.object6_size1[1])
        self.dmg_size = (250, 100)
        self.dmg_pos = (800, self.ground6_pos[1] - self.ground6_height - 0)
        self.dmg_rect = pygame.Rect(self.dmg_pos[0], self.dmg_pos[1],
                                    self.dmg_size[0], self.dmg_size[1])
        self.font = pygame.font.Font(None, 80)

    def display_text_room6(self):
        line1 = "Watch out for this red sea"
        line2 = "It looks deadly!"
        text1 = self.font.render(line1, True, (0, 125, 0))
        text2 = self.font.render(line2, True, (0, 125, 0))

        # Calculate the center position of the screen
        center_x = self.settings.screen_width // 2
        pos_y = self.settings.screen_height // 2 - 300

        # Calculate the position of the first line of text
        text1_x = center_x - text1.get_rect().width // 2
        text1_y = pos_y - text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Calculate the position of the second line of text
        text2_x = center_x - text2.get_rect().width // 2
        text2_y = pos_y + text1.get_rect().height // 2 - text2.get_rect().height // 2

        # Draw the text (each line at a different position)
        game.screen.blit(text1, (text1_x, text1_y))
        game.screen.blit(text2, (text2_x, text2_y))

    # Define the Ground of Room 6
    def room6_ground(self):
        self.ground6_pos = (0, self.settings.screen_height)
        pygame.draw.rect(game.screen, (255, 255, 0), (self.ground6_pos[0], self.ground6_pos[1] - self.ground6_height,
                                                      self.settings.screen_width, self.ground6_height))
        self.ground6_rect = pygame.Rect(self.ground6_pos[0], self.ground6_pos[1] - self.ground6_height,
                                        self.settings.screen_width, self.ground6_height)

    def room6_object(self):
        self.object6_size = (200, 100)
        self.object6_pos = (600, self.ground6_pos[1] - self.ground6_height - self.object6_size[1])
        self.object6_rect = pygame.Rect(self.object6_pos[0], self.object6_pos[1],
                                        self.object6_size[0], self.object6_size[1])
        pygame.draw.rect(game.screen, (255, 255, 0), (self.object6_pos[0], self.object6_pos[1],
                                                      self.object6_size[0], self.object6_size[1]))

    def room6_object1(self):
        self.object6_size1 = (250, 150)
        self.object6_pos1 = (1000, self.ground6_pos[1] - self.ground6_height - self.object6_size1[1])
        self.object6_rect1 = pygame.Rect(self.object6_pos1[0], self.object6_pos1[1],
                                         self.object6_size1[0], self.object6_size1[1])
        pygame.draw.rect(game.screen, (255, 255, 0), (self.object6_pos1[0], self.object6_pos1[1],
                                                      self.object6_size1[0], self.object6_size1[1]))

    def room6_dmg(self):
        self.dmg_size = (200, 25)
        self.dmg_pos = (800, self.ground6_pos[1] - self.ground6_height - 0.1)
        self.dmg_rect = pygame.Rect(self.dmg_pos[0], self.dmg_pos[1],
                                    self.dmg_size[0], self.dmg_size[1])
        pygame.draw.rect(game.screen, (255, 0, 0), (self.dmg_pos[0], self.dmg_pos[1],
                                                    self.dmg_size[0], self.dmg_size[1]))


# initialise Settings before Game Start
settings = Settings()
settings.set_fullscreen(True)
game = GameSettings(settings)
roomGL = GlitchRoom(settings)
room0 = Room0(settings)
room1 = Room1(settings)
room2 = Room2(settings)
room3 = Room3(settings)
room4 = Room4(settings)
room5 = Room5(settings)
room6 = Room6(settings)
clock = pygame.time.Clock()
game.start()
running = True

# set the screen Size
if settings.fullscreen:
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

pygame.display.set_caption(settings.caption)

# Game main Loop
while running:
    clock.tick(240)
    # Check for events
    for event in pygame.event.get():
        # Quit the game if the user closes the window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        # Screen events for jumping and moving the player when pressing Keys
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game.unlock_jump:
                    if game.jumps > 0:
                        game.jumps = game.jumps - 1
                        game.jumping = True
                        game.jump()
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and (event.key == pygame.K_RIGHT or event.key
                                                                            == pygame.K_d):
                game.square_direction = 'stay'
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                game.square_direction = 'left'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                game.square_direction = 'right'
            if event.key == pygame.K_LSHIFT:
                if game.unlock_boost and game.use_boost is False and not game.square_direction == 'stay':
                    game.boost()
                    game.use_boost = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if game.square_direction != 'right':
                    game.square_direction = 'stay'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if game.square_direction != 'left':
                    game.square_direction = 'stay'

    # regulate square boost
    if game.use_boost and game.square_speed >= 1.5:
        if game.jumping is False:
            game.square_speed -= 0.01
        else:
            game.square_speed -= 0.025
    else:
        game.use_boost = False

    # make the square jump
    if game.jumping:
        game.square_velocity += game.gravity
        # Update square's y-position based on velocity
        game.square_height -= game.square_velocity

    if game.room_number == 0:
        # Define what happens in room 1
        if game.jumping and game.square_rect.colliderect(room1.ground_rect):
            game.jumping = False
            game.square_height = room1.ground_height
            game.jumps = 1
    elif game.room_number == -1:
        # Define what happens in room -1
        if game.jumping and game.square_rect.colliderect(room0.ground0_rect):
            game.jumping = False
            game.square_height = room0.ground0_height
            game.jumps = 1
            # Define collision with wall
        if game.square_pos[0] <= 0:
            game.square_width -= game.square_speed
    elif game.room_number == -2:
        if game.jumping and game.square_rect.colliderect(roomGL.ground_rect):
            game.jumping = False
            game.square_height = room1.ground_height
            game.jumps = 1
    elif game.room_number == 1:
        # Define what happens in room 2
        # Define collision with ground
        game.un_jump()
        if game.jumping and game.square_rect.colliderect(room2.ground2_rect):
            game.jumping = False
            game.square_height = room2.ground2_height
            game.jumps = 1
            # Define collision with object
        if game.square_rect.colliderect(room2.object2_rect):
            if room2.object2_rect.right >= game.square_rect.left >= room2.object2_rect.left:
                if game.square_direction == 'left':
                    game.square_width -= game.square_speed
            elif room2.object2_rect.left <= game.square_rect.right <= room2.object2_rect.right:
                if game.square_direction == 'right':
                    game.square_width += game.square_speed
            if room2.object2_rect.top <= game.square_rect.bottom+10 <=\
                    room2.object2_rect.bottom-room2.object2_size[1]+20:
                if game.square_velocity > 0:
                    game.jumping = False
                game.square_height = room2.ground2_height + room2.object2_size[1]
                game.jumps = 1
        if game.square_rect.colliderect(room2.object2_rect2):
            if room2.object2_rect2.right >= game.square_rect.left >= room2.object2_rect2.left:
                if game.square_direction == 'left':
                    game.square_width -= game.square_speed
            elif room2.object2_rect2.left <= game.square_rect.right <= room2.object2_rect2.right:
                if game.square_direction == 'right':
                    game.square_width += game.square_speed
            if room2.object2_rect2.top <= game.square_rect.bottom+10 <=\
                    room2.object2_rect2.bottom-room2.object2_size2[1]+20:
                if game.square_velocity > 0:
                    game.jumping = False
                game.square_height = room2.ground2_height + room2.object2_size2[1]
                game.jumps = 1

        # gravity in room2
        if game.settings.screen_height-room2.ground2_height-game.square_size[1]-10 > game.square_pos[1]:
            if game.square_pos[0]+game.square_size[0] < room2.object2_pos[0] and game.jumping is False:
                game.jumping = True
            elif game.square_pos[0] > room2.object2_pos[0]+room2.object2_size[0] \
                    and game.square_pos[0]+game.square_size[0] < room2.object2_pos2[0]\
                    and game.jumping is False:
                game.jumping = True
            elif game.square_pos[0] > room2.object2_pos2[0] + room2.object2_size2[0] and game.jumping is False:
                game.jumping = True
    elif game.room_number == 2:
        # Define what happens in room 3
        # Define collision with ground
        if game.jumping and game.square_rect.colliderect(room3.ground3_rect):
            game.jumping = False
            game.square_height = room3.ground3_height
            game.jumps = 1
            # Define collision with object
        if game.square_rect.colliderect(room3.object3_rect):
            if room3.object3_rect.right >= game.square_rect.left >= room3.object3_rect.left:
                if game.square_direction == 'left':
                    game.square_width -= game.square_speed
            elif room3.object3_rect.left <= game.square_rect.right <= room3.object3_rect.right:
                if game.square_direction == 'right':
                    game.square_width += game.square_speed
            if room3.object3_rect.top <= game.square_rect.bottom+10 <=\
                    room3.object3_rect.bottom-room3.object3_size[1]+20:
                if game.square_velocity > 0:
                    game.jumping = False
                game.square_height = room3.ground3_height + room3.object3_size[1]
                game.jumps = 1
        if game.square_rect.colliderect(room3.object3_rect2):
            if room3.object3_rect2.right >= game.square_rect.left >= room3.object3_rect2.left:
                if game.square_direction == 'left':
                    game.square_width -= game.square_speed
            elif room3.object3_rect2.left <= game.square_rect.right <= room3.object3_rect2.right:
                if game.square_direction == 'right':
                    game.square_width += game.square_speed
            if room3.object3_rect2.top <= game.square_rect.bottom+10 <=\
                    room3.object3_rect2.bottom-room3.object3_size2[1]+20:
                if game.square_velocity > 0:
                    game.jumping = False
                game.square_height = room3.ground3_height + room3.object3_size2[1]
                game.jumps = 1

        # gravity in room3
        if game.settings.screen_height-room3.ground3_height-game.square_size[1]-10 > game.square_pos[1]:
            if game.square_pos[0]+game.square_size[0] < room3.object3_pos[0] and game.jumping is False:
                game.jumping = True
            elif game.square_pos[0] > room3.object3_pos[0]+room3.object3_size[0] \
                    and game.square_pos[0]+game.square_size[0] < room3.object3_pos2[0]\
                    and game.jumping is False:
                game.jumping = True
            elif game.square_pos[0] > room3.object3_pos2[0] + room3.object3_size2[0] and game.jumping is False:
                game.jumping = True

    elif game.room_number == 3:
        # unlock Boost
        game.un_boost()
        # Define what happens in room 4
        # Define collision with ground
        if game.jumping and game.square_rect.colliderect(room4.ground4_rect):
            game.jumping = False
            game.square_height = room4.ground4_height
            game.jumps = 1
            # Define collision with object
        if game.square_rect.colliderect(room4.object4_rect):
            if room4.object4_rect.right >= game.square_rect.left >= room4.object4_rect.left:
                if game.square_direction == 'left':
                    game.square_width -= game.square_speed
            elif room4.object4_rect.left <= game.square_rect.right <= room4.object4_rect.right:
                if game.square_direction == 'right':
                    game.square_width += game.square_speed
            if room4.object4_rect.top <= game.square_rect.bottom+10 <=\
                    room4.object4_rect.bottom-room4.object4_size[1]+20:
                if game.square_velocity > 0:
                    game.jumping = False
                game.square_height = room4.ground4_height + room4.object4_size[1]
                game.jumps = 1
        if game.square_rect.colliderect(room4.object4_rect2):
            if room4.object4_rect2.right >= game.square_rect.left >= room4.object4_rect2.left:
                if game.square_direction == 'left':
                    game.square_width -= game.square_speed
            elif room4.object4_rect2.left <= game.square_rect.right <= room4.object4_rect2.right:
                if game.square_direction == 'right':
                    game.square_width += game.square_speed
            if room4.object4_rect2.top <= game.square_rect.bottom+10 <=\
                    room4.object4_rect2.bottom-room4.object4_size2[1]+20:
                if game.square_velocity > 0:
                    game.jumping = False
                game.square_height = room4.ground4_height + room4.object4_size2[1]
                game.jumps = 1

        # gravity in room 4
        if game.settings.screen_height-room4.ground4_height-game.square_size[1]-10 > game.square_pos[1]:
            if game.square_pos[0]+game.square_size[0] < room4.object4_pos[0] and game.jumping is False:
                game.jumping = True
            elif game.square_pos[0] > room4.object4_pos[0]+room4.object4_size[0] \
                    and game.square_pos[0]+game.square_size[0] < room4.object4_pos2[0]\
                    and game.jumping is False:
                game.jumping = True
            elif game.square_pos[0] > room4.object4_pos2[0] + room4.object4_size2[0] and game.jumping is False:
                game.jumping = True

    elif game.room_number == 4:
        if game.jumping and game.square_rect.colliderect(room5.ground5_rect):
            game.jumping = False
            game.square_height = room1.ground_height
            game.jumps = 1

        elif game.square_rect.colliderect(room5.object5_rect):
            if room5.object5_rect.right >= game.square_rect.left >= room5.object5_rect.left:
                if game.square_direction == 'left':
                    game.square_width -= game.square_speed
            elif room5.object5_rect.left <= game.square_rect.right <= room5.object5_rect.right:
                if game.square_direction == 'right':
                    game.square_width += game.square_speed
            if room5.object5_rect.top <= game.square_rect.bottom+10 <=\
                    room5.object5_rect.bottom-room5.object5_size[1]+20:
                if game.square_velocity > 0:
                    game.jumping = False
                game.square_height = settings.screen_height - room5.object5_pos[1]
                game.jumps = 1
            elif room5.object5_rect.bottom >= game.square_rect.top - 10 >= \
                    room5.object5_rect.top + room5.object5_size[1] - 20:
                game.square_velocity = 1

        elif game.square_rect.colliderect(room5.object5_rect2):
            if room5.object5_rect2.right >= game.square_rect.left >= room5.object5_rect2.left:
                if game.square_direction == 'left':
                    game.square_width -= game.square_speed
            elif room5.object5_rect2.left <= game.square_rect.right <= room5.object5_rect2.right:
                if game.square_direction == 'right':
                    game.square_width += game.square_speed
            if room5.object5_rect2.top <= game.square_rect.bottom + 10 <= \
                    room5.object5_rect2.bottom - room5.object5_size2[1] + 20:
                if game.square_velocity > 0:
                    game.jumping = False
                game.square_height = settings.screen_height - room5.object5_pos2[1]
                game.jumps = 1
            elif room5.object5_rect2.bottom >= game.square_rect.top - 10 >= \
                    room5.object5_rect2.top + room5.object5_size2[1] - 20:
                game.square_velocity = 1

        elif game.square_rect.colliderect(room5.object5_rect3):
            if room5.object5_rect3.right >= game.square_rect.left >= room5.object5_rect3.left:
                if game.square_direction == 'left':
                    game.square_width -= game.square_speed
            elif room5.object5_rect3.left <= game.square_rect.right <= room5.object5_rect3.right:
                if game.square_direction == 'right':
                    game.square_width += game.square_speed
            if room5.object5_rect3.top <= game.square_rect.bottom + 10 <= \
                    room5.object5_rect3.bottom - room5.object5_size3[1] + 20:
                if game.square_velocity > 0:
                    game.jumping = False
                game.square_height = settings.screen_height - room5.object5_pos3[1]
                game.jumps = 1
            elif room5.object5_rect3.bottom >= game.square_rect.top - 10 >= \
                    room5.object5_rect3.top + room5.object5_size3[1] - 20:
                game.square_velocity = 1

        elif game.square_rect.colliderect(room5.object5_rect4):
            if room5.object5_rect4.right >= game.square_rect.left >= room5.object5_rect4.left:
                if game.square_direction == 'left':
                    game.square_width -= game.square_speed
            elif room5.object5_rect4.left <= game.square_rect.right <= room5.object5_rect4.right:
                if game.square_direction == 'right':
                    game.square_width += game.square_speed
            if room5.object5_rect4.top <= game.square_rect.bottom + 10 <= \
                    room5.object5_rect4.bottom - room5.object5_size4[1] + 20:
                if game.square_velocity > 0:
                    game.jumping = False
                game.square_height = settings.screen_height - room5.object5_pos4[1]
                game.jumps = 1
            elif room5.object5_rect4.bottom >= game.square_rect.top - 10 >= \
                    room5.object5_rect4.top + room5.object5_size4[1] - 20:
                if game.square_velocity < 0:
                    game.square_velocity = 1

        # gravity in room 5
        if game.settings.screen_height-room5.ground5_height-game.square_size[1]-10 > game.square_pos[1]:
            if game.square_pos[0]+game.square_size[0] < room5.object5_pos[0] and game.jumping is False:
                game.jumping = True
            elif game.square_pos[0] > room5.object5_pos[0]+room5.object5_size[0] \
                    and game.square_pos[0]+game.square_size[0] < room5.object5_pos2[0]\
                    and game.jumping is False:
                game.jumping = True
            elif game.square_pos[0] > room5.object5_pos2[0] + room5.object5_size2[0]\
                    and game.square_pos[0]+game.square_size[0] < room5.object5_pos3[0]\
                    and game.jumping is False:
                game.jumping = True
            elif game.square_pos[0] > room5.object5_pos3[0] + room5.object5_size3[0] and game.jumping is False:
                game.jumping = True

    elif game.room_number == 5:
        if game.jumping and game.square_rect.colliderect(room6.ground6_rect):
            game.jumping = False
            game.square_height = room6.ground6_height
            game.jumps = 1

        elif game.square_rect.colliderect(room6.object6_rect):
            if room6.object6_rect.right >= game.square_rect.left >= room6.object6_rect.left:
                if game.square_direction == 'left':
                    game.square_width -= game.square_speed
            elif room6.object6_rect.left <= game.square_rect.right <= room6.object6_rect.right:
                if game.square_direction == 'right':
                    game.square_width += game.square_speed
            if room6.object6_rect.top <= game.square_rect.bottom+10 <=\
                    room6.object6_rect.bottom-room6.object6_size[1]+20:
                if game.square_velocity > 0:
                    game.jumping = False
                game.square_height = settings.screen_height - room6.object6_pos[1]
                game.jumps = 1
            elif room6.object6_rect.bottom >= game.square_rect.top - 10 >= \
                    room6.object6_rect.top + room6.object6_size[1] - 20:
                game.square_velocity = 1

        elif game.square_rect.colliderect(room6.object6_rect1):
            if room6.object6_rect1.right >= game.square_rect.left >= room6.object6_rect1.left:
                if game.square_direction == 'left':
                    game.square_width -= game.square_speed
            elif room6.object6_rect1.left <= game.square_rect.right <= room6.object6_rect1.right:
                if game.square_direction == 'right':
                    game.square_width += game.square_speed
            if room6.object6_rect1.top <= game.square_rect.bottom + 10 <= \
                    room6.object6_rect1.bottom - room6.object6_size1[1] + 20:
                if game.square_velocity > 0:
                    game.jumping = False
                game.square_height = settings.screen_height - room6.object6_pos1[1]
                game.jumps = 1
            elif room6.object6_rect1.bottom >= game.square_rect.top - 10 >= \
                    room6.object6_rect1.top + room6.object6_size1[1] - 20:
                game.square_velocity = 1

        elif game.square_rect.colliderect(room6.dmg_rect):
            game.gameover_screen()

        # gravity in room 6
        if game.settings.screen_height-room6.ground6_height-game.square_size[1]-10 > game.square_pos[1]:
            if game.square_pos[0]+game.square_size[0] < room6.object6_pos[0] and game.jumping is False:
                game.jumping = True
            elif game.square_pos[0] > room6.object6_pos[0]+room6.object6_size[0] \
                    and game.square_pos[0]+game.square_size[0] < room6.object6_pos1[0] \
                    and game.jumping is False:
                game.jumping = True
            elif game.square_pos[0] > room6.object6_pos1[0] + room6.object6_size1[0] and game.jumping is False:
                game.jumping = True

    # make square move
    if game.square_direction == 'right':
        game.square_width -= game.square_speed
    elif game.square_direction == 'left':
        game.square_width += game.square_speed

    # make square teleport to other side
    if game.square_pos[0] > settings.screen_width + 25:
        game.square_width = 90
        game.square_width -= game.square_speed
        game.room_number = game.room_number + 1
    elif game.square_pos[0] < -100 and game.room_number > -1:
        game.square_width = -settings.screen_width + 50
        game.room_number = game.room_number - 1
        game.square_width += game.square_speed

    # Draw BG and square
    screen.fill(settings.bg_color)

    # Draw the red square and the ground
    if game.room_number == 0:
        screen.fill(settings.bg_color)
        room1.room1_ground()
        room1.display_text_room1()
        game.place_square()
    elif game.room_number == -1:
        room0.room0_ground()
        game.place_square()
        room0.display_text_room0()
    elif game.room_number == -2:
        roomGL.glitch_room_ground()
        roomGL.display_text_room_glitch()
        game.place_square()
    elif game.room_number == 1:
        room2.room2_ground()
        room2.room2_object()
        room2.room2_object2()
        room2.display_text_room2()
        game.place_square()
    elif game.room_number == 2:
        room3.room3_ground()
        room3.room3_object()
        room3.room3_object2()
        room3.display_text_room3()
        game.place_square()
    elif game.room_number == 3:
        room4.room4_ground()
        room4.room4_object()
        room4.room4_object2()
        room4.display_text_room4()
        game.place_square()
    elif game.room_number == 4:
        room5.room5_ground()
        room5.room5_object()
        room5.room5_object2()
        room5.room5_object3()
        room5.room5_object4()
        game.place_square()
    elif game.room_number == 5:
        room6.room6_ground()
        room6.room6_object()
        room6.room6_object1()
        room6.room6_dmg()
        room6.display_text_room6()
        game.place_square()
    # Update Screen
    pygame.display.update()
    # Start to Display
    pygame.display.flip()
