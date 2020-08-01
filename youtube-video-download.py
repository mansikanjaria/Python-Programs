1)
from pytube import Youtube
Youtube("Link here").streams.first().download()


2)
import webbrowser
url = "Link here"
download=url[:12]+"ss"+url[12:]
webbrowser.open(download)
