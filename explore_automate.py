import pyautogui

print(pyautogui.size())

# Display cursor position and RGB value
#pyautogui.displayMousePosition()

image = 'file_icon.png'
loc = pyautogui.locateOnScreen(image) #grayscale=True, , confidence=.5
print("file button location", loc)
target_x, target_y = center_of_box(loc)

pyautogui.moveTo(target_x, target_y, duration = 1)
print("above file")
pyautogui.click(target_x, target_y)
print("clicked")

'''
pyautogui.moveTo(100, 100, duration = 1)
pyautogui.click(100, 100)
pyautogui.typewrite("yoyoma !")
pyautogui.hotkey('ctrlleft', 's')
'''
