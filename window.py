from PyQt5.QtWidgets import *
import sys


class App(QWidget):

	def __init__(self):
		super().__init__()
		self.title='RENAME MACHINE'
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.resize(800,600)
		self.center()
		girdLayout=self.layout()
		self.setLayout(girdLayout)

		self.show()


	def layout(self):
		layout=QGridLayout()
		checkbox_group_layout=QGridLayout()
		action_button_layout=QGridLayout()

		# self.source_text=self.text_show()
		# self.destination_text=self.text_show()
		self.file_list_source=self.file_list()
		self.file_list_destination=self.file_list()
		
		cb_number=self.check_button('Number Order')
		cb_letter=self.check_button('Letters')
		self.file_name_input=self.file_name_input()
		add_button=self.button('Add')
		remove_button=self.button('Remove')


		action_group_button=self.group_button()
		action_group_button.addButton(add_button)
		action_group_button.addButton(remove_button)



		group_button=self.group_button()
		group_button.addButton(cb_number)
		group_button.addButton(cb_letter)


		checkbox_group_box=self.group_box('Choose the Mode')
		action_button_group_box=self.group_box('')

		

		# cb_number.stateChanged.connect(self.do_math)
		# cb_letter.stateChanged.connect(self.do_math)
		group_button.buttonToggled.connect(self.on_button_toggled)
		action_group_button.buttonClicked.connect(self.open_file)

		checkbox_group_layout.addWidget(cb_number,0,0)
		checkbox_group_layout.addWidget(cb_letter,0,1)
		checkbox_group_box.setLayout(checkbox_group_layout)

		action_button_layout.addWidget(add_button,0,0)
		action_button_layout.addWidget(remove_button,0,1)
		action_button_group_box.setLayout(action_button_layout)

		# layout.addWidget(self.source_text,0,0)
		# layout.addWidget(self.destination_text,0,1)
		layout.addWidget(self.file_list_source,0,0)
		layout.addWidget(self.file_list_destination,0,1)
		

		layout.addWidget(action_button_group_box,1,0)

		layout.addWidget(checkbox_group_box,2,0)
		layout.addWidget(self.file_name_input,2,1)
	


		return layout


	def center(self):
		qr=self.frameGeometry()
		cp=QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def text_show(self):
		textEdit=QTextEdit()
		textEdit.setPlainText("Example text")
		textEdit.setStyleSheet("background-color:white;")
		textEdit.setReadOnly(True)
		return textEdit

	def check_button(self,title):
		check_button=QCheckBox(title)


		return check_button

	def group_box(self,title):
		group_box=QGroupBox(title)

		return group_box

	def check_button_state(self):

		b=self.sender()

		if b.isChecked()==True:
			print (f'The text from the check bos is: {b.text()}')
			return b.text()


	def group_button(self):
		group_button=QButtonGroup(self)

		# cb_number=QRadioButton('Number Order')
		# cb_letter=QRadioButton('Letters')
		# group_button.addButton(cb_number,id=1)
		# group_button.addButton(cb_letter,id=2)

		return group_button

	def file_name_input(self):
		file_name_input=QLineEdit()
		
		file_name_input.setMaxLength(20)
		file_name_input.setReadOnly(True)

		return file_name_input


	def button(self,title):
		button=QPushButton(title)

		return button

	def on_button_toggled(self,button,checked):

		if checked:

			button_text=button.text()

			if button_text=='Letters':
				print ('RIGHT')
				self.file_name_input.setReadOnly(False)
				self.file_name_input.setFocus()
				self.file_name_input.setPlaceholderText('Please Enter the filename')
				self.file_name_input.setStyleSheet("""
					QLineEdit{

					border-radius: 5px;
					border-bottom: 2px solid blue;
					padding:0.5em 1em;

					}
					""")
			
			elif button_text=='Number Order':
				self.file_name_input.setPlaceholderText('')
				self.file_name_input.setReadOnly(True)
				self.file_name_input.clearFocus()
				self.file_name_input.setStyleSheet("""
					QLineEdit{

					background-color:white;
					
					}
					""")

	def open_file(self,button):
		button_text=button.text()
		print (f'The button you clicked is {button_text}')
		if button_text=="Add":
			file_open=QFileDialog()
			filenames=file_open.getOpenFileNames(None,"Select the files",'.','All files(*.*)')

			if filenames[0]:
				print (f'You select the file is {filenames}')

				for f in filenames[0]:
					self.file_list_source.addItem(QListWidgetItem(f))

	def file_list(self):
		file_list=QListWidget()

		return file_list

	def do_math(self):



		pass
		# check_text=self.check_button_state()

		# if check_text=="Number Order":
		# 	print ('LEFT')
		# elif check_text=="Letters":
		# 	print ('RIGHT')



if __name__=='__main__':

	app=QApplication(sys.argv)
	ex=App()
	sys.exit(app.exec_())