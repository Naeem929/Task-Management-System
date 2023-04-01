import json
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
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.layout import Layout
from kivy.uix.popup import Popup
import mysql.connector as connector
from kivy.app import runTouchApp
from kivy.uix.scrollview import ScrollView
from email.message import EmailMessage
import ssl
import smtplib
Person = ''

sm = ScreenManager()

# screens = [Screen(name='Title {}'.format(i)) for i in range(4)] 
# for i in range(4):
#     sm.add_widget(screens[i])

# LoginScreen
class LogIn_Screen(Screen):
    def __init__(self, **kwargs):
        super(LogIn_Screen, self).__init__(**kwargs)
        self.name='login'
        Window.clearcolor=(1,1,1,1)
        ## Creating a gridlayout for user, pwd and other items etc.
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.3, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        #add widgets to window

        #image widget self.canvas.before will set image Pic.png as background
        with self.canvas.before:
            self.bg = Image(pos=self.pos, size=self.size, source='Pic.png')
            self.bg.opacity=0.4
        # self.window.add_widget(Image(source = "Pic.png"))
        

        self.collector1=GridLayout(spacing=120,row_force_default = True, 
                 row_default_height=70)
        self.collector1.cols=2

        self.button_admin = Button(
                        text="Admin",
                        font_size = 20,
                        bold = True,
                        color=(1,1,1,1),
                        background_color = "#0323EE"
                        )
       # self.button_admin.bind(on_press = self.button_admin_pressed)
        #def botton_admin_pressed(self, instance):
         #   color = (1,1,1,0.1)
        
     
        self.button_employee = Button(
                      text = "Employee",
                      size_hint = (1,0.5),
                      bold = True,
                      font_size = 20,
                      background_color = '#FE1902'
                      )
        

        # label widget
        self.lable_user_name = Label(
                        text="User name",
                        size_hint = (None, None),
                        width = 90,
                        height = 30,
                        font_size = 18,
                        color='#00000',
                        bold = True
                        )
        # text input widget
        self.text_input_user_name = TextInput(multiline = False, #padding_y = (20, 20),
                                            size_hint = (1,0.3),hint_text='xyz@gmail.com')
                                            # width = 10,
                                            # height=20
        self.lable_password = Label(
                         text = "Password",
                         size_hint = (None, None),
                         width = 75,
                         height = 40,
                         font_size = 18,
                         color='#00000',
                         bold = True
                        )
        self.text_input_user_password = TextInput(
                    multiline = False,
                    password= True,
                    hint_text= "Enter Password",
                    handle_image_right= 'eye.png',
                    #padding_y = (20,20),
                    size_hint = (1,0.3)
                    )
        
        self.label_forget_password = Label(text="                                                                                                                                                                                             Forget Password",                                                                                                                               
                        size_hint = (None, None),
                        width = 155,
                        height = 20,
                        font_size = 12,
                        #padding_y = (200,20),
                        color='#564AE1',
                        pos_hint = {"center_x":0.8, "center_y":0.8},
                        bold=True
                        )
        
        self.label_dont_account = Label(
                         text="didn't have account",
                         size_hint = (None, None),
                         width = 105,
                         height = 20,
                         font_size = 12,
                         #padding_y = (200,20),
                         color='#434642',
                         bold = True
                        )

        self.collector=GridLayout(spacing =270 ,row_force_default = True, 
                 row_default_height=40, col_force_default = True, col_default_width = 70 
                  #col_force_default=True,
                  #col_default_width=100
                )
        self.collector.cols=2

        #self.sign_up = GridLayout()
        #self.sign_up.cols=1
        self.button_sign_up = Button(
                        text="Sign up",
                        size_hint = (1,0.7),
                        height=100,
                        width=100,
                        bold = True,
                     #   background_color = '#335BFF',
                      )
        self.button_sign_up.bind(on_release=self.button_Signup_pressed)
        


        #button widget
        #self.login = GridLayout()
        #self.login.cols=1
        self.button_login = Button(
                      text = "log in",
                      size_hint = (1,0.7),
                      height=40,
                      width=100,
                      bold = True,
                      background_color = '#187603'
                      )

        self.button_login.bind(on_press= self.button_login_pressed)


        self.Gap = Label(text="  \n   ")
     #   self.button_login.bind(on_press = self.button_login_pressed)
        
        ## adding items to gridlayout that we've created above
        self.collector1.add_widget(self.button_admin)
        self.collector1.add_widget(self.button_employee)
        self.window.add_widget(self.collector1)
        self.window.add_widget(self.lable_user_name)
        self.window.add_widget(self.text_input_user_name)
        self.window.add_widget(self.lable_password)
        self.window.add_widget(self.text_input_user_password)
        self.window.add_widget(self.label_forget_password)
        self.window.add_widget(self.Gap)
        self.window.add_widget(self.label_dont_account)
        #self.window.add_widget(self.button_login)
        #self.sign_up.add_widget(self.button_sign_up)
        #self.login.add_widget(self.button_login)
        self.collector.add_widget(self.button_sign_up)
        self.collector.add_widget(self.button_login)
        self.window.add_widget(self.collector)
        
        self.add_widget(self.window)
        # sm.add_widget(self)
        
        #self.greeting1.text = "Hello Mr. " + self.user.text + "...!"

    def on_size(self, *args):   
        self.bg.size = self.size

    
    def button_login_pressed(self, instance):
        self.con = connector.connect(host='localhost',
                port = '3306',
                user = 'samad',
                password = 'pass123',
                database = 'pythontest',
                auth_plugin = 'mysql_native_password')


        #def fetch_all(self):
        query = "select * from Register_table"
        cur = self.con.cursor()
        cur.execute(query)
        login_status="no"
        for row in cur:
            lst = list(row)
            if self.text_input_user_name.text in lst and self.text_input_user_password.text in lst:
                login_status= "yes"
            
        if login_status == "yes":
            sm.current='mytasks'

              

            #print("Name: ", row [0])
            #print("Date Of Birth: ", row[1])
            #print("Contact: ", row[2])
            #print("Email: ", row [3])
            #print("User Name: ", row[4])
            #print("password: ", row[5])
        #    print("Confirm Password: "row[6])
            #print()
            #print()


        else:
        # if self.text_input_user_name.text not in lst:
                layout = GridLayout(cols = 1, padding = 10)
  
                popupLabel = Label(text = "incorrect username/password- \n kindly re-enter valid \n username/password ")
                closeButton = Button(text = "Close", size_hint=(0.1,0.1), pos_hint=(0.5,0.5))
    
                layout.add_widget(popupLabel)
                layout.add_widget(closeButton)       
    
            # Instantiate the modal popup and display
                popup = Popup(title ='Login Error',
                        content = layout,
                        size_hint =(0.3, 0.3))
                self.background_color='#030303'
                popup.open()   
                closeButton.bind(on_release = popup.dismiss)
        # self.logger=self.text_input_user_name
        global Person
        Person = self.text_input_user_name.text
        self.text_input_user_name.text=''
        self.text_input_user_password.text=''

        # if self.text_input_user_name.text=='' or self.text_input_user_password.text =='':
        #     layout = GridLayout(cols = 1, padding = 10)
  
        #     popupLabel = Label(text = "Mandatory fields incomplete \n Review and submit again ")
        #     closeButton = Button(text = "Close", size_hint=(0.1,0.1), pos_hint=(0.5,0.5))
    
        #     layout.add_widget(popupLabel)
        #     layout.add_widget(closeButton)       
    
        #     # Instantiate the modal popup and display
        #     popup = Popup(title ='Incomplete Credentials',title_size=16,
        #                 content = layout,
        #                 size_hint =(0.3, 0.3))
        #     self.background_color='#030303'
        #     popup.open()   
        #     closeButton.bind(on_press = popup.dismiss)  
        # self.clear_widgets()
        # self.add_widget(Assign_Task_Screen())
        # if self.text_input_user_password.text == "1234" and self.text_input_user_name.text == "Muhammad Aliyan":
        #else:
         #   sm.current='mytasks'     
          #  self.text_input_user_name.text=''
           # self.text_input_user_password.text=''
        
        # .manager.transition.direction="left" 
    def button_Signup_pressed(self, instance):
        # self.clear_widgets()
        # self.add_widget(Registration_UI()) 
        sm.current='register'
