import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid1(GridLayout):
    def __init__(self,**kwarge):
        super(MyGrid1,self).__init__(**kwarge)
        self.cols = 1

        self.inside = GridLayout()     # making grid inside main gridlayout
        self.inside.cols = 2
        self.inside.add_widget(Label(text="First name: "))
        self.First_name = TextInput(multiline=False)
        self.inside.add_widget(self.First_name)

        self.inside.add_widget(Label(text="Last name: "))
        self.Last_name = TextInput(multiline=False)
        self.inside.add_widget(self.Last_name)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit",font_size=40)
        self.submit.bind(on_press=self.submit_button)
        self.add_widget(self.submit)

    def submit_button(self,instance):
        name = self.First_name.text
        last_name =  self.Last_name.text
        email = self.email.text

        print(f"Hello! {name} your last name is {last_name}. and your email is {email}")

        self.First_name.text = ""
        self.Last_name.text = ""
        self.email.text = ""

class My1App(App):
    def build(self):
        return MyGrid1()

if __name__ == "__main__":
    My1App().run()