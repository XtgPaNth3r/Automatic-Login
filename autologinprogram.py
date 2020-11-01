import pyautogui
import time
username = ''
passw = ''

class coords:
    usernamearea = (coord)
    passwordarea = (coord)
    loginbtn = (coord)

time.sleep(5)
pyautogui.click(coords.usernamearea)
pyautogui.typewrite(username)
pyautogui.click(coords.passwordarea)
pyautogui.typewrite(passw)
pyautogui.click(loginbtn)

'''
repeat this code for the amount of areas to fill in
pyautogui.click(coords.newvar)
pyautogui.typewrite(newvarcoords)
'''
