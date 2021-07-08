#!/bin/env python3

import time
import re
import sys
import warnings
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# use chrome, if set to false firefox will be used
useChrome = True

# moodle link
loginPage = "http://url"

# username and password
loginData = ["username", "password"]

# show completed topics too
showCompleted = True

# mark all topics complete
markAllComplete = True


def driverWait(driver, timeout, element, elementValue, login=0):
    """
    Waits {timeout} seconds for elements to load, before timing out, otherwise quit
    """
    try:
        WebDriverWait(driver, timeout).until(
            expected_conditions.presence_of_all_elements_located((element, elementValue)))
    except:
        if login:
            print("Login Failed.")
            print("Wrong username or password")
        else:
            print("Connection timed out.")
        driver.quit()
        exit(0)


if __name__ == "__main__":
    # initializing driver
    if useChrome:
        options = OptionsChrome()
        options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
    else:
        options = OptionsFirefox()
        options.add_argument('--headless')
        driver = webdriver.Firefox(executable_path="./geckodriver", options=options)

    try:
        driver.get(loginPage)
        print("Logging in...", file=sys.stderr)
    except TimeoutException as e:
        print("Login failed.", file=sys.stderr)
    except:
        print("Time out.", file=sys.stderr)
        driver.quit()
        exit(0)

    # loggging in
    driver.find_element_by_id("username").send_keys(loginData[0])
    driver.find_element_by_id("password").send_keys(loginData[1])
    driver.find_element_by_id("loginbtn").click()

    driverWait(driver, 100, By.CLASS_NAME, "progress-bar", 1)
    print("Login Successful.", file=sys.stderr)

    # list view
    print("# Moodle DS")

    # Change to list view
    temp = driver.find_element_by_id('displaydropdown')
    if(temp.text == 'Card' or temp.text == 'Summary'):
        temp.click()
        driver.find_elements_by_class_name('dropdown-item')[-2].click()
    driverWait(driver, 100, By.CLASS_NAME, "progress-bar", 1)

    # store subjects
    subjects = []
    for x in driver.find_elements_by_class_name("course-listitem"):
        links, name, progress, subId = '', '', '', ''
        try:
            links = str(x.find_elements_by_tag_name("a")[0].get_attribute("href"))
            temp = (x.find_elements_by_tag_name("a")[0].get_attribute("innerHTML"))
            name = temp[(temp.rfind("</span>") + len("</span>") + 1):].lstrip().replace("\n", "").rstrip()
            try:
                progress = str(x.find_element_by_tag_name("strong").get_attribute("innerHTML"))
            except:
                progress = "0"
            subId = str(x.get_attribute("data-course-id"))
            # print("Links:\t" + links)
            # print("- Name:\t" + name)
            # print("  - Progress: " + progress)
            # print("Subject ID: " + subId)
            # print()
        except:
            pass
        if name and [links, name, progress] not in subjects:
            subjects.append([links, name, progress, subId])

    # print(f"\nUpcoming Events...\n")
    # soup = BeautifulSoup(driver.page_source, "html.parser")
    # for each in soup.findAll('div', class_="event"):
    #     event = ''
    #     Id = re.search('course=(.*?)&', str(each.find('a')["href"])).group(1)
    #     for every in subjects:
    #         if every[3] == Id:
    #             event = every[1] + ': '
    #             break
    #     event += str(each.find('a').text)
    #     event += each.find('div').text
    #     print(f'{event}')

    counter = 0
    for each in subjects:
        driver.get(each[0])
        driverWait(driver, 100, By.CLASS_NAME, "btn-link")
        print("\n## " + subjects[counter][1].replace("|", " "))
        print("[Progress: " + subjects[counter][2] + "]" + "(" + subjects[counter][0] + ")")
        # section-0
        i = 0
        try:
            print("### Section-" + str(i))
            while i != -1:
                ID = "section-" + str(i)
                a = driver.find_element_by_id(ID)
                topics = a.find_elements_by_tag_name("li")
                for xx in topics:
                    try:
                        button = xx.find_element_by_class_name("btn-link")
                        title = str(button.find_element_by_class_name("icon").get_attribute("title"))
                        if title.startswith("Completed: "):
                            if showCompleted:
                                title = title[len("Completed: "):len(title) - len(" Select to mark as not complete.")]
                                print("- [x] [" + title + "]", end='')
                                url = str(xx.find_element_by_tag_name("a").get_attribute("href"))
                                print("(" + url + ")", end='')
                                file_type_url = str(xx.find_element_by_tag_name(
                                    "a").find_element_by_tag_name("img").get_attribute("src"))
                                # print(file_type_url)
                                if file_type_url.endswith("/icon"):
                                    # generate the link only for drive, youtube, teams
                                    driver.get(url)
                                    new_url = driver.current_url
                                    print(" [link](" + str(new_url) + ")")
                                    driver.execute_script("window.history.go(-1)")
                                elif file_type_url.endswith("/document-24"):
                                    print(" - word document")
                                elif file_type_url.endswith("/pdf-24"):
                                    print(" - pdf")
                                else:
                                    print()
                        else:
                            title = title[len("Not completed: "):len(title) - len(" Select to mark as not complete.")]
                            print("- [ ] [" + title + "]", end='')
                            url = str(xx.find_element_by_tag_name("a").get_attribute("href"))
                            print("(" + url + ")", end='')
                            file_type_url = str(xx.find_element_by_tag_name(
                                "a").find_element_by_tag_name("img").get_attribute("src"))
                            # print(file_type_url)
                            if file_type_url.endswith("/icon"):
                                # generate the link only for drive, youtube, teams
                                driver.get(url)
                                new_url = driver.current_url
                                print(" [link](" + str(new_url) + ")")
                                driver.execute_script("window.history.go(-1)")
                            elif file_type_url.endswith("/document-24"):
                                print(" - word document")
                            elif file_type_url.endswith("/pdf-24"):
                                print(" - pdf")
                            else:
                                print()

                            # mark it complete
                            if markAllComplete:
                                button.click()
                    except:
                        url = str(xx.find_element_by_tag_name("a").get_attribute("href"))
                        # check if the url is empty
                        if url and showCompleted:
                            print("- [Announcements]", end='')
                            print("(" + url + ")")
                        pass
                i += 1
        except:
            i = -1
            pass
        counter += 1

    driver.quit()
