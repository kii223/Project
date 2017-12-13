from bs4 import BeautifulSoup

info = []
with open('I:/Pycharm/Plan-for-combating-master/week1/1_2/1_2code_of_video/web/new_index.html','r') as webdata:
    Soup = BeautifulSoup(webdata,'lxml')
    images = Soup.select('body > div.main-content > ul > li > img')
    titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    discribs = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    rates = Soup.select('body > div.main-content > ul > li > div.rate > span')
    cates = Soup.select('div.main-content > ul > li > div.article-info > p.meta-info')
# print(images,titles,discrib,rate,cates,sep='\n-------------\n')
for title,image,discrib,rate,cate in zip(titles,images,discribs,rates,cates):
    data ={
        'title':title.get_text(),
        'rate':rate.get_text(),
        'discrib':discrib.get_text(),
        'cate':list(cate.stripped_strings),
        'image':image.get('src')
    }
    info.append(data)

for i in info:
    if float(i['rate']) > 3:
        print(i['title'],i['cate'])







'''
body > div.main - content > ul > li: nth - child(1) > div.article - info > h3 > a
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info > span:nth-child(2)
body > div.main - content > ul > li: nth - child(1) > div.article - info > p.description
body > div.main - content > ul > li: nth - child(1) > img
body > div.main-content > ul > li:nth-child(1) > div.rate > span
'''

