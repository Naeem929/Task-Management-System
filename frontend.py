import kivy
# import kivy 
# kivy.require('1.9.1') # replace with your current kivy version !

# from kivy import Config
# Config.set('graphics', 'multisamples', '0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self). __init__(**kwargs)
        
        self.cols = 1

        # Add Another Grid for text to be entered and one main grid for submit button and result
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # Add widget
        self.top_grid.add_widget(Label(text="Name"))
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Date Of Birth"))
        self.date = TextInput(multiline=False)
        self.top_grid.add_widget(self.date)

        self.top_grid.add_widget(Label(text="Contact"))
        self.contact = TextInput(multiline=False)
        self.top_grid.add_widget(self.contact)

        self.top_grid.add_widget(Label(text="Email"))
        self.mail = TextInput(multiline=False)
        self.top_grid.add_widget(self.mail)

        self.top_grid.add_widget(Label(text="User Name"))
        self.username = TextInput(multiline=False)
        self.top_grid.add_widget(self.username)

        self.top_grid.add_widget(Label(text="Password"))
        self.password = TextInput(multiline=False)
        self.top_grid.add_widget(self.password)

        self.top_grid.add_widget(Label(text="Confirm Password"))
        self.cpass = TextInput(multiline=False)
        self.top_grid.add_widget(self.cpass)

        if self.cpass.text != self.password.text:
            print("Re-Enter same password")

        # Add top_grid into main grid as a widget
        self.add_widget(self.top_grid)

        # Creating Submit Button
        self.submit = Button(text="Submit", font_size=18,
        size_hint_y= None,
        height=50,
        size_hint_x = None,
        width = 200)
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)
    def press(self, instance):
        name = self.name.text
        DOB = self.date.text
        contact = self.contact.text
        email = self.mail.text
        username = self.username.text
        password = self.password.text

        self.add_widget(Label(text=f'Thank you Mr {name}, your details has been updated, please enter your credentials and login'))

        # Clearing data after once entered
        self.name.text =''
        self.date.text =''
        self.contact.text =''
        self.mail.text =''
        self.username.text =''
        self.password.text =''
        self.cpass.text =''
class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()