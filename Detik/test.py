from bs4 import BeautifulSoup
import requests

content = requests.get('http://bmkg.go.id')
soup = BeautifulSoup(content.text,'html.parser')
result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
result = result.findChildren('li')
print(result)