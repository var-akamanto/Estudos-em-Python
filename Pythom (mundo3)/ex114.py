import urllib
import urllib.request
try:
    site = urllib.request.urlopen("https://google.com")
except:
    print("ERRO")
else:
    print("OK")