#!/usr/bin/python3
# coding: utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import shutil
import openpyxl
import urllib.request
import time

# Helper methods
# ** Checking found CSS element
def is_element_width_ok(element):
    element_width = int(element.get_attribute('width'))
    return element_width > 190

def is_element_src_ok(element):
    element_scr_contains_lotr_traits = element.get_attribute('src').find("wikia.nocookie.net/lotr/images") != -1
    return element_scr_contains_lotr_traits

def is_element_contains_extension(str, extension):
    return str.find(extension) != -1

def get_image_extension(url):
    if is_element_contains_extension(url, ".jpg"):
        return '.jpg'
    elif is_element_contains_extension(url, ".png"):
        return '.png'
    elif is_element_contains_extension(url, ".jpeg"):
        return '.jpeg'
    else:
        return '.file'

def is_element_extension_ok(element):
    element_src = element.get_attribute('src')
    return is_element_contains_extension(element_src, '.jpg') or is_element_contains_extension(element_src, '.png') or is_element_contains_extension(element_src, '.jpeg')

def is_element_ok(element):
    is_width_ok     = is_element_width_ok(element)
    is_src_ok       = is_element_src_ok(element)
    is_extension_ok = is_element_extension_ok(element)
    return is_width_ok and is_src_ok and is_extension_ok




def save_image_for_url(url, rusUrl = False, imagesCounter = -1):

    cleanedImgSrc = url

    if not rusUrl:
        urlEndPosition = url.find('/revision')
        cleanedImgSrc = url[:urlEndPosition]

    print('Link found: ' + cleanedImgSrc)
    driver.get(cleanedImgSrc)

    image_file_name = imagename

    if imagesCounter == -1:
        image_file_name = imagename + '.jpg'
    else:
         image_file_name = imagename + str(imagesCounter) + '.jpg'

    driver.get_screenshot_as_file(dir_path + '/' + image_file_name)
    print('***** Image saved!!! *****')



def save_images_for_urlsList(urls_list):
    imagesCounter = 1
    for url in urls_list:
        save_image_for_url(url, imagesCounter)
        imagesCounter += 1

def save_first_image_for_urlsList(urls_list):
    save_image_for_url(urls_list[0])

def rus_save_first_image_for_urlsList(urls_list):
    save_image_for_url(urls_list[0], True)


def retrieve_image_for_url(url, rusUrl = False, imagesCounter = -1):
    cleanedImgSrc = url

    if not rusUrl:
        urlEndPosition = url.find('/revision')
        cleanedImgSrc = url[:urlEndPosition]

    print('Link found: ' + cleanedImgSrc)

    image_file_name = imagename

    if imagesCounter == -1:
        image_file_name = imagename + get_image_extension(url)
    else:
         image_file_name = imagename + str(imagesCounter) + get_image_extension(url)

    urllib.request.urlretrieve(cleanedImgSrc, dir_path + '/' + image_file_name)
    print('***** Image saved!!! *****')

def retrieve_images_for_urlsList(urls_list):
    imagesCounter = 1
    for url in urls_list:
        retrieve_image_for_url(url, imagesCounter)
        imagesCounter += 1

def retrieve_first_image_for_urlsList(urls_list):
    retrieve_image_for_url(urls_list[0])

def rus_retrieve_first_image_for_urlsList(urls_list):
    retrieve_image_for_url(urls_list[0], True)


def create_dir_for_names_images(category_path):
    dir_path = category_path
    os.makedirs(dir_path)
    return dir_path

# +++++++++++++++ SCRIPT START +++++++++++++++

os.chdir('!WORKFLOW')

# *** SCRIPT CONFIGURATION:
cell_start_number   = 710
cell_end_number     = 1399
macos               = 1


if macos == 1:
    # MacOS ver:
    path_to_chromedriver = "/Applications/chromedriver"
else:
    # Windows ver:
    path_to_chromedriver = "C:/chromedriver.exe"

driver = webdriver.Chrome(path_to_chromedriver)

# === 1. Opening source workbook with names ===
workbook = openpyxl.load_workbook('DoneTable.xlsx')
sheet = workbook.get_sheet_by_name('sheet1')

# === 2. Iterating throught cells
for index in range(cell_start_number ,cell_end_number + 1):
    name_cell       = sheet['B'+str(index)]
    link_cell       = sheet['E'+str(index)]

    name        = name_cell.value
    url         = link_cell.value

    print('\n' + str(index-1) + '. ^^^^^^^^^^^^^^ Start processing name: ' + name)
    driver.get(url)

    try:
        phone_box = driver.find_element_by_css_selector('.phones-box')
        phone_box.click()
    except NoSuchElementException:
        print('No phones_box. continue')
        continue

    # phone_box = driver.find_element_by_css_selector('.phones-box')
    # phone_box.click()

    time.sleep(1)

    try:
        phones = driver.find_elements_by_css_selector('.a-phones')
    except NoSuchElementException:
        print('No .a-phones continue')
        continue

    # phones = driver.find_elements_by_css_selector('.a-phones')

    result_phones = ''
    result_phones += phones[0].text

    # for j in range(0, len(phones)):
    #     phone = phones[j]
    #     result_phones += phone.text
    #     if j != len(phones) - 1:
    #         result_phones += ' , '

    # for phone in phones:
    #     result_phones += phone.text + ' \n'

    print(result_phones)

    sheet['F'+str(index)] = result_phones

    workbook.save('resulttableStage1.xlsx')




workbook.save('resulttableStage1.xlsx')
