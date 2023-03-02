# let's start fresh after installing Selenium for simplicity reasons
pip install bs4
pip install selenium
pip install requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

def get_driver():
    # get chrome driver - u can think of the driver as browser
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('./chromedriver', options=options)
    return driver

if __name__ == "__main__":

  print('Creating Driver')
  driver = get_driver()

  # With the same metaphor, you can insert URL to the browser
  print('Fetching the page')
  driver.get(YOUTUBE_TRENDING_URL)

  # now, we can get the page title
  print('Page title:', driver.title)

  print('Getting the video divs')
  video_div_class = 'ytd-video-renderer'
  # video_div = driver.find_element(By.CLASS_NAME, video_div_class)
  video_div = driver.find_elements_by_class_name(video_div_class)

  print(f'Found {len(video_div)} videos')



