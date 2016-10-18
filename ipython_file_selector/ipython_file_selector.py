from ipywidgets import DOMWidget
from traitlets import Unicode, Int, List, observe
import os

class IPFileSelector(DOMWidget):
    _view_module = Unicode('nbextensions/ipython_file_selector/ipython_file_selector', sync=True)
    _view_name = Unicode('IPFileSelector', sync=True)
    home_path = Unicode(os.getcwd()).tag(sync=True)
    current_path = Unicode().tag(sync=True)
    count = Int(555).tag(sync=True)
    subdirs = List().tag(sync=True)
    subfiles = List().tag(sync=True)

    selected = dict()

    def __init__(self, *args, **kwargs):
        super(IPFileSelector, self).__init__(*args, **kwargs)
        self.on_msg(self.handleMsg)

    def handleMsg(self, widget, content, buffers=None):
        if (content['type'] == 'init'):
            self.current_path_changed(None)
        if (content['type'] == 'select'):
            self.selected = content['selected']

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
