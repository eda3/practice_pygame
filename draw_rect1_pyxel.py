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
        pyxel.rect(10, 20, 120, 70, Color.RED)

        # Red:Rectangle(line weight 3)
        pyxel.rectb(150, 10, 250, 40, Color.RED)

        # Green:Rectangle
        pyxel.rect(100, 80, 180, 130, Color.LIME_GREEN)

        # Blue:Rectangle,Rect Object
        pyxel.rect(200, 60, 340, 120, Color.SYAN_BLUE)

        # Yellow:Rectangle,Rect Object
        pyxel.rect(30, 160, 130, 210, Color.YELLOW)

        pass


App()
