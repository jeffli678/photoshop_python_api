# Import local modules
from photoshop_python_api.basic_option import BasicOption
from photoshop_python_api.core import Core


class PhotoshopSaveOptions(BasicOption, Core):
    object_name = 'PhotoshopSaveOptions'

    def __int__(self):
        super(PhotoshopSaveOptions, self).__init__()
        # If true, the alpha channels are saved.
        self.AlphaChannels = False
        # If true, the annotations are save
        self.AnnotationsProperty = False
        self.Layers = True
