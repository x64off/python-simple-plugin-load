import uuid
class TestPlugin:
    __ID = str(uuid.uuid4())
    def __init__(self,App):
        import tkinter as tk
        App.NewLabel = tk.Label(text = 'Test Plugin')
        App.NewLabel.pack()
    @property
    def ID(self):
        return self.__ID