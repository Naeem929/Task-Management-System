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
from kivy.core.window import Window


## Tip: always do the settings first then add data to layouts
## Tip2: always name the variables meaningful and with the type as well in-order to make code more readable.

class SayHello(FloatLayout):
    def __init__(self, **kwargs):
        super(SayHello, self).__init__(**kwargs)

    # Add Task bar
# Add Another Grid for text to be entered and one main grid for submit button and result
        self.top_grid = GridLayout(row_force_default=True,
        row_default_height=50)
        self.top_grid.cols = 5
        self.top_grid.size_hint= (1,0.2)
        self.top_grid.pos_hint= {"center_x":0.5, "center_y":0.9}      
        # Adding logo on top left
        self.Group_Icon=Image(size_hint=(0.35,0.1), pos={0,0.1}, source='logo.png')
        self.top_grid.add_widget(self.Group_Icon)

        self.Assign_Task = Button(text='Assign Task')
        self.top_grid.add_widget(self.Assign_Task)

        self.My_Tasks = Button(text='My Tasks')
        self.top_grid.add_widget(self.My_Tasks)

        self.Profile = Button(text='Profile',size_hint_x=None, width=80, pos_hint={1,None})
        self.top_grid.add_widget(self.Profile)

        self.logout = Button(text='Logout',size_hint_x=None, width=80, pos_hint={1,None})
        self.top_grid.add_widget(self.logout)

       
        # Add top_grid into main grid as a widget
        self.add_widget(self.top_grid)
        
        #add widgets to windowy
  
        ## Creating a gridlayout for user, pwd and other items etc.
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.75)
        self.window.pos_hint = {"center_x": 0.35, "center_y":0.55}
        self.window.clearcolor=(0,0,0,1)

        ## Creating a layout for inserting images.
        self.imageside = GridLayout()
        self.imageside.cols = 1
        self.imageside.size_hint = (0.3, 0.7)
        self.imageside.pos_hint = {"center_x": 0.8, "center_y":0.5}

        self.vision_collector= GridLayout()
        self.vision_collector.cols=1

        self.mission_collector= GridLayout()
        self.mission_collector.cols=1

        self.logo=Image(pos=self.pos, size=self.size, source='logo.jpeg')
        self.logo2=Image(pos=self.pos, size=self.size, source='logo.jpeg')
        self.mission=Label(text='Mission Statement', font_size=16, bold=True, color= '#000000')
        self.mission_statement=Label(text='Our mission is to be market\nleader developing simple applications \n creating a revolution in development\n market',font_size=12, halign="left", color= '#1C2833')

        self.vision= Label(text="Achievements", font_size=16, halign="left", color='#000000', bold=True)
        self.vision_statement= Label(text='%%here will be the recent achievements\n of our company%%',font_size=12, halign="left",color='#000000')
        
        self.mission_collector.add_widget(self.logo)
        self.mission_collector.add_widget(self.mission)
        self.mission_collector.add_widget(self.mission_statement)

        self.vision_collector.add_widget(self.logo2)
        self.vision_collector.add_widget(self.vision)
        self.vision_collector.add_widget(self.vision_statement)

        self.imageside.add_widget(self.mission_collector)
        self.imageside.add_widget(self.vision_collector)

        self.add_widget(self.imageside)


        #image widget self.canvas.before will set image Pic.png as background
        Window.clearcolor=(0.9, 0.9, 0.9,1)
        # self.window.add_widget(Image(source = "Pic.png"))
 
        # label widget
        self.lable_user_name = Label(
                        text="Project name",
                        size_hint = (None, None),
                        width = 90,
                        height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_user_name = TextInput(multiline = False, padding_y = (20, 20), size_hint = (0.2,0.7))
        # self.lable_password = Label(
                        # text = "Project Domain",
                        # size_hint = (None, None),
                        # width = 90,
                        # height = 30,
                        # font_size = 13,
                        # color=(0,0,2,1)
                        # )
        #self.text_input_user_password = TextInput(
                   # multiline = False,
                   # padding_y = (20,20),
                   # size_hint = (0.2,0.7)
                   # )
         # label widget
        self.lable_description = Label(
                        text="Description",
                        size_hint = (None, None),
                        width = 90,
                        height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_description = TextInput(multiline = False, padding_y = (20, 20), size_hint = (0.2,3))
        #button widget
        self.button_assign = Button(
                      text = "Decline",
                      bold = True,
                      background_color = (0.7,0,0,1),
                    #   spacing=10
                      )
        #button widget
        self.button_cancel = Button(
                      text = "Accept",
                      bold = True,
                      background_color = (0,0,2,1),
                    #   spacing=10
                      )
        self.button_assign.pos_hint= (0,0.9)
        self.collector=GridLayout(padding=6)
        self.collector.cols=2
        # self.collector.pos_hint=(0,0.8),


        self.assign_to= GridLayout(row_force_default=True,
        row_default_height= 30,
        col_force_default=True,
        col_default_width=225)
        self.assign_to.cols=1
        self.lable_assign_to = Label(
                        text="Efforts",
                        # size_hint = (None,None),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_assign_to = TextInput(multiline = False, padding_y = 20)
        #self.lable_start_date = Label(
                        #text="Start Date",
                        # size_hint = (0.5,3),
                        #width = 90,
                        #height = 30,
                        #font_size = 13,
                        #color=(0,0,2,1)
                        #)
        # text input widget
        #self.text_input_start_date = TextInput(multiline = False, padding_y = 20)

        self.efforts= GridLayout(row_force_default=True,
        row_default_height=30,
        col_force_default=True,
        col_default_width=225)
        self.efforts.cols=1
        self.lable_efforts = Label(
                        text="Deadline",
                        # size_hint = (0.5,3),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_efforts = TextInput(multiline = False, padding_y =20)

        #self.lable_deadline = Label(
                        #text="Deadline",
                        # size_hint = (0.5,3),
                        # width = 90,
                        # height = 30,
                        #font_size = 13,
                        #color=(0,0,2,1)
                        #)
        # text input widget
        #self.text_input_deadline = TextInput(multiline = False, padding_y = 20)

        # nigotiation layout

        self.nigotiate= GridLayout()
        self.assign_to.cols=1
        self.nigotiate.pos_hint = {"center_x": 0.35, "center_y":0.7}
        self.nigotiate.size_hint= (0.6,0.2)

        # nigotiate button
        self.button_nigotiate = Button(
                      text = "Nigotiate",
                      bold = True,
                      background_color = (0,0,2,1),
                    #   spacing=10
                      )


        # Reason Lable
        self.lable_reason = Label(
                        text="Reason",
                        size_hint = (None,None),
                        width = 90,
                        height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input reason widget
        self.text_input_reason = TextInput(multiline = True)
        self.lable_propose_efforts = Label(
                        text="Propose your efforts",
                        # size_hint = (0.5,3),
                        #width = 90,
                        #height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input propose efforts widget
        self.text_input_propose_efforts = TextInput(multiline = False, size_hint=(0.6,0.2))


        #submit button

        self.button_submit = Button(
                      text = "Submit",
                      bold = True,
                      background_color = (0,0,2,1),
                      size_hint = (None,None),
                      width = 2 ,
                      height = 1 ,
                      pos_hint = (2,1)
                    #   spacing=10
                      )

        self.nigotiate.add_widget (self.button_nigotiate)
        self.nigotiate.add_widget (self.lable_reason)
        self.nigotiate.add_widget (self.text_input_reason)
        self.nigotiate.add_widget (self.lable_propose_efforts)
        self.nigotiate.add_widget (self.text_input_propose_efforts)
        self.nigotiate.add_widget (self.button_submit)

        self.button_assign.bind(on_press = self.assign_botton_pressed)

        # adding items to gridlayout that we've created above
        self.window.add_widget(self.lable_user_name)
        self.window.add_widget(self.text_input_user_name)
        #self.window.add_widget(self.lable_password)
        #self.window.add_widget(self.text_input_user_password)
        self.window.add_widget(self.lable_description)
        self.window.add_widget(self.text_description)
        self.assign_to.add_widget(self.lable_assign_to)
        self.assign_to.add_widget(self.text_input_assign_to)
        #self.assign_to.add_widget(self.lable_start_date)
        #self.assign_to.add_widget(self.text_input_start_date)
        #self.assign_to.add_widget(self.button_assign)
        self.efforts.add_widget(self.lable_efforts)
        self.efforts.add_widget(self.text_input_efforts)
        #self.efforts.add_widget(self.lable_deadline)
        #self.efforts.add_widget(self.text_input_deadline)
        self.collector.add_widget(self.assign_to)
        self.collector.add_widget(self.efforts)
        self.assign_to.add_widget(self.button_cancel)
        self.efforts.add_widget(self.button_assign)
        self.window.add_widget(self.collector)
        self.window.add_widget(self.nigotiate)

        ## self itself is a FloatLayout, so add the gridlayout(self.window) to it.
        self.add_widget(self.window)
        #return self.window

    def assign_botton_pressed(self,instance):
        pass

    # def on_size(self, *args):   
    #     self.bg.size = self.size
        
class SplashApp(App):
    def build(self):
        return SayHello()

if __name__ == "__main__":
    SplashApp().run()