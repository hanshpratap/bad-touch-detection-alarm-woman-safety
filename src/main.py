import cv2
from src.utils.config_loader import load_config
from src.detector import TouchDetector
from src.alarm import AlarmPlayer


def main():
    config = load_config()
    detector = TouchDetector(distance_threshold=config["distance_threshold"])
    alarm = AlarmPlayer(audio_file=config["audio_file"])

    cap = cv2.VideoCapture(config["camera_index"])

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame, touched = detector.detect_touch(frame)

        if touched:
            alarm.play_alarm()
        else:
            alarm.stop_alarm()

        cv2.imshow("Bad Touch Detect", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
