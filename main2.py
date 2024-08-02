import os
import shutil
import pickle

add_function = input("Do you want to add a Tag(s) (Type Add Tag): ")
function = (input("1. Do you want to: Save a folder (Type 1) \n2. Delete a folder (Type 2) \n3. Save a file (Type 3) \n4. Delete a file (Type 4) \n5. View the folder list (Type View Folders) \n6. View the file list (Type View Files) \n7. Check if a file is there (Type Check File) \n8. Check if a folder is there (Type Check Folder) \n9. Rename File \n10. Rename Folder \n11. "'{add_function}'"\n12. Import File" ))

ErrorMsg1 = "already exists"
ErrorMsg2 = "not found"

desired_parent_path = input("Would you like to continue in this folder as the parent (Type Stay) or change to a different parent folder path(Type Change): ")

if desired_parent_path == 'Stay' : 
	parent_folder_path = '/Users/akshsinha/Desktop'

elif desired_parent_path == 'Change' :
      different_parent_path = input("Enter the path for the new parent folder: ")
      parent_folder_path = different_parent_path

else :
	print("bruh")

def add_tag() :
	add_tag_name = input("Enter the name of the tag: ")

	add_tag_files_name = input("Enter the name of the file you want to add under this tag: ")
      
	add_tag_quest = input("Do you want to just create the tag(Type Create) \nWrite to a file in the tag(Type Write) \nRead a file from the tag(Type Read) \nDelte a file from the tag(Type Delete)\n Or load an already existing file from the tag(Type Load) \n:")

	while True:
            tag_cont_quest = input("Do you want to continue to" '{add_tag_quest}'"?")
            if tag_cont_quest == 'yes' :
            	add_tag_name = tag_folder = {}

            	def create_pseudo_file (pseudo_file_name):
            		tag_folder[pseudo_file_name] = ""

            	def write_pseudo_file (pseudo_file_name, content) :
            		if pseudo_file_name in tag_folder :
            			tag_folder[pseudo_file_name] += content

            	def read_pseudo_file (pseudo_file_name) :
            		if pseudo_file_name in tag_folder :
            			return tag_folder[pseudo_file_name]

            		else :
            			return ""

            	def delete_pseudo_file(pseudo_file_name) :
            		if pseudo_file_name in tag_folder:
            			del tag_folder[pseudo_file_name]

      		def save_simulated_folder():
      			with open("simulated_folder_data.pickle", "wb") as file:
      				pickle.dump(tag_folder, file)

      		def load_simulated_folder():
      			global tag_folder

      			try:
      				with open("tag_folder_data.pickle", "rb") as file:
      					tag_folder = pickle.load(file)

      			except FileNotFoundError:
      				tag_folder = {}

      		load_simulated_folder()
      		if add_tag_quest == 'Create' :
      			create_file("add_tag_files_name")

      		elif add_tag_quest == 'Write' :
      			write_to_file("add_tag_files_name", "This is some content.")

      		elif add_tag_quest == 'Read' :
      			print(read_file("add_tag_files_name")) 

      		elif add_tag_quest == 'Delete' :
      			delete_file("add_tag_files_name")

      		elif add_tag_quest == 'Load' :
      			print(read_file("add_tag_files_name"))  

      		else:
      			print("bruh")

      		save_simulated_folder() 
      	else:
      		print("bruh")
      		break

def save_file() :
	f_name = (input("Enter the name of the file: "))
	f_path = os.path.join (parent_folder_path, f_name)
	f_quest = input("Would you like to add data to this file from an already existing file: ")
	if f_quest == 'yes' :
		f_quest_folder = input("Enter the name of the folder this file is in: ")
		try :
			f_quest_folder_path = os.path.input (parent_folder_path, f_quest_folder)
			f_quest_file = input("Enter the name of source file: ")
			try :
				f_quest_file_path = os.path.join (f_quest_folder_path, f_quest_file)

				def transfer_data(f_quest_file_path, f_path) :
					with open(f_quest_file_path, "r") as source_file :
						with open(f_path, "w") as dest_file :
							data = source_file.read()
							dest_file.write(data)
							transfer_data(f_quest_file_path, f_path)	

			except FileExistsError:
				print(f"'{f_quest_file}' '{ErrorMsg1}'.")
			except FileNotFoundError:
				print(f"'{f_quest_file}' '{ErrorMsg2}'.")

		except FileExistsError:
			print(f"'{f_quest_folder}' '{ErrorMsg1}'.")
		except FileNotFoundError:
			print(f"'{f_quest_folder}' '{ErrorMsg2}'.")
	else :
		print("bruh")

def save_name() :
	p_name = (input("Enter the name of the folder: "))
	p_folder_path = os.path.join(parent_folder_path, p_name)
	os.makedirs(p_folder_path)
	print(f"New folder '{p_name}' created at '{parent_folder_path}'")

	while True:
		command = input("Do you want to add a file in this folder: ")

		if command.lower() == 'yes':
			f_name = input("Enter the name of the file: ")
			f_path = os.path.join (p_name, f_name)
			open(f_path, "a").close()
			print(f"New file '{f_name}' created at '{p_name}'")
		elif command.lower() == 'no':
			print("bruh")
			break
		else :
			print("bruh")

