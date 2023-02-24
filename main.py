# import necessary libraries
from PIL import ImageGrab # for taking screenshots
import mouse # for simulating mouse movements and clicks
import keyboard # for detecting key presses
import win32api # for scrolling down
import time # for adding delays
import pyperclip # for copying and pasting text
import os # for using operating system functionalites
from pynput.mouse import Button, Controller as MouseController # for highlighting text using mouse
from pynput.keyboard import Key, Controller as KeyboardController # for simulating key presses
from datetime import datetime # for using the systems current time

def chooseOption():
    option = int(input("Option 1: Go to inventory and start on whatever page you would like.\nOption 2: Specifically select if you get asked for steam mobile confirmation.\nSelect(1 or 2): "))
    if option == 2:
        print("Before starting confirm that you have the marketable filter selected in the inventory.")
        return option
    elif option == 1:
        return option
    else:
        print("Option not available, try again.")
        chooseOption()

# asks user for their monitors resolution
# NOTE THIS WILL NOT WORK EXCEPT FOR THE SECOND OPTION
def resolutionOption():
    resolution = int(input("Option 1: 1080p\nOption 2: 2k (2560)\nOption 3: 4k (3840)\nSelect your monitor resolution: "))
    if resolution == 1:
        resolution_x = 1920
        resolution_y = 1080
        return resolution_x, resolution_y
    elif resolution == 2:
        resolution_x = 2560
        resolution_y = 1440
        return resolution_x, resolution_y
    elif resolution == 3:
        resolution_x = 3840
        resolution_y = 2160
        return resolution_x, resolution_y
    else:
        print("Option not available, try again.")
        resolutionOption()

def find_pixel(color, x_start, y_start, x_end, y_end, scroll_amount, resolution_x, resolution_y):
    while True:
        screenshot = ImageGrab.grab(bbox=(0, 0, resolution_x, resolution_y)) # take a screenshot
        found = False
        # checks every x-axis pixel for every y-axis pixel (left-right/top-down)
        for y in range(y_start, y_end):
            for x in range(x_start, x_end):
                pixel = screenshot.getpixel((x, y))
                if pixel == color: # if the color is found
                    print(f"Pixel with color {color} found at ({x}, {y})")
                    mouse.move(x, y) 
                    found = True
                    break
            if found:
                break
        if found:
            return x, y
        else:
            # scroll by the specified amount
            win32api.mouse_event(0x0800, 0, 0, scroll_amount, 0) # simulate scrolling
            time.sleep(0.5)

# variables
items = []
times = []
option = chooseOption()
resolution_x, resolution_y = resolutionOption()
x_iterations = 0
y_iterations = 0

input("Press enter to begin the script...")
print("Starting Script")
print("")

# Get the current date and time and format it as string
fileTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# Used to get the current directory and full file path to generate the text log
filename = f"output_{fileTime}.txt"
filepath = os.path.join(os.getcwd(), filename)

