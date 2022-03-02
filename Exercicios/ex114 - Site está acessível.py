import webbrowser
import urllib
import urllib.request
import selenium

try:
    #site = webbrowser.open('http://pudim.com.br/')
    site=urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Tudo OK')
    print(site.read())