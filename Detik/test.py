from bs4 import BeautifulSoup
import requests

content = requests.get('http://bmkg.go.id')
print(content)