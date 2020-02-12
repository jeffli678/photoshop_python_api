from photoshop_python_api import Application
from photoshop_python_api import JPEGSaveOptions
from photoshop_python_api import SolidColor


def hello_world():
    app = Application()
    app.documents.add(800, 500, 72, "Hello-World")
    doc = app.document
    new_doc = doc.artLayers.add()
    text_color = SolidColor()
    text_color.RGB.Red = 225
    text_color.RGB.Green = 0
    text_color.RGB.Blue = 0
    new_text_layer = new_doc
    new_text_layer.Kind = 2
    new_text_layer.TextItem.Contents = "Hello, World!"
    new_text_layer.TextItem.Position = [160, 167]
    new_text_layer.TextItem.Size = 36
    new_text_layer.TextItem.Color = text_color.option
    options = JPEGSaveOptions()
    # # save to jpg
    jpg = 'c:/hello_world.jpg'
    doc.saveAs(jpg, options, as_copy=True)
    app.eval_javascript('alert("save to jpg: {}")'.format(jpg))


if __name__ == '__main__':
    hello_world()
