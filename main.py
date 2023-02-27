import os

class Rename:
	def __init__(self):
		
		pass


	
	def rules(self,mode,file_count,start_number,position):
		new_file_names=[]

		for n in range(start_number,file_count+start_number):
			new_file=f'{n:0{len(str(file_count))}}'
			new_file_names.append(new_file)

		if mode=='digits':

			return new_file_names
			
		if mode=='letters':
			if position[0]=='prefix':
				new_file=map(lambda x:position[1]+x,new_file_names)
				new_file_names=list(new_file)
			elif position[0]=='appendix':
				new_file=map(lambda x:x+position[1],new_file_names)
				new_file_names=list(new_file)

			return new_file_names





	def get_path_file_name(self,file_path):

		dir_path=os.path.dirname(file_path)
		file_name=os.path.basename(file_path)

		return (dir_path,file_name)



	def change_name(self,source_name,destination_name):

		if os.path.exists(source_name):
			try:
				os.rename(source_name,destination_name)
				print (f'Source:{source_name} to Destination:{destination_name}')
			except:
				print ('Error in destination path!')
		else:
			print ('Source path Error!')		


	def run(self):
		pass



# if __name__=='__main__':

# 	source_name="D:\\Code\\Python_Apps\\rename\\newLLL.txt"
# 	destination_name="D:\\Code\\Python_Apps\\rename\\newBIG.txt"
# 	one=Rename()
# 	one.run(source_name,destination_name)
