import tkinter as tk
import os, sys
from pathlib import Path

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Window Settings
        self.geometry('300x50')
        self.title('Simple Plugin Loader')
        self.resizable(0,0)
        self.Label = tk.Label(text = 'Test Label')
        self.Label.pack()
        # Plugins Directory
        self.Plugins_Directory = 'plugins'
        # Plugins Dict
        self.Plugins = {}
        # Load Plugins
        self.Load_Plugins()
    def Load_Plugins(self):
        # Plugins are .zip archive with the .plgn extension
        Plugins = list(Path(self.Plugins_Directory).rglob("*.[pP][lL][gG][nN]"))
        for Plugin in Plugins:
            try:
                sys.path.append(os.path.abspath(Plugin))
                Plugin_Name = os.path.basename(Plugin).split('.')[0]
                exec('from {0} import {0}'.format(Plugin_Name))
                exec('self.Plugins["{0}"] = {0}(self) if hasattr({0},"ID") else None'.format(Plugin_Name))
            except Exception as Ex:
                print(Ex)
        # Loading *.py files
        PythonFiles = list(Path(self.Plugins_Directory).rglob("*.[pP][yY]"))
        for File in PythonFiles:
            PythonFile_Name = os.path.basename(File).split('.')[0]
            PythonFile_Path = [directory for directory in os.path.split(File)[:-1] if directory]
            PythonFile_Path.append(PythonFile_Name)
            path = ".".join(PythonFile_Path)
            try:
                exec('from {0} import {1}'.format(path,PythonFile_Name))
                exec('self.Plugins["{0}"] = {0}(self) if hasattr({0},"ID") else None'.format(PythonFile_Name))
            except Exception as Ex:
                print(Ex)
        self.Plugins = { Plugin:self.Plugins[Plugin] for Plugin in self.Plugins if self.Plugins[Plugin]}

if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
