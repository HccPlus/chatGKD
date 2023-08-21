
from requests import get
from bs4 import BeautifulSoup
from json import dumps
from pprint import pprint


url = 'https://tieba.baidu.com/f?kw=孙笑川'


def getList(url):
    response = get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all(
        attrs={'class': 'threadlist_title pull_left j_th_tit'})
    # pprint(posts)
    idList = []

    for item in posts:
        id = item.a['href'][3:]
        idList.append(id)

    return idList


# 参数id为字符串
def getPost(id):
    response = get('https://tieba.baidu.com/p/' + str(id))
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    pageNum = soup.find(attrs={'class': 'l_reply_num'}).find_all(
        name='span')[-1].get_text(strip=True)
    pageNum = int(pageNum)

    textList = []
    for i in range(pageNum):
        response = get('https://tieba.baidu.com/p/' +
                       str(id) + '?pn=' + str(i + 1))
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        floors = soup.find_all(
            attrs={'class': 'd_post_content j_d_post_content'})
        # pprint(floors)
        for item in floors:
            floor = item.get_text(strip=True)
            textList.append(floor)
        print()
        file = open('log', 'w')
        file.write('\r(%d/%d)Readed' % (i + 1, pageNum))
        file.close()

    # file = open('sunba.html', 'w', encoding='UTF-8')
    # file.write(html)
    # file.close()
    # print()
    return textList


idList = getList(url)
pprint(idList)

dataBase = []
for i in range(len(idList)):
    print('getting:', idList[i])
    dataBase.append(getPost(idList[i]))

jsonStr = dumps(dataBase, ensure_ascii=False)
file = open('DataBase.json', 'w')
file.write(jsonStr)
file.close()
