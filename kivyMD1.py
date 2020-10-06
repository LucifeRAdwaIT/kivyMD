# in this file we learn to add text with diffrent 'font,color,align' and
# we add diffrent icon on our app 

import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
class FirstApp(MDApp):
    def build(self):
        text_label = MDLabel(text="Hello World!",halign="center",theme_text_color="Custom",
                            text_color=(43/255.0,164/255.0,55/255.0,1),   #here 1 is opecity of text which we use to display
                            font_style="H1")   #we can choise any type of font

        icon = MDIcon(icon='language-python',halign="center")
        return text_label

FirstApp().run()