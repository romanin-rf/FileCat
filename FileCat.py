import os
import sys
import json
import base64
import time
import math
import tkinter
import webbrowser
import wget
import zipfile
import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image

local_dir = os.getcwd()
os.chdir(path = "..")
local_dir_dush = os.getcwd()
os.chdir(path = local_dir)

dev_sintax = ["-dev", "-ml", "-w", "-h", "-t"]

# Создание функций
def calculate_whole_percentage(max_var, var, percent):
	one_percentage = max_var / percent
	not_whole_output = var / one_percentage
	whole_output = math.ceil(not_whole_output)
	if whole_output >= percent:
		output = percent
	else:
		output = whole_output
	return output

def UpdateCheck(cfgd):
	NameFileUpdateAPI = str(wget.download(cfgd["url"]))
	if str(sys.platform) == "win32":
		with open(str(local_dir) + "\\" + NameFileUpdateAPI) as FileDataUpdate:
			UpdateAPIData = json.load(FileDataUpdate)
		os.remove(str(local_dir) + "\\" + NameFileUpdateAPI)
	else:
		if str(sys.platform) == "linux":
			with open(str(local_dir) + "/" + NameFileUpdateAPI) as FileDataUpdate:
				UpdateAPIData = json.load(FileDataUpdate)
			os.remove(str(local_dir) + "/" + NameFileUpdateAPI)
		else:
			raise OSError("ваша операционная система не поддерживаеться")
	if UpdateAPIData["version-api"] > cfgd["version-api"]:
		NeedUpdate = True
	else:
		NeedUpdate = False
	return NeedUpdate, UpdateAPIData["url"]

# Проверка наличия MSGBox
if str(sys.platform) == "win32":
	dir_msgb = local_dir + "\\data\\bin\\win32\\msgb.exe"
	if os.path.exists(dir_msgb):
		working_dir_msgb = True
	else:
		working_dir_msgb = False
	if dev_sintax[0] in sys.argv:
		print("- WORKING_DIR_MSGB:", working_dir_msgb)

# Загрузка данных
if str(sys.platform) == "win32":
	with open('{0}\\config.json'.format(os.getcwd())) as cnfFILE:
		config_data = json.load(cnfFILE)
	with open('{0}\\user_data.json'.format(os.getcwd())) as user_data_file:
		usr_data_base = json.load(user_data_file)
	usr_data = json.loads(base64.urlsafe_b64decode(usr_data_base).decode())
	with open('{0}\\languages\\{1}'.format(local_dir, config_data["language"])) as LANGFILE:
		language_data = json.load(LANGFILE)
else:
	if str(sys.platform) == "linux":
		with open('{0}/config.json'.format(os.getcwd())) as cnfFILE:
			config_data = json.load(cnfFILE)
		with open('{0}/user_data.json'.format(os.getcwd())) as user_data_file:
			usr_data_base = json.load(user_data_file)
		usr_data = json.loads(base64.urlsafe_b64decode(usr_data_base).decode())
		with open('{0}/languages/{1}'.format(local_dir, config_data["language"])) as LANGFILE:
			language_data = json.load(LANGFILE)
	else:
		raise OSError("ваша операционная система не поддерживаеться")

# Вывод параметров для разрабочика
if dev_sintax[0] in sys.argv:
	print("- LANGUAGE:", config_data["language"])
	print("- VERSION:", config_data["version"])
	print("- VERSION_API:", config_data["version-api"])
	print("- ARGV:", sys.argv)

# Проверка обновления
NeedUpdateData, URLUpdate = UpdateCheck(cfgd = config_data)
if (str(sys.platform) == "win32") and (working_dir_msgb == True) and (NeedUpdateData == True) and (URLUpdate != None):
	NumberButtonPress = int(os.popen("\"{0}\" -msg \"FileCat.exe\" \"A new update has been released! Update the program?\" 68".format(dir_msgb)).read())
	if NumberButtonPress == 6:
		os.chdir(path = local_dir_dush)
		name_file_update = str(wget.download(str(URLUpdate)))
		if zipfile.is_zipfile(name_file_update):
			zipfile.ZipFile(str(name_file_update), 'r').extractall()
			exit()
		else:
			os.system("\"{0}\" -msg \"FileCat.exe\" \"Failed to update the program! Go to the developer's website and download the updated version\" 16".format(dir_msgb))
			os.remove(name_file_update)
			exit()

