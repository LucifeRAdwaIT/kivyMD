# MDTextField and Dailog Button

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton , MDFloatingActionButton , MDFlatButton
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.dialog import MDDialog 
KV = '''
ScreenManager:
    Hello:
    Bye:
<Hello>:
    name: 'hello'
    MDLabel:
        id : main_text
        text:'Hello App!'
        halign:'center'
        theme_text_color:'Custom'
        text_color: 122/255,34/255,77/255,1
        font_style : 'H2'

    MDIconButton:
        icon : 'language-python'  
        user_font_size : '50sp'  
        theme_text_color:'Custom'
        text_color: 1,200/255,50/255,1
        pos_hint : {'center_x':0.05,'center_y':0.95}

    MDFloatingActionButton:
        icon : 'language-java'    
        user_font_size : '25sp'  
        pos_hint : {'center_x':0.95,'center_y':0.94}
        md_bg_color : app.theme_cls.primary_color
        on_press:
            root.manager.current = 'bye'
            root.manager.transition.direction = 'left'

    MDRectangleFlatButton:
        text: 'Theme Changer'
        pos_hint : {'center_x':0.6,'center_y':0.94}
        on_press:app.theme_changer() 

    MDRectangleFlatButton:
        text: 'Property Changer'
        pos_hint : {'center_x':0.3,'center_y':0.94}
        on_press:app.property_changer()     
<Bye>:
    name : 'bye'
    MDFloatingActionButton:
        icon : 'language-php'    
        user_font_size : '25sp'  
        pos_hint : {'center_x':0.3,'center_y':0.34}
        md_bg_color : app.theme_cls.primary_color
        on_press:
            root.manager.current = 'hello'
            root.manager.transition.direction = 'right'

    MDRectangleFlatButton:
        text: "Submit"
        pos_hint : {'center_x':0.6,'center_y':0.34}
        on_press:app.check_username()

    MDTextField:
        id : username_text
        hint_text : "Enter User Name"
        color_mode : "custom"
        line_color_normal : app.theme_cls.primary_color
        line_color_focus : 0,1,0,1
        helper_text : "Required"
        helper_text_mode : "on_error"
        # mode : "rectangle"
        icon_right : "account"
        icon_right_color : 0,0,1,1
        pos_hint : {'center_x':0.5,'center_y':0.5}
        required : True
        size_hint : (0.8,0.1)

'''
class Hello(Screen):
    pass
class Bye(Screen):
    pass
sm = ScreenManager()
sm.add_widget(Hello(name="hello"))
sm.add_widget(Bye(name="bye"))

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        screen = Screen()
        self.help_str = Builder.load_string(KV)
        screen.add_widget(self.help_str)
        return screen

    def theme_changer(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:   
            self.theme_cls.theme_style = "Dark" 

    def property_changer(self):
        if self.help_str.get_screen('hello').ids.main_text.text == "Bye App!" :
            self.help_str.get_screen('hello').ids.main_text.text = "Hello App!"
        else:
            self.help_str.get_screen('hello').ids.main_text.text = "Bye App!" 
    def check_username(self):
        username_check = True
        username_data = self.help_str.get_screen('bye').ids.username_text.text
        try:
            int(username_data)
        except:
            username_check = False
        if username_check or username_data.split()==[]:
            cancel_button = MDFlatButton(text="Cancel",on_press=self.close_dailog)
            self.user_dailog = MDDialog(title="Invailid Username",text="Please enter a valid username",size_hint=(0.4,0.1),buttons=[cancel_button]) 
            self.user_dailog.open()
     
    def close_dailog(self,object):
        self.user_dailog.dismiss()
DemoApp().run()