# Import local modules
from photoshop_python_api.core import Core
from photoshop_python_api.basic_option import BasicOption


class PDFSaveOptions(BasicOption, Core):
    object_name = 'PDFSaveOptions'

    def __init__(self):
        super(PDFSaveOptions, self).__init__()


