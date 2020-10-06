from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton 

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Pink"       # change color        
        self.theme_cls.primary_hue = 'A700'           # change hue        
        self.theme_cls.theme_style = 'Dark'           # change theme        
        screen = Screen()
        icon_btn = MDRectangleFlatButton(text="Click",
                                pos_hint={'center_x':0.5,'center_y':0.9}) 
        screen.add_widget(icon_btn)
        return screen

MyApp().run()