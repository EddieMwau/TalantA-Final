import webbrowser

from kivy.uix.screenmanager import Screen


class Helper(Screen):
    def open_url(self):
        url = 'file:///home/eddie/Desktop/final_project/talanta-web/startbootstrap-new-age-gh-pages/FAQ/index.html'
        webbrowser.open(url)
