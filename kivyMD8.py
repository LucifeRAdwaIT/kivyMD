# list box Advance

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
            OneLineIconListItem:
                text : "Python"
                IconLeftWidget:
                    icon : 'language-python'
            OneLineAvatarListItem:
                text : "Corona"
                ImageLeftWidget:
                    source : "corona.jpg"

<Bye>:
    name : "bye" 

'''
class Hello(Screen):
    pass
class Bye(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Hello(name="hello"))
class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.helper_text = Builder.load_string(KV)
        screen.add_widget(self.helper_text)
        return screen
DemoApp().run()        
