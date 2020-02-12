photoshop_python_api
====================
The API for using COM objects and interfaces of photoshop.

More information about Component Object Model (COM):
https://docs.microsoft.com/en-us/windows/desktop/com/component-object-model--com--portal


https://photoshop-python-api.readthedocs.io

Official javascript API docs:
http://wwwimages.adobe.com/www.adobe.com/content/dam/acom/en/devnet/photoshop/pdfs/photoshop-cc-javascript-ref-2015.pdf


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
Photoshop Scripting Reference:
https://theiviaxx.github.io/photoshop-docs/Photoshop/index.html

```python

from photoshop_python_api import Application
from photoshop_python_api import JPEGSaveOptions
from photoshop_python_api import SolidColor

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

```
