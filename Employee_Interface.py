import kivy
from kivy.app import App
from kivy.graphics import *
from kivy.graphics import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.stacklayout import StackLayout


class SayHello(FloatLayout):
    def __init__(self, **kwargs):
        super(SayHello, self).__init__(**kwargs)
        self.collector_1 = GridLayout()
        self.collector_1.cols = 1
        self.collector= GridLayout(cols=2,
                                #size_hint = (0.6,0.7),
                                #pos_hint = {"center_x":0.7, "center_y":1}
                                )
        self.window = GridLayout()
        self.window.cols = 1
      

        self.lable_title_of_task = Label(
                                text="Title of Task",
                                size_hint=(None,None),
                                width= 90,
                                height=30,
                                #pos_hint = {"center_x":2,"center_y":1},
                                font_size=15,
                                color=(128,128,128)
                                ) 

        self.text_input_title_of_task= TextInput(
                                multiline = True,
                                #padding_y = (20,20),
                                size_hint = (0.2,0.2)
                                )

        self.lable_description = Label(
                                text="Decription",
                                size_hint=(None,None),
                                width= 90,
                                height=30,
                                font_size=15,
                                color=(128,128,128)
                                )
                                
        self.text_input_description= TextInput(
                                multiline = True, 
                                #padding_y = (20,20),
                                size_hint = (0.2,0.6)
                                )

        self.lable_effort = Label(
                                text="Effort",
                                size_hint=(None,None),
                                width= 80,
                                height=20,
                                font_size=15,
                                color=(128,128,128)
                                ) 

        self.text_input_effort = TextInput(
                                multiline = False, 
                                #padding_y = (20,20),
                                size_hint = (0.1,0.01),
                                )

        self.lable_deadline = Label(
                                text="Deadline",
                                size_hint=(None,None),
                                width= 80,
                                height=20,
                                font_size=15,
                                color=(128,128,128)
                                )

        self.text_input_deadline = TextInput(
                                multiline = False, 
                                #padding_y = (20,20),
                                size_hint = (0.1,0.01)
                                )

        self.lable_reason = Label(
                                text="Reason",
                                size_hint=(None,None),
                                width= 70,
                                height=30,
                                font_size=15,
                                color = (128,128,128)
                                )

        self.text_input_reason = TextInput(
                                multiline = True, 
                                #padding_y = (10,10),
                                #size_hint = (0,2),
                                #pos_hint = {"center_x": 2, "center_y":4}
                                )

        self.lable_Propose_effort = Label(
                                text="Propose Your Effort",
                                size_hint=(None,None),
                                width= 130,
                                height=30,
                                font_size=15,
                                color = (128,128,128)
                                )

        self.text_input_Propose_effort = TextInput(multiline = False, size_hint = (0,.2),padding_y = (10,10))
        
        self.button_accept = Button(
                      text = "Accept",
                      size_hint = (0.02,0.01),
                      bold = True,
                      background_color = (255,0,0)
                      )
        self.button_decline = Button(
                      text ="Decline",
                      size_hint = (0.1, 0.15),
                      pos_hint = {"x":.4, "top":1},
                      bold = True,
                      background_color = (255,0,0)
        )
        self.button_negotiate = Button(
                      text ="Negotiate",
                      size_hint = (0.1,0.1),
                      bold = True,
                      background_color = (50,205,50)
        )
        self.button_submit = Button(
                      text ="Submit",
                      size_hint = (0.1,0.1),
                      pos_hint = {"center_x": 0.7, "center_y":0.7},
                      bold = True,
                      background_color = (0,191,255)
        )
        
        self.connect = GridLayout()
        self.connect.cols = 2

        self.effort = GridLayout()
        self.effort.cols = 1

        self.deadline = GridLayout()
        self.deadline.cols = 1

        self.connect_1 = GridLayout()
        self.connect_1.cols = 1



        self.window.add_widget(self.lable_title_of_task)
        self.window.add_widget(self.text_input_title_of_task)
        self.window.add_widget(self.lable_description)
        self.window.add_widget(self.text_input_description)

        self.effort.add_widget(self.lable_effort)
        self.effort.add_widget(self.text_input_effort)
        self.effort.add_widget(self.button_accept)
        
        self.deadline.add_widget(self.lable_deadline)
        self.deadline.add_widget(self.text_input_deadline)
        self.deadline.add_widget(self.button_decline)
        
        self.connect_1.add_widget(self.button_negotiate)
        self.connect_1.add_widget(self.lable_reason)
        self.connect_1.add_widget(self.text_input_reason)
        self.connect_1.add_widget(self.lable_Propose_effort)
        self.connect_1.add_widget(self.text_input_Propose_effort)
        self.connect_1.add_widget(self.button_submit)
        
        self.connect.add_widget(self.effort)
        self.connect.add_widget(self.deadline)
        
        self.collector.add_widget(self.window)
        self.collector.add_widget(self.connect)
        self.collector.add_widget(self.connect_1)
        self.collector_1.add_widget(self.collector)
        
         
        self.add_widget(self.collector_1)


        self.button_accept.bind(on_press = self.accept_button_pressed)
        self.button_decline.bind(on_press = self.decline_button_pressed)
        self.button_negotiate.bind(on_press = self.negotiate_button_pressed)
        self.button_submit.bind(on_press = self.submit_button_pressed)

    def accept_button_pressed(self, instance):
        pass

    def decline_button_pressed(self, instance):
        pass

    def negotiate_button_pressed(self, instance):
        pass

    def submit_button_pressed(self, instance):
        pass

class SpApp(App):
    def build(self):
        return SayHello()

if __name__ == "__main__":
    SpApp().run()