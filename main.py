import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

class EyeControlledMouse:
    def __init__(self):
        # Initialize MediaPipe Face Mesh
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        # Initialize drawing utilities
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

        # Get screen dimensions
        self.screen_width, self.screen_height = pyautogui.size()


        # Smoothing parameters
        self.smooth_factor = 0.5  
        self.prev_x, self.prev_y = 0, 0
        
        # Sensitivity multipliers
        self.horizontal_sensitivity = 1.5
        self.vertical_sensitivity = 2.2 
        
        # Blink detection parameters
        self.blink_threshold = 0.21
        self.blink_counter = 0
        self.click_cooldown = 0
        
        # Eye landmarks indices (MediaPipe face mesh)
        self.left_eye = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
        self.right_eye = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
        
        # Iris landmarks
        self.left_iris = [474, 475, 476, 477]
        self.right_iris = [469, 470, 471, 472]
        
        # Calibration parameters
        self.calibrated = False
        self.eye_region_left = None
        self.eye_region_right = None

        def get_eye_aspect_ratio(self, eye_landmarks):
       
        # Vertical eye landmarks
        A = np.linalg.norm(eye_landmarks[1] - eye_landmarks[5])
        B = np.linalg.norm(eye_landmarks[2] - eye_landmarks[4])
        
        # Horizontal eye landmark
        C = np.linalg.norm(eye_landmarks[0] - eye_landmarks[3])
        
        # Eye Aspect Ratio
        ear = (A + B) / (2.0 * C)
        return ear
        
