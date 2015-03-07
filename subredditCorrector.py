import praw, time, os

r = praw.Reddit(user_agent = USER_AGENT) 
print("Logging in")
r.login()
already_done = []

banned_subs = []

def run_bot():
	print("Starting Stream")
	stream = praw.helpers.comment_stream(r, "all", limit = None, verbosity = 3)
	for comment in stream:
		arr = []
		comment_text = comment.body.lower()
		for word in comment_text.split():
			if word.find("r/") == 0:
				arr.append(word)
		notBanned = comment.subreddit.display_name in banned_subs
		if comment.id not in already_done and len(arr) > 0:
			if comment.id is not notBanned:
				print("Match Found! Comment id:" + comment.id + " Subreddit: " + comment.subreddit.display_name)
				reply = ""
				for match in arr:
					reply = reply + "\n/" + match
				comment.reply(reply)
				already_done.append(comment.id)


while True:
	run_bot()

