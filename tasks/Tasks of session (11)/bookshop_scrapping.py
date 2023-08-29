import requests
from bs4 import BeautifulSoup
url="https://books.toscrape.com/"
i=1;
while(True):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    main = soup.find_all("ol",{"class":'row'})
    pages = soup.find_all("ul", {"class": 'pager'})
    books=main[0].find_all("li")
    for book in books:
        title=book.find('h3').text.strip()
        price=book.find("div",{"class":"product_price"}).find("p",{"class":"price_color"}).text.strip()
        print(title)
        print(price)
        print("----------")
    try:
        i+=1
        if(i>=3):
            url = "https://books.toscrape.com/catalogue/" + pages[0].find("li", {"class": "next"}).find('a', href=True)['href']
        else:
            url="https://books.toscrape.com/"+pages[0].find("li",{"class":"next"}).find('a',href=True)['href']
    except:
        break




