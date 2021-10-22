# increase youtube views with python
# Developer: Mohammad Ali Bazzazi (me)

print("""
_______________     __________   _______   _______    _________   _______    #
|              \   |          |        /         /   |         |        /   
|               |  |          |       /         /    |         |       /     |
|              /   |          |      /         /     |         |      /      |
|_____________|    |__________|     /         /      |_________|     /       |
|              \   |          |    /         /       |         |    /        |
|               |  |          |   /         /        |         |   /         |
|              /   |          |  /         /         |         |  /          |
|_____________/    |          | /_______  /_______   |         | /______     |
""")
print("*********************************************************************************")
print("*"+" "*79+"*")
print("*  Copyright of Mohammad Ali Bazzazi, 2021 ©                                    *")
print("*"+" "*79+"*")
print("*  https://www.youtube.com/channel/UCeLKoNs3c72Vc-OG3uNQxGw?sub_confirmation=1  *")
print("*"+" "*79+"*")
print("*********************************************************************************")

################## START ##################

# import kardan ketabkhane ha
from selenium import webdriver
import time, os

# nasbe ketabkhane selenium, lotfan be internet vasl bashid!
# baraye windows
try:
    os.system("pip install selenium")
except:
    pass

# baraye linux
try:
    os.system("sudo apt install python3-pip")
    os.system("pip3 install selenium")
except:
    pass

# ijad dota list baraye link ha va driver ha
# link video haye khod ra dar list links garar bedid
links=["link 1", "link 2"]
drivers=[]

# betedade link ha driver ijad mikonam
for i in range(0, len(links)):
    # path chrome driver ra bedune .exe jeloye executable_path="" vared konid
    drivers.append(webdriver.Chrome(executable_path="chrome driver path"))

# har link ra dar panjare haye jodagane baz mikonam
for driver in drivers:
    # baz kardan link video dar yek panjare chrome
    driver.get(links[drivers.index(driver)])

# ijad yek halge baraye inke har 60 sanye safhe chrome ra refresh konad
# shoma mitavanid bejaye 60 har adade dige garar bedid
while 1:
    # sabr kardan be modat 60 sec
    time.sleep(60)
    # ba estefade az driver.refresh() panjare haye chrome ra refresh mikonm
    for driver in drivers:
        driver.refresh()

################## END ##################

# please subscribe and like youtube channel
