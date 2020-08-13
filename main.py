import os, json, time

# Выгрузка config.json
with open('config.json') as cnfFILE:
	config_data = json.load(cnfFILE)

if config_data["language"] == "None":

	languages_list = os.listdir(path = "{0}\\languages".format(os.getcwd()))
	print("Write your language from the list:")
	wag = 0
	text_list_languages = ""

	while wag != len(languages_list):

		text_list_languages = text_list_languages + languages_list[wag] + " _ "
		wag += 1

	print(text_list_languages)
	enter = True
	while enter:

		user_enter_language = str(input("> "))

		if user_enter_language in languages_list:

			config_data["language"] = str(user_enter_language)

			with open('config.json', 'w') as cnfFILE:
				json.dump(config_data, cnfFILE)

			enter = False
''' Надо дописать загрущик выбраного языка '''

os.system("pause")