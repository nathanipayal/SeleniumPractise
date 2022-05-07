from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains



def flip_coin(driver, java_count, c_count):

    search_field = driver.find_element_by_name("q")

    search_field.send_keys("flip coin")
    search_field.send_keys(Keys.RETURN)

    time.sleep(5)

    hAndt = driver.find_elements_by_class_name("PmF7Ce")
    heads = hAndt[0]
    tails = hAndt[1]

    flip_again = driver.find_elements_by_class_name("kIGsIe")[2]

    time.sleep(5)

    for i in range(3):
        flip_again.click()
        time.sleep(5)
        java = heads.get_attribute("aria-hidden")
        c = tails.get_attribute("aria-hidden")

        if java == "false":
            java_count += 1
        else:
            c_count += 1
        print(java_count, c_count)

    time.sleep(3)

    if java_count == c_count:
        flip_again.click()
        time.sleep(5)
        java = heads.get_attribute("aria-hidden")
        c = tails.get_attribute("aria-hidden")

        if java == "true":
            java_count += 1
        else:
            c_count += 1

    print("FINAL POINTS:-----", f"JAVA - {java_count}", f"C++ - {c_count}")


def roll_dice(driver, java_count, c_count):

    search_field = driver.find_element_by_name("q")
    search_field.clear()
    search_field.send_keys("roll a die")
    search_field.send_keys(Keys.RETURN)

    time.sleep(5)

    all_dices = driver.find_elements_by_class_name("YRQ7vd")

    for i in range(10):
        all_dices[0].click()

        all_dices[1].click()

        all_dices[2].click()

        all_dices[3].click()

        all_dices[4].click()

        all_dices[5].click()

    time.sleep(7)
    print("Done rolling die")


if __name__ == "__main__":

    path = "/Users/payalnathani/Downloads/chromedriver"

    driver = webdriver.Chrome(path)
    driver.get("https://google.com")

    java_count = 0
    c_count = 0

    flip_coin(driver, java_count, c_count)
    roll_dice(driver, java_count, c_count)

    if java_count > c_count:

        print("WE ARE GOINGGGG TO DOOOO JAAAAAAAAAVVVAAAAAAAAAAA")

    else:

        print("WE ARE GOINGGGGGGG TOOOO DOOOO C++++++++++++++++++")

    driver.quit()
