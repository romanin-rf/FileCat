import os
import sys
import json
import base64
import time
import math
import tkinter
import webbrowser
import wget
import ctypes
import PySimpleGUI as sg
import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image

local_dir = str(os.getcwd())
os.chdir(path = "..")
local_dir_dush = str(os.getcwd())
os.chdir(path = local_dir)
root_about = None
about_window_first_open = False

dev_sintax = ["-dev", "-ml", "-w", "-h", "-t", "-cmdl"]

# Загрузка данных
if sys.platform == "win32":
	with open('{0}\\config.json'.format(local_dir)) as cnfFILE:
		config_data = json.load(cnfFILE)
	with open('{0}\\user_data.json'.format(local_dir)) as user_data_file:
		usr_data_base = json.load(user_data_file)
	usr_data = json.loads(base64.urlsafe_b64decode(usr_data_base).decode())
	with open('{0}\\languages\\{1}'.format(local_dir, config_data["language"])) as LANGFILE:
		language_data = json.load(LANGFILE)
else:
	if sys.platform == "linux":
		with open('{0}/config.json'.format(local_dir)) as cnfFILE:
			config_data = json.load(cnfFILE)
		with open('{0}/user_data.json'.format(local_dir)) as user_data_file:
			usr_data_base = json.load(user_data_file)
		usr_data = json.loads(base64.urlsafe_b64decode(usr_data_base).decode())
		with open('{0}/languages/{1}'.format(local_dir, config_data["language"])) as LANGFILE:
			language_data = json.load(LANGFILE)
	else:
		raise OSError("Your OS is not supported")

# Скачивание UpdateFileCat
if not(str(config_data["name-update"]) in os.listdir()):
	list_of_actions = ["wget.download(\"{0}\")".format(config_data["url-update-pyw"]), "os.chdir(\"..\")", "wget.download(\"{0}\")".format(config_data["url-update-exe"]), "os.chdir(\"dist\")"]
	wag = 0
	while wag != len(list_of_actions):
		try:
			eval(str(list_of_actions[wag]))
		except:
			try:
				exec(str(list_of_actions[wag]))
			except:
				pass
		sg.one_line_progress_meter('Download UpdateFileCat', (wag + 1), len(list_of_actions), '-key-')
		wag += 1
	ctypes.windll.user32.MessageBoxW(0, "Loading the module for updates: Finished!", "File Cat", 64)

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

# Создание окна
root = Tk()
if (dev_sintax[0] in sys.argv) and (dev_sintax[2] in sys.argv) and (dev_sintax[3] in sys.argv):
	width_root = sys.argv[int(sys.argv.index(dev_sintax[2])) + 1]
	height_root = sys.argv[int(sys.argv.index(dev_sintax[3])) + 1]
	root.geometry('{0}x{1}'.format(width_root, height_root))
else:
	root.geometry('700x130')
root.resizable(width = False, height = False)
if sys.platform == "win32":
	root.iconbitmap('icon.ico')
if (dev_sintax[0] in sys.argv) and (dev_sintax[4] in sys.argv):
	title_root = str(sys.argv[int(sys.argv.index(dev_sintax[4])) + 1])
	root.title("{0}".format(title_root))
else:
	if dev_sintax[0] in sys.argv:
		root.title("{0} - Developer Mode".format(language_data["name_window"]))
	else:
		root.title("{0}".format(language_data["name_window"]))

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

# Выгрузка изображений
if sys.platform == "win32":
	githun_img = ImageTk.PhotoImage(Image.open("{0}\\data\\img\\github.pctr".format(local_dir)))
	icon_about_win = ImageTk.PhotoImage(Image.open("{0}\\data\\img\\icon64.pctr".format(local_dir)))
	money_img = ImageTk.PhotoImage(Image.open("{0}\\data\\img\\coin.pctr".format(local_dir)))
	progress_img = ImageTk.PhotoImage(Image.open("{0}\\data\\img\\progress.pctr".format(local_dir)))
else:
	if sys.platform == "linux":
		githun_img = ImageTk.PhotoImage(Image.open("{0}/data/img/github.pctr".format(local_dir)))
		icon_about_win = ImageTk.PhotoImage(Image.open("{0}/data/img/icon64.pctr".format(local_dir)))
		money_img = ImageTk.PhotoImage(Image.open("{0}/data/img/coin.pctr".format(local_dir)))
		progress_img = ImageTk.PhotoImage(Image.open("{0}/data/img/progress.pctr".format(local_dir)))

