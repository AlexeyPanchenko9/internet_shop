import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
# Переходим на сайт
driver.get("http://practice.automationtesting.in/")
# Проскороллим страницу вниз
driver.execute_script("window.scrollBy(0, 600);")
PRESS_SELENIUM_RUBY = driver.find_element_by_css_selector(
    "#text-22-sub_row_1-0-2-0-0 .attachment-shop_catalog").click()
time.sleep(2)
PRESS_REVIEWS = driver.find_element_by_css_selector("[href='#tab-reviews']").click()
time.sleep(2)
# Ставим оценку 5 звезд
PRESS_5_STARS = driver.find_element_by_css_selector(" .stars .star-5").click()
time.sleep(2)
# Заполняем поля отзыва
TEXT_REVIEW = driver.find_element_by_id("comment")
TEXT_REVIEW.send_keys("Nice book!")
TEXT_NAME = driver.find_element_by_id("author")
TEXT_NAME.send_keys("Aleksey")
TEXT_EMAIL = driver.find_element_by_id("email")
TEXT_EMAIL.send_keys("panchenko@google.com")
PRESS_SUBMIT = driver.find_element_by_id("submit").click()
