import pyxel
from const import Color


class App:
    def __init__(self):
        pyxel.init(255, 255)
        pyxel.cls(Color.PEACH)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pass


App()
