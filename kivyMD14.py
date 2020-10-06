# chips

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder

KV = '''
ScreenManager:
    Hello:

<Hello>:
    id: 'hello'
    MDChooseChip:
        MDChip:
            label : 'Facebook'
            icon : 'facebook'
            check : True
            # callback : app.call
            selected_chip_color: 0,0,1,1
        MDChip:
            label : 'Google'
            icon : 'google'
            check : True
            selected_chip_color: 0,0,1,1
            

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
    def call(self,instance,value):
        print(instance,value,sep='\n')
DemoApp().run()