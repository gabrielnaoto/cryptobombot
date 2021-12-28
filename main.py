import pyautogui

# This is the base script to locate and click a image in the screen
location = pyautogui.locateOnScreen('image.png', confidence=0.75)
point = pyautogui.center(location)
x, y = point
pyautogui.click(x, y)
