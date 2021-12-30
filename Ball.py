import pygame

from Movable import Movable
from Screen import Screen


class Ball(Movable):
    def draw(self):
        pygame.draw.circle(Screen.get_screen(), Screen.get_color(),
                           (self.x_position, self.y_position), self.size)
        self.calculate_position(Screen.get_left(), Screen.get_right(),
                                Screen.get_top(), Screen.get_bottom(), 0.01)
        # print(f'x_position: {self.x_position}, y_position: {self.y_position}')
        pygame.draw.circle(Screen.get_screen(), self.color,
                           (self.x_position, self.y_position), self.size)
