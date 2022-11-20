import OpenCVPage.emotion_detector_model as cv
import PygamePage.scene0 as pg
import GlobalVariable.game_var as gb_var
import GlobalVariable.game_setting as gb_setting
import threading


def thread_function(func):
    while gb_setting.IS_RUNNING:
        func()


if __name__ == '__main__':
    main_emotion_detector = cv.EmotionDetector()
    main_pygame_window = pg.MainPygameWindow()
    emotion_thread = threading.Thread(target=thread_function, args=(main_emotion_detector.main_loop, ))
    emotion_thread.start()

    while gb_setting.IS_RUNNING:
        gb_var.EMOTION = main_emotion_detector.label
        main_pygame_window.main_loop()

