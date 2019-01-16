from requests import get
from bs4 import BeautifulSoup

#pages = [str(i) for i in range(1,5)]
#for page in pages:
response = get('https://www.defacto.com.tr/kadin')

#url = 'https://www.mavi.com/kadin/c/1?page=6#page=6'
#response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

containers = html_soup.find_all('div', class_ = 'product-item col-md-4 col-sm-4 col-xs-6')

filename = "defacto.csv"
f = open(filename, "w")

headers = "Brand; product_feat; tot_price\n"
 	
f.write(headers)


for contain in containers:
    #title = contain.img["title"]

    feature = contain.findAll("div",{"class":"prc-name"})
    product_feat = feature[0].text.strip()

    price = contain.findAll("div",{"class":"market"})
    pricemark = contain.findAll("i",{"class":"market-withoutsale"})
    tot_price = pricemark[0].text.strip()

    brand = "Defacto"

    print("brand: " + brand)
    #print("title: " + title)
    print("product_feat: " + product_feat)
    print("tot_price: " + tot_price)

    f.write(brand +  ";" + product_feat.replace('\n', '') + ";" + tot_price.replace('\n', '') + "\n")


f.close()