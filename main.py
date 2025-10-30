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
