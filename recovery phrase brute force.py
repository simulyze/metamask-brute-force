import pyautogui
import keyboard
import time
import sys
import tkinter as tk
import random
import pyperclip
import threading

def get_coordinates():
    print("Move your mouse to the desired location and press the 'left arrow' key to capture the coordinates...")
    keyboard.wait('left arrow')
    x, y = pyautogui.position()
    print("First coordinates captured:", x, y)
    print("Move your mouse to the second desired location and press the 'left arrow' key again to capture the coordinates...")
    keyboard.wait('left arrow')
    x2, y2 = pyautogui.position()
    print("Second coordinates captured:", x2, y2)
    return x, y, x2, y2

def main():
    print("Press INSERT key to start the automation.")
    print("Press END key to stop the automation.")

    automation_running = False

    while True:
        if keyboard.is_pressed('insert') and not automation_running:
            print("Automation started.")
            x, y, x2, y2 = get_coordinates()
            automation_running = True

        while automation_running:
            # Perform the sequence of actions
            pyautogui.click(x=x, y=y)
            pyautogui.doubleClick(x=x2, y=y2)
            pyautogui.hotkey('ctrl', 'v')  # Auto paste
            time.sleep(0.7)  # Add a small delay

            # Check if END key is pressed to stop the automation
            if keyboard.is_pressed('end'):
                print("Automation stopped.")
                automation_running = False

        # Add a one-second delay after restarting the automation
        time.sleep(0)

def select_random_words(file_path):
    try:
        # Read words from the text file
        with open(file_path, "r") as file:
            words = file.read().split()
        
        # Check if there are enough words
        if len(words) < 12:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Please add more words to the file.")
            return
        
        # Select 12 random words from the list
        random_words = random.sample(words, 12)
        
        # Display the selected random words
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "12 Random words:\n" + "\n".join(random_words))
        
        # Copy the generated words to the clipboard
        pyperclip.copy("\n".join(random_words))
    except FileNotFoundError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "File not found. Please make sure the file exists.")

# Create a Tkinter window
window = tk.Tk()
window.title("Random Word Generator")

# Define the path to the document
file_path = r"C:\Users\codys\OneDrive\Desktop\seed phrase random word generator.txt"

# Create a text widget to display the result
result_text = tk.Text(window, height=10, width=40)
result_text.pack(pady=10)

# Create a button to generate random words
generate_button = tk.Button(window, text="Generate Words", command=lambda: select_random_words(file_path))
generate_button.pack(pady=5)

# Start the main function in a separate thread
automation_thread = threading.Thread(target=main)
automation_thread.start()

# Run the Tkinter event loop
window.mainloop()
