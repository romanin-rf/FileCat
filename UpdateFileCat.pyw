import PySimpleGUI as sg
import zipfile
import ctypes
import time
import wget
import json
import sys
import os

# Переменые для работы
local_dir = str(os.getcwd())
os.chdir(path = "..")
local_dir_dush = str(os.getcwd())
os.chdir(path = local_dir)

# Загрузка данных
if sys.platform == "win32":
	with open('{0}\\config.json'.format(local_dir)) as cnfFILE:
		config_data = json.load(cnfFILE)
else:
	if sys.platform == "linux":
		with open('{0}/config.json'.format(local_dir)) as cnfFILE:
			config_data = json.load(cnfFILE)
	else:
		raise OSError("Your OS is not supported")

# Функции для работы
def UpdateCheck(cfgd):
	sg.one_line_progress_meter('UpdateCheck', 0, 3, '-key-')
	NameFileUpdateAPI = wget.download(cfgd["url"])
	sg.one_line_progress_meter('UpdateCheck', 1, 3, '-key-')
	if sys.platform == "win32":
		with open(local_dir + "\\" + NameFileUpdateAPI) as FileDataUpdate:
			UpdateAPIData = json.load(FileDataUpdate)
		sg.one_line_progress_meter('UpdateCheck', 2, 3, '-key-')
		os.remove(local_dir + "\\" + NameFileUpdateAPI)
		sg.one_line_progress_meter('UpdateCheck', 3, 3, '-key-')
	else:
		if sys.platform == "linux":
			with open(local_dir + "/" + NameFileUpdateAPI) as FileDataUpdate:
				UpdateAPIData = json.load(FileDataUpdate)
			sg.one_line_progress_meter('UpdateCheck', 2, 3, '-key-')
			os.remove(local_dir + "/" + NameFileUpdateAPI)
			sg.one_line_progress_meter('UpdateCheck', 3, 3, '-key-')
		else:
			raise OSError("Your OS is not supported")
	if UpdateAPIData["version-api"] > cfgd["version-api"]:
		NeedUpdate = True
	else:
		NeedUpdate = False
	return NeedUpdate, UpdateAPIData["url"]

# Проверка обновления
try:
	NeedUpdateData, URLUpdate = UpdateCheck(cfgd = config_data)
	if (sys.platform == "win32") and (NeedUpdateData == True) and (URLUpdate != None):
		NumberButtonPress = int(ctypes.windll.user32.MessageBoxW(0, "A new update has been released! Update the program?", "UpdateFileCat", 68))
		if NumberButtonPress == 6:
			sg.one_line_progress_meter('InstalledUpdate', 0, 4, '-key-')
			os.chdir(path = local_dir_dush)
			sg.one_line_progress_meter('InstalledUpdate', 1, 4, '-key-')
			name_file_update = str(wget.download(URLUpdate))
			sg.one_line_progress_meter('InstalledUpdate', 2, 4, '-key-')
			if zipfile.is_zipfile(name_file_update):
				sg.one_line_progress_meter('InstalledUpdate', 3, 4, '-key-')
				zipfile.ZipFile(str(name_file_update), 'r').extractall()
				sg.one_line_progress_meter('InstalledUpdate', 4, 4, '-key-')
				ctypes.windll.user32.MessageBoxW(0, "The update is installed", "UpdateFileCat", 64)
			else:
				sg.one_line_progress_meter('InstalledUpdate', 4, 4, '-key-')
				ctypes.windll.user32.MessageBoxW(0, "Failed to update the program! Go to the developer's website and download the updated version", "UpdateFileCat", 16)
				os.remove(name_file_update)
				exit()
	else:
		ctypes.windll.user32.MessageBoxW(0, "No update required", "UpdateFileCat", 64)
except:
	ctypes.windll.user32.MessageBoxW(0, "Failed to get update information. Possible problems:\n1. There is no internet connection\n2. The developer provided an incorrect update link", "UpdateFileCat", 16)