if dev_sintax[0] in sys.argv:
	print("\n- NeedUpdateData:", NeedUpdateData)
	print("- URLUpdate:", URLUpdate)

# Создание окна
root = Tk()
if (dev_sintax[0] in sys.argv) and (dev_sintax[2] in sys.argv) and (dev_sintax[3] in sys.argv):
	width_root = int(sys.argv[int(sys.argv.index(dev_sintax[2])) + 1])
	height_root = int(sys.argv[int(sys.argv.index(dev_sintax[3])) + 1])
	root.geometry('{0}x{1}'.format(width_root, height_root))
else:
	root.geometry('700x130')
root.resizable(width = False, height = False)
if str(sys.platform) == "win32":
	root.iconbitmap('icon.ico')
if (dev_sintax[0] in sys.argv) and (dev_sintax[4] in sys.argv):
	title_root = str(sys.argv[int(sys.argv.index(dev_sintax[4])) + 1])
	root.title("{0}".format(title_root))
else:
	if dev_sintax[0] in sys.argv:
		root.title("{0} - Developer Mode".format(language_data["name_window"]))
	else:
		root.title("{0}".format(language_data["name_window"]))

# Выгрузка изображений
if str(sys.platform) == "win32":
	githun_img = ImageTk.PhotoImage(Image.open("{0}\\data\\img\\github.png".format(local_dir)))
else:
	if str(sys.platform) == "linux":
		githun_img = ImageTk.PhotoImage(Image.open("{0}/data/img/github.png".format(local_dir)))

# Обрабочик прогресса
def handler_progress():
	global usr_data
	if (usr_data["save"]["start-value"] * usr_data["save"]["multiplier-start-value"]) <= usr_data["save"]["you-user"]:
		usr_data["save"]["multiplier-start-value"] += usr_data["setting"]["speed-rise-multiplier-start-value"]
		usr_data["save"]["money"] += (usr_data["setting"]["start-money-for-lvl"] * usr_data["save"]["multiplier-money"])
		usr_data["save"]["multiplier-money"] += usr_data["setting"]["speed-rise-multiplier-money"]
	max_start_value = usr_data["save"]["start-value"] * usr_data["save"]["multiplier-start-value"]
	progress_percentage = calculate_whole_percentage(max_var = max_start_value, var = usr_data["save"]["you-user"], percent = 100)
	usr_data_base = base64.urlsafe_b64encode(json.dumps(usr_data).encode()).decode()
	with open('user_data.json', "w") as user_data_file:
		json.dump(usr_data_base, user_data_file)
	return max_start_value, usr_data["save"]["you-user"], progress_percentage

max_start_value_progress, value_progress_user, percentage_progress_user = handler_progress()

# Создание объектов
if str(sys.platform) == "win32":
	language_change_B = Button(root, text = "{0}".format(language_data['name_lang']), width = 11)
	version_text_var = Label(root, text = "{0}: {1}".format(language_data["text_window"]["text_version"], config_data["version"]), bg = "black", fg = "white", width = 25)
	notification_bar = Label(root, text = "", bg = "grey", fg = "white", width = 74)
else:
	if str(sys.platform) == "linux":
		language_change_B = Button(root, text = "{0}".format(language_data['name_lang']), width = 8)
		version_text_var = Label(root, text = "{0}: {1}".format(language_data["text_window"]["text_version"], config_data["version"]), bg = "black", fg = "white", width = 22)
		notification_bar = Label(root, text = "", bg = "grey", fg = "white", width = 65)
