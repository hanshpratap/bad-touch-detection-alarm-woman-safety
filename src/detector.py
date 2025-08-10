import cv2
import mediapipe as mp
import math

class TouchDetector:
    def __init__(self, distance_threshold=0.07):
        self.distance_threshold = distance_threshold
        self.mp_hands = mp.solutions.hands
        self.mp_face_mesh = mp.solutions.face_mesh
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.face_mesh = self.mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    def calc_distance(self, p1, p2):
        return math.dist(p1, p2)

    def detect_touch(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        hand_results = self.hands.process(rgb_frame)
        face_results = self.face_mesh.process(rgb_frame)

        if not hand_results.multi_hand_landmarks or not face_results.multi_face_landmarks:
            return frame, False

        h, w, _ = frame.shape
        touched = False

        target_ids = [13, 14, 1, 152]  # Mouth, Nose, Chest approx

        for face_landmarks in face_results.multi_face_landmarks:
            for hand_landmarks in hand_results.multi_hand_landmarks:
                for target_id in target_ids:
                    target = face_landmarks.landmark[target_id]
                    tx, ty = int(target.x * w), int(target.y * h)

                    for hl in hand_landmarks.landmark:
                        hx, hy = int(hl.x * w), int(hl.y * h)
                        dist = self.calc_distance((tx, ty), (hx, hy)) / w

                        if dist < self.distance_threshold:
                            touched = True
                            cv2.putText(frame, " BAD TOUCH DETECTED!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                                        1, (0, 0, 255), 2)
                            break

        return frame, touched
