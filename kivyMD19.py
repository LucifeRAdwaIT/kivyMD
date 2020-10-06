# bottom sheet part-3
 
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory
import webbrowser 
KV = '''
<Customsheet@BoxLayout>:
    orientation : "vertical"
    height : "400dp"
    size_hint_y : None

    MDToolbar:
        title : "Custom Bottom Sheet"
    ScrollView:
        OneLineIconListItem:
            text : "Preview"
            on_press : app.open()
            IconLeftWidget:
                icon : "page-previous"
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
        self.custom = MDCustomBottomSheet(screen=Factory.Customsheet())
        self.custom.open()
    def open(self):
        webbrowser.open("https://google.com")    
DemoApp().run()        
