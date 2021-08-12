import pygame
from pygame import event
from models.ControllerInput import ControllerInput

#
LOOP_FRAME = 10000000

controller = ControllerInput(0)


def main():
    frame = 0

    while True:
        test_process()
        frame += 1
        if frame >= LOOP_FRAME:
            break
    return


def test_process():
    for e in event.get():
        if e.type == pygame.JOYBUTTONDOWN:
            print("a: {0}, b: {1}, x: {2}, y: {3}".format(
                controller.button_a_pressed,
                controller.button_b_pressed,
                controller.button_x_pressed,
                controller.button_y_pressed
            ))
        elif e.type == pygame.JOYAXISMOTION:
            stick_left_x, stick_left_y = controller.stick_left_axis
            print("x: {0}, y: {1}".format(stick_left_x, stick_left_y))

    return


if __name__ == '__main__':
    main()