# My Tasks Screen
class Task_Screen(Screen):
    def __init__(self, **kwargs):
        super(Task_Screen, self).__init__(**kwargs)

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
        self.Assign_Task.bind(on_release=self.Assign_Task_button_pressed)
        self.top_grid.add_widget(self.Assign_Task)
      
        self.My_Tasks = Button(text='My Tasks')
        self.My_Tasks.bind(on_release=self.My_Task_button_pressed)
        self.top_grid.add_widget(self.My_Tasks)

        self.Profile = Button(text='Profile',size_hint_x=None, width=80, pos_hint={1,None})
        self.Profile.bind(on_release= self.Profile_button_pressed)
        self.top_grid.add_widget(self.Profile)

        self.logout = Button(text='Logout',size_hint_x=None, width=80, pos_hint={1,None})
        self.logout.bind(on_release=self.logout_button_pressed)
        self.top_grid.add_widget(self.logout)

        # Add top_grid into main grid as a widget
        self.add_widget(self.top_grid)      
        Window.clearcolor=(0.9, 0.9, 0.9,1)
        
        # adding layout for name and picture
        self.user_details_layout= GridLayout(cols=2, size_hint=(0.2,0.2), pos_hint={'right':1,'y':0.72})

        self.user_name=Label(text=str(Person) ,font_name='Comic',font_size=16,color=(0,0,0,1), bold= True) #this variable will contain the user name fetched from the DB 
        self.user_picture=Image(pos=self.pos, size=self.size, source='loginpic.png')

        self.user_details_layout.add_widget(self.user_name)
        self.user_details_layout.add_widget(self.user_picture)

        self.add_widget(self.user_details_layout)
        self.My_task_lable=AnchorLayout(pos_hint={'x':0.01,'y':0.75},size_hint=(0.2,0.07))
        self.My_task_lable.add_widget(Label(text='My Tasks',color=(0,0,0,1),font_size=23,italic=True,bold=True))
        self.add_widget(self.My_task_lable)

        self.My_task_table=GridLayout(
            cols=5, spacing=5, size_hint_y=None
            )
        #self.My_task_table.cols = 2
        #orientation = 'tb-lr'
        # Make sure the height is such that there is something to scroll.
        self.My_task_table.bind(minimum_height=self.My_task_table.setter('height'))
        self.con = connector.connect(host='localhost',
                port = '3306',
                user = 'samad',
                password = 'pass123',
                database = 'pythontest',
                auth_plugin = 'mysql_native_password')

    #    def fetch_all(self):
        query = "select * from admininterface_table where assign_to = Assigner"
        cur = self.con.cursor()
        cur.execute(query)
     #   for row in cur:
     #       print("Project Name: ", row [0])
      #      print("Project domain: ", row[1])
      #      print("Description:", row[2])
       ##    print("Effort: ", row[4])
         #   print("Start date:", row[5])
          #  print("dead line", row[6])
        #    print("Confirm Password: "row[6])
       #     print()
        #    print()

        for row in cur:
            for i in [0,1,5,6,7]:
                btn = Label(text=str(row[i]), size_hint_y=None,height=25, color=(0, 0, 0, 1))
                self.My_task_table.add_widget(btn)
        root = ScrollView(
            size_hint=(0.8, 0.3), 
            pos_hint={'x':0.1, 'y':0.45}
            #size=(0.2, 0.2)
            #size=(Window.width, Window.height)
            )
        #self.My_task_table.add_widget(root)
        root.add_widget(self.My_task_table)
        #self.add_widget(self.My_task_table)
        self.add_widget(root)
        # runTouchApp(root)

        self.Assigned_task_lable=AnchorLayout(pos_hint={'x':0.05,'y':0.37},size_hint=(0.2,0.07))
        self.Assigned_task_lable.add_widget(Label(text='My Assigned Tasks',color=(0,0,0,1),font_size=23,italic=True,bold=True))
        self.add_widget(self.Assigned_task_lable)

        self.Assigned_task_table=GridLayout(
            cols=5, spacing=10, size_hint_y=None
            )
        #self.My_task_table.cols = 2
        #orientation = 'tb-lr'
        # Make sure the height is such that there is something to scroll.
        self.Assigned_task_table.bind(minimum_height=self.Assigned_task_table.setter('height'))
        self.con = connector.connect(host='localhost',
                port = '3306',
                user = 'samad',
                password = 'pass123',
                database = 'pythontest',
                auth_plugin = 'mysql_native_password')

    #    def fetch_all(self):
        query = "select * from admininterface_table where Assigner = Assigner"
        cur = self.con.cursor()
        cur.execute(query)
     #   for row in cur:
     #       print("Project Name: ", row [0])
      #      print("Project domain: ", row[1])
      #      print("Description:", row[2])
       ##    print("Effort: ", row[4])
         #   print("Start date:", row[5])
          #  print("dead line", row[6])
        #    print("Confirm Password: "row[6])
       #     print()
        #    print()

        for row in cur:
            for i in [0,1,3,5,6]:
                btn = Label(text=str(row[i]), size_hint_y=None,height=25, color=(0, 0, 0, 1))
                self.Assigned_task_table.add_widget(btn)
        root = ScrollView(
            size_hint=(0.8, 0.3), 
            pos_hint={'x':0.1, 'y':0.06}
            #size=(0.2, 0.2)
            #size=(Window.width, Window.height)
            )
        #self.My_task_table.add_widget(root)
        root.add_widget(self.Assigned_task_table)
        #self.add_widget(self.My_task_table)
        self.add_widget(root)
        # runTouchApp(root)


    def Assign_Task_button_pressed(self, instance):
        sm.current='assigntask'
        # return(Assign_Task_Screen)

    def My_Task_button_pressed(self, instance):
        sm.current='mytasks'
        # sm.refresh(Task_Screen)

    def Profile_button_pressed(self, instance):
        layout = GridLayout(cols = 1, padding = 10, spacing = 10)
  
        popupLabel = Label(text = "This feature is under \n development")
        popupLabe2 = Image(source='gugh.png',size=(200,200))
        closeButton = Button(text = "Close", size_hint=(0.1,0.1), pos_hint=(0.5,0.5))

        layout.add_widget(popupLabel)
        layout.add_widget(popupLabe2)
        layout.add_widget(closeButton)       

        # Instantiate the modal popup and display
        popup = Popup(title ='Oops',
                    content = layout,
                    size_hint =(0.3, 0.3))
        self.background_color='#030303'
        popup.open()   

    # Attach close button press with popup.dismiss action
        closeButton.bind(on_press = popup.dismiss)

    def logout_button_pressed(self,instance):
        sm.current='login'
        # sm.refresh()

