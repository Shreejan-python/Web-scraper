from selenium import webdriver

choice = input("Youtube, Kaggle, Github, Codewithharry : ")

if choice=='Youtube':
    url = 'https://www.youtube.com'
    browser = webdriver.Chrome()
    browser.get(url)
elif choice=='Codewithharry':
    url2 = 'http://codewithharry.com/'
    browser2 = webdriver.Chrome()
    browser2.get(url2)

elif choice=='Kaggle':
    url3 = 'https://www.kaggle.com/'
    browser3 = webdriver.Chrome()
    browser3.get(url3)

elif choice=='Github':
    url4 = 'https://github.com/'
    browser4 = webdriver.Chrome()
    browser4.get(url4)
