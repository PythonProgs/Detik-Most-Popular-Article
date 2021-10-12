from bs4 import BeautifulSoup
import requests

def ekstraksi_data_detik():
    try:
        content = requests.get('http://detik.com')
    except Exception:
        return None

    soup = BeautifulSoup(content.text,'html.parser')
    result = soup.find('div', {'class':'box cb-mostpop'})
    result = result.findChildren('h3')

    article1 = None
    article2 = None
    article3 = None
    article4 = None
    article5 = None
    i = 0

    for res in result:
        if i == 0:
            article1 = res.text
        elif i == 1:
            article2 = res.text
        elif i == 2:
            article3 = res.text
        elif i == 3:
            article4 = res.text
        elif i == 4:
            article5 = res.text
        i = i + 1

    article = dict()
    article['article1'] = article1
    article['article2'] = article2
    article['article3'] = article3
    article['article4'] = article4
    article['article5'] = article5
    return article

def tampilkan_data_detik(article):
    if article is None:
        print("Tidak bisa menemukan data artikel terpopuler")
        return
    print("Artikel paling terkenal di detik: ")
    print(f"1. {article['article1']}")
    print(f"2. {article['article2']}")
    print(f"3. {article['article3']}")
    print(f"4. {article['article4']}")
    print(f"5. {article['article5']}")
