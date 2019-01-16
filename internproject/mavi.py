from requests import get
from bs4 import BeautifulSoup

pages = [str(i) for i in range(1,5)]
for page in pages:
    response = get('https://www.mavi.com/kadin/c/1?page=' + page + '#page=' + page )


html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

containers = html_soup.find_all('div', class_ = 'item')

filename = "mavi.csv"
f = open(filename, "w")

headers = "Brand; title; product_feat; tot_price\n"
 	
f.write(headers)

for contain in containers:
    title = contain.img["title"]

    feature = contain.findAll("div",{"class":"features"})
    product_feat = feature[0].text.strip()

    price = contain.findAll("div",{"class":"price"})
    tot_price = price[0].text.strip()

    brand = "Mavi"

    print("brand: " + brand)
    print("title: " + title)
    print("product_feat: " + product_feat)
    print("tot_price: " + tot_price)

    f.write(brand + ";" + title + ";" + product_feat.replace('\n', '') + ";" + tot_price.replace('\n', '') + "\n")


f.close()
