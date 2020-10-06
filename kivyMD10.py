# snackbar and progressbar

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder

KV = '''
ScreenManager:
    Hello:
  
<Hello>:
    name : 'hello' 
    #:import Snackbar kivymd.uix.snackbar.Snackbar
    MDIconButton:
        icon : 'android'
        pos_hint : {'center_x':0.5,'center_y':0.5}
        on_press : Snackbar(text="Hi. i am snackbar").show()
    MDProgressBar:
        value : 40
        pos_hint : {'center_y':0.02}
'''
class Hello(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Hello(name="hello"))

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.help_str = Builder.load_string(KV)
        screen.add_widget(self.help_str)
        return screen
DemoApp().run()