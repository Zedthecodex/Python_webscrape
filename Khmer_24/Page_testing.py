import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

# driver = webdriver.Chrome(PATH)

# def Item_Type(Type):
#     switcher = {
#         1: "computer-and-accessories",
#         2: ""
#     }
#    return switcher.get(Type,"")

Item_Type = 0;
Type = input("Please enter the type of item u are searching for \n 1).Electronics \n 2).Other things")
Type = int (Type)
if Type == 1:
    Item_Type = 'computer-and-accessories'
    print(Item_Type)
else :
    Item_Type = ''

search = input("please enter the item needed searching\n")
item_pass = search.replace(" ","+")
amount_pages = int(input ("Please insert the amount of pages you'd like to scrape (50 items per page) :"))
cap = amount_pages*50
print (cap)
i =0

while i <= cap:
    x = str(i)
    driver = webdriver.Chrome(PATH)
    url =  'https://www.khmer24.com/en/search?q='+ item_pass + '&category=' + Item_Type + '&perpage=' + x
    driver.get(url)
    print(driver.title)
    time.sleep(3)
    driver.quit()
    i = i + 50

print("Damn son")

# https://www.khmer24.com/en/search?q=gaming+computer&category=
#https://www.khmer24.com/en/search.html?q=gaming+computer&category=computer-and-accessories&per_page=50
# https://www.khmer24.com/en/search?q=gaming+computer&category=computer-and-accessories
#https://www.khmer24.com/en/search?q=gaming+computer&category=&perpage=50


# https://www.khmer24.com/en/search?q=gaming+computer&category=computer-and-accessories
# https://www.khmer24.com/en/search.html?q=gaming+computer&category=computer-and-accessories&per_page=50