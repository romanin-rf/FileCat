import json, os

data = 	{
			"name_lang": 			"English", 
			"name_window": 			"File Cat", 
			"text_window": 			{
										"text_version":		"Version",
										"text_progress":	"(1) Progess",
										"text_money":		"(2) Money",
										"text_bites":		"Bite(s)"
									},
			"button_text_window":	{
										"feed_the_cat":		"Feed"
									},
			"errors_feed":			{
										"not_dir":			"You put a bowl for your cat",
										"not_files_in_dir":	"You did not put cat food",
										"many_files":		"You put too much food on your cat"
									},
			"successfully":			{
										"cat_ate":			"Yum-yum-yum"
									}
		}
# ֍
with open('EN.json', 'w') as file:
	json.dump(data, file)

print(data)

os.system("pause")