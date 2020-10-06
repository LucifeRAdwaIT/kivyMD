from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton  
import json
import os
import requests
KV = '''
ScreenManager:
    First:
    Login:
    Singup:
    Welcome:
    Main:
<First>:
    name : 'first'
    MDLabel:
        text : "First App"
        font_style : 'H2'
        halign : 'center'
        pos_hint : {'center_y':0.8}
        theme_text_color : "Custom"
        text_color : (0,0,1,1)
    MDRaisedButton:
        text : "Login"
        pos_hint : {'center_x':0.35,'center_y':0.4} 
        on_release : 
            root.manager.current = 'login'
            root.manager.transition.direction = 'up'
    MDRaisedButton:
        text : "Sing Up"
        pos_hint : {'center_x':0.65,'center_y':0.4} 
        on_release:
            root.manager.current = 'singup'
            root.manager.transition.direction = 'up'      
    
<Login>:
    name : 'login'
    MDTextField:
        id : email
        hint_text : "Enter Email"
        color_mode : 'custom'
        line_color_normal : app.theme_cls.primary_color
        line_color_focus : 0,0,0,1
        pos_hint : {'center_x':0.5,'center_y':0.8}
        helper_text : "Email is Required"
        helper_text_mode : 'on_error'
        mode : 'rectangle'
        required : True
        size_hint : (0.8,0.1)
    MDTextField:
        id : password
        hint_text : "Enter Password"
        line_color_normal : app.theme_cls.primary_color
        line_color_focus : 0,0,0,1
        pos_hint : {'center_x':0.5,'center_y':0.65}    
        helper_text : "Password is Required"
        helper_text_mode : 'on_error'
        mode : 'rectangle'
        required : True
        size_hint : (0.8,0.1)
        password : True
    MDRaisedButton:
        text : "Login"
        pos_hint : {'center_x':0.5,'center_y':0.5} 
        on_release: 
            app.login() 
            app.username_changer()

    MDRaisedButton:
        text : "Back"
        pos_hint : {'center_x':0.5,'center_y':0.4} 
        on_release:
            root.manager.current = 'first'
            root.manager.transition.direction = 'down'      
<Singup>:
    name : 'singup'
    MDTextField:
        id : email
        hint_text : "Enter Email"
        color_mode : 'custom'
        line_color_normal : app.theme_cls.primary_color
        line_color_focus : 0,0,1,1
        pos_hint : {'center_x':0.5,'center_y':0.8}
        helper_text : "Email is Required"
        helper_text_mode : 'on_error'
        mode : 'rectangle'
        required : True
        size_hint : (0.7,0.1)
    MDTextField:
        id : username
        hint_text : "Enter User Name"
        color_mode : 'custom'
        line_color_normal : app.theme_cls.primary_color
        line_color_focus : 0,0,1,1
        pos_hint : {'center_x':0.5,'center_y':0.65}
        helper_text : "Username is Required"
        helper_text_mode : 'on_error'
        mode : 'rectangle'
        required : True
        size_hint : (0.7,0.1)
    MDTextField:
        id : password
        hint_text : "Enter Password"
        color_mode : 'custom'
        line_color_normal : app.theme_cls.primary_color
        line_color_focus : 0,0,1,1
        pos_hint : {'center_x':0.5,'center_y':0.5}    
        helper_text : "Password is Required"
        helper_text_mode : 'on_error'
        mode : 'rectangle'
        required : True
        size_hint : (0.7,0.1)
        password : True
    MDRaisedButton:
        text : "Sing Up"
        pos_hint : {'center_x':0.35,'center_y':0.4} 
        on_release: app.singup()

    MDRaisedButton:
        text : "Back"
        pos_hint : {'center_x':0.65,'center_y':0.4} 
        on_release:
            root.manager.current = 'first'
            root.manager.transition.direction = 'down'     
<Welcome>:
    name : 'welcome'  
    MDLabel:
        id : user_name
        text : "Welcome"
        halign : 'center'
        pos_hint:  {'center_y':0.7}
        theme_text_color:'Custom'
        text_color: 122/255,34/255,77/255,1
        font_style : 'H2'
    MDFloatingActionButton:
        pos_hint : {'center_x':0.1,'center_y':0.94}
        icon : 'arrow-left' 
        on_press: 
            app.login()  
            root.manager.current = 'login'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        pos_hint : {'center_x':0.9,'center_y':0.94}
        icon : 'arrow-right' 
        on_press:
            app.change_detail()
            root.manager.current = 'main'
            root.manager.transition.direction = 'left'   
<Main>:
    name : 'main'        
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation : 'vertical'
                    MDToolbar :
                        title : "Menu"
                        elevation : 10
                        left_action_items: [['menu',lambda x : main_nav.set_state()]]
                    Widget:
        MDNavigationDrawer:
            id : main_nav   
            BoxLayout:
                orientation : 'vertical'
                Image:
                    id : profile_img 
                    source : "corona.jpg"       

                MDLabel:
                    id : username
                    text : "First App" 
                    font_style : 'H5'
                    size_hint_y : None
                    height : self.texture_size[1]
                
                MDLabel:
                    id : useremail
                    text : "firstapp@gmail.com" 
                    font_style : 'H6'
                    size_hint_y : None
                    height : self.texture_size[1]
                ScrollView: 
                    MDList:
                        OneLineIconListItem:
                            text : "Logout"
                            on_release:
                                root.manager.current = 'login'
                                root.manager.transition.direction = 'right'  
                            IconLeftWidget:
                                icon : 'logout'
'''