def delete_name() :
	d_name_view_quest = input("Would you like to view the folders in the directory: ")
	if d_name_view_quest == 'yes' :
		view_names()
		d_name = input("Enter the name of the folder you want to delete: ")

		try :
			d_name_path = os.path.join (parent_folder_path, d_name)
			shutil.rmtree(d_name_path)
			print(f"Folder '{d_name}' deleted at '{parent_folder_path}'")
		except FileExistsError :
			print(f"Folder '{d_name}' '{ErrorMsg1}'.")
		except FileNotFoundError :
			print(f"Folder '{d_name}' '{ErrorMsg2}'.")

	else :
		d_name = input("Enter the name of the folder you want to delete: ")

		try :
			d_name_path = os.path.join (parent_folder_path, d_name)
			shutil.rmtree(d_name_path)
			print(f"Folder '{d_name}' deleted at '{parent_folder_path}'")
		except FileExistsError :
			print(f"Folder '{d_name}' '{ErrorMsg1}'.")
		except FileNotFoundError :
			print(f"Folder '{d_name}' '{ErrorMsg2}'.")

def delete_file() :
	d_folder = input("Enter the name of the folder the file you want to delete is in: ")
	d_file_view_quest = input("Would like to view the files in this folder: ")

	if d_file_view_quest == 'yes' :
		v_folder = d_folder
		v_folder_path = os.path.join (parent_folder_path, v_folder)
		files = os.listdir(v_folder_path)

		if len(files) == 0:
			print("This folder is empty.")
		else :
			folders = ""
			j = 0
			for f in files : 
				if os.path.isfile(os.path.join(parent_folder_path,f)) :
					j = j + 1
					if j == 1 :
						print("Files in the folder:")
					if f[0] != "." and f[0] != "~":
						print(f)

		try :
			d_folder_path = os.path.join (parent_folder_path, d_folder)
			d_file = input("Enter the name of the file you want to delete: ")

			try :
				d_file_path = os.path.join (d_folder_path, d_file)
				print(d_file_path)
				os.remove(d_file_path)
				print(f"'{d_file}' removed '{d_folder}'")
			except FileExistsError :
				print(f"'{d_file}' '{ErrorMsg1}' '{d_folder}.'")
			except FileNotFoundError :
				print(f"'{d_file}' '{ErrorMsg2}'.")

		except FileExistsError :
			print(f"'{d_folder}' '{ErrorMsg1}'.")
		except FileNotFoundError :
			print(f"'{d_folder}' '{ErrorMsg2}'.")

		while True :
			command_delete_file = input("Do you want to delete another file in this folder: ")

			if command_delete_file.lower() == 'yes' :
				f_d_name = input("Enter the name of the file you want to delete: ")
				try :
					f_d_path = os.path.join(d_folder_path, f_d_name)
					os.remove(f_d_path)
					print(f"'{f_d_name}' removed from '{d_folder}'")
				except FileExistsError :
					print(f"'{f_d_name}' '{ErrorMsg1}'")
				except FileNotFoundError :
					print(f"'{f_d_name}' '{ErrorMsg2}'")

			elif command_delete_file.lower() == 'no' :
				print("bruh")
				break
			else :
				print("bruh")

	else :
		try :
			d_folder_path = os.path.join (parent_folder_path, d_folder)
			d_file = input("Enter the name of the file you want to delete: ")

			try :
				d_file_path = os.path.join (d_folder_path, d_file)
				print(d_file_path)
				os.remove(d_file_path)
				print(f"'{d_file}' removed '{d_folder}'")
			except FileExistsError :
				print(f"'{d_file}' '{ErrorMsg1}' '{d_folder}.'")
			except FileNotFoundError :
				print(f"'{d_file}' '{ErrorMsg2}'.")

		except FileExistsError :
			print(f"'{d_folder}' '{ErrorMsg1}'.")
		except FileNotFoundError :
			print(f"'{d_folder}' '{ErrorMsg2}'.")

		while True :
			command_delete_file = input("Do you want to delete another file in this folder: ")

			if command_delete_file.lower() == 'yes' :
				f_d_name = input("Enter the name of the file you want to delete: ")
				try :
					f_d_path = os.path.join(d_folder_path, f_d_name)
					os.remove(f_d_path)
					print(f"'{f_d_name}' removed from '{d_folder}'")
				except FileExistsError :
					print(f"'{f_d_name}' '{ErrorMsg1}'")
				except FileNotFoundError :
					print(f"'{f_d_name}' '{ErrorMsg2}'")

			elif command_delete_file.lower() == 'no' :
				print("bruh")
				break
			else :
				print("bruh")

