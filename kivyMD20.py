from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder

KV = '''
ScreenManager:
    Hello:

<Hello>:
    name : 'hello'
    BoxLayout:
        orientation : 'vertical'
        MDToolbar:
            title : "Navigation Bar"
            md_bg_color : 0.2,0.2,0.2,1
            specific_text_color : 1,1,1,1
        
        MDBottomNavigation:
            panel_color : 1,1,1,1

            MDBottomNavigationItem:
                name : 'python'
                text : "Python"
                icon : 'language-python'

                MDLabel : 
                    text : "This is a Python Page"
                    halign : 'center' 

            MDBottomNavigationItem:
                name : 'c++'
                text : "C++"
                icon : 'language-cpp'

                MDLabel : 
                    text : "This is a C++ Page"
                    halign : 'center'         
'''
class Hello(Screen):
    pass
sm = ScreenManager()
sm.add_widget(Hello(name="hello"))

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        help_str = Builder.load_string(KV)
        screen.add_widget(help_str)
        return screen

DemoApp().run()