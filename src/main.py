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
    if layout != 1033:
        win32api.LoadKeyboardLayout(str(layout), 0) 

print("All configured keyboard languages unloaded!")

import winreg

def remove_keyboard_layout(layout_id):
    # Open the keyboard layouts key
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Keyboard Layout\\Preload", 0, winreg.KEY_ALL_ACCESS)

    try:
        i = 0
        while True:
            # Enumerate the values
            value_name, value_data, _ = winreg.EnumValue(key, i)

            # If the value data matches the layout ID, delete the value
            if value_data == layout_id:
                winreg.DeleteValue(key, value_name)
                print(f"Removed keyboard layout {layout_id}")

            i += 1
    except WindowsError:
        # No more values to enumerate
        pass

    # Close the key
    winreg.CloseKey(key)

# Remove the Latvian keyboard layout
remove_keyboard_layout("00000409")