from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextFieldRect

KV = '''
ScreenManager:
    Hello:

<Hello>:
    id: 'hello'
    MDLabel:
        text:'User Name: '
        halign:'center'
        theme_text_color:'Custom'
        text_color: 122/255,34/255,77/255,1
        font_style : 'H2'
    MDRectangleFlatButton:
        text:"Click"
        pos_hint:{'center_x':0.5,'center_y':0.35}   
    MDIcon:
        icon : 'android'
        font_size : 50
        pos_hint:{'center_x':0.5,'center_y':0.5}   
        theme_text_color : 'Custom'
        text_color : 0,1,0,1    
'''
class Hello(Screen):
    pass
sm = ScreenManager()
sm.add_widget(Hello(name="hello"))

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        help_str = Builder.load_string(KV)
        screen.add_widget(help_str)
        return screen

DemoApp().run()