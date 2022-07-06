import re, warnings
from tqdm import tqdm
from lxml import etree
from bs4 import BeautifulSoup
from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

def tag_cleanup(html):
    html = str(html)
    cleanr = re.compile('<.*?>')
    string = (re.sub(cleanr, '', html))
    string = string.strip()
    return string

def main():
    URL = r'https://www.nba.com/players'
    
    CUR_DIR = Path(__file__).parent
    PROGRAM = 'chromedriver.exe'
    PATH = CUR_DIR / PROGRAM
    
    OPTIONS = webdriver.ChromeOptions()
    OPTIONS.add_argument('--headless')
    
    try:
        BROWSER = webdriver.Chrome(PATH, options=OPTIONS)
        
    except WebDriverException:
        BINARY = 'D:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        OPTIONS.binary_location = BINARY
        OPTIONS.add_experimental_option('excludeSwitches', ['enable-logging'])
        BROWSER = webdriver.Chrome(PATH, options=OPTIONS)
    
    try:  
        BROWSER.get(URL)
        WebDriverWait(BROWSER, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'players-list')))
        
        SELECT = Select(BROWSER.find_element_by_xpath('//*[@id="__next"]/div[2]/div[3]/section/div/div[2]/div[1]/div[7]/div/div[3]/div/label/div/select'))
        SELECT.select_by_visible_text('All')
        
        SOURCE = BROWSER.page_source
        BROWSER.close()
        
        SOUP = BeautifulSoup(SOURCE, 'lxml')
        
        TABLE = SOUP.find_all('table', class_ = 'players-list')[0].find_all('tbody')[0]
        
        for ROW in TABLE.find_all('tr', class_ = 'players-list'):
            pass
    
    except:
        pass
    
    IMG_URL = f'https://cdn.nba.com/headshots/nba/latest/1040x760/203500.png'
    
if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    main()