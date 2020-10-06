# Toast

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivymd.toast import toast
KV = '''
ScreenManager:
    Hello:
    Bye:
<Hello>:
    name : "hello"
    MDRaisedButton:
        text:'Toast up'
        pos_hint : {'center_x':0.5,'center_y':0.5}
        user_font_size : '80sp'
        on_press : app.toast_up()

<Bye>:
    name : "bye" 
    MDLabel : 
        text : "Hello"
'''
class Hello(Screen):
    pass
class Bye(Screen):
    pass
class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.helper_text = Builder.load_string(KV)
        screen.add_widget(self.helper_text)
        return screen
    def toast_up(self):
        toast("Hello!")   
DemoApp().run()        
