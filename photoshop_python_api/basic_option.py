

class BasicOption(object):
    def __int__(self, *args, **kwargs):
        self._data = kwargs

    def __setattr__(self, key, value):
        if '_Core__initialised' not in self.__dict__:
            return object.__setattr__(self, key, value)
        elif '_data' in self.__dict__ and key in self._data:
            self._data[key] = value
        else:
            return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        try:
            return self.__getattribute__(item)
        except AttributeError:
            try:
                if '_data' in self.__dict__:
                    return self._data[item]
            except KeyError:
                raise AttributeError(item)

    @property
    def option(self):
        return self.app

    def save_as(self, doc, file_path, as_copy=True, extension_type=2):
        """Saves the Document with the specified save options."""
        return doc.saveAs(file_path, self.option, as_copy,
                          extension_type)
