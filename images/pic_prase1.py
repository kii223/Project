from bs4 import BeautifulSoup
import requests
import time
import urllib
import urllib.request
urls_walk = ['http://www.jpmsg.com/meinv/walk_meinv_{}.html'.format(str(i)) for i in range(140, 142)]
url = 'http://www.jpmsg.com/meinv/walk_meinv_140.html'
'''for url in urls_walk:'''
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
srcs = soup.select('body > div.wrapper > div.column-content > div > div > div > a:nth-of-type(1) > img')
print(srcs)
'''
x = 1
for url in urls:
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.select('#MyContent > p > img')
    for image in imgs:
        image = image.get('src')
        urllib.request.urlretrieve(image, 'I:\Pycharm\Project\pic\%s.jpg' % x)
        print(x)
        time.sleep(0.5)
        x = x + 1
    print(url)
'''








'''
#taplc_attraction_coverpage_attraction_0 > div:nth-child(1) > div > div > div.shelf_item_container > div:nth-child(1) > div.poi > div > div.item.name > a
#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.listing_title > a
#lazyload_585054151_5
#lazyload_585054151_5
#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.photo_booking.non_generic > a
'''
'''
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Cookie': 'VRMCID=%1%V1*id.10568*llp.%2F*e.1513003750512; TAUnique=%1%enc%3AZMGapcuykyYsiU2eMyrfH7xWCn3LoI4lUvzrLVXkc101QsIvfKZfHg%3D%3D; TAPD=cn.tripadvisor.com; TASSK=enc%3AANMXkbTwhyIrFVR4W9685AaNMBQa%2BeZ00%2Fb4nz8f3Vzy1%2Bojec7%2BiP6kET67eJpbiR2QiLjf1HcOg90kutvNh4A%2FR9zb9F7DhiC%2BNl1SZDu%2BA3y%2BEmWAFvyn8nfSHDUfNw%3D%3D; TART=%1%enc%3ACMxqX9jI6HzmO432F7uBaa2qRlj1BS6OpjRktb89%2BPnDwrIExybMDa6zmAQRKzoIkagyFvowwb0%3D; ki_u=34457eb0-9922-f0f4-9ecb-c58f; ki_s=175381%3A1.1.0.0.2; __gads=ID=2154e1c201bba92a:T=1512399364:S=ALNI_MZjB7_nBCgNTIZw-dZe52I256Wj4Q; ServerPool=X; PMC=V2*MS.39*MD.20171204*LD.20171206; PAC=AKqjWJDy-OxzfMZrRQ_4FRCUFKmIX8jTe__5uo9YhlwAEpiwgOUy-L6kyPrVbC66tV4OFNCD20l12J3-Bl89j--fL0cX4CXMxqvdSClYH1vRVh6AdK9FFgaYrVgQyG3iMuY1oUs2GZQqVhBstPYft3yF5FRyxrq3d_dUFK1KhCXCyhviMZjitViuNqc8E16UhA%3D%3D; ki_t=1512398990004%3B1512568336485%3B1512568336485%3B3%3B3; ki_r=; SecureLogin2=3.4%3AAF8DfA9NLl2AF5y0XmdLZqjIu5Q8vvgDhhiy5eJ0lDO3YQaS0rp4fhAqP4hUY4rYQodCSlitDDMoxjCMgTMDaUZoSNb0zo3aksaYufA3mLz77PMRaotuBq5SdzGwpWnumudiHLWSlEkpBaRQoF%2F0gQnR0FynacbVA%2BLDnU99XrE8mummW5KtD3mqJtMunYq0JLO4b88zwoVr7yfaAU0VEqg%3D; TAAuth3=3%3A112c83d2ab067e10373b7e1b5ee9e892%3AAKLOPPqz8r0CamGq%2BdWLcYczqcRa01KiCLE5PZNhLn%2B%2FSWRtyDtLBh11f2YuAyWeM68OpoxbI9qSswaFTSmwVOsyOUiNXUDb%2F1Qzc4sEnwpQJBt7ew8s25X5k0GdrQzLnchuhznHZKHPTZZyiDVBf%2BPriulrd7UyfwGEMx7bPwIzF376l2d5913ClDp9AXrqxeKcFZdIZ%2FdrLSQ145eedHw%3D; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCpmPopunder_1%2C%2C-1%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C1%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7Ccatchpers%2C3%2C1513003790%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; roybatty=TNI1625!AOJmpTmxcxeL%2FsGIQ8EHCAyKznE5cVlkcwi0douXgLJi6cy1%2FgJyws1%2F4J%2FVn%2FSh3CP3SlgmuezTWOzw8s5fNecwm4wao%2BgxB%2FXkFAPtYRIawR59pBd1YWkv81fb%2Bgh6A%2BYJeruhIlhiIfk6Pxy%2F6Fr%2FssEhJxZTw2QRlX6Z5xTi%2C1; TASession=%1%V2ID.2D1E5F7395C69629CD239A744D5A967F*SQ.68*PR.427%7C*LS.DemandLoadAjax*GR.90*TCPAR.13*TBR.82*EXEX.48*ABTR.68*PHTB.4*FS.3*CPU.82*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.69B8EEC11C1F8A382DCEC95DD6A59C96*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.60763; TATravelInfo=V2*AY.2017*AM.12*AD.17*DY.2017*DM.12*DD.18*A.2*MG.-1*HP.2*FL.3*RVL.104365_340l587661_340l60763_340*DSM.1512570155026*RS.1; TAUD=LA-1512558684307-1*RDD-1-2017_12_06*LD-11470705-2017.12.17.2017.12.18*LG-11470707-2.1.F.'
}
urlSaves = 'https://cn.tripadvisor.com/Saves/69733279'
webData = requests.get(urlSaves, headers=headers)
soup = BeautifulSoup(webData.text, 'lxml')
titles = soup.select('a.title')
print(titles)
'''