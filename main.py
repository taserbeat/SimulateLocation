from models.GPS import GPS
import os
import logging
import pygame
from pygame import event
from models.ControllerInput import ControllerInput
from models.GPS import GPS

# 定数
GPS_BIAS = 1.0e-8

# 環境変数の読み込み
XCODE_SIMLOC_GPX_FULL_PATH = os.environ.get("XCODE_SIMLOC_GPX_FULL_PATH")
if (XCODE_SIMLOC_GPX_FULL_PATH is None) or (not os.path.exists(XCODE_SIMLOC_GPX_FULL_PATH)):
    logging.error("XCODE_SIMLOC_GPX_FULL_PATH has something wrong.")
    exit(-1)

# コントローラと接続
controller = ControllerInput(0)

# GPS座標
gps = GPS()

done = False
while not done:
    for e in event.get():
        # ボタンが押された場合
        if e.type == pygame.JOYBUTTONDOWN:
            # Bボタンが押されたらループを終了
            if controller.button_b_pressed:
                done = True
                pass
        # ジョイスティックに入力があった場合
        if e.type == pygame.JOYAXISMOTION:
            stick_x, stick_y = controller.stick_left_axis
            added_lat = stick_y * GPS_BIAS
            added_lon = stick_x * GPS_BIAS
            print(f'added_lat: {added_lat}, added_lon: {added_lon}')
            gps.add(added_lat, added_lon)
            pass

        pass

    print(f'緯度: {gps.lat}, 経度: {gps.lon}')
