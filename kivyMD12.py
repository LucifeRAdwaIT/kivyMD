# TapTargetView

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivymd.uix.taptargetview import MDTapTargetView
KV = '''
ScreenManager:
    Hello:
    Bye:
<Hello>:
    name : 'hello'  
    MDIconButton:
        icon : 'arrow-right'
        pos_hint : {'center_x':0.5,'center_y':0.5}
        user_font_size : '100sp'  
        on_press :
            root.manager.current = 'bye'
            root.manager.transition.direction = 'left'
            app.open_target()

<Bye>:
    name : 'bye'
    MDLabel:
        text : "Welcome"
        halign : 'center'
        theme_text_color:'Custom'
        text_color: 122/255,34/255,77/255,1
        font_style : 'H2'     
    MDIconButton:
        id : t_btn
        icon : 'plus'
        pos_hint : {'center_x':0.1,'center_y':0.1}
        user_font_size : '100sp'  
        on_press :
            root.manager.current = 'bye'
            root.manager.transition.direction = 'left'    
            app.close_target()
    MDIconButton:
        id : next
        icon : 'arrow-right'
        disabled : True
        pos_hint : {'center_x':0.9,'center_y':0.1}
        user_font_size : '45sp'          
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
        self.targetview = MDTapTargetView(widget = self.help_str.get_screen('bye').ids.t_btn,title_text="next",
                        widget_position='left_bottom',title_text_size='20sp',description_text="go text",outer_radius='80dp',
                        description_text_color=[1,0,0,1],outer_circle_alpha=0.40,target_radius="40dp")
        return screen
    def open_target(self):
        self.targetview.start()
    def close_target(self):
        self.targetview.stop()    
        self.help_str.get_screen('bye').ids.next.disabled = False
DemoApp().run()