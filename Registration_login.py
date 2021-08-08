import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
# _______________________________________________
# TEST 1
# Переходим на сайт
driver.get("http://practice.automationtesting.in/")
time.sleep(2)
# Нажимаем на вкладку My Account
PRESS_MY_ACCOUNT = driver.find_element_by_css_selector(
    "[href='http://practice.automationtesting.in/my-account/']").click()
# В поле регистрации вводим email и пароль и нажимаем "Register"
TEXT_EMAIL = driver.find_element_by_id("reg_email")
TEXT_EMAIL.send_keys("panchenko@google.com")
TEXT_PASSWORD = driver.find_element_by_id("reg_password")
TEXT_PASSWORD.send_keys("equAlizer135%246")
some_element = driver.find_element_by_id("content").click()
PRESS_BTN_REG = driver.find_element_by_css_selector(
    " .register .woocommerce-Button").click()
driver.quit()
# _______________________________________________
# TEST 2
# Переходим на сайт
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
time.sleep(2)
# Нажимаем на вкладку My Account
PRESS_MY_ACCOUNT = driver.find_element_by_css_selector(
    "[href='http://practice.automationtesting.in/my-account/']").click()
# В поле login вводим email и пароль и нажимаем "Register"
TEXT_LOGIN= driver.find_element_by_id("username")
TEXT_LOGIN.send_keys("panchenko@google.com")
TEXT_PASSWORD_LOG = driver.find_element_by_id("password")
TEXT_PASSWORD_LOG.send_keys("equAlizer135%246")
PRESS_BTN_LOGIN = driver.find_element_by_css_selector(
    " .login .woocommerce-Button").click()
# Проверка что Logout присутствует на странице
element = driver.find_element_by_class_name("csstransitions")
element_get_text = element.text
assert "Logout" in element_get_text
driver.quit()