# Assigning Task Screen
class Assign_Task_Screen(Screen):
    def __init__(self, **kwargs):
        self.name='assigntask'
        super(Assign_Task_Screen, self).__init__(**kwargs)

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
        self.Assign_Task.bind(on_release=self.Assign_Task_button_pressed)
        self.top_grid.add_widget(self.Assign_Task)

        self.My_Tasks = Button(text='My Tasks')
        self.My_Tasks.bind(on_release=self.My_Task_button_pressed)
        self.top_grid.add_widget(self.My_Tasks)

        self.Profile = Button(text='Profile',size_hint_x=None, width=80, pos_hint={1,None})
        self.Profile.bind(on_release= self.Profile_button_pressed)
        self.top_grid.add_widget(self.Profile)

        self.logout = Button(text='Logout',size_hint_x=None, width=80, pos_hint={1,None})
        self.logout.bind(on_release=self.logout_button_pressed)
        self.top_grid.add_widget(self.logout)

       
        # Add top_grid into main grid as a widget
        self.add_widget(self.top_grid)
        
        #add widgets to windowy
  
        ## Creating a gridlayout for user, pwd and other items etc.
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
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

        self.logo=Image(pos=self.pos, size=self.size, source='side_logo.jpg')
        self.logo2=Image(pos=self.pos, size=self.size, source='side_logo.jpg')
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
                        text="Task name",
                        size_hint = (None, None),
                        width = 90,
                        height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_user_name = TextInput(multiline = False, padding_y = (10, 10), size_hint = (0.2,0.7))
        self.lable_password = Label(
                         text = "Task Domain",
                         size_hint = (None, None),
                         width = 90,
                         height = 30,
                         font_size = 13,
                         color=(0,0,2,1)
                        )
        self.text_input_user_password = TextInput(
                    multiline = False,
                    padding_y = (10,10),
                    size_hint = (0.2,0.7)
                    )
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
        self.text_description = TextInput(multiline = True, padding_y = (10, 10), size_hint = (0.2,3))
        #button widget
        self.button_assign = Button(
                      text = "Assign",
                      bold = True,
                      background_color = (0,0,2,1),
                    #   spacing=10
                      )

        #button widget
        self.button_cancel = Button(
                      text = "Cancel",
                      bold = True,
                      background_color = (0.7,0,0,1),
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
                        text="Assign to",
                        # size_hint = (None,None),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_assign_to = TextInput(multiline = False, padding_y = 5)
        self.lable_start_date = Label(
                        text="Start Date",
                        # size_hint = (0.5,3),
                        #width = 90,
                        #height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_start_date = TextInput(multiline = False, padding_y = 5,hint_text = 'dd-mm-yyyy')

        self.efforts= GridLayout(row_force_default=True,
        row_default_height=30,
        col_force_default=True,
        col_default_width=225)
        self.efforts.cols=1
        self.lable_efforts = Label(
                        text="Efforts",
                        # size_hint = (0.5,3),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_efforts = TextInput(multiline = False, padding_y =5,hint_text = '123 hrs/day')

        self.lable_deadline = Label(
                        text="Deadline",
                        # size_hint = (0.5,3),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_deadline = TextInput(multiline = False, padding_y = 5,hint_text = "dd-mm-yyyy")

        self.button_assign.bind(on_press = self.assign_botton_pressed)

        # adding items to gridlayout that we've created above
        self.window.add_widget(self.lable_user_name)
        self.window.add_widget(self.text_input_user_name)
        self.window.add_widget(self.lable_password)
        self.window.add_widget(self.text_input_user_password)
        self.window.add_widget(self.lable_description)
        self.window.add_widget(self.text_description)
        self.assign_to.add_widget(self.lable_assign_to)
        self.assign_to.add_widget(self.text_input_assign_to)
        self.assign_to.add_widget(self.lable_start_date)
        self.assign_to.add_widget(self.text_input_start_date)
        #self.assign_to.add_widget(self.button_assign)
        self.efforts.add_widget(self.lable_efforts)
        self.efforts.add_widget(self.text_input_efforts)
        self.efforts.add_widget(self.lable_deadline)
        self.efforts.add_widget(self.text_input_deadline)
        self.collector.add_widget(self.assign_to)
        self.collector.add_widget(self.efforts)
        self.assign_to.add_widget(Label(text='\n'))
        self.assign_to.add_widget(self.button_cancel)
        self.efforts.add_widget(Label(text='\n'))
        self.efforts.add_widget(self.button_assign)
        self.window.add_widget(self.collector)
        self.add_widget(self.window)
        self.con = connector.connect(host='localhost',
                port = '3306',
                user = 'samad',
                password = 'pass123',
                database = 'pythontest',
                auth_plugin = 'mysql_native_password')

#
        query = 'create table if not exists admininterface_table(name varchar(100) primary key,domain varchar(50),description varchar(200),assign_to varchar(50) ,effort varchar(50),start_date varchar(20), deadline varchar(20), Assigner varchar(100))'#, cpassword varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("admin table created")


    def insert_user(self,name,domain,description,assign_to,effort,start_date,deadline,Assigner):
        query = "insert into admininterface_table(name,domain,description,assign_to,effort,start_date,deadline,Assigner) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,domain,description,assign_to,effort,start_date,deadline,Person)

        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("details saved to db")


 #   def fetch_all(self):
  #      query = "select * from admin_table"
   #     cur = self.con.cursor()
    #    cur.execute(query)
     #   for row in cur:
     #       print("Project Name: ", row [0])
      #      print("Project domain: ", row[1])
      #      print("Description:", row[2])
       ##    print("Effort: ", row[4])
         #   print("Start date:", row[5])
          #  print("dead line", row[6])
        #    print("Confirm Password: "row[6])
       #     print()
        #    print()


    def assign_botton_pressed(self, instance):
        
        name = self.text_input_user_name.text
        domain = self.text_input_user_password.text
        description = self.text_description.text
        assign_to = self.text_input_assign_to.text
        effort = self.text_input_efforts.text
        start_date = self.text_input_start_date.text
        deadline = self.text_input_deadline.text
        Assigner = Person
        Assign_Task_Screen.insert_user(self,name,domain,description,assign_to,effort, start_date, deadline,Assigner)
        
        email_sender = 'taskmanagementsystem3@gmail.com'
        email_password = 'phawrvrennykpyxz'
        #Person = LogIn_Screen.self.text_input_user_name.text

        email_receiver = [assign_to]#,'aliyanmujahid2000@gmail.com']
        subject=name
        body = "Hello! Dear Employee you have been assigned a new task by Mr." + Person +" for further details login to your TMS account" 
        # print(Person)
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        # print("mail sent")
        layout = GridLayout(cols = 1, padding = 10, spacing = 10)
  
        popupLabel = Label(text = "The task has been assigned ")
        popupLabe2 = Image(source='tick.png',size=(300,250))
        closeButton = Button(text = "Ok", size_hint=(0.1,0.1), pos_hint=(0.5,0.5))

        layout.add_widget(popupLabel)
        layout.add_widget(popupLabe2)
        layout.add_widget(closeButton)       

        # Instantiate the modal popup and display
        popup = Popup(title ='Assigned',
                    content = layout,
                    size_hint =(0.3, 0.3))
        self.background_color='#90EE90'
        popup.open()   

    # Attach close button press with popup.dismiss action
        closeButton.bind(on_press = popup.dismiss)

        # Clearing data after once entered
        self.text_input_user_name.text =''
        self.text_input_user_password.text=''
        self.text_description.text=''
        self.text_input_assign_to.text=''
        self.text_input_efforts.text=''
        self.text_input_start_date.text=''
        self.text_input_deadline.text=''
        

        
        ## self itself is a FloatLayout, so add the gridlayout(self.window) to it.
      #  self.add_widget(self.window)
        #return self.window
        # sm.add_widget(self)

    def Assign_Task_button_pressed(self, instance):
        sm.current='assigntask'

    def My_Task_button_pressed(self, instance):
        sm.current='mytasks'

    def Profile_button_pressed(self, instance):
        layout = GridLayout(cols = 1, padding = 10, spacing = 10)
  
        popupLabel = Label(text = "This feature is under \n development")
        popupLabe2 = Image(source='gugh.png',size=(200,200))
        closeButton = Button(text = "Close", size_hint=(0.1,0.1), pos_hint=(0.5,0.5))

        layout.add_widget(popupLabel)
        layout.add_widget(popupLabe2)
        layout.add_widget(closeButton)       

        # Instantiate the modal popup and display
        popup = Popup(title ='Oops',
                    content = layout,
                    size_hint =(0.3, 0.3))
        self.background_color='#030303'
        popup.open()   

    # Attach close button press with popup.dismiss action
        closeButton.bind(on_press = popup.dismiss)

    def logout_button_pressed(self,instance):
        sm.current='login'


    #def assign_botton_pressed(self,instance):

        
    
# RegisterScreen
class Registration_UI(Screen):
    def __init__(self, **kwargs):
        super(Registration_UI, self). __init__(**kwargs)
        self.name='register'
        self.cols = 1
        self.orientation= 'vertical'
        Window.clearcolor=(1,1,1,1)

        #image widget self.canvas.before will set image Pic.png as background
        with self.canvas.before:
            self.bg= Image(pos=self.pos, size=self.size, source='Pic.png')
            self.bg.opacity=0.4

        # adding heading on the registration page
        self.add_widget(Label(text="REGISTRATION",
            font_size=26, 
            pos_hint={"center_x":0.5,"center_y":0.95},
            size_hint_x= None,
            height=70,
            size_hint_y= None,
            width = 300,
            bold=True,
            color='#000000'))
            
        # Add Another Grid for text to be entered and one main grid for submit button and result
        self.top_grid = GridLayout(row_force_default=True,
        row_default_height=50,
        spacing=10)
        self.top_grid.cols = 2
        self.top_grid.size_hint= (0.5,0.7)
        self.top_grid.pos_hint= {"center_x":0.5, "center_y":0.5}

        


        # Add widget
        self.top_grid.add_widget(Label(text="Name", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.Uname = TextInput(multiline=False,hint_text='Enter Your Full Name')
        self.top_grid.add_widget(self.Uname)

        self.top_grid.add_widget(Label(text="Date Of Birth", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.date = TextInput(multiline=False,hint_text='dd-mm-yyyy')
        self.top_grid.add_widget(self.date)

        self.top_grid.add_widget(Label(text="Contact", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.contact = TextInput(multiline=False,hint_text='+92-123-456789')
        self.top_grid.add_widget(self.contact)

        self.top_grid.add_widget(Label(text="Email", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.mail = TextInput(multiline=False,hint_text='xyz@gmail.com')
        self.top_grid.add_widget(self.mail)

        self.top_grid.add_widget(Label(text="User Name", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.username = TextInput(multiline=False,hint_text='could be same as Name')
        self.top_grid.add_widget(self.username)

        self.top_grid.add_widget(Label(text="Password", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.password = TextInput(multiline=False, password=True, hint_text='******')
        self.top_grid.add_widget(self.password)

        self.top_grid.add_widget(Label(text="Confirm Password", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.cpass = TextInput(multiline=False,password= True,hint_text='must be same as password')
        self.top_grid.add_widget(self.cpass)

        # if self.cpass.text != self.password.text:
        #     print("Re-Enter same password")

        # Add top_grid into main grid as a widget
        self.add_widget(self.top_grid)

        # Creating Image Upload Button
        self.upload = Button(text="Upload Image", font_size=22,
        pos_hint={"center_x":0.5,"center_y":0.199},
        size_hint_x= None,
        height=70,
        size_hint_y= None,
        width = 250,
        background_color='#0000FF')
        self.upload.bind(on_release = self.upload_photo)
        self.add_widget(self.upload)
        self.add_widget(Label(text="or drop a file",
            font_size=16, 
            pos_hint= {"center_x":0.5,"center_y":0.129},
            size_hint_x= None,
            height=30,
            size_hint_y= None,
            width = 250,
            color='#000000'))

        self.register_back_button_collector=GridLayout(pos_hint={'x':0.4,'y':-0.1},size_hint=(0.7,None), height=150,spacing=265)
        self.register_back_button_collector.cols=2
        # Creating Submit Button
        self.submit = Button(text="Register", font_size=18,
        pos_hint={"x":0.7},
        size_hint_x= None,
        width=100,
        size_hint_y= None,
        height = 50,
        background_color='#008000')

        # Creating Back Button
        self.back = Button(text="Back", font_size=18,
        pos_hint={"x":1},
        size_hint_x= None,
        width=100,
        size_hint_y= None,
        height = 50,
        background_color='#696969')

        self.submit.bind(on_release = self.submit_button_released)
        self.back.bind(on_release= self.back_button_pressed)
        
        self.register_back_button_collector.add_widget(self.back)
        self.register_back_button_collector.add_widget(self.submit)
        
        self.add_widget(self.register_back_button_collector)
        # sm.add_widget(self)


    #def submit_button_released(self, instance):
        self.con = connector.connect(host='localhost',
                port = '3306',
                user = 'samad',
                password = 'pass123',
                database = 'pythontest',
                auth_plugin = 'mysql_native_password')


        query = 'create table if not exists Register_table(name varchar(50),DOB varchar(20),contact varchar(20), email varchar(40) primary key not null, username varchar(200), password varchar(12))'#, cpassword varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("registration table created")


    def insert_user(self,name,DOB,contact,email, username, password) :
            query = "insert into Register_table(name,DOB,contact,email, username, password) values('{}','{}','{}','{}','{}','{}')".format(name,DOB,contact,email, username, password)

            print(query)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("user saved to db")


   # def fetch_all(self):
    #    query = "select * from registration_table"
     #   cur = self.con.cursor()
      # for row in cur:
       #     print("Name: ", row [0])
        #    print("Date Of Birth: ", row[1])
         #   print("Contact: ", row[2])
          #  print("Email: ", row [3])
           # print("User Name: ", row[4])
           # print("password: ", row[5])
        #    print("Confirm Password: "row[6])
           # print()
           # print()


    def submit_button_released(self, instance):
        name = self.Uname.text
        DOB = self.date.text
        contact = self.contact.text
        email = self.mail.text
        username = self.username.text
        password = self.password.text
        
       # MyLayout.fetch_all(self)
        # self.add_widget(Label(text=f'Thank you Mr {name}, your details has been updated, please enter your credentials and login'))

        # Clearing data after once entered
        
        if self.cpass.text != self.password.text:
            layout = GridLayout(cols = 1, padding = 10)
  
            popupLabel = Label(text = "password and confirm- \n password are not same")
            closeButton = Button(text = "Close", size_hint=(0.1,0.1), pos_hint=(0.5,0.5))
    
            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)       
    
            # Instantiate the modal popup and display
            popup = Popup(title ='Re-enter Credentials',
                        content = layout,
                        size_hint =(0.3, 0.3))
            self.background_color='#030303'
            popup.open()   
            closeButton.bind(on_release = popup.dismiss)

        if self.Uname.text=='' or self.date.text=='' or self.contact.text=='' or self.mail.text=='' or self.username.text=='' or self.password.text=='':
            layout = GridLayout(cols = 1, padding = 10)
  
            popupLabel = Label(text = "Mandatory fields incomplete \n Review and submit again ")
            closeButton = Button(text = "Close", size_hint=(0.1,0.1), pos_hint=(0.5,0.5))
    
            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)       
    
            # Instantiate the modal popup and display
            popup = Popup(title ='Incomplete data',title_size=16,
                        content = layout,
                        size_hint =(0.3, 0.3))
            self.background_color='#030303'
            popup.open()   
            closeButton.bind(on_press = popup.dismiss)            
        # Attach close button press with popup.dismiss action
          
        else:
            # self.clear_widgets()
            # self.add_widget(LogIn_Screen())
            nam = self.Uname.text
            DOB = self.date.text
            contact = self.contact.text
            email = self.mail.text
            username = self.username.text
            password = self.password.text
            Registration_UI.insert_user(self,name,DOB,contact,email,username,password)

# here the data needs to be sent to server before being erased
            sm.current='login'

        # # Clearing data after once entered
            self.username.text =''
            self.date.text =''
            self.contact.text =''
            self.mail.text =''
            self.username.text =''
            self.password.text =''
            self.cpass.text =''
    
    def on_size(self, *args):   
        self.bg.size = self.size
     
    def upload_photo(self, instance):
        layout = GridLayout(cols = 1, padding = 10, spacing = 10)
  
        popupLabel = Label(text = "This feature is under \n development")
        popupLabe2 = Image(source='gugh.png',size=(200,200))
        closeButton = Button(text = "Close", size_hint=(0.1,0.1), pos_hint=(0.5,0.5))

        layout.add_widget(popupLabel)
        layout.add_widget(popupLabe2)
        layout.add_widget(closeButton)       

        # Instantiate the modal popup and display
        popup = Popup(title ='Oops',
                    content = layout,
                    size_hint =(0.3, 0.3))
        self.background_color='#030303'
        popup.open()   

    # Attach close button press with popup.dismiss action
        closeButton.bind(on_press = popup.dismiss)

    def back_button_pressed(self,instance):
        sm.current='login'


# class ParentScreen2(Screen):
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)
#         super_box=BoxLayout(orientation ='vertical')
#         csm=ScreenManager()
#         cs1=LogIn_Screen(name="login")
#         cs2=Registration_UI(name="register")
#         csm.add_widget(cs1)
#         csm.add_widget(cs2)
#         csm.current="child_screen1"
#         self.csm=csm



class SplashApp(App):
    def build(self): 
        # sm = ScreenManager()
        sm.add_widget(LogIn_Screen(name='login'))
        sm.add_widget(Registration_UI(name='register'))
        sm.add_widget(Assign_Task_Screen(name='assigntask'))
        sm.add_widget(Task_Screen(name='mytasks'))
        sm.current='login'

        return sm

if __name__ == "__main__":
    SplashApp().run() 