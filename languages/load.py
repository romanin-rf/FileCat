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
										'feed_the_cat': 'Feed',
										'about_program': 'About program'
									},
			'errors_feed':	{
								'not_dir':			'You gave your cat a bowl',
								'not_files_in_dir':	'You didn\'t put your cat food',
								'many_files':		'You put your cat too much food and threw up'
							},
			'successfully':	{
								'cat_ate':	'Yum-yum-yum'
							},
			'about_win':	{
								'title': 			'About program',
								'developers': 		['Roman Slabicky'],
								'testers':			['Alexander Shabaev', 'Alexander Kolegaev'],
								'developer_text':	'Developer:',
								'developers_text':	'Developers:',
								'tester_text':		'Tester:',
								'testers_text':		'Testers:'
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
										'feed_the_cat':	'Покормить',
										'about_program': 'О программе'
									},
			'errors_feed':	{
								'not_dir':			'Вы поставили своему коту миску',
								'not_files_in_dir':	'Вы не положили своему коту еды',
								'many_files':		'Вы положили своему коту слишком много еды и его вырвало'
							},
			'successfully':	{
								'cat_ate': 'Ням-ням-ням'
							},
			'about_win':	{
								'title': 			'О программе',
								'developers': 		['Роман Слабицкий'],
								'testers':			['Александр Шабаев', 'Александр Кульгаев'],
								'developer_text':	'Разработчик:',
								'developers_text':	'Разработчики:',
								'tester_text':		'Тестировщик:',
								'testers_text':		'Тестировщики:'
							}
}
EN:
{
			'name_lang': 	'English',
			'name_window': 	'File Cat',
			'text_window': 	{
								'text_version':		'Version',
								'text_progress':	'(1) Progress',
								'text_money':		'(2) Coins',
								'text_bites': 		'Byte(s)'
							}, 
			'button_text_window':	{
										'feed_the_cat': 'Feed',
										'about_program': 'About program'
									},
			'errors_feed':	{
								'not_dir':			'You gave your cat a bowl',
								'not_files_in_dir':	'You didn\'t put your cat food',
								'many_files':		'You put your cat too much food and threw up'
							},
			'successfully':	{
								'cat_ate':	'Yum-yum-yum'
							},
			'about_win':	{
								'title': 			'About program',
								'developers': 		['Roman Slabicky'],
								'testers':			['Alexander Shabaev', 'Alexander Kolegaev'],
								'developer_text':	'Developer:',
								'developers_text':	'Developers:',
								'tester_text':		'Tester:',
								'testers_text':		'Testers:'
							}
}
UK:
{
			'name_lang':	'Український',
			'name_window':	'Файловий Кіт',
			'text_window':	{
								'text_version':		'Версія',
								'text_progress':	'(1) Прогрес',
								'text_money':		'(2) Монет',
								'text_bites':		'Байт(ів)'
							}, 
			'button_text_window':	{
										'feed_the_cat':	'Погодувати',
										'about_program': 'Про програму'
									},
			'errors_feed':	{
								'not_dir':			'Ви поставили своєму коту миску',
								'not_files_in_dir':	'Ви не поклали своєму коту їжі',
								'many_files':		'Ви поклали своєму коту занадто багато їжі і його вирвало'
							},
			'successfully':	{
								'cat_ate': 'Ням-ням-ням'
							},
			'about_win':	{
								'title':			'Про програму',
								'developers':		['Роман Слабицкий'],
								'testers':			['Олександр Шабаєв', 'Олександр Кульгаєв'],
								'developer_text':	'Розробник:',
								'developers_text':	'Розробники:',
								'tester_text':		'Тестувальник:',
								'testers_text':		'Тестувальники:'
							}
}
"""
with open('en-eng.json', 'w') as file:
	json.dump(data, file)

print(data)

os.system("pause")