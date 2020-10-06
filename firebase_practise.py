from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
import json
from kivy.core import Window
Window.size = (350,600)
KV = '''
ScreenManager:
    First:
    Login:
    Singin:
<First>:
    name : 'first'
    MDLabel:
        text : 'App'
        halign : 'center'
        pos_hint : {'center_y':0.8}
        font_style : 'H2'
        theme_text_color : 'Custom'
        text_color : (0,0,1,0.81)
    MDRaisedButton:
        text : 'Login'
        pos_hint : {'center_x':0.5,'center_y':0.4}
        on_press : 
            root.manager.current = "login"
            root.manager.transition.direction = 'up'
    MDRaisedButton:
        text : 'Singin'
        pos_hint : {'center_x':0.5,'center_y':0.6}
        on_press : 
            root.manager.current = "singin"
            root.manager.transition.direction = 'up'
<Login>:
    name : 'login'
    MDLabel:
        text : 'Login'
        halign : 'center'
        pos_hint : {'center_y':0.9}
        font_style : 'H2'
        theme_text_color : 'Custom'
        text_color : (0,0,1,0.81)
    MDFlatButton:
        text : 'Create New Account'
        pos_hint : {'center_x':0.5,'center_y':0.2}
        font_style : 'H6'
        theme_text_color : 'Custom'
        text_color : (0,0,1,0.7)
        on_press:
            root.manager.current = "singin"
            root.manager.transition.direction = 'left'
    MDTextField:
        id : user_email
        pos_hint : {'center_x':0.5,'center_y':0.6}
        mode : 'rectangle'
        line_color_focus : 0,1,0,1
        helper_text : "Email Required"
        helper_text_mode : "on_error"
        hint_text : "Enter Email"    
        required : True    
        size_hint : (0.7,0.1)
    MDTextField:
        id : user_password
        pos_hint : {'center_x':0.5,'center_y':0.5}
        mode : 'rectangle'
        line_color_focus : 0,0,1,1
        helper_text : "Password Required"
        helper_text_mode : "on_error"
        hint_text : "Enter Password"
        required : True
        password : True
        size_hint : (0.7,0.1)
    MDRaisedButton:
        text : 'Login'
        pos_hint : {'center_x':0.5,'center_y':0.4}
        on_release : 
            app.login()            
<Singin>:
    name : 'singin'
    MDLabel:
        text : 'Singin'
        halign : 'center'
        pos_hint : {'center_y':0.9}
        font_style : 'H2'
        theme_text_color : 'Custom'
        text_color : (0,0,1,0.81)
    MDTextField:
        id : user_email
        pos_hint : {'center_x':0.5,'center_y':0.7}
        mode : 'rectangle'
        line_color_focus : 0,1,0,1
        helper_text : "Email Required"
        helper_text_mode : "on_error"
        hint_text : "Enter Email"    
        required : True    
        size_hint : (0.7,0.1)
    MDTextField:
        id : user_name
        pos_hint : {'center_x':0.5,'center_y':0.6}
        mode : 'rectangle'
        line_color_focus : 0,1,0,1
        helper_text : "Username Required"
        helper_text_mode : "on_error"
        hint_text : "Enter Username"
        required : True
        size_hint : (0.7,0.1)
    MDTextField:
        id : user_password
        pos_hint : {'center_x':0.5,'center_y':0.5}
        mode : 'rectangle'
        line_color_focus : 0,0,1,1
        helper_text : "Password Required"
        helper_text_mode : "on_error"
        hint_text : "Enter Password"
        required : True
        password : True
        size_hint : (0.7,0.1)
    MDRaisedButton:
        text : 'Singin'
        pos_hint : {'center_x':0.5,'center_y':0.35}
        on_release : 
            app.singin()
            # root.manager.current = "login"
            # root.manager.transition.direction = 'left'                        
    MDFlatButton:
        text : 'Already Have a account'
        pos_hint : {'center_x':0.5,'center_y':0.2}
        font_style : 'H6'
        theme_text_color : 'Custom'
        text_color : (0,0,1,0.7)
        on_press:
            root.manager.current = "login"
            root.manager.transition.direction = 'left'    
'''
class First(Screen):
    pass
class Login(Screen):
    pass
class Singin(Screen):
    pass

sm = ScreenManager()
sm.add_widget(First(name = 'first'))
sm.add_widget(Login(name = 'login'))
sm.add_widget(Singin(name = 'singin'))

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        self.help_str = Builder.load_string(KV)
        self.url = "https://fir-practse.firebaseio.com/.json"
        screen.add_widget(self.help_str)
        return screen
    
    def singin(self):
        email = self.help_str.get_screen('singin').ids.user_email.text    
        username = self.help_str.get_screen('singin').ids.user_name.text 
        password = self.help_str.get_screen('singin').ids.user_password.text
        if email.split() == [] or username.split() == [] or password.split()  == []:
            Cancel = MDFlatButton(text="Retry",on_press=self.cancel) 
            self.dailog = MDDialog(title="Invalid Input",text="Please enter a valid Input",
                                    size_hint=(0.7,0.1),buttons=[Cancel])
            self.dailog.open()
        elif ("@" not in email):
            Cancel = MDFlatButton(text="Retry",on_press=self.cancel) 
            self.dailog = MDDialog(title="Invalid Email",text="Please enter a valid Email",
                                    size_hint=(0.7,0.1),buttons=[Cancel])
            self.dailog.open()
        elif (len(password)<5):
            Cancel = MDFlatButton(text="Retry",on_press=self.cancel) 
            self.dailog = MDDialog(title="Invalid Password",text="Please enter a strong Password",
                                    size_hint=(0.7,0.1),buttons=[Cancel])
            self.dailog.open()
        else:
            singin_info = str({f'\"{email}\":{{"Password":\"{password}\","Username":\"{username}\"}}'})
            singin_info = singin_info.replace(".","-")
            singin_info = singin_info.replace("\'","")
            to_database = json.loads(singin_info)
            requests.patch(url=self.url,json=to_database)
    def login(self):
        check_input = True
        self.login_info = False
        user_email = self.help_str.get_screen('login').ids.user_email.text
        user_pass = self.help_str.get_screen('login').ids.user_password.text
        try:
            int(user_email)
        except:
            check_input = False    

        if check_input or (user_email.split()==[]) or (user_pass.split()==[]):
            cancel_btn = MDFlatButton(text="Retry",on_press=self.cancel_button)
            self.dailog_box = MDDialog(title="Invalid Input",text="Please enter a valid Input",size_hint=(0.7,0.1),buttons=[cancel_btn])
            self.dailog_box.open()

    def cancel(self,object):
        self.dailog.dismiss()
    def cancel_button(self,object):
        self.dailog_box.dismiss()
MainApp().run()