# button and function

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton , MDFloatingActionButton
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextFieldRect

KV = '''
ScreenManager:
    Hello:
    Bye:
<Hello>:
    name: 'hello'
    MDLabel:
        id : main_text
        text:'Hello App!'
        halign:'center'
        theme_text_color:'Custom'
        text_color: 122/255,34/255,77/255,1
        font_style : 'H2'

    MDIconButton:
        icon : 'language-python'  
        user_font_size : '50sp'  
        theme_text_color:'Custom'
        text_color: 1,200/255,50/255,1
        pos_hint : {'center_x':0.05,'center_y':0.95}

    MDFloatingActionButton:
        icon : 'language-java'    
        user_font_size : '25sp'  
        pos_hint : {'center_x':0.95,'center_y':0.94}
        md_bg_color : app.theme_cls.primary_color
        on_press:
            root.manager.current = 'bye'
            root.manager.transition.direction = 'left'

    MDRectangleFlatButton:
        text: 'Theme Changer'
        pos_hint : {'center_x':0.6,'center_y':0.94}
        on_press:app.theme_changer() 

    MDRectangleFlatButton:
        text: 'Property Changer'
        pos_hint : {'center_x':0.3,'center_y':0.94}
        on_press:app.property_changer()     
<Bye>:
    name : 'bye'
    MDLabel :
        text : 'This is Java Page'       
        halign:'center'
        theme_text_color:'Custom'
        text_color: 122/255,34/255,77/255,1
        font_style : 'H2' 
    MDFloatingActionButton:
        icon : 'language-php'    
        user_font_size : '25sp'  
        pos_hint : {'center_x':0.5,'center_y':0.34}
        md_bg_color : app.theme_cls.primary_color
        on_press:
            root.manager.current = 'hello'
            root.manager.transition.direction = 'right'
'''
class Hello(Screen):
    pass
class Bye(Screen):
    pass
sm = ScreenManager()
sm.add_widget(Hello(name="hello"))
sm.add_widget(Bye(name="bye"))

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        screen = Screen()
        self.help_str = Builder.load_string(KV)
        screen.add_widget(self.help_str)
        return screen

    def theme_changer(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:   
            self.theme_cls.theme_style = "Dark" 

    def property_changer(self):
        if self.help_str.get_screen('hello').ids.main_text.text == "Bye App!" :
            self.help_str.get_screen('hello').ids.main_text.text = "Hello App!"
        else:
            self.help_str.get_screen('hello').ids.main_text.text = "Bye App!"    
DemoApp().run()