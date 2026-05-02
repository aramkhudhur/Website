# AI Slide Pilot (Python Prototype)

AI Slide Pilot is a simple Python program that listens to your voice and controls slides by pressing keyboard arrows.

It **does not** use a browser extension and **does not** use Google Slides API for live control.
It works by sending keyboard key presses, so it can control:
- Google Slides (presentation mode)
- Microsoft PowerPoint (slideshow mode)
- Canva presentations (presentation mode)
- Any other slideshow that uses left/right arrow keys

## Features
- Real-time microphone listening
- Speech-to-text using `SpeechRecognition`
- Command detection for:
  - `next slide`
  - `next`
  - `move on`
  - `continue`
  - `previous slide`
  - `go back`
- Presses:
  - Right Arrow for next slide
  - Left Arrow for previous slide
- 2-second cooldown to avoid accidental multi-skip
- Prints detected speech and actions in terminal
- Beginner-friendly, commented Python code

## Requirements
- Windows 10 or 11
- Python 3.9+ (Python 3 required)
- Microphone
- Internet connection (used by the default Google speech recognition backend)

## Installation (Windows)

1. **Install Python 3**
   - Download from: https://www.python.org/downloads/
   - During setup, check **"Add Python to PATH"**.

2. **Open Command Prompt** in the project folder.

3. **(Recommended) Create and activate a virtual environment:**
   ```bat
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bat
   pip install SpeechRecognition pyautogui pyaudio
   ```

   If `pyaudio` fails to install on your machine, try:
   ```bat
   pip install pipwin
   pipwin install pyaudio
   ```

## Run

```bat
python ai_slide_pilot.py
```

## How to use

1. Open your slideshow in **presentation mode** (Google Slides / PowerPoint / Canva).
2. Click the slideshow window so it is focused.
3. Run `ai_slide_pilot.py` in terminal.
4. Say commands like:
   - "next slide" (moves right)
   - "go back" (moves left)

## Example terminal output

```text
Detected: next slide
Moving to next slide
Detected: go back
Moving to previous slide
```

## Notes
- Keep your microphone close and speak clearly.
- There is a built-in 2-second cooldown to prevent accidental repeated slide changes.
- Press `Ctrl + C` in terminal to stop the program.
