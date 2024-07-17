#!/usr/bin/env python
import pyperclip
import time
import pykakasi


def get_clipboard_data():
    """Get the current clipboard data."""
    return pyperclip.paste()


kks = pykakasi.kakasi()


def main():
    previous_clipboard_data = get_clipboard_data()

    while True:
        current_clipboard_data = get_clipboard_data()

        if current_clipboard_data != previous_clipboard_data:
            result = kks.convert(current_clipboard_data)
            for item in result:
                if item["orig"] != item["hira"]:
                    print(f"""{item["orig"]}  {item["hira"]}""")
            print()
            previous_clipboard_data = current_clipboard_data

        time.sleep(1)  # Adjust the sleep duration based on your preference


if __name__ == "__main__":
    main()