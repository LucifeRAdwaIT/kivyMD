# list box normal

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivymd.uix.list import MDList , OneLineListItem , TwoLineListItem , ThreeLineListItem
KV = '''
ScreenManager:
    Hello:
    Bye:
<Hello>:
    name : "hello"
    
    ScrollView:
        MDList:
            id : ls
            OneLineListItem:
                text : "Hello"
            TwoLineListItem:
                text : "Second Item"
                secondary_text : "this is secondary text"
            ThreeLineListItem:
                text : "Third item"       
                secondary_text : "this is secondary text"
                tertiary_text : "this is 3rd text"

<Bye>:
    name : "bye" 

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
    def on_start(self):
        for i in range(20):
            self.helper_text.get_screen('hello').ids.ls.add_widget(
                OneLineListItem(text=f"item {i}")
               )
            self.helper_text.get_screen('hello').ids.ls.add_widget(
                TwoLineListItem(text=f"item {i}",secondary_text=f"second item {i}")
            )   
DemoApp().run()        