# Создание объектов
if sys.platform == "win32":
	language_change_B = Button(root, text = "{0}".format(language_data['name_lang']), width = 11)
	notification_bar = Label(root, text = "", bg = "grey", fg = "white", width = 100)
else:
	if sys.platform == "linux":
		language_change_B = Button(root, text = "{0}".format(language_data['name_lang']), width = 8)
		notification_bar = Label(root, text = "", bg = "grey", fg = "white", width = 88)
bit_progressbar = ttk.Progressbar(root, length = 595)
bit_progressbar["value"] = percentage_progress_user
bit_progressbar_value_text = Label(root, text = "{0}: {1} {4} \\{2} {4} ({3} %)".format(language_data["text_window"]["text_progress"], value_progress_user, max_start_value_progress, percentage_progress_user, language_data["text_window"]["text_bites"]))
money_vaule_text = Label(root, text = "{0}: {1}".format(language_data["text_window"]["text_money"], usr_data["save"]["money"]))
button_feed_the_cat = Button(root, text = "{0}".format(language_data["button_text_window"]["feed_the_cat"]))
about_program = Button(root, text = str(language_data["button_text_window"]["about_program"]))
money_img_label = Label(root, image = money_img)
progress_img_label = Label(root, image = progress_img)
# Объекты для разрабочика
if (dev_sintax[0] in sys.argv) and (dev_sintax[1] in sys.argv):
	text_info_multipliers = Label(root, text = "\"multiplier-start-value\": {0}\n\"multiplier-money\": {1}".format(usr_data["save"]["multiplier-start-value"], usr_data["save"]["multiplier-money"]))
if (dev_sintax[0] in sys.argv) and (dev_sintax[5] in sys.argv):
	command_line_devepoler = Entry(root, width = 108)
	command_line_devepoler_enter = Button(root, text = ">>>")

# Логикa
def language_change_click(event):
	if sys.platform == "win32":
		list_languages = os.listdir(path = "{0}\\languages".format((local_dir)))
	else:
		if sys.platform == "linux":
			list_languages = os.listdir(path = "{0}/languages".format((local_dir)))

	id_lang_list = 0
	while True:
		if config_data["language"] == list_languages[id_lang_list]:
			break
		id_lang_list += 1
	
	id_lang_list += 1
	if id_lang_list == len(list_languages):
		id_lang_list = 0
	if sys.platform == "win32":
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
		if sys.platform == "linux":
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
	if sys.platform == "win32":
		with open('{0}\\config.json'.format(local_dir), 'w') as cnfFILE:
			json.dump(config_data, cnfFILE)

		with open('{0}\\config.json'.format(local_dir)) as cnfFILE:
			config_data = json.load(cnfFILE)
	else:
		if sys.platform == "linux":
			with open('{0}/config.json'.format(local_dir), 'w') as cnfFILE:
				json.dump(config_data, cnfFILE)

			with open('{0}/config.json'.format(local_dir)) as cnfFILE:
				config_data = json.load(cnfFILE)

	root.quit()

