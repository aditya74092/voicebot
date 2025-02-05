import speech_recognition as sr
from voicebot.screen_analyzer import ScreenAnalyzer # Import ScreenAnalyzer from the same package

import pyautogui
import time
import re

class VoiceBot:
    def __init__(self):
        self.last_action = None  # Store last command
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.analyzer = ScreenAnalyzer()

    def listen(self):
        """Listens for voice commands and converts them to text."""
        with self.mic as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
            audio = self.recognizer.listen(source, phrase_time_limit=5)
        
        try:
            return self.recognizer.recognize_google(audio).lower()
        except:
            return ""

    def parse_command(self, command):
        """Understands natural language commands and extracts intent."""
        actions = []

        if "click" in command:
            match = re.search(r"click on (.*?)$", command)
            if match:
                actions.append(("click", match.group(1)))
        
        if "scroll down" in command:
            times = self.extract_number(command) or 1
            actions.append(("scroll", -500 * times))
        elif "scroll up" in command:
            times = self.extract_number(command) or 1
            actions.append(("scroll", 500 * times))

        if "switch to" in command:
            match = re.search(r"switch to (.*?)$", command)
            if match:
                actions.append(("switch", match.group(1)))

        return actions

    def extract_number(self, command):
        """Extracts a number from a spoken command (e.g., 'scroll down 3 times')."""
        match = re.search(r"(\d+)", command)
        return int(match.group(1)) if match else None

    def execute_command(self, command):
        """Executes parsed voice commands with intelligent logic."""
        actions = self.parse_command(command)

        for action, target in actions:
            if action == "click":
                coords = self.analyzer.find_element(target)
                if coords:
                    pyautogui.moveTo(*coords)
                    pyautogui.click()
                    print(f"Clicked on {target} at {coords}")
                else:
                    print(f"Could not find {target}")

            elif action == "scroll":
                pyautogui.scroll(target)

            elif action == "switch":
                if self.analyzer.switch_to_window(target):
                    print(f"Switched to {target}")
                else:
                    print(f"Could not switch to {target}")

        self.last_action = command

def main():
    bot = VoiceBot()
    while True:
        command = bot.listen()
        if command:
            print(f"Executing: {command}")
            bot.execute_command(command())

if __name__ == "__main__":
    main()

