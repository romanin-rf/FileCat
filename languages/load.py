import json, os

data = 	{
			"name_lang": 	"Русский", 
			"name_window": 	"Файловый Кот", 
			"text_window": 	{
								"text_version": "Версия",
								"text_progress": "Прогресс",
								"text_warning": "Привет. Не ругайся я знаю, что это очень очень сырая игра\nНо сам посуди, я просто делаю игру по фану и продавать я её е собираюсь\nТо есть это изначально сложно назвать игрой)))"
							}
		}

with open('RU.json', 'w') as file:
	json.dump(data, file)

print(data)

os.system("pause")