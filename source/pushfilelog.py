from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
# from gooleapiclient import MediaFileUpload
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  
# upload_file_list = ['log.csv']
upload_file = 'log.csv'
id_file = '1Ziu40zgreC0U6OqhOPS50hAGv-bew8zb'  # get from address IP on drive
def pushfilelog():
	global id_file
	# gfile = drive.CreateFile({'parents': [{'id': '1TJdg_Qy15MMo8jB6IQCB09orEFkWqPrb'}]})   # link to drive
	gfile = drive.CreateFile({'id': id_file})   # link to drive
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.
	# print("file: ", gfile)
	# media_content = MediaFileUpload(upload_file)
	# service.file().update(
	# 	fileId=id_file,
	# 	media_body = media_content
	# ).execute()
	# for upload_file in upload_file_list:
	# 	gfile = drive.CreateFile({'parents': [{'id': '1TJdg_Qy15MMo8jB6IQCB09orEFkWqPrb'}]})   # link to drive
	# 	# Read file and set it as the content of this instance.
	# 	gfile.SetContentFile(upload_file)
	# 	gfile.Upload() # Upload the file.