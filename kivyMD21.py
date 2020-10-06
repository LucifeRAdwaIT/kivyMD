# expension panel

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel , MDExpansionPanelThreeLine

KV = '''

<Content>:
    adaptive_height : True

    MDLabel:
        text : "hello"
        halign : 'center'
ScreenManager:
    Hello:

<Hello>:
    name : 'hello'
    
    ScrollView:
        MDGridLayout:
            id : box
            cols : 1
            adaptive_height : True
    
'''
class Hello(Screen):
    pass
class Content(MDBoxLayout):
    pass
sm = ScreenManager()
sm.add_widget(Hello(name="hello"))

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.help_str = Builder.load_string(KV)
        screen.add_widget(self.help_str)
        return screen
    def on_start(self):
        for i in range(10):
            self.help_str.get_screen('hello').ids.box.add_widget(
                MDExpansionPanel(
                    icon = 'corona.jpg',
                    content = Content(),
                    panel_cls = MDExpansionPanelThreeLine(
                        text = "Main Text",
                        secondary_text = "text 1",
                        tertiary_text = "text 2" 
                    )
                )
            )

DemoApp().run()