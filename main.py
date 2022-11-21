import OpenCVPage.emotion_detector_model as cv
import PygamePage.game_window as pg
import GlobalVariable.game_var as gb_var
import threading


def thread_function(func):
    while gb_var.IS_RUNNING:
        func()


if __name__ == '__main__':
    main_emotion_detector = cv.EmotionDetector()
    main_pygame_window = pg.MainPygameWindow()
    emotion_thread = threading.Thread(target=thread_function, args=(main_emotion_detector.main_loop, ))
    emotion_thread.start()

    while gb_var.IS_RUNNING:
        if not gb_var.IS_PAUSING:
            gb_var.EMOTION = main_emotion_detector.label
        gb_var.CUR_SCENE.mainloop()
