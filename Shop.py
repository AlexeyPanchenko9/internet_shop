import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# ________________________________TEST 1___________________________
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
# Нажимаем вкладку SHOP и выбираем необходимую книгу
PRESS_SHOP = driver.find_element_by_css_selector(
    "#menu-item-40 > [href='http://practice.automationtesting.in/shop/']").click()
PRESS_ON_BOOK = driver.find_element_by_css_selector(
    " .products .post-181 .attachment-shop_catalog").click()
# Проверяем название книги
element = driver.find_element_by_class_name("product_title")
element_get_text = element.text
assert "HTML5 Forms" in element_get_text
if element_get_text == ("HTML5 Forms"):
    print("Заголовок книги называется HTML5 Forms")
else:
    print("Заголовок книги НЕ называется HTML5 Forms")
driver.quit()
# ________________________________TEST 2___________________________
# Переходим на сайт
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
time.sleep(2)
# Нажимаем на вкладку My Account
PRESS_MY_ACCOUNT = driver.find_element_by_css_selector(
    "[href='http://practice.automationtesting.in/my-account/']").click()
# В поле login вводим email и пароль и нажимаем "Login"
TEXT_LOGIN= driver.find_element_by_id("username")
TEXT_LOGIN.send_keys("panchenko@google.com")
TEXT_PASSWORD_LOG = driver.find_element_by_id("password")
TEXT_PASSWORD_LOG.send_keys("equAlizer135%246")
PRESS_BTN_LOGIN = driver.find_element_by_css_selector(
    " .login .woocommerce-Button").click()
PRESS_SHOP = driver.find_element_by_css_selector(
    "#menu-item-40 > [href='http://practice.automationtesting.in/shop/']").click()
# Заходим на вкладку HTML
PRESS_HTML = driver.find_element_by_css_selector(
    "[href='http://practice.automationtesting.in/product-category/html/']").click()
# FIND_NUMBER_OF_BOOKS = driver.find_element_by_link_text('3')
FIND_NUMBER_OF_BOOKS = driver.find_element_by_css_selector(" .cat-item-19 .count")
FIND_NUMBER_OF_BOOKS_TEXT = FIND_NUMBER_OF_BOOKS.text
assert "(3)" in FIND_NUMBER_OF_BOOKS_TEXT
if FIND_NUMBER_OF_BOOKS_TEXT == ("(3)"):
    print("Количество книг в разделе HTML : 3")
else:
    print("Количество книг в разделе HTML НЕ 3")
driver.quit()
# ________________________________TEST 3___________________________
# Переходим на сайт
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
time.sleep(2)
# Нажимаем на вкладку My Account
PRESS_MY_ACCOUNT = driver.find_element_by_css_selector(
    "[href='http://practice.automationtesting.in/my-account/']").click()
# В поле login вводим email и пароль и нажимаем "Login"
TEXT_LOGIN= driver.find_element_by_id("username")
TEXT_LOGIN.send_keys("panchenko@google.com")
TEXT_PASSWORD_LOG = driver.find_element_by_id("password")
TEXT_PASSWORD_LOG.send_keys("equAlizer135%246")
PRESS_BTN_LOGIN = driver.find_element_by_css_selector(
    " .login .woocommerce-Button").click()
PRESS_SHOP = driver.find_element_by_css_selector(
    "#menu-item-40 > [href='http://practice.automationtesting.in/shop/']").click()
# НЕ СМОГ ПРОВЕРИТЬ СОСТОЯНИЕ!!!!!!!!!!!!!!
element = driver.find_element_by_class_name("orderby")
select = Select(element)
select.select_by_value("menu_order")
driver.quit()
# ________________________________TEST 4___________________________
# Переходим на сайт
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
time.sleep(2)
# Нажимаем на вкладку My Account
PRESS_MY_ACCOUNT = driver.find_element_by_css_selector(
    "[href='http://practice.automationtesting.in/my-account/']").click()
