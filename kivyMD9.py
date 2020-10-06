# Makeing gallary

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder

KV = '''
ScreenManager:
    Hello:
<MyTile@SmartTileWithStar>
    size_hint_y : None
    height : "240dp"    
<Hello>:
    name : 'hello' 
    ScrollView:
        MDGridLayout:
            cols : 3
            padding : dp(4) , dp(4)
            spacing : dp(8)
            MyTile:
                source : "corona.jpg" 
                text : "[size=26]Corana[/size]"
            MyTile:
                source : "corona.jpg" 
                text : "[size=26][color=#000FFFF]Corana[/color][/size]"
            MyTile:
                stars:5
                source : "corona.jpg"            
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