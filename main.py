# import necessary libraries
from PIL import ImageGrab # for taking screenshots
import mouse # for simulating mouse movements and clicks
import keyboard # for detecting key presses
import win32api # for scrolling down
import time # for adding delays
import pyperclip # for copying and pasting text
from pynput.mouse import Button, Controller as MouseController # for highlighting text using mouse
from pynput.keyboard import Key, Controller as KeyboardController # for simulating key presses

items = []

input("Press enter to begin the script...")
print("Starting Script")
print("")

# continue running the loop until the 'q' key is pressed
while not keyboard.is_pressed('q'):
    print("(Hold q to end)")
    # define the color to be detected in RGB format
    

    # loop through the screen and check if it matches the color
    while True:
        color = (94, 94, 94)
        screenshot = ImageGrab.grab() # take a screenshot
        found = False
        for x in range(screenshot.width):
            for y in range(screenshot.height-20):
                pixel = screenshot.getpixel((x, y))
                if pixel == color: # if the color is found
                    print(f"Pixel with color {color} found at ({x}, {y})")
                    mouse.move(x, y) 
                    found = True
                    break
            if found:
                break

        if found:
            break
        else:
            # scroll down by 100 pixels
            win32api.mouse_event(0x0800, 0, 0, 100, 0) # simulate scrolling down
            time.sleep(0.5)

    mouse = MouseController()
    mouse.position = (x, y)
    time.sleep(0.1)
    mouse.click(Button.left)
    time.sleep(0.5)
    mouse.position = (x - 110, y + 65)
    time.sleep(0.1)
    mouse.click(Button.left)
    time.sleep(0.1)
    mouse.position = (x - 700, y + 300)
    time.sleep(0.2)
    mouse.click(Button.left)
    time.sleep(0.5)
    
    while True:
        color = (94, 133, 43)
        screenshot = ImageGrab.grab() # take a screenshot
        found = False
        for x in range(screenshot.width):
            for y in range(screenshot.height):
                pixel = screenshot.getpixel((x, y))
                if pixel == color: # if the color is found
                    print(f"Pixel with color {color} found at ({x}, {y})")
                    mouse.move(x, y) 
                    found = True
                    break
            if found:
                break

        if found:
            break
        else:
            # scroll down by 100 pixels
            win32api.mouse_event(0x0800, 0, 0, -100, 0) # simulate scrolling down
            time.sleep(0.5)

    # highlight the text by dragging the mouse
    
    mouse.position = (x + 85, y - 65) 
    mouse.press(Button.left) 
    # move the mouse to the right in small steps
    for i in range(40):
        mouse.move(1, 0) 
        time.sleep(0.01) 
    mouse.release(Button.left) 

    # simulate pressing Control + V to paste the highlighted text
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

    # move to a determined position, press the delete key and paste the copied text
    mouse.position = (1415, 879) 
    time.sleep(1)
    mouse.click(Button.left) 
    keyboard_controller.press(Key.backspace)
    keyboard_controller.release(Key.backspace)
    keyboard_controller.press(Key.ctrl)
    keyboard_controller.press('v')
    keyboard_controller.release('v')
    keyboard_controller.release(Key.ctrl)

    # move the mouse to copy more text and paste it
    mouse.position = (1005, 526)
    mouse.press(Button.left)
    for i in range(50):
        mouse.move(8, 0)
        time.sleep(0.001)
    mouse.release(Button.left)

    # simulate keyboard shortcut to copy text to clipboard
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
    pixel_color = screenshot.getpixel((x, y))

    color = (0, 117, 255)

    if pixel_color != color:
        time.sleep(0.5)
        mouse.click(Button.left)
        print("Checked terms of Steam Subscriber Agreement")
    else:
        print("Terms of Steam Subscriber Agreement already checked")

    time.sleep(0.5)
    mouse.position = (1560, 962)
    time.sleep(0.1)
    mouse.click(Button.left)
    time.sleep(0.5)
    mouse.position = (1600, 865)
    time.sleep(0.1)
    mouse.click(Button.left)

    # print out the item and its price
    print(f"Now selling {item} for {price}")
    print("")
    items.append({"item": item, "price": price})
    time.sleep(3)

print("")
print("List of all items and prices.")
time.sleep(2)
num = 0
for item in items:
    num += 1
    print(f"{num}. {item['item']} is being sold for {item['price']}")
input("Press enter to exit...")
