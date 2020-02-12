photoshop_python_api
====================
The API for using COM objects and interfaces of photoshop.

More information about Component Object Model (COM):
https://docs.microsoft.com/en-us/windows/desktop/com/component-object-model--com--portal


https://photoshop-python-api.readthedocs.io

Official javascript API docs:
http://wwwimages.adobe.com/www.adobe.com/content/dam/acom/en/devnet/photoshop/pdfs/photoshop-cc-javascript-ref-2015.pdf

Photoshop Scripting Reference:
https://theiviaxx.github.io/photoshop-docs/Photoshop/index.html

Has been tested and used Photoshop version:
    - cc2020
    - cc2019
    - cc2018
    - cc2017
    - cs6

install
-------
Clone from github.
```cmd
git clone https://github.com/loonghao/photoshop_python_api.git
```
Install package.
```cmd
python setup.py install
```

Hello World
-----------

```python

from photoshop_python_api.application import Application
from photoshop_python_api.save_options import JPEGSaveOptions
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
```