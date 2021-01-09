import json, os

data = 	{
			'name_lang': 	'English',
			'name_window': 	'File Cat',
			'text_window': 	{
								'text_version':		'Version',
								'text_progress':	'(1) Progress',
								'text_money':		'(2) Coins',
								'text_bites': 		'Byte(s)'
							}, 
			'button_text_window':	{
										'feed_the_cat': 'Feed'
									},
			'errors_feed':	{
								'not_dir':			'You gave your cat a bowl',
								'not_files_in_dir':	'You didn\'t put your cat food',
								'many_files':		'You put your cat too much food and threw up'
							},
			'successfully':	{
								'cat_ate':	'Yum-yum-yum'
							}
}
# ֍

"""
RU:
{
			'name_lang':	'Русский',
			'name_window':	'Файловый Кот',
			'text_window':	{
								'text_version':		'Версия',
								'text_progress':	'(1) Прогресс',
								'text_money':		'(2) Монет',
								'text_bites':		'Байт(ов)'
							}, 
			'button_text_window':	{
										'feed_the_cat':	'Покормить'
									},
			'errors_feed':	{
								'not_dir':			'Вы поставили своему коту миску',
								'not_files_in_dir':	'Вы не положили своему коту еды',
								'many_files':		'Вы положили своему коту слишком много еды и его вырвало'
							},
			'successfully':	{
								'cat_ate': 'Ням-ням-ням'
							}
}
"""
with open('en-eng.json', 'w') as file:
	json.dump(data, file)

print(data)

os.system("pause")