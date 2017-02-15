import praw


USERAGENT = 'script:userflair_bulk_remover:1.0 (by /u/iPlain)'
username = 'enter_username_here'
password = 'enter_password_here'
client_id = 'enter_client_id_here'
client_secret = 'enter_client_secret_here'

target_subreddit = 'enter_subreddit_here'

#Fill either one of these two lists with a list of css classes that should be left or removed. Only fill one.
css_classes_to_remove = []

css_classes_to_not_remove = []


r = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=USERAGENT, username=username, password=password)

sub = r.subreddit(target_subreddit)

num_changed = 0

changing = []

if css_classes_to_not_remove and css_classes_to_remove or not css_classes_to_not_remove and not css_classes_to_remove:
	print('Either fill css_classes_to_remove or css_classes_to_not_remove with a list of css_classes, do not fill both. This script will not run unless one and only one list has items')

elif css_classes_to_not_remove:
	for flair in sub.flair():
		if flair['flair_css_class'] == None:
			continue

		elif flair['flair_css_class'] not in css_classes_to_not_remove:
			changing.append(flair['user'])
			num_changed += 1
		

elif css_classes_to_remove:
	for flair in sub.flair():
		if flair['flair_css_class'] == None:
			continue

		elif flair['flair_css_class'] in css_classes_to_remove:
			changing.append(flair['user'])
			num_changed += 1


sub.flair.update(changing)
print(str(num_changed) + ' flairs have been changed.')
