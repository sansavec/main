import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
driver.get('https://sat.tvmucho.com/app/tvmucho/?free&autostart&subscription=uk')
    
jwtoken = driver.execute_script('return window.localStorage["token"]')
   
if jwtoken:
  with open('token', 'w') as f:
    f.write(jwtoken)

driver.quit()