# creates log file including the current time
with open(filepath, 'w') as file:
    file.write(f"Script starting at {fileTime}\n----------------------------------------------------------------------------------------------------------------------------------------\n")
    
    # continue running the loop until the 'q' key is pressed
    while not keyboard.is_pressed('q'):
        print("(Hold q to end)")
        
        if option == 1:
            # loop through the screen and check if it matches the color
            x, y = find_pixel((94, 94, 94), 1280, 0, 2560, 1440, 100, resolution_x, resolution_y)

            mouse = MouseController()
            mouse.position = (x, y)
            time.sleep(0.1)
            mouse.click(Button.left)
            time.sleep(0.5)
            mouse.position = (x - 120, y + 65)
            time.sleep(0.1)
            mouse.click(Button.left)
            time.sleep(0.1)
            mouse.position = (x - 700, y + 300)
            time.sleep(0.2)
            mouse.click(Button.left)
            time.sleep(0.5)
            
            x, y = find_pixel((94, 133, 43), 1280, 0, 2560, 1420, -100, resolution_x, resolution_y)
        else:
            x, y = find_pixel((94, 94, 94), 1280, 0, 2560, 1440, 100, resolution_x, resolution_y)
            mouse = MouseController()
            mouse.position = ((x - 700) + (100 * x_iterations), (y + 300) + (100 * y_iterations))
            time.sleep(0.2)
            mouse.click(Button.left)
            time.sleep(0.5)
            
        x, y = find_pixel((94, 133, 43), 1280, 0, 2560, 1420, -100, resolution_x, resolution_y)
        mouse = MouseController()
        mouse.position = (x, y)

        # highlight the text by dragging the mouse
        mouse.position = (x + 85, y - 65)
        mouse.press(Button.left)
        for i in range(40):
            mouse.move(1, 0) 
            time.sleep(0.01) 
        mouse.release(Button.left) 

        # copy sell amount
        keyboard_controller = KeyboardController()
        keyboard_controller.press(Key.ctrl)
        keyboard_controller.press('c')
        keyboard_controller.release('c')
        keyboard_controller.release(Key.ctrl)
        time.sleep(0.1)
        
        clipboard_text = pyperclip.paste() # get the text from clipboard
        print(f"Copied {clipboard_text}")
        price = clipboard_text 

        # move the mouse back to the original position and click it
        mouse.position = (x, y) 
        mouse.click(Button.left)

        # paste the sell amount
        mouse.position = (1415, 879) 
        time.sleep(1)
        mouse.click(Button.left) 
        keyboard_controller.press(Key.backspace)
        keyboard_controller.release(Key.backspace)
        keyboard_controller.press(Key.ctrl)
        keyboard_controller.press('v')
        keyboard_controller.release('v')
        keyboard_controller.release(Key.ctrl)

        # highlight item name
        mouse.position = (1005, 526)
        mouse.press(Button.left)
        for i in range(50):
            mouse.move(8, 0)
            time.sleep(0.001)
        mouse.release(Button.left)

        # copy item name
        keyboard_controller.press(Key.ctrl)
        keyboard_controller.press('c')
        keyboard_controller.release('c')
        keyboard_controller.release(Key.ctrl)
        time.sleep(0.1)

        # get the text from the clipboard and assign it to a variable
        clipboard_text = pyperclip.paste()
        print(f"Copied {clipboard_text}")
        item = clipboard_text

        # move to a determined position and click the mouse
        screenshot = ImageGrab.grab()
        mouse.position = (900, 920)
        time.sleep(0.5)
        x, y = mouse.position
        
        # Checks if Steam Subscriber Agreement is checked
        pixel_color = screenshot.getpixel((x, y))
        color = (0, 117, 255)
        if pixel_color != color:
            time.sleep(0.2)
            mouse.click(Button.left)
            print("Checked terms of Steam Subscriber Agreement")
        else:
            print("Terms of Steam Subscriber Agreement already checked")

        time.sleep(0.1)
        mouse.position = (1560, 962)
        time.sleep(0.1)
        mouse.click(Button.left)
        time.sleep(0.5)
        mouse.position = (1600, 865)
        time.sleep(0.1)
        mouse.click(Button.left)

        # steam mobile authentication popup
        if option == 2:
            time.sleep(0.5)
            mouse.position = (1900, 770)
            time.sleep(1)
            mouse.click(Button.left)
            print("Steam Mobile Verification Required")

        # print out the item and its price
        print(f"Now selling {item} for {price}")
        print("")
        current_time = datetime.now().strftime("%H:%M:%S")
        times.append(current_time)
        items.append({"item": item, "price": price})
        time.sleep(2)
        
        # Looping through all 25 items on each page
        x_iterations += 1
        if x_iterations == 5:
            x_iterations = 0
            y_iterations += 1
        if y_iterations == 5:
            y_iterations = 0
            x, y = find_pixel((94, 94, 94), 1280, 0, 2560, 1440, 100, resolution_x, resolution_y)
            mouse.position = (x - 250 , y + 775)
            time.sleep(0.5)
            mouse.click(Button.left)
            time.sleep(1)

    print("")
    print("List of all items and prices.")
    time.sleep(2)

    # prints results in command prompt

    num = 0
    for item in items:
        time = times[num]
        output = f"{time} #{num}| {item['item']} is being sold for {item['price']}\n"
        print(output)
        file.write(output)
        num += 1

input("Press enter to exit...")
