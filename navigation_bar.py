# navigationbar

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder

KV = '''
ScreenManager:
    Hello:
    Bye:
<Hello>:
    name : 'hello'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation : 'vertical'
                    MDToolbar :
                        title : "Menu"
                        elevation : 10
                        left_action_items : [['menu',lambda x : nav_drawer.toggle_nav_drawer()]]

                    MDBottomAppBar:
                        MDToolbar:
                            title: 'About'
                            left_action_items : [['language-python',lambda x: app.navigation_draw()]]  
                            type : 'bottom'
                            # mode : 'free-end'
                            icon : 'coffee'
                            on_action_button : app.navigation_draw()
                    Widget:
        MDNavigationDrawer:
            id : nav_drawer  
            BoxLayout:
                orientation : 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source:'Corona.jpg'
                MDLabel:
                    text:'Demo App'
                    font_style : 'H5'
                    size_hint_y : None
                    height : self.texture_size[1]           
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Binod'
                            IconLeftWidget:
                                icon : 'android'
                        OneLineIconListItem:
                            text: 'Satyam'
                            IconLeftWidget:
                                icon : 'face-profile'
                        OneLineIconListItem:
                            text: 'Adwait'
                            IconLeftWidget:
                                icon : 'arrow-right'                
<Bye>:
    name : 'bye'
    MDLabel:
        text:'Hello!'
        halign:'center'
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
sm.add_widget(Bye(name="bye"))

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        help_str = Builder.load_string(KV)
        screen.add_widget(help_str)
        return screen
    def navigation_draw(self):
        pass
DemoApp().run()