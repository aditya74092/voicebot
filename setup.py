from setuptools import setup, find_packages

setup(
    name="voicebot",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "speechrecognition",
        "pyautogui",
        "opencv-python",
        "numpy",
        "pytesseract",
        "appscript",
        "easyocr",
        "torch",
        "ultralytics"
    ],
    entry_points={
        'console_scripts': [
            'voicebot = voicebot.voice_bot:main',
        ],
    },

    author="Aditya Chowdhary",
    description="An AI-powered voice-controlled UI automation bot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS",
    ],
)