bit_progressbar = ttk.Progressbar(root, length = 595)
bit_progressbar["value"] = percentage_progress_user
bit_progressbar_value_text = Label(root, text = "{0}: {1} {4} \\{2} {4} ({3} %)".format(language_data["text_window"]["text_progress"], value_progress_user, max_start_value_progress, percentage_progress_user, language_data["text_window"]["text_bites"]))
money_vaule_text = Label(root, text = "{0}: {1}".format(language_data["text_window"]["text_money"], usr_data["save"]["money"]))
button_feed_the_cat = Button(root, text = "{0}".format(language_data["button_text_window"]["feed_the_cat"]))
github_link = Label(root, image = githun_img)
# Объекты для разрабочика
if (dev_sintax[0] in sys.argv) and (dev_sintax[1] in sys.argv):
	text_info_multipliers = Label(root, text = "\"multiplier-start-value\": {0}\n\"multiplier-money\": {1}".format(usr_data["save"]["multiplier-start-value"], usr_data["save"]["multiplier-money"]))

# Логикa
def language_change_click(event):
	if str(sys.platform) == "win32":
		list_languages = os.listdir(path = "{0}\\languages".format((local_dir)))
	else:
		if str(sys.platform) == "linux":
			list_languages = os.listdir(path = "{0}/languages".format((local_dir)))

	id_lang_list = 0
	while True:
		if config_data["language"] == list_languages[id_lang_list]:
			break
		id_lang_list += 1
	
	id_lang_list += 1
	if id_lang_list == len(list_languages):
		id_lang_list = 0
	if str(sys.platform) == "win32":
		name_file_lang, type_file_lang = os.path.splitext("{0}\\languages\\{1}".format(local_dir, list_languages[id_lang_list]))
		while type_file_lang != ".json":
			name_file_lang, type_file_lang = os.path.splitext("{0}\\languages\\{1}".format(local_dir, list_languages[id_lang_list]))
			if type_file_lang == ".json":
				break
			else:
				if id_lang_list == len(list_languages):
					id_lang_list = 0
			id_lang_list += 1
	else:
		if str(sys.platform) == "linux":
			name_file_lang, type_file_lang = os.path.splitext("{0}/languages/{1}".format(local_dir, list_languages[id_lang_list]))
			while type_file_lang != ".json":
				name_file_lang, type_file_lang = os.path.splitext("{0}/languages/{1}".format(local_dir, list_languages[id_lang_list]))
				if type_file_lang == ".json":
					break
				else:
					if id_lang_list == len(list_languages):
						id_lang_list = 0
				id_lang_list += 1

	loading_text_language(event, id_lang_list, list_languages, config_data)

def loading_text_language(event, id_lang, list_langs, config_data):
	id_lang_list = id_lang
	list_languages = list_langs

	config_data["language"] = list_languages[id_lang_list]
	if str(sys.platform) == "win32":
		with open('{0}\\config.json'.format(local_dir), 'w') as cnfFILE:
			json.dump(config_data, cnfFILE)

		with open('{0}\\config.json'.format(local_dir)) as cnfFILE:
			config_data = json.load(cnfFILE)
	else:
		if str(sys.platform) == "linux":
			with open('{0}/config.json'.format(local_dir), 'w') as cnfFILE:
				json.dump(config_data, cnfFILE)

			with open('{0}/config.json'.format(local_dir)) as cnfFILE:
				config_data = json.load(cnfFILE)

	root.quit()

