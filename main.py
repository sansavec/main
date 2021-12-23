from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

opts = Options()
opts.add_argument('--headless')

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=opts)
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
driver.get('https://sat.tvmucho.com/app/tvmucho/?free&autostart&subscription=uk')

#jwtoken = driver.execute_script('return window.localStorage["token"]')
jwtoken = driver.execute_script('return window.localStorage')
print(jwtoken)

if jwtoken:
  with open('token', 'w') as f:
    f.write(jwtoken)

print('Quitting driver...')
driver.quit()

