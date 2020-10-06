# bottom sheet

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivymd.uix.bottomsheet import MDListBottomSheet
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
        user_font_size : '100sp'
        on_release : app.bottom_layer() 

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
    def call_Back(self,x):
        toast(x)    
    def bottom_layer(self):
        botton_sheet = MDListBottomSheet(radius=10,radius_from='top')
        for i in range(10):
            botton_sheet.add_item(f"item {i+1}",lambda x, y=i: self.call_Back(f"item {y+1} clicked"))
        botton_sheet.open()
DemoApp().run()        
