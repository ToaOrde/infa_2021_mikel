import pygame
import math

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 127, 80)
blue = (0, 0, 255)

FPS = 500
brick_width = 60
brick_height = 15
paddle_width = 75
paddle_height = 10
paddle_loc_x = display_width / 2
paddle_loc_y = (display_height - (5 * paddle_height))
ball_radius = 7
ball_diameter = 2 * ball_radius

state_won = 2
state_playing = 1
state_game_over = 3
state_ball_in_paddle = 0

class Arkanoid():
    def __init__(self):
        pygame.init()

        self.lives = 3
        self.state = state_ball_in_paddle
        self.score = 0

        self.paddle = pygame.Rect(paddle_loc_x, paddle_loc_y, paddle_width, paddle_height)
        self.ball = pygame.Rect(paddle_loc_x, paddle_width, ball_radius, ball_radius)
        self.font = pygame.font.SysFont(None, 30)
        self.bricks()

    def bricks(self):
        y = 70
        self.bricks_list = []
        for i in range(7):
            x = ((math.floor(display_width / (brick_width + 1))) / 2) - 2
            for j in range(13):
                self.bricks_list.append(pygame.Rect(x, y, brick_width, brick_height))
                x += brick_width + 1
            y += brick_height + 1

    def draw_bricks(self):
        for brick in self.bricks_list:
            pygame.draw.rect(gameDisplay, orange, brick)

    def stats(self):
        if self.font:
            font_surface = self.font.render("score: " + str(self.score) + "    lives: " + str(self.lives), False, black)
            gameDisplay.blit(font_surface, (0, 580))

    def game_information(self, message):
        if self.font:
            size = self.font.size(message)
            font_surface = self.font.render(message, True, black)
            x_text_coord = (display_width - size[0]) / 2
            y_text_coord = (display_height - size[1]) / 2
            gameDisplay.blit(font_surface, (x_text_coord, y_text_coord))

    def ball_movement(self):
        self.ball.left += self.ball_vel[0]
        self.ball.top += self.ball_vel[1]

        if self.ball.left <= 0:
            self.ball.left = 0
            self.ball_vel[0] = -self.ball_vel[0]
        elif self.ball.left >= display_width - ball_radius:
            self.ball.left = display_width - ball_radius
            self.ball_vel[0] = -self.ball_vel[0]

        if self.ball.top < 0:
            self.ball.top = 0
            self.ball_vel[1] = -self.ball_vel[1]
        elif self.ball.top >= display_height - ball_radius:
            self.ball.top = display_height - ball_radius
            self.ball_vel[1] = - self.ball_vel[1]

    def collisions(self):
        for brick in self.bricks_list:
            if self.ball.colliderect(brick):
                self.score += 1
                self.ball_vel[1] = - self.ball_vel[1]
                self.bricks_list.remove(brick)
                break

        if len(self.bricks_list) == 0:
            self.state = state_won

        if self.ball.colliderect(self.paddle):
            self.ball.top = paddle_loc_y - ball_radius
            self.ball_vel[1] = - self.ball_vel[1]
        elif self.ball.top > display_height - ball_diameter:
            self.lives -= 1
            if self.lives > 0:
                self.state = state_ball_in_paddle
            else:
                self.state = state_game_over

    def inputs(self):
        press = pygame.key.get_pressed()
        if press[pygame.K_LEFT]:
            self.paddle.left -= 1
            if self.paddle.left < 0:
                self.paddle.left = 0

        if press[pygame.K_RIGHT]:
            self.paddle.right += 1
            if self.paddle.right > display_width:
                self.paddle.right = display_width

        if press[pygame.K_SPACE] and self.state == state_ball_in_paddle:
            self.ball_vel = [1, -1]
            self.state = state_playing
        elif press[pygame.K_RETURN] and (self.state == state_won or self.state == state_game_over):
            self.__init__()

    def main_loop(self):
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            self.inputs()

            if self.state == state_playing:
                self.ball_movement()
                self.collisions()
            elif self.state == state_ball_in_paddle:
                self.ball.left = self.paddle.left + self.paddle.width / 2
                self.ball.top = self.paddle.top - self.paddle.height
                self.game_information("Press space to start game")
            elif self.state == state_won:
                self.game_information("you won, press 'enter' to play again")
            elif self.state == state_game_over:
                self.game_information("Game over, press 'enter' to play again")

            pygame.draw.rect(gameDisplay, black, self.paddle)
            pygame.draw.circle(gameDisplay, blue, (self.ball.left, self.ball.top + 4), ball_radius)
            self.draw_bricks()
            self.stats()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True

            clock.tick(FPS)

Arkanoid().main_loop()

pygame.quit()
quit()