def view_names() :
	files = os.listdir(parent_folder_path)
	if len(files) == 0:
		print("This directory is empty.")
	else :
		folders = ""
		j = 0
		for f in files : 
			if os.path.isdir(os.path.join(parent_folder_path,f)) :
				j = j + 1
				if j == 1 :
					print("Folders in the diectory:")
				print(f)

def view_files() :
	v_folder = input("Enter the name of the folder in which you want to view the files: ")
	v_folder_path = os.path.join (parent_folder_path, v_folder)
	files = os.listdir(v_folder_path)

	if len(files) == 0:
		print("This folder is empty.")
	else :
		folders = ""
		j = 0
		for f in files : 
			if os.path.isfile(os.path.join(parent_folder_path,f)) :
				j = j + 1
				if j == 1 :
					print("Files in the folder:")
				if 	f[0] != "." and f[0] != "~":
					print(f)

from os.path import exists
def check_file() :
	file_folder = input("Enter the name of the folder the file would be in: ")

	try : 
		file_folder_path = os.path.join (parent_folder_path, file_folder)
		file_exists = input("Enter the name of the file that u want to check: ")

		try :
			file_exists_path = os.path.join (file_folder_path, file_exists)
			file_exists_check = exists(file_exists_path)

			if file_exists_check == True :
				print(f"'{file_exists}' exists in '{file_folder}'.")
			else :
				print(f"'{file_exists_path}' does not exist in '{file_folder}'.")
		except FileExistsError :
			print(f"'{file_exists}' '{ErrorMsg1}'.")
		except FileNotFoundError :
			print(f"'{file_exists}' '{ErrorMsg2}'.")

	except FileExistsError :
		print(f"'{file_folder}' '{ErrorMsg1}'.")
	except FileNotFoundError :
		print(f"'{file_folder}' '{ErrorMsg2}'.")

def check_folder() :
  	folder_exists = input("Enter the name of the folder you want check the existance of: ")

  	try :
  		folder_exists_path = os.path.join(parent_folder_path, folder_exists)
  		folder_exists_check = exists(folder_exists_path)

  		if folder_exists_check == True :
  			print(f"'{folder_exists}' exists at '{folder_exists_path}'")

  	except FileExistsError :
  		print(f"'{folder_exists}' '{ErrorMsg1}'.")
  	except FileNotFoundError :
  		print(f"'{folder_exists}' '{ErrorMsg2}'.")

def rename_file(old_file_name, new_file_name) :
	rename_file_folder_path = os.path.join (parent_folder_path, rename_file_folder)
	old_file_name_path = os.path.join (rename_file_folder_path, old_file_name)
	new_file_name_path = os.path.join (rename_file_folder_path, new_file_name)

	try :
		os.rename (old_file_name_path, new_file_name_path)
		print(f"'{old_file_name}' renamed to '{new_file_name}'")
	except FileNotFoundError :
		print(f"File'{old_file_name}' '{ErrorMsg2}'.")
	except FileExistsError :
		print(f"File '{new_file_name}' already exists as '{old_file_name}'")

def rename_folder(old_folder_name, new_folder_name) :
	old_folder_name_path = os.path.join (parent_folder_path, old_folder_name)
	new_folder_name_path = os.path.join (parent_folder_path, new_folder_name)

	try :
		os.rename (old_folder_name_path, new_folder_name_path)
		print(f"'{old_folder_name}' renamed to '{new_folder_name}'")
	except FileNotFoundError :
		print(f"'{old_folder_name}' '{ErrorMsg2}'.")
	except FileExistsError :
		print(f"'{new_folder_name}' already exists as '{old_folder_name}'")

def import_file() :
	import_file_source = input("Enter the name of the source file: ")
	import_file_source_path = os.path.join (parent_folder_path, import_file_source)

	import_file_dest_folder = input("Enter the name of the destination folder: ")
	import_file_dest_folder_path = os.path.join (parent_folder_path, import_file_dest_folder)
	
	shutil.move (import_file_source_path, import_file_dest_folder_path)
	print(f"'{import_file_source}' moved to '{import_file_dest_folder}'")

if function == '1' :
	save_name()

elif function == '3' :
	save_file() 

elif function == '2' :    
	delete_name()

elif function == '4' :
	delete_file()

elif function == 'View Folders' :
	view_names()

elif function == 'View Files' :
	view_files()

elif function == 'Check File' :
	check_file()

elif function == 'Check Folder' :
	check_folder()

elif function == 'Rename File' :
	rename_file_folder = input("Enter the name of the folder in which the file is located: ")
	old_file_name = input("Enter the file name: ")
	new_file_name = input("Enter the new name for this file: ")
	rename_file(old_file_name, new_file_name)

elif function == 'Rename Folder' :
	old_folder_name = input("Enter the name of the folder: ")
	new_folder_name = input("Enter the new name for the folder: ")
	rename_folder(old_folder_name, new_folder_name)

elif function == 'Add Tag' :
	add_tag()

elif function == 'Import File' :
	import_file()

else :
	print("bruh")