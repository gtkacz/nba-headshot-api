import re, warnings, pandas as pd, os
from tqdm import tqdm
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
        BINARY = r'D:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
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
        INFORMATION = {}
        
        TABLE = SOUP.find_all('table', class_ = 'players-list')[0]
        TBODY = TABLE.find_all('tbody')[0]
        
        DF_ROW_LIST = []
        
        for ROW in tqdm(TBODY.find_all('tr')):
            INFO_RAW = ROW.find_all('td', class_ = 'primary text RosterRow_primaryCol__19xPQ')[0]
            
            ID = INFO_RAW.find_all('a', href=True)[0]['href'].split('/')[2]
            
            PLAYER_NAME_RAW = INFO_RAW.find_all('p', class_ = 't6')
            PLAYER_NAME = f'{PLAYER_NAME_RAW[0].text} {PLAYER_NAME_RAW[1].text}'
            
            TEAM = ROW.find_all('td', class_ = 'text')[1].text
            
            DF_ROW_LIST.append({
                'ID': ID,
                'Name': PLAYER_NAME,
                'Team': TEAM
            })
            
        DF = pd.DataFrame(DF_ROW_LIST)
        DF.to_csv(f'{os.path.abspath(os.path.join(os.getcwd(), os.pardir))}\\data.csv', encoding='utf-8', index=False)
    
    except TimeoutException:
        print('Request timed out.')
    
if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    main()