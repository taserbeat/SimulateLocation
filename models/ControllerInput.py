import pygame
from pygame import joystick


class ControllerInput:
    def __init__(self, joystick_index: int = 0):
        pygame.init()
        self.__joy = joystick.Joystick(joystick_index)
        self.__joy.init()
        return

    def update(self):
        return

    @property
    def joy(self):
        return self.__joy

    @property
    def button_a_pressed(self):
        return self.__joy.get_button(3)

    @property
    def button_b_pressed(self):
        return self.__joy.get_button(2)

    @property
    def button_x_pressed(self):
        return self.__joy.get_button(1)

    @property
    def button_y_pressed(self):
        return self.__joy.get_button(0)

    @property
    def stick_left_axis(self):
        origin_x, origin_y = self.__joy.get_axis(0), self.__joy.get_axis(1)
        converted_x, converted_y = int(origin_x * 100), int(-origin_y * 100)
        return converted_x, converted_y
