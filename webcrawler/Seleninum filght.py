from selenium import webdriver
browser = webdriver.Chrome("C:/Users/Tanker/Downloads/chromedriver_win32/chromedriver.exe")
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights"
browser.get(url) # url로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
# browser.find_element_by_link_text("27")[0].click() # [0] -> 이번 달
# browser.find_element_by_link_text("28")[0].click() # [0] -> 이번 달

# 다음달 27, 28일 선택
# browser.find_element_by_link_text("27")[0].click() # [1] -> 다음 달
# browser.find_element_by_link_text("28")[0].click() # [1] -> 다음 달

# 이번 달 27, 다음 달 28일 선택
browser.find_element_by_link_text("27")[0].click() # [0] -> 이번 달
browser.find_element_by_link_text("28")[1].click() # [1] -> 다음 달