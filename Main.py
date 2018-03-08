from GUITools import *
from updatedGraphics import *

print("hello how're you?")
win = GraphWin("Window", 500, 500)
master = win
button(master, text="Test", command="print(\"hi\")", height=50, width=50)
win.getMouse()
