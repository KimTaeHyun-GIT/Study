from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
 
# 다나와 사이트 검색
 
options = Options()
options.add_argument('headless'); # headless는 화면이나 페이지 이동을 표시하지 않고 동작하는 모드
 
# webdirver 설정(Chrome, Firefox 등)
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=options) # 브라우저 창 안보이기
# driver = webdriver.Chrome() # 브라우저 창 보이기
 
# 크롬 브라우저 내부 대기 (암묵적 대기)
driver.implicitly_wait(5)
 
# 브라우저 사이즈
driver.set_window_size(1920,1280)
 
# 페이지 이동(열고 싶은 URL)
driver.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')
 
# 제조사별 검색 
WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()
 
# 원하는 모델 카테고리 클릭 
WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="selectMaker_simple_priceCompare_A"]/li[16]/label'))).click()

time.sleep(2)
 
#bs4 초기화
soup = BeautifulSoup(driver.page_source, 'html.parser')
 
# 상품 리스트 선택
goods_list = soup.select('li.prod_item.prod_layer')

for v in goods_list:
    if v.find('div', class_='prod_main_info'):
        # 상품 모델명, 가격, 이미지
        name = v.select_one('p.prod_name > a').text.strip()
        price = v.select_one('p.price_sect > a').text.strip()
        img_link = v.select_one('div.thumb_image > a > img').get('data-original')
        if img_link == None:
            img_link = v.select_one('div.thumb_image > a > img').get('src')
        print(name, price, img_link)
    print()
    
# 브라우저 종료
driver.close()  