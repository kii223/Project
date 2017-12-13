from bs4 import BeautifulSoup

info = []
with open('I:/Pycharm/Plan-for-combating-master/week1/1_2/1_2answer_of_homework/1_2_homework_required/index.html','r') as web_data:
    Soup = BeautifulSoup(web_data,'lxml')
    images = Soup.select('body > div:nth-of-type(1) > div > div.col-md-9 > div:nth-of-type(2) > div > div > img')
    titles = Soup.select('body > div:nth-of-type(1) > div > div.col-md-9 > div:nth-of-type(2) > div > div > div.caption > h4 > a')
    discribs = Soup.select('body > div:nth-of-type(1) > div > div.col-md-9 > div:nth-of-type(2) > div > div > div.caption > p')
    views = Soup.select('body > div:nth-of-type(1) > div > div.col-md-9 > div:nth-of-type(2) > div > div > div.ratings > p.pull-right')
    rates = Soup.select('body > div:nth-of-type(1) > div > div.col-md-9 > div:nth-of-type(2) > div > div > div.ratings > p:nth-of-type(2)')
    prices = Soup.select('body > div:nth-of-type(1) > div > div.col-md-9 > div:nth-of-type(2) > div > div > div.caption > h4.pull-right')
    #lenRate = []
    #for i in rates:
    #    lenRate.append(len(i.find_all('span','glyphicon glyphicon-star')))
    for image,title,discrib,view,rate,price in zip(images,titles,discribs,views,rates,prices):
        data = {
            'title':title.get_text(),
            'discrib':discrib.get_text(),
            'view':view.get_text(),
            'rate':'%s stars' % len(rate.find_all('span','glyphicon glyphicon-star')),
            'price':price.get_text(),
            'image':image.get('src')
        }
        info.append(data)


    for i in info:
        print(i)



'''for title,image,discrib,rate,cate in zip(titles,images,discribs,rates,cates):
    data ={
        'title':title.get_text(),
        'rate':rate.get_text(),
        'discrib':discrib.get_text(),
        'cate':list(cate.stripped_strings),
        'image':image.get('src')
    }
    info.append(data)
'''








'''
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4:nth-child(2) > a
/html/body/div[1]/div/div[2]/div[2]/div[1]/div/img
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > img
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > img
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4:nth-child(2) > a
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p:nth-child(2) > span:nth-child(1)
'''

