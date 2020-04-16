#!/usr/bin/env python3 

import webbrowser  

def request_user_approval():
	response = input("Do you want to read this?")
	return response

def open_wiki_article():
	url = "https://en.wikipedia.org/wiki/Special:Random"
	webbrowser.open(url, new=0, autoraise=True)
	return
	
def main():
	response = 'n'
	while response == 'n':
		open_wiki_article()
		response = request_user_approval().lower()
	return

main()




