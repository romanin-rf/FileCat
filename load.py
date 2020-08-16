import json

data = {
	"name_lang": "Український",
	"name_window": "Файловий Кіт",
	"text_window": 	{"text_version": "Версія"}
}

with open('UK.json', "w") as file:
	json.dump(data, file)