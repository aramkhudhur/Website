"""
AI Slide Pilot
--------------
Listens to your microphone and moves slideshow slides using voice commands.

Supported commands:
- next slide / next / move on / continue  -> Right Arrow key
- previous slide / go back                -> Left Arrow key
"""

import sys
import time

import pyautogui
import speech_recognition as sr


# Command phrases the program should understand.
NEXT_COMMANDS = {"next slide", "next", "move on", "continue"}
PREVIOUS_COMMANDS = {"previous slide", "go back"}

# Cooldown in seconds to avoid accidental multiple key presses.
COOLDOWN_SECONDS = 2


def classify_command(text: str) -> str | None:
    """Return "next", "previous", or None based on recognized text."""
    normalized = text.lower().strip()

    # Exact phrase match first (most reliable and beginner-friendly).
    if normalized in NEXT_COMMANDS:
        return "next"
    if normalized in PREVIOUS_COMMANDS:
        return "previous"

    # Fallback contains-match for slightly longer phrases,
    # e.g. "okay next slide please".
    if any(phrase in normalized for phrase in NEXT_COMMANDS):
        return "next"
    if any(phrase in normalized for phrase in PREVIOUS_COMMANDS):
        return "previous"

    return None


def main() -> None:
    recognizer = sr.Recognizer()
    last_action_time = 0.0

    print("AI Slide Pilot is starting...")
    print("Listening for commands: next slide, next, move on, continue, previous slide, go back")
    print("Press Ctrl + C to stop.\n")

    # Try to open the default microphone and fail gracefully if unavailable.
    try:
        mic = sr.Microphone()
    except OSError:
        print("Error: No microphone was detected. Please connect a microphone and try again.")
        sys.exit(1)
    except Exception as exc:
        print(f"Error initializing microphone: {exc}")
        sys.exit(1)

    with mic as source:
        # Reduce impact of constant background noise.
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Microphone ready. Start speaking...\n")

        while True:
            try:
                # Listen to one speech chunk.
                audio = recognizer.listen(source, phrase_time_limit=4)

                # Convert speech to text using Google Web Speech API.
                # (No direct Google Slides API control is used.)
                heard_text = recognizer.recognize_google(audio)
                print(f"Detected: {heard_text}")

                command = classify_command(heard_text)
                if command is None:
                    continue

                # Enforce cooldown to prevent rapid accidental skips.
                now = time.time()
                if now - last_action_time < COOLDOWN_SECONDS:
                    print("Cooldown active: ignoring command to avoid accidental multiple slide changes.")
                    continue

                if command == "next":
                    print("Moving to next slide")
                    pyautogui.press("right")
                elif command == "previous":
                    print("Moving to previous slide")
                    pyautogui.press("left")

                last_action_time = now

            except sr.UnknownValueError:
                # Speech was heard but not understood.
                print("Detected: [unrecognized speech]")
            except sr.RequestError as exc:
                # Network/API issue while converting speech to text.
                print(f"Speech recognition service error: {exc}")
                print("Check your internet connection and try again.")
            except KeyboardInterrupt:
                print("\nStopping AI Slide Pilot. Goodbye!")
                break
            except Exception as exc:
                # Catch-all so the app keeps running if one loop fails.
                print(f"Unexpected error: {exc}")


if __name__ == "__main__":
    main()
