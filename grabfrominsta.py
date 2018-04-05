#Save this as 3 seperate files, one having the grabfrom insta function, one for the CLI interface, one for the GUI interface
from urllib import request

def grabfrominsta(url):
	if("?taken-by" in url):
		url = url.split("?")
		url = url[0]
	html = request.urlopen(url)
	html = html.read()
	html = str(html)[2:-1]
	line = html.split("<")
	for i in line:
		if('meta property="og:image"' in i):
			upurl = i
	upurl = upurl.split('"')
	upurl = upurl[3]
	return upurl