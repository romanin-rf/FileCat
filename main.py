import os, json, time

# Выгрузка config.json
with open('config.json') as cnfFILE:
	config_data = json.load(cnfFILE)

if config_data["language"] == "None":
	languages_list = os.listdir(path = "{0}\\languages".format(os.getcwd()))
	