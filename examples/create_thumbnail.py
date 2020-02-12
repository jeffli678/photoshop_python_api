from photoshop_python_api import Application
from photoshop_python_api import JPEGSaveOptions


def create_thumbnail():
    app = Application()
    doc = app.activeDocument
    orig_name = doc.name
    width_str = doc.width
    height_str = doc.height
    thumb_name = '{}_tumb'.format(orig_name)
    index = width_str / 1280

    thumb_width = int(width_str / index)

    thumb_height = int(height_str / index)
    print(thumb_height, width_str)

    thumb_doc = doc.duplicate(orig_name)
    thumb_doc.resize_image(thumb_width, thumb_height)
    thumb_doc.saveAs('c:/{}.jpg'.format(thumb_name), JPEGSaveOptions(),
                     as_copy=True)
    thumb_doc.close()


if __name__ == '__main__':
    create_thumbnail()