def feed_the_cat_button(event):
	global usr_data
	if config_data["eat-dir"] in os.listdir(path = local_dir_dush):
		if sys.platform == "win32":
			dush_dir = local_dir_dush + "\\" + config_data["eat-dir"] + "\\"
		else:
			if sys.platform == "linux":
				dush_dir = local_dir_dush + "/" + config_data["eat-dir"] + "/"
		dush_file = os.listdir(path = dush_dir)
		wag_handler_files = 0
		while wag_handler_files != len(dush_file):
			if str(dush_file[wag_handler_files]).endswith(".txt") != True:
				dush_file.remove(str(dush_file[wag_handler_files]))
			else:
				wag_handler_files += 1
			if dev_sintax[0] in sys.argv:
				print("DUSH_DIR:", dush_dir)
				print("DUSH_FILE:", dush_file)
				print("WAG:", wag_handler_files)
		if len(dush_file) != 0:
			size_files = 0
			wag = 0
			max_start_value_progress, value_progress_user, percentage_progress_user = handler_progress()
			errors_handlers = False
			while wag != int(len(dush_file)):
				if os.path.isfile(dush_dir + str(dush_file[wag])):
					size_files += int(os.path.getsize((dush_dir + str(dush_file[wag]))))
					if int(max_start_value_progress) >= size_files:
						os.remove(dush_dir + str(dush_file[wag]), dir_fd = None)
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
				notification_bar["text"] = language_data["successfully"]["cat_ate"]
			else:
				usr_data["save"]["you-user"] = 0
				max_start_value_progress, value_progress_user, percentage_progress_user = handler_progress()
				bit_progressbar["value"] = percentage_progress_user
				bit_progressbar_value_text["text"] = "{0}: {1} {4} \\{2} {4} ({3} %)".format(language_data["text_window"]["text_progress"], value_progress_user, max_start_value_progress, percentage_progress_user, language_data["text_window"]["text_bites"])
				notification_bar["text"] = language_data["errors_feed"]["many_files"]
		else:
			notification_bar["text"] = language_data["errors_feed"]["not_files_in_dir"]
	else:
		os.mkdir("{0}\\{1}".format(local_dir_dush, config_data["eat-dir"]), mode = 0o777, dir_fd = None)
		max_start_value_progress, value_progress_user, percentage_progress_user = handler_progress()
		bit_progressbar["value"] = percentage_progress_user
		bit_progressbar_value_text["text"] = "{0}: {1} {4} \\{2} {4} ({3} %)".format(language_data["text_window"]["text_progress"], value_progress_user, max_start_value_progress, percentage_progress_user, language_data["text_window"]["text_bites"])
		money_vaule_text["text"] = "{0}: {1}".format(language_data["text_window"]["text_money"], usr_data["save"]["money"])
		notification_bar["text"] = language_data["errors_feed"]["not_dir"]

def github_open_link(event):
	webbrowser.open_new("https://github.com/romanin-rf/FileCat")

def handler_command_line(event):
	global config_data, usr_data
	command_developer_user = str(command_line_devepoler.get())
	try:
		user_output_command = eval(str(command_developer_user))
		ctypes.windll.user32.MessageBoxW(0, (("Вход:\n{0}\n\nВывод:\n".format(command_developer_user)) + str(user_output_command)), str(sys.argv[0]), 64)
	except:
		try:
			user_output_command = exec(str(command_developer_user))
			ctypes.windll.user32.MessageBoxW(0, (("Вход:\n{0}\n\nВывод:\n".format(command_developer_user)) + str(user_output_command)), str(sys.argv[0]), 64)
		except:
			if command_developer_user == "exit()":
				root.quit()
			else:	
				ctypes.windll.user32.MessageBoxW(0, "При вводе этой команды:\n{0}\n\n!!! ПРОИЗОШЛА ОШИБКА !!!".format(command_developer_user), str(sys.argv[0]), 16)

def about_window(event):
	global root_about
	root_about = Toplevel(root)
	root_about.title(language_data["name_window"] + " - " + language_data["about_win"]["title"])
	root_about.resizable(width = False, height = False)
	root_about.iconbitmap('icon.ico')
	root_about.geometry('335x125')
	icon_about_win_label = Label(root_about, image = icon_about_win)
	if not(len(language_data["about_win"]["developers"]) > 1):
		developer_list = Label(root_about, text = "{0}\n* {1} *".format(language_data["about_win"]["developer_text"], language_data["about_win"]["developers"][0]))
	else:
		text_developer_list = ""
		wag = 0
		while wag != len(language_data["about_win"]["developers"]):
			text_developer_list += ("* " + language_data["about_win"]["developers"][wag] + " *\n")
			wag += 1
		developer_list = Label(root_about, text = "{0}\n{1}".format(language_data["about_win"]["developers_text"], text_developer_list))
	if not(len(language_data["about_win"]["testers"]) > 1):
		testers_list = Label(root_about, text = "{0}\n* {1} *".format(language_data["about_win"]["tester_text"], language_data["about_win"]["tester_text"][0]))
	else:
		text_testers_list = ""
		wag = 0
		while wag != len(language_data["about_win"]["testers"]):
			text_testers_list += ("* " + str(language_data["about_win"]["testers"][wag]) + " *\n")
			wag += 1
		testers_list = Label(root_about, text = "{0}\n{1}".format(language_data["about_win"]["testers_text"], text_testers_list))
	version_label = Label(root_about, text = "{0}: {1}".format(language_data["text_window"]["text_version"], config_data["version"]))
	github_link = Label(root_about, image = githun_img)
	github_link.bind('<Button-1>', github_open_link)
	github_link.place(x = 295, y = 85)
	icon_about_win_label.place(x = 5, y = 5)
	version_label.place(x = 80, y = 5)
	developer_list.place(x = 80, y = 25)
	testers_list.place(x = 80, y = 65)