def feed_the_cat_button(event):
	global usr_data
	if config_data["eat-dir"] in os.listdir(path = local_dir_dush):
		if str(sys.platform) == "win32":
			dush_dir = str(str(local_dir_dush) + "\\" + str(config_data["eat-dir"])) + "\\"
		else:
			if str(sys.platform) == "linux":
				dush_dir = str(str(local_dir_dush) + "/" + str(config_data["eat-dir"])) + "/"
		dush_file = os.listdir(path = dush_dir)
		wag_handler_files = 0
		while wag_handler_files != int(len(dush_file)):
			if str(dush_file[wag_handler_files]).endswith(".txt") != True:
				dush_file.remove(str(dush_file[wag_handler_files]))
			else:
				wag_handler_files += 1
			if dev_sintax[0] in sys.argv:
				print("DUSH_DIR:", dush_dir)
				print("DUSH_FILE:", dush_file)
				print("WAG:", wag_handler_files)
		if int(len(dush_file)) != 0:
			size_files = 0
			wag = 0
			max_start_value_progress, value_progress_user, percentage_progress_user = handler_progress()
			errors_handlers = False
			while wag != int(len(dush_file)):
				if os.path.isfile(str(dush_dir) + str(dush_file[wag])):
					size_files += int(os.path.getsize((str(dush_dir) + str(dush_file[wag]))))
					if int(max_start_value_progress) >= size_files:
						os.remove((str(dush_dir) + str(dush_file[wag])), dir_fd = None)
					else:
						errors_handlers = True
						break
				wag += 1
			if errors_handlers != True:
				usr_data["save"]["you-user"] += size_files
				max_start_value_progress, value_progress_user, percentage_progress_user = handler_progress()
				bit_progressbar["value"] = percentage_progress_user
				bit_progressbar_value_text["text"] = "{0}: {1} {4} \\{2} {4} ({3} %)".format(language_data["text_window"]["text_progress"], value_progress_user, max_start_value_progress, percentage_progress_user, language_data["text_window"]["text_bites"])
				money_vaule_text["text"] = "{0}: {1}".format(language_data["text_window"]["text_money"], usr_data["save"]["money"])
				notification_bar["text"] = str(language_data["successfully"]["cat_ate"])
			else:
				usr_data["save"]["you-user"] = 0
				max_start_value_progress, value_progress_user, percentage_progress_user = handler_progress()
				bit_progressbar["value"] = percentage_progress_user
				bit_progressbar_value_text["text"] = "{0}: {1} {4} \\{2} {4} ({3} %)".format(language_data["text_window"]["text_progress"], value_progress_user, max_start_value_progress, percentage_progress_user, language_data["text_window"]["text_bites"])
				notification_bar["text"] = str(language_data["errors_feed"]["many_files"])
		else:
			notification_bar["text"] = str(language_data["errors_feed"]["not_files_in_dir"])
	else:
		os.mkdir("{0}\\{1}".format(local_dir_dush, config_data["eat-dir"]), mode = 0o777, dir_fd = None)
		max_start_value_progress, value_progress_user, percentage_progress_user = handler_progress()
		bit_progressbar["value"] = percentage_progress_user
		bit_progressbar_value_text["text"] = "{0}: {1} {4} \\{2} {4} ({3} %)".format(language_data["text_window"]["text_progress"], value_progress_user, max_start_value_progress, percentage_progress_user, language_data["text_window"]["text_bites"])
		money_vaule_text["text"] = "{0}: {1}".format(language_data["text_window"]["text_money"], usr_data["save"]["money"])
		notification_bar["text"] = str(language_data["errors_feed"]["not_dir"])

def github_open_link(event):
	webbrowser.open_new("https://github.com/romanin-rf/FileCat/releases")

# Параметры объекта и их привязка к логике
language_change_B.bind('<Button-1>', language_change_click)
button_feed_the_cat.bind('<Button-1>', feed_the_cat_button)
github_link.bind('<Button-1>', github_open_link)

# Выгрузка объектов на экран
language_change_B.place(x = 5, y = 5)
version_text_var.place(x = 0, y = 110)
bit_progressbar.place(x = 100, y = 5)
bit_progressbar_value_text.place(x = 100, y = 30)
money_vaule_text.place(x = 100, y = 50)
button_feed_the_cat.place(x = 5, y = 75)
notification_bar.place(x = 180, y = 110)
github_link.place(x = 660, y = 70)
if (dev_sintax[0] in sys.argv) and (dev_sintax[1] in sys.argv):
	text_info_multipliers.place(x = 500, y = 30)

root.mainloop()
usr_data_base = base64.urlsafe_b64encode(json.dumps(usr_data).encode()).decode()
with open('user_data.json', "w") as user_data_file:
	json.dump(usr_data_base, user_data_file)