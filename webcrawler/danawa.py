from bs4 import BeautifulSoup # BeautifulSoup 임포트
from selenium import webdriver # selenium 임포트
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('C:/Users/Tanker/Downloads/chromedriver_win32/chromedriver.exe') # 크롬 드라이버 위치 잡아주기
#driver.implicitly_wait(3) # 웹 자원 로드 시간 3초
#driver.get('https://nid.naver.com/nidlogin.login') # 네이버 로그인 페이지 접속

#driver.find_element_by_name('id').send_keys('naver_id') # 아이디 보내기
#driver.find_element_by_name('pw').send_keys('mypassword1234') # 비밀번호 보내기

#driver.find_element_by_xpath('//*[@id="log.login"]').click() # 로그인 버튼 클릭
 
# 다나와 사이트 검색
 
options = Options()
options.add_argument('headless'); # headless는 화면이나 페이지 이동을 표시하지 않고 동작하는 모드
 
# webdirver 설정(Chrome, Firefox 등)
chromedriver_autoinstaller.install()
# driver = webdriver.Chrome(options=options) # 브라우저 창 안보이기
driver = webdriver.Chrome() # 브라우저 창 보이기
 
# 크롬 브라우저 내부 대기 (암묵적 대기)
driver.implicitly_wait(5)
 
# 브라우저 사이즈
driver.set_window_size(1920,1280)
 
# 페이지 이동(열고 싶은 URL)
driver.get('http://prod.danawa.com/list/?cate=112747')
 
# 페이지 내용
# print('Page Contents : {}'.format(driver.page_source))
 
# 제조사별 검색 (XPATH 경로 찾는 방법은 이미지 참조)
WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="searchMakerRep3132"]'))).click()
 
# 원하는 모델 카테고리 클릭 (XPATH 경로 찾는 방법은 이미지 참조)
WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="searchAttributeValueRep706768"]'))).click()
 
# 2차 페이지 내용
# print('After Page Contents : {}'.format(driver.page_source))
 
# 검색 결과가 렌더링 될 때까지 잠시 대기
time.sleep(2)
 
#bs4 초기화
soup = BeautifulSoup(driver.page_source, 'html.parser')
 
# 소스코드 정리
# print(soup.prettify())
 
# 상품 리스트 선택
# goods_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')
goods_list = soup.select('li.prod_item.prod_layer')
 
# 상품 리스트 확인
# print(goods_list)
 
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

