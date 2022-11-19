import OpenCVPage.emotion_detector_model as cv
import PygamePage.scene0 as pg

if __name__ == '__main__':
    main_emotion_detector = cv.EmotionDetector()
    main_pygame_window = pg.MainPygameWindow()

    while True:
        main_emotion_detector.main_loop()
        print("Current emotion:", main_emotion_detector.label)
        main_pygame_window.main_loop()
