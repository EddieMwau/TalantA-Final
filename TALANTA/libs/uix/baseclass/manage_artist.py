from kivy.uix.screenmanager import Screen
import pymysql


class ManageArtist(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cancel_clicked(self):
        self.manager.current = 'account'

    def update_profile(self):

        self.manager.current = 'account'

    def upload_art(self):
        self.manager.current = 'upload'
