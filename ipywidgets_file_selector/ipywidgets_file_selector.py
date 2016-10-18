from ipywidgets import DOMWidget
from traitlets import Unicode, List, Dict, observe
import os

class IPFileSelector(DOMWidget):
    _view_module = Unicode('nbextensions/ipywidgets_file_selector/ipywidgets_file_selector', sync=True)
    _view_name = Unicode('IPFileSelector', sync=True)
    home_path = Unicode().tag(sync=True)
    current_path = Unicode().tag(sync=True)
    subdirs = List().tag(sync=True)
    subfiles = List().tag(sync=True)
    selected = Dict().tag(sync=True)

    def __init__(self, *args, **kwargs):
        super(IPFileSelector, self).__init__(*args, **kwargs)
        self.home_path = kwargs.get('home', os.getcwd())
        self.on_msg(self.handleMsg)

    def handleMsg(self, widget, content, buffers=None):
        if (content['type'] == 'init'):
            self.current_path_changed(None)
        if (content['type'] == 'select'):
            pass

    @observe('current_path')
    def current_path_changed(self, change):
        subdirs_temp = [ ]
        subfiles_temp = [ ]
        if (os.path.isdir(self.current_path)):
            for f in os.listdir(self.current_path):
                ff = self.current_path + "/" + f
                if os.path.isdir(ff):
                    subdirs_temp.append(ff)
                else:
                    subfiles_temp.append(ff)
        self.subdirs = subdirs_temp
        self.subfiles = subfiles_temp
        msg = dict()
        msg["type"] = "dir_update"
        self.send(msg)

    @observe('selected')
    def test_changed(self, change):
        pass
