# list

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
KV = '''
ScreenManager:
    Hello:
    Bye:
<Hello>:
    name : 'hello' 
<Bye>:
    name : 'bye'
    MDLabel:
        id : text
        text : "Welcome"
        halign : 'center'
        theme_text_color:'Custom'
        text_color: 122/255,34/255,77/255,1
        font_style : 'H2'    
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
        self.help_str = Builder.load_string(KV)
        screen.add_widget(self.help_str)
        table = MDDataTable(pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(0.9,0.6),check=True,rows_num=7,
                            column_data = [
                                ("food",dp(30)),
                                ("Calories",dp(30)),
                                ("price",dp(30)),
                                ("Must-buy",dp(30))
                            ],
                            row_data=[
                                ("Apple","300","50","no"),
                                ("Mango","300","50","no"),
                                ("Banana","300","50","no"),
                                ("Pea","300","50","no"),
                                ("Litchy","300","50","no"),
                                ("PineApple","300","50","no"),
                                ("Orange","300","50","no")
                            ])
        
        table.bind(on_check_press = self.check_press)
        table.bind(on_row_press = self.row_press)
        self.help_str.get_screen('hello').add_widget(table)
        
        return screen
    def check_press(self,instance_tabel,current_row):
        self.help_str.get_screen('bye').manager.current = 'bye'
        self.help_str.get_screen('bye').manager.transition.direction = 'left'
        self.help_str.get_screen('bye').ids.text.text = current_row[0]
        
    def row_press(self,instance_tabel,current_row):
        pass
DemoApp().run()