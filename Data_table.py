from kivy.metrics import dp
from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window

class S_1(MDScreen):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# data_table = None
		self.window = MDBoxLayout()
		self.collector = MDGridLayout()
		self.my_task = MDGridLayout()
		self.label_my_task = MDLabel(
				text = "My Task",
				color = (0,0,0,1)
		)

		self.table_1 = MDDataTable(
			pos_hint={"center_y": 0.17, "center_x": 0.3},
            size_hint=(0.9, 0.6),
            #use_pagination=False,
			column_data = [
				("ID", dp(60)),
				("Title of Task", dp(100)),
				("Effort", dp(60)),
				("Deadline", dp(60))
			],
			row_data = [
				("", "", "", ""),
				("", "", "", ""),
				("", "", "", ""),
				("", "", "", ""),
			]

			)

		self.my_assigned_task = MDGridLayout()
		self.label_my_assigned_task = MDLabel(
				text = "My Assigned Task",
				color = (0,0,0,1),
		)

		self.table_2 = MDDataTable(
			pos_hint={"center_y": 0.9, "center_x": 0.3},
            size_hint=(0.1, 0.1),
            #use_pagination=False,
			column_data = [
				("ID", dp(60)),
				("Title of Task", dp(100)),
				("Effort", dp(60)),
				("Deadline", dp(60))
			],
			row_data = [
				("", "", "", ""),
				("", "", "", ""),
				("", "", "", ""),
				("", "", "", ""),
			])


		self.my_task.add_widget(self.label_my_task)
		self.my_task.add_widget(self.table_1)
		self.my_assigned_task.add_widget(self.label_my_assigned_task)
		self.my_assigned_task.add_widget(self.table_2)

		self.collector.add_widget(self.my_task)
		self.collector.add_widget(self.my_assigned_task)
		
		self.window.add_widget(self.collector)
		self.add_widget(self.window)
		
class myApp(MDApp):
	def build(self):
		return S_1()

if __name__ == "__main__":
    myApp().run()