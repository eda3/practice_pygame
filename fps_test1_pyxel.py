import pyxel


class App:
    __counter = 0

    def __init__(self):
        pyxel.init(255, 255)
        pyxel.cls(1)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.__counter += 1

    def draw(self):
        _color = 7
        _message = "count is {}".format(self.__counter)
        pyxel.text(50, 50, _message, _color)


App()
