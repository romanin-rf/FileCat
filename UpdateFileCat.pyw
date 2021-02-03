import datetime
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
	NameFileUpdateAPI = wget.download(cfgd["url"])
	if sys.platform == "win32":
		with open(local_dir + "\\" + NameFileUpdateAPI) as FileDataUpdate:
			UpdateAPIData = json.load(FileDataUpdate)
		os.remove(local_dir + "\\" + NameFileUpdateAPI)
	else:
		if sys.platform == "linux":
			with open(local_dir + "/" + NameFileUpdateAPI) as FileDataUpdate:
				UpdateAPIData = json.load(FileDataUpdate)
			os.remove(local_dir + "/" + NameFileUpdateAPI)
		else:
			raise OSError("Your OS is not supported")
	if UpdateAPIData["version-api"] > cfgd["version-api"]:
		NeedUpdate = True
	else:
		NeedUpdate = False
	return NeedUpdate, UpdateAPIData["url"]

def last_check_update():
	global config_data
	user_time_start, user_func_time_start = [], datetime.datetime.now()

	last_func_check_update = datetime.datetime(config_data["last-check-update"][2], config_data["last-check-update"][1], config_data["last-check-update"][0], config_data["last-check-update"][3], config_data["last-check-update"][4])

	if str(time.strftime("%d", time.localtime()))[0] == "0":
		user_time_start.append(int(str(time.strftime("%d", time.localtime()))[1]))
	else:
		user_time_start.append(int(time.strftime("%d", time.localtime())))
	if str(time.strftime("%m", time.localtime()))[0] == "0":
		user_time_start.append(int(str(time.strftime("%m", time.localtime()))[1]))
	else:
		user_time_start.append(int(time.strftime("%m", time.localtime())))

	user_time_start.append(int(time.strftime("%Y", time.localtime())))

	if (str(time.strftime("%H", time.localtime()))[0] == "0"):
		user_time_start.append(int(str(time.strftime("%H", time.localtime()))[1]))
	else:
		user_time_start.append(int(time.strftime("%H", time.localtime())))
	if (str(time.strftime("%M", time.localtime()))[0] == "0"):
		user_time_start.append(int(str(time.strftime("%M", time.localtime()))[1]))
	else:
		user_time_start.append(int(time.strftime("%M", time.localtime())))

	passed_last_check_update_seconds = (user_func_time_start - last_func_check_update).seconds

	if passed_last_check_update_seconds > 3600:
		NeedCheckToLastCheck = True
		config_data["last-check-update"] = user_time_start
		with open('{0}\\config.json'.format(local_dir), "w") as cnfFILE:
			json.dump(config_data, cnfFILE)
	else:
		NeedCheckToLastCheck = False

	return NeedCheckToLastCheck

# Проверка обновления
try:
	if last_check_update() == True:
		NeedUpdateData, URLUpdate = UpdateCheck(cfgd = config_data)
	else:
		NeedUpdateData = False
	if (sys.platform == "win32") and (NeedUpdateData == True) and (URLUpdate != None):
		NumberButtonPress = int(ctypes.windll.user32.MessageBoxW(0, "A new update has been released! Update the program?", "File Cat", 68))
		if NumberButtonPress == 6:
			os.chdir(path = local_dir_dush)
			name_file_update = str(wget.download(URLUpdate))
			if zipfile.is_zipfile(name_file_update):
				ctypes.windll.user32.MessageBoxW(0, "The File Cat downloaded the update and after installing the application will give you an error, this is normal and means the program has been updated", "File Cat", 16)
				zipfile.ZipFile(str(name_file_update), 'r').extractall()
				exit()
			else:
				ctypes.windll.user32.MessageBoxW(0, "Failed to update the program! Go to the developer's website and download the updated version", "File Cat", 16)
				os.remove(name_file_update)
				exit()
except:
	ctypes.windll.user32.MessageBoxW(0, "Failed to get update information. Possible problems:\n1. There is no internet connection\n2. The developer provided an incorrect update link", "File Cat", 16)