# В поле login вводим email и пароль и нажимаем "Login"
TEXT_LOGIN = driver.find_element_by_id("username")
TEXT_LOGIN.send_keys("panchenko@google.com")
TEXT_PASSWORD_LOG = driver.find_element_by_id("password")
TEXT_PASSWORD_LOG.send_keys("equAlizer135%246")
PRESS_BTN_LOGIN = driver.find_element_by_css_selector(
    " .login .woocommerce-Button").click()
PRESS_SHOP = driver.find_element_by_css_selector(
    "#menu-item-40 > [href='http://practice.automationtesting.in/shop/']").click()
PRESS_ON_BOOK_1 = driver.find_element_by_css_selector(
     ".woocommerce-LoopProduct-link > "
     "[src='http://practice.automationtesting.in/wp-content/uploads/2017/01/Android-Quick-Start-Guide-300x300.png']").click()
# Проверяем старую цену книги
PRICE_OLD = driver.find_element_by_css_selector("del > span")
element_get_text_1 = PRICE_OLD.text
assert "₹600.00" in element_get_text_1
if element_get_text_1 == ("₹600.00"):
    print("Старая цена книги ₹600.00")
else:
    print("Старая цена книги не ₹600.00")
# Проверяем новую цену книги
PRICE_NEW = driver.find_element_by_css_selector("ins > span")
element_get_text_2 = PRICE_NEW.text
assert "₹450.00" in element_get_text_2
if element_get_text_2 == ("₹450.00"):
    print("Новая цена книги ₹450.00")
else:
    print("Новая цена книги не ₹450.00")
# Проверка что изображение книги присутсвует и нажимаем на него
PICTURE_check = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "attachment-shop_single")))
PICTURE_check.click()
# Проверяем прогрузку изображения и закрываем предпросмотр
PICTURE_VIEW = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "fullResImage")))
BTN_CLOSE = driver.find_element_by_class_name("pp_close").click()
driver.quit()
# ________________________________TEST 5___________________________
# Переходим на сайт
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
PRESS_SHOP = driver.find_element_by_css_selector(
    "#menu-item-40 > [href='http://practice.automationtesting.in/shop/']").click()
PRESS_ADD_BASKET = driver.find_element_by_css_selector(
    "[href='/shop/?add-to-cart=182']").click()
time.sleep(3)
# Проверяем количество товаров и цену в корзине
ITEMS_BASKET = driver.find_element_by_class_name("cartcontents")
element_get_text_3 = ITEMS_BASKET.text
assert "1 Item" in element_get_text_3
if element_get_text_3 == ("1 Item"):
    print("В корзине 1 товар")
else:
    print("В корзине НЕ 1 товар")
PRICE_BASKET = driver.find_element_by_css_selector(" .wpmenucart-contents .amount")
element_get_text_4 = PRICE_BASKET.text
assert "₹180.00" in element_get_text_4
if element_get_text_4 == ("₹180.00"):
    print("Стоимость ₹180.00")
else:
    print("Стоимость НЕ ₹180.00")
ITEMS_BASKET.click()
# Явное ожидание, что отобразилась стоимость
PRICE_SHOW = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, " .cart-subtotal .woocommerce-Price-amount"), "₹180.00"))
PRICE_SHOW_TOTAL = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, " .order-total .woocommerce-Price-amount"), "₹"))
driver.quit()
# ________________________________TEST 6___________________________
# Переходим на сайт
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
PRESS_SHOP = driver.find_element_by_css_selector(
     "#menu-item-40 > [href='http://practice.automationtesting.in/shop/']").click()
# Проскороллим страницу вниз
driver.execute_script("window.scrollBy(0, 300);")
# Добавляем книги в корзину и переходим в нее
PRESS_ADD_BASKET_FIRST_BOOK = driver.find_element_by_css_selector(
    "[href='/shop/?add-to-cart=182']").click()
time.sleep(3)
PRESS_ADD_BASKET_SECOND_BOOK = driver.find_element_by_css_selector(
    "[href='/shop/?add-to-cart=180']").click()
