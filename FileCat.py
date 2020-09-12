import os, json, time, tkinter, math, logging
from tkinter import *
import tkinter.ttk as ttk

def calculate_whole_percentage(max_var, var, percent):
	one_percentage = max_var / percent
	not_whole_output = var / one_percentage
	whole_output = math.ceil(not_whole_output)
	if whole_output >= percent:
		output = percent
	else:
		output = whole_output
	return output

logging_file = "{0}\\log\\{1}".format(os.getcwd(), 'FileCat{0}.log'.format(time.strftime("(%d-%m-%Y)", time.localtime())))

logging.basicConfig(
	level = logging.DEBUG, 
	format = '%(asctime)s : %(levelname)s : %(message)s', 
	filename = logging_file, 
	filemode = 'w'
)
logging.info("---- Стадия загрузки --------------------------------------")
try:
	with open('config.json') as cnfFILE:
		config_data = json.load(cnfFILE)
	logging.debug("FileCat загрузил библеотеки")
except:
	logging.warning("FileCat неудалось загрузить библеотеки")
	exit()

try:
	with open('user_data.json') as user_data_file:
		usr_data = json.load(user_data_file)
	logging.debug("FileCat загрузил пользовательские сохранения")
except:
	logging.warning("FileCat неудалось загрузить пользовательские сохранения")
	exit()

try:
	with open('{0}\\languages\\{1}'.format(os.getcwd(), config_data["language"])) as LANGFILE:
		language_data = json.load(LANGFILE)
	logging.debug("FileCat загрузил языковой словарь")
except:
	logging.warning("FileCat неудалось загрузить языковой словарь")

root = Tk() # Создание окна
root.geometry('700x600') # Размер окна
root.resizable(width = False, height = False) # Блокировка размера окна, чтобы его нельзя было изменить
root.title("{0}".format(language_data["name_window"])) # Имя окна
logging.debug("FileCat успешно создал окно")

# Создание объектов
language_change_B = Button(root, text = "{0}".format(language_data['name_lang']))
logging.debug("FileCat загрузил элемент окна под названием 'language_change_B'")

version_text_var = Label(root, text = "{0}: {1}".format(language_data["text_window"]["text_version"], config_data["version"]))
logging.debug("FileCat загрузил элемент окна под названием 'version_text_var'")

bit_progressbar = ttk.Progressbar(root, length = 570)
logging.debug("FileCat загрузил элемент окна под названием 'bit_progressbar'")

bit_progressbar_value_text = Label(root, text = "{0}: *\\* (* %)".format(language_data["text_window"]["text_progress"]))
logging.debug("FileCat загрузил элемент окна под названием 'bit_progressbar_value_text'")

money_vaule_text = Label(root, text = "{0}: {1}".format(language_data["text_window"]["text_money"], usr_data["save"]["money"]))
logging.debug("FileCat загрузил элемент окна под названием 'money_vaule_text'")

# Логика
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
logging.debug("FileCat загрузил функцию 'language_change_click'")

def loading_text_language(event, id_lang, list_langs, config_data):
	id_lang_list = id_lang
	list_languages = list_langs

	config_data["language"] = list_languages[id_lang_list]
	with open('config.json', 'w') as cnfFILE:
		json.dump(config_data, cnfFILE)

	with open('config.json') as cnfFILE:
		config_data = json.load(cnfFILE)

	with open('{0}\\languages\\{1}'.format(os.getcwd(), config_data["language"])) as LANGFILE:
		language_data = json.load(LANGFILE)

	logging.info("FileCat сменил язык")

	root.quit()
logging.debug("FileCat загрузил функцию 'loading_text_language'")

# Параметры объекта и их привязка к логике
language_change_B.bind('<Button-1>', language_change_click)
logging.debug("FileCat забиндил 'language_change_B' к функцие 'language_change_click'")

# Выгрузка объектов на экран
language_change_B.place(x = 5, y = 5)
logging.debug("FileCat поставил элемент 'language_change_B'")

version_text_var.place(x = 5, y = 580)
logging.debug("FileCat поставил элемент 'version_text_var'")

bit_progressbar.place(x = 100, y = 5)
logging.debug("FileCat поставил элемент 'bit_progressbar'")

bit_progressbar_value_text.place(x = 100, y = 30)
logging.debug("FileCat поставил элемент 'bit_progressbar_value_text'")

money_vaule_text.place(x = 100, y = 50)
logging.debug("FileCat поставил элемент 'money_vaule_text'")

logging.debug("FileCat полностью готов к работе!!!")
logging.info("---- Стадия пользования -----------------------------------")

root.mainloop()

logging.info("---- Стадия закрытия --------------------------------------")
logging.debug("FileCat был выключен")