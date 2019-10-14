from kivy.app import App

from gui.MenuScreen import MenuScreen
from gui.ScreenManagement import ScreenManagement
from gui.SettingsScreen import SettingsScreen


class GuiApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = ScreenManagement()

    def build(self):
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(SettingsScreen(name='settings'))
        return self.sm
