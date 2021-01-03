import json, os

data = 	{
			"name_lang": 			"Русский", 
			"name_window": 			"Файловый Кот", 
			"text_window": 			{
										"text_version":		"Версия",
										"text_progress":	"(1) Прогресс",
										"text_money":		"(2) Монет",
										"text_bites":		"Байт(ов)"
									},
			"button_text_window":	{
										"feed_the_cat":		"Покормить"
									},
			"errors_feed":			{
										"not_dir":			"Вы поставили своему коту миску",
										"not_files_in_dir":	"Вы не положили своему коту еды",
										"many_files":		"Вы положили своему коту слишком много еды"
									},
			"successfully":			{
										"cat_ate":			"Ням-ням-ням"
									}
		}
# ֍
with open('RU.json', 'w') as file:
	json.dump(data, file)

print(data)

os.system("pause")