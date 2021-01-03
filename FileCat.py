import os
import sys
import json
import time
import math
import tkinter
import tkinter.ttk as ttk
from tkinter import *

def calculate_whole_percentage(max_var, var, percent):
	one_percentage = max_var / percent
	not_whole_output = var / one_percentage
	whole_output = math.ceil(not_whole_output)
	if whole_output >= percent:
		output = percent
	else:
		output = whole_output
	return output

with open('config.json') as cnfFILE:
	config_data = json.load(cnfFILE)

with open('user_data.json') as user_data_file:
	usr_data = json.load(user_data_file)

with open('{0}\\languages\\{1}'.format(os.getcwd(), config_data["language"])) as LANGFILE:
	language_data = json.load(LANGFILE)

root = Tk() # Создание окна
root.geometry('{0}x{1}'.format(config_data["window"][0], config_data["window"][1])) # Размер окна
root.resizable(width = False, height = False) # Блокировка размера окна, чтобы его нельзя было изменить
root.title("{0}".format(language_data["name_window"])) # Имя окна

# Обрабочик
def handler_progress():
	global usr_data
	if usr_data["save"]["start-value"] <= usr_data["save"]["you-user"]:
		usr_data["save"]["multiplier-start-value"] += usr_data["setting"]["speed-rise-multiplier-start-value"]
		usr_data["save"]["money"] += (usr_data["setting"]["start-money-for-lvl"] * usr_data["save"]["multiplier-money"])
		usr_data["save"]["multiplier-money"] += usr_data["setting"]["speed-rise-multiplier-money"]
	max_start_value = usr_data["save"]["start-value"] * usr_data["save"]["multiplier-start-value"]
	progress_percentage = calculate_whole_percentage(max_var = max_start_value, var = usr_data["save"]["you-user"], percent = 100)
	with open('user_data.json', "w") as user_data_file:
		json.dump(usr_data, user_data_file)
	return max_start_value, usr_data["save"]["you-user"], progress_percentage

max_start_value_progress, value_progress_user, percentage_progress_user = handler_progress()

# Создание объектов
language_change_B = Button(root, text = "{0}".format(language_data['name_lang']), width = 11)
version_text_var = Label(root, text = "{0}: {1}".format(language_data["text_window"]["text_version"], config_data["version"]), bg = "black", fg = "white", width = 25)
bit_progressbar = ttk.Progressbar(root, length = 570)
bit_progressbar["value"] = percentage_progress_user
bit_progressbar_value_text = Label(root, text = "{0}: {1} {4} \\{2} {4} ({3} %)".format(language_data["text_window"]["text_progress"], value_progress_user, max_start_value_progress, percentage_progress_user, language_data["text_window"]["text_bites"]))
money_vaule_text = Label(root, text = "{0}: {1}".format(language_data["text_window"]["text_money"], usr_data["save"]["money"]))
button_feed_the_cat = Button(root, text = "{0}".format(language_data["button_text_window"]["feed_the_cat"]))
notification_bar = Label(root, text = "", bg = "grey", fg = "white", width = 74)
# Объекты для разрабочика
if "-dev" in sys.argv:
	text_info_multipliers = Label(root, text = "\"multiplier-start-value\": {0}\n\"multiplier-money\": {1}".format(usr_data["save"]["multiplier-start-value"], usr_data["save"]["multiplier-money"]))

# Логикa
def language_change_click(event):
	list_languages = os.listdir(path = "{0}\\languages".format((os.getcwd())))

	id_lang_list = 0
	while True:
		if config_data["language"] == list_languages[id_lang_list]:
			break
		id_lang_list += 1
	
	id_lang_list += 1
	if id_lang_list == len(list_languages):
		id_lang_list = 0
	name_file_lang, type_file_lang = os.path.splitext("{0}\\languages\\{1}".format(os.getcwd(), list_languages[id_lang_list]))
	while type_file_lang != ".json":
		name_file_lang, type_file_lang = os.path.splitext("{0}\\languages\\{1}".format(os.getcwd(), list_languages[id_lang_list]))
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
	with open('config.json', 'w') as cnfFILE:
		json.dump(config_data, cnfFILE)

	with open('config.json') as cnfFILE:
		config_data = json.load(cnfFILE)

	root.quit()

def feed_the_cat_button(event):
	global usr_data
	if config_data["eat-dir"] in os.listdir(path = "."):
		dush_dir = str(str(os.getcwd()) + "\\" + str(config_data["eat-dir"])) + "\\"
		dush_file = os.listdir(path = dush_dir)
		if int(len(dush_file)) != 0:
			size_files = 0
			wag = 0
			max_start_value_progress, value_progress_user, percentage_progress_user = handler_progress()
			errors_handlers = False
			while wag != int(len(dush_file)):
				if os.path.isfile(str(dush_dir) + str(dush_file[wag])):
					if int(max_start_value_progress) >= size_files:
						size_files += int(os.path.getsize((str(dush_dir) + str(dush_file[wag]))))
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
				notification_bar["text"] = str(language_data["errors_feed"]["many_files"])
		else:
			notification_bar["text"] = str(language_data["errors_feed"]["not_files_in_dir"])
	else:
		os.mkdir("{0}".format(config_data["eat-dir"]), mode = 0o777, dir_fd = None)
		max_start_value_progress, value_progress_user, percentage_progress_user = handler_progress()
		bit_progressbar["value"] = percentage_progress_user
		bit_progressbar_value_text["text"] = "{0}: {1} {4} \\{2} {4} ({3} %)".format(language_data["text_window"]["text_progress"], value_progress_user, max_start_value_progress, percentage_progress_user, language_data["text_window"]["text_bites"])
		money_vaule_text["text"] = "{0}: {1}".format(language_data["text_window"]["text_money"], usr_data["save"]["money"])
		notification_bar["text"] = str(language_data["errors_feed"]["not_dir"])

# Параметры объекта и их привязка к логике
language_change_B.bind('<Button-1>', language_change_click)
button_feed_the_cat.bind('<Button-1>', feed_the_cat_button)

# Выгрузка объектов на экран
language_change_B.place(x = 5, y = 5)
version_text_var.place(x = 0, y = 110)
bit_progressbar.place(x = 100, y = 5)
bit_progressbar_value_text.place(x = 100, y = 30)
money_vaule_text.place(x = 100, y = 50)
button_feed_the_cat.place(x = 5, y = 75)
notification_bar.place(x = 180, y = 110)
if "-dev" in sys.argv:
	text_info_multipliers.place(x = 500, y = 30)

root.mainloop()
with open('user_data.json', "w") as user_data_file:
	json.dump(usr_data, user_data_file)