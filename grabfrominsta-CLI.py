from grabfrominsta import grabfrominsta
from urllib import request

def main():
	if __name__ == '__main__':
		inurl = input("Input url please: ")
		picurl = grabfrominsta(inurl)
		savetopath = input("Path to save to please: ")
		request.urlretrieve(picurl,savetopath)
		input("Done! Press Enter to Continue")

if __name__ == '__main__':
	main()