class First(Screen):
    pass
class Login(Screen):
    pass
class Singup(Screen):
    pass
class Welcome(Screen):
    pass
class Main(Screen):
    pass
sm = ScreenManager()
sm.add_widget(First(name="first"))
sm.add_widget(Login(name="login"))
sm.add_widget(Singup(name="singup"))
sm.add_widget(Welcome(name="welcome"))
sm.add_widget(Main(name="main"))

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        self.help_str = Builder.load_string(KV)
        self.url = "https://fir-b3b38.firebaseio.com/.json"
        screen.add_widget(self.help_str)
        return screen
    def singup(self):
        email = self.help_str.get_screen('singup').ids.email.text    
        username = self.help_str.get_screen('singup').ids.username.text 
        password = self.help_str.get_screen('singup').ids.password.text
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
            try:
                singup_info = str({f'\"{email}\":{{"Password":\"{password}\","Username":\"{username}\"}}'})   
                singup_info = singup_info.replace(".","-")
                singup_info = singup_info.replace("\'","")
                to_database = json.loads(singup_info)
                requests.patch(url=self.url,json = to_database)
                self.help_str.get_screen('login').manager.current = 'login'
            except:
                cancel_btn1 = MDFlatButton(text="Retry",on_press=self.cancel_button1)
                self.dailog1 = MDDialog(title="Oops!",text="Something went worng!",size_hint=(0.7,0.1),buttons=[cancel_btn1])
                self.dailog1.open()     

    auth = "fzsWVliF5HwVlZLoeCf4i9owW1EnzczEMUfv42u4"       ## aurthentication key

    def login(self):
        check_input = True
        self.login_info = False
        user_email = self.help_str.get_screen('login').ids.email.text
        user_pass = self.help_str.get_screen('login').ids.password.text
        try:
            int(user_email)
        except:
            check_input = False    

        if check_input or (user_email.split()==[]) or (user_pass.split()==[]):
            cancel_btn = MDFlatButton(text="Retry",on_press=self.cancel_button)
            self.dailog_box = MDDialog(title="Invalid Username",text="Please enter a valid Username And Password",size_hint=(0.7,0.1),buttons=[cancel_btn])
            self.dailog_box.open()
        else:
            try:
                suppored_user_email = user_email.replace('.','-')
                suppored_user_pass = user_pass.replace('.','-')
                request = requests.get(self.url+'?auth'+self.auth) 
                data = request.json()
                email = set()
                for key,value in data.items():
                    email.add(key)
                if suppored_user_email in email and suppored_user_pass == data[suppored_user_email]['Password']:
                    self.login_info = True
                    self.username = data[suppored_user_email]['Username']
                    self.email = suppored_user_email                    
                    self.help_str.get_screen('welcome').manager.current = 'welcome'
                    with open("app.json","w+") as f:
                        pass
                else:
                    cancel_btn1 = MDFlatButton(text="Retry",on_press=self.cancel_button1)
                    self.dailog1 = MDDialog(title="Invalid Input",text="User not Found",size_hint=(0.7,0.1),buttons=[cancel_btn1])
                    self.dailog1.open() 
            except:
                cancel_btn1 = MDFlatButton(text="Retry",on_press=self.cancel_button1)
                self.dailog1 = MDDialog(title="Oops!",text="Something went worng!",size_hint=(0.7,0.1),buttons=[cancel_btn1])
                self.dailog1.open()  
    def on_start(self):
        try:
            with open("app.json") as f:
                self.help_str.get_screen('main').manager.current = "main"
        except :
            self.help_str.get_screen('first').manager.current = "first"
    def change_detail(self):        
        if self.login_info:
            self.help_str.get_screen('main').ids.username.text = f"{self.username}"
            self.help_str.get_screen('main').ids.useremail.text = f"{self.email}"
    def username_changer(self):
        if self.login_info:
            self.help_str.get_screen('welcome').ids.user_name.text = f"Welcome {self.username}"
    def cancel_button1(self,object):
        self.dailog1.dismiss()
    def cancel_button(self,object):
        self.dailog_box.dismiss()
    def cancel(self,object):
        self.dailog.dismiss()
        
MainApp().run()