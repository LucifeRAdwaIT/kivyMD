# bottom sheet part-3
 
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivymd.uix.bottomsheet import MDListBottomSheet , MDGridBottomSheet
from kivymd.toast import toast
import webbrowser
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
        webbrowser.open(f"https://{x}.com")    
    def bottom_layer(self):
        data = {
            "Facebook" : 'facebook-box',
            "YouTube" : 'youtube',
            "Twitter" : "twitter-box",
            "Camera" : "camera"  
        }
        botton_sheet = MDGridBottomSheet(radius=10,radius_from='top')
        for i in data.items():
            botton_sheet.add_item(i[0],lambda x,y=i[0]:self.call_Back(y),icon_src=i[1])
        botton_sheet.open()
DemoApp().run()        
