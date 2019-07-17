from kivy.uix.screenmanager import Screen


class Manage(Screen):

    def cancel_clicked(self):
        self.manager.current = 'account'

    def update_profile(self):
        self.manager.current = 'account'
