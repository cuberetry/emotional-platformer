import OpenCVPage.driver_code as cv

if __name__ == '__main__':
    main_emotion_detector = cv.EmotionDetector()

    while True:
        main_emotion_detector.main_loop()
