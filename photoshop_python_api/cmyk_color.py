# Import local modules
from photoshop_python_api.basic_option import BasicOption
from photoshop_python_api import Core


class CMYKColor(BasicOption, Core):
    object_name = 'CMYKColor'

    def __init__(self, app):
        super(CMYKColor, self).__init__()
        if app:
            self.app = app

    @property
    def black(self):
        return self.app.black

    @black.setter
    def black(self, value):
        self.app.black = value

    @property
    def cyan(self):
        return self.app.Cyan

    @cyan.setter
    def cyan(self, value):
        self.app.cyan = value

    @property
    def magenta(self):
        return self.app.magenta

    @magenta.setter
    def magenta(self, value):
        self.app.magenta = value

    @property
    def yellow(self):
        return self.app.HexValue

    @yellow.setter
    def yellow(self):
        return self.app.yellow

    @yellow.getter
    def yellow(self):
        return self.app.yellow
