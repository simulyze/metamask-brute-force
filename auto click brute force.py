import pyautogui
import keyboard
import time

# Function to wait for the right arrow key press or delete key press
def wait_for_right_arrow_or_delete():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'right':
                return True
            elif event.name == 'delete':
                return False

# Function to perform mouse click at given coordinates
def perform_click(x, y):
    pyautogui.click(x, y)

# Function to type given text
def perform_typing(text):
    pyautogui.typewrite(text)

# Function to scroll all the way down
def scroll_all_the_way_down():
    pyautogui.scroll(-10000)

# Function to press a key
def press_key(key):
    keyboard.press(key)
    keyboard.release(key)

# Function to move mouse cursor to given coordinates
def move_mouse(x, y):
    pyautogui.moveTo(x, y)

# Steps to be performed
steps = [
    lambda: move_mouse(960, 410),
    lambda: move_mouse(2495, 1260),
    (2873, 1831),
    "00000000",
    (2782, 1317),
    "00000000",
    (2776, 1464),
    (2799, 1629),
    (2867, 1469),
    (2890, 1554),
    (2890, 1554),
    (2888, 1061),
    (3465, 120),
    (3414, 388),
    (3307, 665),
    (3140, 436),
    (2915, 40),
    (3471, 490),
    (3023, 592),
    (2610, 1378),
    (2755, 1623),
    (2868, 1965),
    lambda: scroll_all_the_way_down()
]

# Main loop to perform steps
while True:  # Outer loop to restart from the first step
    for step in steps:
        if not wait_for_right_arrow_or_delete():  # Check if delete key was pressed
            break  # Exit the inner loop to restart from the first step
        if callable(step):
            step()  # Call the function if step is a function
        elif isinstance(step, tuple):
            perform_click(step[0], step[1])
        else:
            perform_typing(step)
