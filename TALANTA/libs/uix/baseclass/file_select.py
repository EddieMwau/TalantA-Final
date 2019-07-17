from kivy.uix.screenmanager import Screen


class FileSelect(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cancel_clicked(self):

        self.manager.current = 'upload'

    def select_item_clicked(self):
        filechooser = self.ids.filechooser

        selection = filechooser.selection

        print(selection)
        self.manager.get_screen('upload').labelText = selection[0]
        self.manager.current = 'upload'
