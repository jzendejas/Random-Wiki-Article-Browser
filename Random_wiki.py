#!/usr/bin/env python3 

import webbrowser
import time
import tkinter 


def request_user_approval():
	response = input("Do you want to read this?")
	return response

def open_wiki_article():
	url = "https://en.wikipedia.org/wiki/Special:Random"
	webbrowser.open(url, new=0, autoraise=True)
	
	btn1.destroy()
	
	lbl.configure(text="Do you want to read this?")
	
	btn2 = tkinter.Button(window, text="Yes", command=close_tkinter_window)
	btn2.grid(column=0, row=1)
	btn2.config(height=5, width=5)
	
	btn3 = tkinter.Button(window, text="No", command=open_wiki_article_repeat)
	btn3.grid(column=2, row=1)
	btn3.config(height=5, width=5)
	return btn2, btn3
	
	
def open_wiki_article_repeat():
	url = "https://en.wikipedia.org/wiki/Special:Random"
	webbrowser.open(url, new=0, autoraise=True)
	
	
	
def close_tkinter_window():
	window.destroy()
	return
	


def main():
	response = 'n'
	while response == 'n':
		open_wiki_article()
		time.sleep(10)
		response = request_user_approval().lower()
	return
	
	
window = tkinter.Tk()

window.geometry('210x130')

window.title("Random Wiki Article Fetcher")

lbl = tkinter.Label(window, text="Ready to Wiki?", font=("Arial Bold", 10))
lbl.grid(column=0, row=0, columnspan=3)

btn1 = tkinter.Button(window, text="Go!", command=open_wiki_article)
btn1.grid(column=1, row=1)
btn1.config(height=5, width=5)

window.wm_attributes("-topmost", 1)

window.mainloop()




