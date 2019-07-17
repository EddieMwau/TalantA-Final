# -*- coding: utf-8 -*-
#
# This file created with KivyCreatorProject
# <https://github.com/HeaTTheatR/KivyCreatorProgect
#
# Copyright © 2017 Easy
#
# For suggestions and questions:
# <kivydevelopment@gmail.com>
# 
# LICENSE: MIT

from kivy.app import App
from kivy.core.window import Window
import webbrowser

from kivy.uix.screenmanager import Screen


class About(Screen):
    def open_url(self, instance, url):
        webbrowser.open(url)

    def logout(self):
        App.get_running_app().stop()
        Window.close()
