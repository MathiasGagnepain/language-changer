import win32api
from win32con import WM_INPUTLANGCHANGEREQUEST
from win32gui import GetForegroundWindow
from win32api import SendMessage

win32api.LoadKeyboardLayout('00000409',1) # to switch to english
win32api.LoadKeyboardLayout('00000426',1) # to switch to latvian

keyboardList = win32api.GetKeyboardLayoutList()
kayboardLayout = win32api.GetKeyboardLayoutName()  # win32api.GetKeyboardLayout(0) # to get the current keyboard layout
print(kayboardLayout)
print(keyboardList)

if SendMessage( GetForegroundWindow(), WM_INPUTLANGCHANGEREQUEST, 0, 0x4260426) == 0:
    print('Keyboard layout changed!')

for layout in keyboardList:
    if layout != 1033:  # 1033 is the decimal equivalent of 00000409
        win32api.LoadKeyboardLayout(str(layout), 0) 

print("All configured keyboard languages unloaded!")
