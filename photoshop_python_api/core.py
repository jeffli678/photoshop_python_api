# Import built-in modules
try:
    import _winreg as winreg
except ImportError:
    import winreg

import os
from shutil import rmtree
from tempfile import mkdtemp

# Import third-party modules
from comtypes.client import CreateObject

# Import local modules
from photoshop_python_api.errors import PhotoshopPythonAPIError


class Core(object):
    _root = 'Photoshop'
    REG_PATH = "Software\\Adobe\\Photoshop"
    _object_name = 'Application'
    object_name = None
    sub_object_name = None
    title = 'Photoshop Python API'

    def __init__(self, ps_version=None):
        # The photoshop version to COM progid mappings.
        # You can use `regedit` and go to
        # `Computer` > `HKEY_CLASSES_ROOT` > `Photoshop.Application` to find
        # progid ID.
        self.mappings = {
            '2020': 140,
            '2019': 130,
            '2018': 120,
            '2017': 110,
            'cs6': 60
        }
        self.app = None
        self.version = os.getenv('PS_VERSION', ps_version)
        self.app_id = self.mappings.get(self.version,
                                        self._get_install_version())
        try:
            self.adobe = self.instance_app(self.app_id)
        except WindowsError:
            try:
                self.adobe = self.instance_app(self._get_install_version())
            except WindowsError:
                raise PhotoshopPythonAPIError('Please check if you have '
                                              'Photoshop installed correctly.')
        self.__initialised = True

    def get_application_path(self):
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                              "{}\\{}".format(self.REG_PATH, self.app_id))
        return winreg.QueryValueEx(key, 'ApplicationPath')[
                   0] + 'Photoshop'

    def __getattribute__(self, item):
        try:
            return super(Core, self).__getattribute__(item)
        except AttributeError:
            return getattr(self.app, item)

    def instance_app(self, ps_id):
        names = [self._root]
        if not self.object_name:
            names.append(self._object_name)
        else:
            names.append(self.object_name)
        if self.sub_object_name:
            names.append(self.sub_object_name)
        names.append(ps_id)
        if self.object_name:
            progress_id = self._get_name(names)
            self.app = self._create_object(progress_id, dynamic=True)
        progress_id = self._get_name(names)
        return self._create_object(progress_id, dynamic=True)

    def _get_install_version(self):
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                              self.REG_PATH)
        self.app_id = winreg.EnumKey(key, 0).split('.')[0]
        return self.app_id

    @staticmethod
    def _create_object(*args, **kwargs):
        return CreateObject(*args, **kwargs)

    @staticmethod
    def _get_name(list_):
        return '.'.join(list_)

    def string_id_to_type_id(self, string):
        return self.adobe.stringIDToTypeID(string)

    def char_id_to_type_id(self, char):
        return self.adobe.charIDToTypeID(char)

    @property
    def action_descriptor(self):
        name = self._get_name([self._root, 'ActionDescriptor', self.app_id])
        return self._create_object(name)

    def run_jsx(self, jsx):
        id60 = self.string_id_to_type_id("AdobeScriptAutomation Scripts")
        action = self.action_descriptor
        id61 = self.char_id_to_type_id("jsCt")
        action.putPath(id61, jsx)
        id62 = self.char_id_to_type_id("jsMs")
        action.putString(id62, "null")
        self.adobe.executeAction(id60, action, 2)

    def eval_javascript(self, command):
        dir_ = mkdtemp(prefix='photoshop_python_api_')
        js = os.path.join(dir_, 'temp_script.jsx')
        with open(js, 'w') as file_obj:
            file_obj.write(command)
        self.run_jsx(js)
        rmtree(dir_)
