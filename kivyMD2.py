# we learn to add diffrent kind of button like icon button , RectangleFlatButton

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton , MDRectangleFlatButton , MDIconButton , MDFloatingActionButton

class MyApp(MDApp):
    def build(self):
        screen = Screen()
        flat_btn = MDRectangleFlatButton(text="Click",
                                         pos_hint={'center_x':0.3,'center_y':0.5})    # button is on center 

        icon_btn = MDFloatingActionButton(icon='language-java',
                                pos_hint={'center_x':0.6,'center_y':0.5}) 
        screen.add_widget(icon_btn)
        screen.add_widget(flat_btn)
        return screen

MyApp().run()