# Import local modules
from photoshop_python_api.core import Core


class Layer(Core):
    def __init__(self):
        super(Layer, self).__init__()

    @property
    def activeLayer(self):
        return self.adobe.activeDocument.activeLayer

    @property
    def allLocked(self):
        return self.activeLayer.allLocked

    @property
    def blendMode(self):
        return self.activeLayer.blendMode

    @property
    def bounds(self):
        return self.activeLayer.bounds

    @property
    def boundsNoEffects(self):
        return self.activeLayer.boundsNoEffects
