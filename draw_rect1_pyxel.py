import pyxel
from const import Color


class App:
    def __init__(self):
        pyxel.init(255, 255)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(Color.PEACH)

        # Red:Rectangle(fill)

        # Red:Rectangle(line weight 3)

        # Green:Rectangle

        # Blue:Rectangle,Rect Object

        # Yellow:Rectangle,Rect Object

        pass


App()
