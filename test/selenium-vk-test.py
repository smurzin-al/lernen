from selenium import webdriver
import time

try:
    link = 'https://vk.com/'
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)

    browser.find_element_by_css_selector('#index_email').send_keys('login')
    browser.find_element_by_css_selector('#index_pass').send_keys('password')
    browser.find_element_by_css_selector('#index_login_button').click()

    messanger = browser.find_elements_by_css_selector(' span.left_label.inl_bl')
    for el in messanger:
        if el.text == 'Мессенджер':
            el.click()
    dialogs = browser.find_element_by_css_selector('#im_dialogs_search')
    dialogs.send_keys('Избранное')
    talks = browser.find_elements_by_css_selector('span._im_dialog_link')
    for el in talks:
        if el.text == 'Избранное':
            el.click()
            break

    editor = browser.find_element_by_css_selector('.im_editable')
    editor.click()
    editor.send_keys('gggggg'+'\n')
    browser.find_element_by_css_selector('.im_editable').click()

finally:
    time.sleep(20)
    browser.quit()

