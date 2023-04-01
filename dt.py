from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.uix.button import  MDRectangleFlatButton
from kivymd.uix.screen import MDScreen

class S_1(MDScreen):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# data_table = None
		#self.collector = MDGridLayout()
		#self.my_task = MDGridLayout(
			#pos_hint = {'center_x': 0.3,'center_y': 0.4},
			#size_hint = (300, 1000)

		#)
		self.size = (300,100)
		self.label_my_task = MDLabel(
				text = "My Task",
				color = (0,0,0,1),
				pos_hint = {"center_x": 0.15,"center_y": 0.9},
				size_hint=(0.2, 0.1)
		)

		self.table_1 = MDDataTable(
			pos_hint={"center_y": 0.7, "center_x": 0.5},
            size_hint=(0.9, 0.3),
			use_pagination=True,
			column_data = [
				("ID", dp(40)),
				("Title of Task", dp(100)),
				("Effort", dp(40)),
				("Deadline", dp(40))
			],
			row_data = [
				(f"{i+1}","", "", "", "") for i in range(50)
			],

			)

		self.label_my_assigned_task = MDLabel(
				text = "My Assigned Task",
				color = (0,0,0,1),
				pos_hint = {"center_x": 0.15,"center_y": 0.5},
				size_hint=(0.2, 0.1)
		)

		self.table_2 = MDDataTable(
			pos_hint={"center_y": 0.3, "center_x": 0.5},
            size_hint=(0.9, 0.3),
            use_pagination=True,
			column_data = [
				("ID", dp(40)),
				("Title of Task", dp(100)),
				("Effort", dp(40)),
				("Deadline", dp(40))
			],
			row_data = [
				(f"{i+1}","", "", "", "") for i in range(50)
			],
			)

		self.button_next = MDRectangleFlatButton(
				text = "Next",
				theme_text_color = "Custom",
				text_color = "black",
				md_bg_color = "lightblue",
				line_color = "lightblue",
				pos_hint={"center_y": 0.06, "center_x": 0.9},
            	size_hint=(0.1, 0.01),
		)

		self.button_previous = MDRectangleFlatButton(
				text = "Previous",
				theme_text_color = "Custom",
				md_bg_color = "grey",
				text_color = "black",
				line_color = "grey",
				pos_hint={"center_y": 0.06, "center_x": 0.1},
            	size_hint=(0.1, 0.01),
		)


		
		self.add_widget(self.label_my_task)
		self.add_widget(self.label_my_assigned_task)
		self.add_widget(self.table_1)
		self.add_widget(self.table_2)
		self.add_widget(self.button_next)
		self.add_widget(self.button_previous)
		#self.add_widget(self.button_previous)
		
		#self.collector.add_widget(self.my_task)
		
		#self.add_widget(self.collector)
		
class myApp(MDApp):
	def build(self):
		return S_1()

if __name__ == "__main__":
    myApp().run()