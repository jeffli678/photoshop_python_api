# Import local modules
from photoshop_python_api.core import Core
from photoshop_python_api.document import Document
from photoshop_python_api.solid_color import SolidColor
from photoshop_python_api.basic_option import BasicOption
from photoshop_python_api.application import Application
from photoshop_python_api.save_options import GIFSaveOptions
from photoshop_python_api.save_options import JPEGSaveOptions
from photoshop_python_api.save_options import PNGSaveOptions
from photoshop_python_api.save_options import PDFSaveOptions
from photoshop_python_api.save_options import ExportOptionsSaveForWeb
from photoshop_python_api.save_options import PhotoshopSaveOptions
from photoshop_python_api.save_options import TiffSaveOptions

# All public api.
__all__ = [
    "Core",
    "BasicOption",
    "Document",
    "SolidColor",
    "Application",
    "JPEGSaveOptions",
    "GIFSaveOptions",
    "PhotoshopSaveOptions",
    "ExportOptionsSaveForWeb",
    "TiffSaveOptions",
    "PDFSaveOptions",
    "PNGSaveOptions"

]
__title__ = 'photoshop_python_api'
__version__ = '0.2.0'
__author__ = 'Long Hao'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018 Long Hao'
