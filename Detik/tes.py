import requests


content = requests.get('https://bmkg.go.id')


print(content.status_code)