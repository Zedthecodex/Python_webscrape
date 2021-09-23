import time
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

file1= open ("D:\Python\Dumb_names.txt","wb")
file2= open ("D:\Python\Dumb_numbers.txt","w")
file3= open ("D:\Python\Location.txt","wb")
file4= open ("D:\Python\Time.txt", "w")
file5= open ("D:\Python\Item_hits.txt","w")
file6 = open ("D:\Python\False.txt", "w")

#driver = webdriver.Chrome(PATH)

Item_Type = 0;
Type = input("Please enter the type of item u are searching for \n 1).Electronics \n 2).Laptops \n 3).Other \n")
Type = int (Type)

Laptops = False
if Type == 1:
    Item_Type = 'computer-and-accessories'

    print(Item_Type)

elif Type ==2:
    Laptops = True;
else :
    Item_Type = ''


search = input("please enter the item needed searching\n")
item_pass = search.replace(" ","+")
amount_pages = int(input("Please insert the amount of pages needed scraping (1 page = 50 items) : "))
cap = (amount_pages-1)*50
i=0


while i <= cap :
    x= str(i)
    driver = webdriver.Chrome(PATH)
    if Laptops == True :
        url = 'https://www.khmer24.com/en/c-laptops.html?per_page=' + x
    else :
        url = 'https://www.khmer24.com/en/search?q=' + item_pass + '&category=' + Item_Type + '&per_page=' + x
    driver.get(url)
    items = driver.find_elements_by_xpath('//li[@class="item "]')
    element = driver.find_elements_by_xpath('//span[@class="price"][1]')
    product_names = driver.find_elements_by_xpath('//h2[@class="item-title truncate truncate-2 "]')
    Location = driver.find_elements_by_xpath('//ul[@class="list-unstyled summary"]/li[1]')
    Time = driver.find_elements_by_xpath('//ul[@class="list-unstyled summary"]/li[2]')
    Hits = driver.find_elements_by_xpath('//ul[@class="list-unstyled summary"]/li[3]')

    for name in product_names:
        print(name.text)
        name1 = name.text + "\n"
        encoded = name1.encode("utf8")

        file1.write(encoded)

    for price in element:
        print(price.text)

        file2.write(price.text + "\n")

    for place in Location:
        print(place.text)
        places = place.text + "\n"
        encoded = places.encode("utf8")

        file3.write(encoded)

    for Hour in Time:
        print(Hour.text)
        Hours = Hour.text + "\n"

        file4.write(Hours)

    for Popularity in Hits:
        print(Popularity.text)
        Popularities = Popularity.text + "\n"

        file5.write(Popularities)

    i = i + 50
    time.sleep(2)
    driver.quit()



time.sleep(3)

driver.quit()