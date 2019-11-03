#! python3

import pyautogui, os

os.chdir('C:\\pythonScripts\\outlookauto')

# increase PAUSE if I need to open outlook and wait for splash screen
pyautogui.PAUSE = 0.5
iconLocation = pyautogui.locateOnScreen('01 outlookicon.PNG')
iconCentre = pyautogui.center(iconLocation)
pyautogui.click(iconCentre)

iconLocation = pyautogui.locateOnScreen('02 outlookfile.PNG')
iconCentre = pyautogui.center(iconLocation)
pyautogui.click(iconCentre)

# if Automatic Replies are already on, turn them off
try:
	pyautogui.PAUSE = 0.5
	iconLocation = pyautogui.locateOnScreen('06 off.PNG')
	iconCentre = pyautogui.center(iconLocation)
	pyautogui.click(iconCentre)

# if Automatic Replies are not already on, turn them on
except:
	pyautogui.PAUSE = 1
	iconLocation = pyautogui.locateOnScreen('03 autoreply.PNG')
	iconCentre = pyautogui.center(iconLocation)
	pyautogui.click(iconCentre)

	pyautogui.PAUSE = 0.5
	iconLocation = pyautogui.locateOnScreen('04 sendreplies.PNG')
	iconCentre = pyautogui.center(iconLocation)
	pyautogui.click(iconCentre)

	iconLocation = pyautogui.locateOnScreen('05 ok.PNG')
	iconCentre = pyautogui.center(iconLocation)
	pyautogui.click(iconCentre)
