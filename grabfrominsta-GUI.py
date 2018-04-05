from grabfrominsta import grabfrominsta
from urllib import request
import tkinter as tk
from tkinter import filedialog


def main():
	def browse():
		text = filedialog.asksaveasfilename()
		saveasfilebox.insert(0,text)
	def download():
		url = inurlbox.get()
		outfilepath = saveasfilebox.get()
		request.urlretreive(url,outfilepath)
	root = tk.Tk()
	root.title("GrabFromInsta")
	tk.Label(root,text = "Input Url").pack()
	inurlbox = tk.Entry(root)
	inurlbox.pack()
	tk.Label(root,text = "Output File Name").pack()
	saveasfilebox = tk.Entry(root)
	saveasfilebox.pack()
	browsebut = tk.Button(root,text = "Browse",command = browse)
	browsebut.pack()
	downloadbut = tk.Button(root,text = "Download",command = download)
	downloadbut.pack()
	root.mainloop()

if __name__ == '__main__':
	main()