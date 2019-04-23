from selenium import webdriver
from time import sleep

def get_screenshots():
    path_to_chromedriver = "/Applications/chromedriver"

    driver = webdriver.Chrome(path_to_chromedriver)

    page_down_buttons = driver.find_elements_by_xpath('//button[@class="pdfemb-next"]')

    button = page_down_buttons[2]

    num = 1

    while num != 750:
        driver.save_screenshot(str(num) + ".png")
        button.click()
        num += 1
        sleep(1)