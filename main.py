from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

opts = Options()
opts.add_argument('--headless')

count = 0
while count < 20:
    #s = Service(ChromeDriverManager().install())
    #driver = webdriver.Chrome(service=s, options=opts)
    #driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=opts)
    driver.get('https://sat.tvmucho.com/app/tvmucho/?free&autostart&subscription=uk')

    jwtoken = driver.execute_script('return window.localStorage')
    print(jwtoken)
    print('Quitting driver...')
    driver.quit()

    if jwtoken:
        with open('token', 'w') as f:
            f.write(jwtoken)
        break

    count += 1
