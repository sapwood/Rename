from PyQt5.QtWidgets import *
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys,os


class App(QWidget):

	def __init__(self):
		super().__init__()
		self.title='RENAME MACHINE'
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.resize(1000,1000)
		self.center()
		girdLayout=self.layout()
		self.setLayout(girdLayout)

		self.show()


	def layout(self):
		layout=QGridLayout()
		
		# add_remove_group_layout=QGridLayout()




		self.file_list_source=self.file_list()
		self.file_list_destination=self.file_list()
		
		# Create Buttons and Textinput 
		self.number_check_button=self.check_button('Number Order')
		self.letter_check_button=self.check_button('Letters')
		self.file_name_input=self.text_input()
		add_button=self.button('Add')
		remove_button=self.button('Remove')
		preview_button=self.button('Preview')
		start_button=self.button('Start')

		#Create Dropdown
		self.drop_down=self.drop_down()

		#Create Start_number input
		self.start_number_input=self.text_input()

		#Create Status Bar
		self.status_bar = QStatusBar()


		# Button group is abstract 
		# Add 'Number Order' and 'Letters' check buttons to a group 'number_letter_button_group' ''
		number_letter_button_group=self.button_group([self.number_check_button,self.letter_check_button])

		# Add 'Add' and 'Remove' buttons to a group 'add_remove_button_group'
		add_remove_button_group=self.button_group([add_button,remove_button])

		# Add 'Preview' and 'Start' buttons to a group 'preview_start_button_group'
		preview_start_button_group=self.button_group([preview_button,start_button])






		# Add buttons to a group box that would locates buttons together
		number_letter_group_box=self.group_box('Choose the Mode')
		add_remove_group_box=self.group_box('')
		preview_start_group_box=self.group_box('')



		
		# Connect the widgets with the action function.
		number_letter_button_group.buttonToggled.connect(self.on_button_toggled)
		add_remove_button_group.buttonClicked.connect(self.open_file)
		preview_start_button_group.buttonClicked.connect(self.rename_file)





		# Add widgets to layout and locate the specific position
		checkbox_group_layout=self.button_layout({self.number_check_button:[0,0],self.letter_check_button:[0,1],self.drop_down:[1,1],self.start_number_input:[1,0]})
		checkbox_group_layout.setColumnStretch(0,1)
		checkbox_group_layout.setColumnStretch(1,3)
		add_remove_group_layout=self.button_layout({add_button:[0,0],remove_button:[0,1]})
		preview_start_group_layout=self.button_layout({preview_button:[0,0],start_button:[0,1]})

		#Apply the corrsponding layout to group box
		number_letter_group_box.setLayout(checkbox_group_layout)
		add_remove_group_box.setLayout(add_remove_group_layout)
		preview_start_group_box.setLayout(preview_start_group_layout)


		# Add the group box and other widgets to main layout
		layout.addWidget(self.file_list_source,0,0)
		layout.addWidget(self.file_list_destination,0,1)		
		layout.addWidget(add_remove_group_box,1,0)
		layout.addWidget(preview_start_group_box,1,1)
		layout.addWidget(number_letter_group_box,2,0)
		layout.addWidget(self.file_name_input,2,1)
		layout.addWidget(self.status_bar,3,0,1,2)
	


		return layout


	def center(self):
		qr=self.frameGeometry()
		cp=QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())


	def check_button(self,title):
		check_button=QCheckBox(title)


		return check_button

	def drop_down(self):

		drop_down=QComboBox() 
		drop_down.addItems(['Prefix','Appendix'])

		return drop_down

	def group_box(self,title):
		group_box=QGroupBox(title)

		return group_box

	def check_button_state(self):

		b=self.sender()

		if b.isChecked()==True:
			print (f'The text from the check bos is: {b.text()}')
			return b.text()


	def button_group(self,buttons):
		button_group=QButtonGroup(self)
		for b in buttons:
			button_group.addButton(b)


		return button_group

	def text_input(self):
		text_input=QLineEdit()
		
		text_input.setMaxLength(20)
		text_input.setReadOnly(True)

		return text_input


	def button(self,title):
		button=QPushButton(title)

		return button

	def button_layout(self,widget):
		layout=QGridLayout()
		for w in widget:
			layout.addWidget(w,widget[w][0],widget[w][1])

		return layout



	def on_button_toggled(self,button,checked):

		if checked:

			self.file_name_input.setStyleSheet("""
					QLineEdit{

					border-radius: 5px;
					border-bottom: 2px solid blue;
					padding:0.5em 1em;

					}
					""")

			button_text=button.text()

			if button_text=='Letters':
			
				self.file_name_input.setReadOnly(False)
				self.file_name_input.setFocus()
				self.file_name_input.setPlaceholderText('Please Enter the filename')
				validator = QRegExpValidator(QRegExp("^\\w*$"), self.file_name_input)
				self.file_name_input.setValidator(validator)

				self.start_number_input.setReadOnly(True)
				self.start_number_input.setPlaceholderText('')
				self.start_number_input.setText('')

			
			elif button_text=='Number Order':


				self.file_name_input.setPlaceholderText('')
				self.file_name_input.setReadOnly(True)
				self.file_name_input.setStyleSheet("""
					QLineEdit{

					background-color:white;

					}
					""")
				
				self.start_number_input.setReadOnly(False)
				self.start_number_input.setFocus()
				self.start_number_input.setPlaceholderText('Start Number')
				self.start_number_input.setText('0')

				validator = QRegExpValidator(QRegExp("^[0-9]*$"), self.start_number_input)
				self.start_number_input.setValidator(validator)


	def open_file(self,button):
		button_text=button.text()
		# print (f'The button you clicked is {button_text}')
		count=self.file_list_source.count()
		



		if button_text=="Add":
			file_open=QFileDialog()
			filenames=file_open.getOpenFileNames(None,"Select the files",'.','All files(*.*)')
			if count:
				exsit_files=[self.file_list_source.item(i).text() for i in range(count)]
				# print (f'exsit_files are {exsit_files}')
			else:
				exsit_files=[]
			
			if filenames[0]:
				# print (f'You select the file is {filenames}')

				for f in filenames[0]:

					if count==0:
						self.file_list_source.addItem(QListWidgetItem(f))
					else:
						if f not in exsit_files:
							self.file_list_source.addItem(QListWidgetItem(f))
		if button_text=="Remove":
			selcted_items=self.file_list_source.selectedItems()
			if selcted_items:

				for item in selcted_items:
					
					self.file_list_source.takeItem(self.file_list_source.row(item))
			else:
				self.status_bar.showMessage('No file is selected.')


	def rename_file(self,button):
		button_text=button.text()
		list_destination_cout=self.file_list_destination.count()

		# Clear the Destination List When there are some exsit

		count=self.file_list_source.count()

		

		if button_text=="Preview":
			if list_destination_cout:
				self.file_list_destination.clear()

			if count:

				path_dic=self.get_list_items(count)

				
				if self.number_check_button.isChecked():

					if self.start_number_input.text():

						if int(self.start_number_input.text())==0:
						 	start_number=0
						else:
							start_number=int(self.start_number_input.text().lstrip('0'))
						
						zero_place=len(str(count+start_number))

						self.add_ranamed_list(path_dic,start_number,zero_place,count,'number')

	
						

				if self.letter_check_button.isChecked():
					if self.file_name_input.text():
						mode=self.drop_down.currentText()
						if mode=="Prefix":

							self.add_ranamed_list(path_dic,None,None,count,'Prefix')
			
						elif mode=="Appendix":
							self.add_ranamed_list(path_dic,None,None,count,'Appendix')
					else:
						self.status_bar.showMessage('You have to input the new file name')
				else:

					self.status_bar.showMessage('You have to choose the mode.')
			else:

				self.status_bar.showMessage('You have to add the files first.')
						

		if button_text=="Start":

			if not list_destination_cout:
				self.status_bar.showMessage('Destination list is empty, Preview first')
			elif count!=list_destination_cout:
				self.status_bar.showMessage('DO the preview first. Source and Destination amount should be the same.')
			else:
				reply = QMessageBox.warning(self, 'Warning', 'Are you sure you want to RENAME?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
				if reply==QMessageBox.Yes:

					for i in range(count):
						source_text=self.file_list_source.item(i).text()
						destination_text=self.file_list_destination.item(i).text()
						os.rename(source_text,destination_text)

						self.file_list_source.item(i).setText(destination_text)
					
					self.status_bar.showMessage('Rename Done!')





	

	def get_list_items(self,count):

		path_dic={}
 
		for i in range(count):
			
			item=self.file_list_source.item(i)

			file_full_path=item.text()
			base_path=file_full_path.rsplit('/',1)[0]+'/'
			file_name=file_full_path.split('/')[-1]
			path_dic[i]=[base_path,file_name]

		

		return path_dic


	def add_ranamed_list(self,path_dic,start_number,zero_place,count,mode):

	

		for k in path_dic:
			extension=path_dic[k][-1].split('.')[-1]
			if mode=="number":
				if zero_place:
					path_dic[k][-1]=f'{start_number:0{zero_place}d}.{extension}'
					start_number+=1
			elif mode=="Prefix":
				path_dic[k][-1]=f'{self.file_name_input.text()}{k:0{len(str(count))}d}.{extension}'
			elif mode=="Appendix":
				path_dic[k][-1]=f'{k:0{len(str(count))}d}{self.file_name_input.text()}.{extension}'

		
			self.file_list_destination.addItem(QListWidgetItem(''.join(path_dic[k])))

	

	


	def file_list(self):
		file_list=QListWidget()
		file_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

		return file_list





if __name__=='__main__':

	app=QApplication(sys.argv)
	ex=App()
	sys.exit(app.exec_())