from photoshop_python_api import Application
from photoshop_python_api import JPEGSaveOptions
from photoshop_python_api.solid_color import SolidColor

app = Application()
app.documents.add(800, 500, 72, "Hello-World")
doc = app.document
new_doc = doc.artLayers.add()
textColor = SolidColor()
textColor.RGB.Red = 225
textColor.RGB.Green = 0
textColor.RGB.Blue = 0
newTextLayer = new_doc
newTextLayer.Kind = 2
newTextLayer.TextItem.Contents = "Hello, World!"
newTextLayer.TextItem.Position = [160, 167]
newTextLayer.TextItem.Size = 36
newTextLayer.TextItem.Color = textColor.option
options = JPEGSaveOptions()
# # save to jpg
jpg = 'c:/hello_world.jpg'
doc.save_as(jpg, options, as_copy=True)
app.eval_javascript('alert("save to jpg: {}")'.format(jpg))
