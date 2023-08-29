import requests
from bs4 import BeautifulSoup
url = 'https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date=8/21/2023#'
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
championships = soup.find_all('div', class_='matchCard')
for i in range(len(championships)):
    f = open("12-21-2023_yallacora","a",encoding="utf-8")
    f.write(f"\n")
    f.write(f"\t\t{championships[i].contents[1].find('h2').text.strip()}")
    f.write(f"\n")
    matches = championships[i].contents[3].find_all('li')
    for match in matches:
        try:
            channel=match.find('div',{"class":'channel'}).text.strip()
        except:
            channel=""
        status = match.find('div', {"class": 'matchStatus'}).text.strip()
        teamA = match.find('div', {"class": 'teamA'}).text.strip()
        teamB = match.find('div', {"class": 'teamB'}).text.strip()
        results = match.find('div', {'class':'MResult'}).find_all('span', {'class':'score'})
        score=f"{results[0].text.strip()} - {results[1].text.strip()}"
        time = match.find('div', {'class': 'MResult'}).find('span', {'class': 'time'}).text.strip()
        #print(f'{channel}\t\t{status}\n{teamA} {score} {teamB}\n\t\t{time}\n' )
        #with open("12-21-2023_yallacora", "a", encoding="utf-8") as f:
        f.write(f'{channel}\t\t{status}\n\t{teamA}{score}{teamB}\n\t\t{time}\n')
        f.write(f"\n")
        f.write(f"-"*50)
        f.write(f"\n")
    f.write(f"\n")
    f.write(f"\n")
    f.write(f"="*50)
    f.write(f"\n")
    f.write(f"\n")







