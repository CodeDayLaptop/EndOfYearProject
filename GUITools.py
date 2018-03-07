# Author: Andrew Moore
# A library with the purpose of simplifying the ability to add GUI objects. EX: Buttons


class button(object):
    def __init__(self, win):
        self.canvas = win

    def __str__(self):
        return "A button object"

    def pressed(self, mouseloc):
        if mouseloc.GetX() >= self.x1 and mouseloc.GetX() <= self.x2 \
                and mouseloc.GetY() <= self.Y1 and mouseloc.GetY() >= self.y2:
            pass