ITEMS_BASKET = driver.find_element_by_class_name("cartcontents").click()
time.sleep(3)
# Удаляем первую книгу из корзины и отменяем удаление
REMOVE_BOOK = driver.find_element_by_css_selector("[data-product_id ='182']").click()
time.sleep(3)
UNDO_BOOK = driver.find_element_by_css_selector(" .woocommerce-message > a").click()
#  Изменяем количество книг в заказе и обновляем данные в корзине
COUNT_BOOK = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]").clear()
COUNT_BOOK = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]").click()
COUNT_BOOK_1 = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
COUNT_BOOK_1.send_keys("3")
BTN_UPDATE_BASKET = driver.find_element_by_css_selector("[value='Update Basket']").click()
# Проверяем количество книг в заказе
COUNT_BOOK_1 = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
GET_ATTRIBUTE = COUNT_BOOK_1.get_attribute("value")
if GET_ATTRIBUTE == ("3"):
    print("Количество книг JS Data Structures and Algorithm в корзине: ", GET_ATTRIBUTE)
else:
    print("Ошибка. Количество книг неверное")
time.sleep(3)
# Нажимаем на кнопку Apply Coupon и дожидаемся сообщения о необходимости добавить код купона
BTN_APPLY_COUPON = driver.find_element_by_css_selector("[value='Apply Coupon']").click()
MESSAGE_INFO = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))
driver.quit()
# ________________________________TEST 7___________________________
# Переходим на сайт
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
PRESS_SHOP = driver.find_element_by_css_selector(
    "#menu-item-40 > [href='http://practice.automationtesting.in/shop/']").click()
# Проскороллим страницу вниз
driver.execute_script("window.scrollBy(0, 300);")
# Добавляем книгу в корзину и переходим в нее
PRESS_ADD_BASKET_BOOK = driver.find_element_by_css_selector(
    "[href='/shop/?add-to-cart=182']").click()
time.sleep(3)
ITEMS_BASKET = driver.find_element_by_class_name("cartcontents").click()
# Нажимаем Proceed to check out
PRESS_PROCEED_TO_CHECK_OUT = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, " .wc-proceed-to-checkout .checkout-button")))
PRESS_PROCEED_TO_CHECK_OUT.click()
# Вводим в поля данные
FIELD_FIRST_NAME = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing_first_name_field .input-text ")))
FIELD_FIRST_NAME.send_keys("Alexey")
FIELD_LAST_NAME = driver.find_element_by_css_selector(
    "#billing_last_name_field .input-text ").send_keys("Ivanov")
FIELD_EMAIL = driver.find_element_by_css_selector(
    "#billing_email_field .input-text").send_keys("panchenko@google.com")
FIELD_PHONE = driver.find_element_by_id("billing_phone").send_keys("88005551525")
FIELD_COUNTRY = driver.find_element_by_class_name("select2-container").click()
CHANGE_COUNTRY = driver.find_element_by_css_selector(
    " .select2-search .select2-input").send_keys("Poland")
CHANGE_COUNTRY_1 = driver.find_element_by_class_name("select2-match").click()
FIELD_ADRESS = driver.find_element_by_css_selector(
    "#billing_address_1_field .input-text").send_keys("Moskovskaya Avenue")
FIELD_ZIP = driver.find_element_by_css_selector(
    "#billing_postcode_field .input-text").send_keys("55580011")
FIELD_CITY = driver.find_element_by_css_selector(
    "#billing_city_field .input-text").send_keys("Warsaw")
# Проскороллим страницу вниз
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
# Выбираем тип оплаты
CHOICE_TYPE_OF_PAY = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#payment_method_cheque.input-radio")))
CHOICE_TYPE_OF_PAY.click()
# Нжимаем Place Order
BTN_PLACE_ORDER = driver.find_element_by_id("place_order").click()
# Проверяем наличие информационного текста и верного типа оплаты
MESSAGE_INFO_1 = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"),
    "Thank you. Your order has been received."))
TYPE_PAY = driver.find_element_by_css_selector("table > tfoot > tr:nth-child(3) > td")
TYPE_PAY_text = TYPE_PAY.text
assert "Check Payments" in TYPE_PAY_text
if TYPE_PAY_text == ("Check Payments"):
    print("Выбран тип оплаты: Check Payments")
else:
    print("Выбран тип оплаты НЕ: Check Payments")
driver.quit()