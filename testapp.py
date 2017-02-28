from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '320')

class MainScreen(Screen):
    pass

class GamesScreen(Screen):
    pass

screens = Builder.load_file('CAT.kv')

class CATApp(App):
    def build(self):
        return screens

if __name__ == '__main__':
  CATApp().run()
