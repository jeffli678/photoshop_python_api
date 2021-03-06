from photoshop._core import Photoshop
from photoshop.artlayer import ArtLayer
from photoshop.layer import Layer

class ArtLayers(Photoshop):

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def _layers(self):
        return [layer for layer in self.app]

    def __len__(self):
        return self.length

    @property
    def length(self):
        return len(self._layers)

    @property
    def parent(self):
        return self.app.parent

    @property
    def typename(self):
        return self.app.typename

    def add(self):
        """Adds an element."""
        return Layer(self.app.add())

    def getByName(self, name):
        return self.app.getByName(name)

    def removeAll(self):
        return self.app.removeAll()

    def link(self, layer):
        self.app.link(layer)
