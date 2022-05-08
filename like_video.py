from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

path = "/Users/payalnathni/Downloads/chromedriver"

driver = webdriver.Chrome(path)
driver.get("https://www.youtube.com/channel/UCIPPMRA040LQr5QPyJEbmXA/videos")

time.sleep(3)
nav = driver.find_element_by_id("buttons")
sign_in = nav.find_elements_by_tag_name("ytd-button-renderer")[0]
sign_in = sign_in.find_element_by_tag_name("a").click()

time.sleep(5)

email_input = driver.find_element_by_id("identifierId")
email_input.send_keys("payalnathani@gmail.com")
email_input.send_keys(Keys.RETURN)

time.sleep(3)

password = driver.find_element_by_name("password")
password.send_keys("pass")
password.send_keys(Keys.RETURN)


time.sleep(5)

SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        print("break")
        break
    last_height = new_height

time.sleep(2)
count = 0

links_of_all_videos = []
links = driver.find_elements_by_xpath('//*[@id="video-title"]')
for link in links:
    links_of_all_videos.append(link.get_attribute("href"))
print(f"total {len(links_of_all_videos)} videos")

for link in links_of_all_videos[144:]:
    driver.get(link)

    time.sleep(3)

    check_like = driver.find_element_by_xpath(
        "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button"
    )

    is_liked = check_like.get_attribute("aria-pressed")

    like_action = ActionChains(driver)

    like_button = driver.find_element_by_xpath(
        '//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a'
    )

    if is_liked == "true":
        time.sleep(2)

        like_action.move_to_element(like_button).click()
        time.sleep(2)
        like_action.move_to_element(like_button).click()
        like_action.perform()
        time.sleep(1)

    else:
        time.sleep(2)
        like_action.move_to_element(like_button).click().perform()
        time.sleep(1)

    count += 1
    print(f"liked {count} video")

print(f"Likeeeddddd alll {count} vidddddeeoooossssssss !!!!!!!!!!!!!!!!!!!!")
driver.quit()
