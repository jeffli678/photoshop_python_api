from photoshop_python_api import Document
from photoshop_python_api import SolidColor


def create_color_text():
    doc = Document()
    doc_ref = doc.artLayers
    text_color = SolidColor()
    text_color.cmyk.cyan = 225
    text_color.cmyk.magenta = 0
    text_color.cmyk.blue = 1
    new_text_layer = doc_ref.add()
    ps_text_layer = 2  # from enum PsLayerKind
    new_text_layer.kind = ps_text_layer
    new_text_layer.textItem.Contents = "Hello, World!"
    new_text_layer.textItem.Position = [160, 167]
    new_text_layer.textItem.Size = 36
    new_text_layer.textItem.Color = text_color.option


if __name__ == '__main__':
    create_color_text()
