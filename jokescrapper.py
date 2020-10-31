import requests
import lxml
from bs4 import BeautifulSoup
import re


def dadjokes():
    source = requests.get(
        "https://www.boredpanda.com/funny-dad-jokes-puns/?utm_source=google&utm_medium=organic&utm_campaign=organic").text

    soup = BeautifulSoup(source, 'lxml')
    article = soup.find_all('article')

    contents = soup.find_all("span", class_="bordered-description")

    with open('joke.txt', "w") as f:
        for content in contents:
            content = content.text
            f.writelines(content + '\n')

dadjokes()

'''    content = content.findAll('li')

    jokes = []
    for x, con in enumerate(content):
        con = str(con)
        con = con[4:]
        con = con[:-5]

        if '<em>' or '</em>' or '\n' or '<i>' or '</i>' or '<br/>' or '\xa0' in con:
            con = con.replace("<em>", "")
            con = con.replace("</em>", "")
            con = con.replace("\n", "")
            con = con.replace('<i>', "")
            con = con.replace('</i>', "")
            con = con.replace('<br/>', "")
            con = con.replace("\xa0", "")

        jokes.append(con)

    with open('jokes.txt', "w") as f:
        for joke in jokes:
            f.writelines(joke + '\n')
'''