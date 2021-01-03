import json, os

data = 	{
			"name_lang": 			"Русский", 
			"name_window": 			"Файловый Кот", 
			"text_window": 			{
										"text_version":		"Версия",
										"text_progress":	"Прогресс",
										"text_money":		"Монет",
										"text_bites":		"Байт(ов)"
									},
			"button_text_window":	{
										"feed_the_cat":		"Покормить"
									}
		}

with open('RU.json', 'w') as file:
	json.dump(data, file)

print(data)

os.system("pause")