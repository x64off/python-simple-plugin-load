import uuid
class LabelEdit:
    __ID == str(uuid.uuid4())
    def __init__(self,App):
        App.Label['text'] = "Label Edit Plugin"
    @property
    def ID(self):
        return self.__ID