def handler_about_window(event):
	global about_window_first_open
	if about_window_first_open == False:
		about_window_first_open = True
		about_window(event)
	else:
		if not(int(root_about.winfo_exists()) == 1):
			about_window(event)

def PluginImport():
	global root, config_data, usr_data, about_window_first_open
	list_files_plugin = os.listdir()
	list_load_plugin = []
	list_plugin_all = []
	list_plugin_system = []
	list_plugin_init = []
	wag = 0
	while wag != len(list_files_plugin):
		if list_files_plugin[wag].endswith(".py") and (list_files_plugin[wag] != os.path.basename("{0}".format(sys.argv[0]))):
			list_plugin_all.append(str(list_files_plugin[wag][:(len(list_files_plugin[wag]) - 3)]))
			try:
				exec("import " + str(list_files_plugin[wag][:(len(list_files_plugin[wag]) - 3)]))
				list_load_plugin.append(str(list_files_plugin[wag][:(len(list_files_plugin[wag]) - 3)]))
			except:
				pass
		wag += 1
	wag_init = 0
	while wag_init != len(list_load_plugin):
		try:
			exec("{0}.{1}({2})".format(list_load_plugin[wag_init], eval("{0}.info[1]".format(list_load_plugin[wag_init])), eval("\", \".join({0}.info[2])".format(list_load_plugin[wag_init]))))
			list_plugin_init.append(list_load_plugin[wag_init])
		except:
			pass
		wag_init += 1
	text_msgb = ""
	wag_msgb = 0
	while wag_msgb != len(list_plugin_all):
		if list_plugin_all[wag_msgb] in list_load_plugin:
			if str(eval("{0}.info[0]".format(list_plugin_all[wag_msgb]))) == "app":
				text_msgb += "{0} is loaded... ок\n".format(list_plugin_all[wag_msgb])
				if list_plugin_all[wag_msgb] in list_plugin_init:
					text_msgb += "{0} is initialized... ок\n".format(list_plugin_all[wag_msgb])
				else:
					text_msgb += "{0} is not initialized... error code\n".format(list_plugin_all[wag_msgb])
			else:
				if str(eval("{0}.info[0]".format(list_plugin_all[wag_msgb]))) == "system":
					pass
				else:
					text_msgb += "{0} is not loaded... error info\n".format(list_plugin_all[wag_msgb])
		else:
			text_msgb += "{0} is not loaded... error code\n".format(list_plugin_all[wag_msgb])
		wag_msgb += 1
	if len(text_msgb) != 0:
		ctypes.windll.user32.MessageBoxW(0, text_msgb, str(sys.argv[0]), 64)

# Параметры объекта и их привязка к логике
language_change_B.bind('<Button-1>', language_change_click)
button_feed_the_cat.bind('<Button-1>', feed_the_cat_button)
about_program.bind('<Button-1>', handler_about_window)
if (dev_sintax[0] in sys.argv) and (dev_sintax[5] in sys.argv):
	command_line_devepoler_enter.bind('<Button-1>', handler_command_line)

# Выгрузка объектов
language_change_B.place(x = 5, y = 5)
bit_progressbar.place(x = 100, y = 5)
bit_progressbar_value_text.place(x = 120, y = 30)
money_vaule_text.place(x = 120, y = 50)
button_feed_the_cat.place(x = 5, y = 75)
notification_bar.place(x = 0, y = 110)
about_program.place(x = 610, y = 30)
money_img_label.place(x = 100, y = 50)
progress_img_label.place(x = 100, y = 30)
# Выгрузка объектов для разрабочика
if (dev_sintax[0] in sys.argv) and (dev_sintax[1] in sys.argv):
	text_info_multipliers.place(x = 500, y = 30)
if (dev_sintax[0] in sys.argv) and (dev_sintax[5] in sys.argv):
	command_line_devepoler.place(x = 5, y = 140)
	command_line_devepoler_enter.place(x = 660, y = 135)

# Загрузка плагинов
PluginImport()

# Конец
root.mainloop()
usr_data_base = base64.urlsafe_b64encode(json.dumps(usr_data).encode()).decode()
with open('user_data.json', "w") as user_data_file:
	json.dump(usr_data_base, user_data_file)