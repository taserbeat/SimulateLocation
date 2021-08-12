-- load env
set XCODE_SIMULOC_MENU_NAME to system attribute "XCODE_SIMULOC_MENU_NAME"

-- click simulac on XCode
tell application "System Events" to tell process "Xcode"
		click menu item XCODE_SIMULOC_MENU_NAME of menu 1 of menu item "Simulate Location" of menu 1 of menu bar item "Debug" of menu bar 1
end tell
