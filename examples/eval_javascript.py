from photoshop_python_api import Application


def eval_javascript():
    app = Application()
    jsx = r"""
    var doc = app.activeDocument;
    var orig_name = doc.name;
    alert(orig_name);
    """
    app.eval_javascript(jsx)


if __name__ == '__main__':
    eval_javascript()
