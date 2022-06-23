from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  
# upload_file_list = ['log.csv']
upload_file = 'log.csv'
def pushfilelog():
	gfile = drive.CreateFile({'parents': [{'id': '1TJdg_Qy15MMo8jB6IQCB09orEFkWqPrb'}]})   # link to drive
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.
	# for upload_file in upload_file_list:
	# 	gfile = drive.CreateFile({'parents': [{'id': '1TJdg_Qy15MMo8jB6IQCB09orEFkWqPrb'}]})   # link to drive
	# 	# Read file and set it as the content of this instance.
	# 	gfile.SetContentFile(upload_file)
	# 	gfile.Upload() # Upload the file.