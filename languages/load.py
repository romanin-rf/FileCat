import json, os

data = 	{
			"name_lang": 	"Русский", 
			"name_window": 	"Файловый Кот", 
			"text_window": 	{
								"text_version": "Версия",
								"text_progress": "Прогресс",
								"text_money": "Монет"
							}
		}

with open('RU.json', 'w') as file:
	json.dump(data, file)

print(data)

os.system("pause")