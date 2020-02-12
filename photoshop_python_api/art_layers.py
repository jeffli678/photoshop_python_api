# Import local modules
from photoshop_python_api.core import Core


class ArtLayers(Core):
    def __init__(self):
        super(ArtLayers, self).__init__()

    @property
    def artLayers(self):
        return self.adobe.activeDocument.artLayers

    @property
    def length(self):
        return self.artLayers.length

    @property
    def parent(self):
        return self.artLayers.parent

    @property
    def typename(self):
        return self.artLayers.Typename

    def add(self):
        return self.artLayers.add()

    def get_by_name(self, name):
        return self.artLayers.getByName(name)

    def remove_all(self):
        return self.artLayers.removeAll()
