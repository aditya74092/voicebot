import pyautogui
import cv2
import numpy as np
import pytesseract
from appscript import app
import easyocr
import torch
from ultralytics import YOLO

class ScreenAnalyzer:
    def __init__(self):
        # Load YOLOv8 Model (Pre-trained for UI detection)
        self.model = YOLO("yolov8n.pt")  # Change to a UI-specific model if available
        self.ocr_reader = easyocr.Reader(['en'])  # English OCR

    def capture_screen(self):
        """Captures the screen and preprocesses it for AI detection."""
        screenshot = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Resize for better detection
        scale_percent = 150
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        img = cv2.resize(img, (width, height))

        return img

    def detect_ui_elements(self):
        """Detects UI elements dynamically using AI."""
        img = self.capture_screen()
        results = self.model(img)
        
        detected_elements = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
                label = result.names[int(box.cls)]  # Class name
                confidence = box.conf[0].item()  # Confidence score
                
                detected_elements.append({
                    "label": label,
                    "coords": (x1, y1, x2, y2),
                    "confidence": confidence
                })

        return detected_elements

    def find_element(self, target_name):
        """Finds a UI element by name using Accessibility API or OCR."""
        if element := self._find_via_accessibility(target_name):
            return element
        
        return self._find_via_ocr(target_name)

    def _find_via_accessibility(self, target_name):
        """Uses macOS Accessibility API to find UI elements."""
        system_events = app('System Events')
        try:
            for process in system_events.processes.get():
                for window in process.windows.get():
                    for ui_element in window.UI_elements.get():
                        if target_name.lower() in ui_element.name.get().lower():
                            position = ui_element.position.get()
                            return (position[0], position[1])
        except Exception as e:
            print(f"Accessibility API error: {e}")
        return None

    def _find_via_ocr(self, target_name):
        """Uses OCR to find UI elements with text labels."""
        img = self.capture_screen()
        results = self.ocr_reader.readtext(img)

        for (bbox, text, prob) in results:
            if target_name.lower() in text.lower():
                x1, y1, x2, y2 = bbox[0][0], bbox[0][1], bbox[2][0], bbox[2][1]
                return (x1 + x2) // 2, (y1 + y2) // 2  

        return None  

    def switch_to_window(self, app_name):
        """Switches to a specific application window."""
        system_events = app('System Events')
        try:
            system_events.processes[app_name].frontmost.set(True)
            return True
        except:
            return False
