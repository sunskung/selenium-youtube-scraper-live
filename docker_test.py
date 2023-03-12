from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def lambda_handler(event, context):

    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/opt/chromedriver',chrome_options=options)
    driver.get('https://www.google.com/')

    driver.close();
    driver.quit();

    response = {
        "statusCode": 200,
        "body": "Selenium Headless Chrome Initialized"
    }

    return response