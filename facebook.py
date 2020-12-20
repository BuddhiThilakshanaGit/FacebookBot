from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


class FacebookAdder:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.prefs = {"profile.managed_default_content_settings.images": 2,
                      "profile.managed_default_content_settings.notifications": 2,  "profile.managed_default_content_settings.popups": 2}

    def run_normal(self):
        self.chrome_options.add_experimental_option(
            "prefs", {self.prefs[1], self.prefs[2]})
        self.driver = webdriver.Chrome(
            r"C:\\webdrivers\\chromedriver.exe", chrome_options=self.chrome_options)

    def run_in_image_off_mode(self):
        self.chrome_options.add_experimental_option("prefs", self.prefs)
        self.driver = webdriver.Chrome(
            r"C:\\webdrivers\\chromedriver.exe", chrome_options=self.chrome_options)

    def login(self, gmail, password):
        self.driver.get("https://facebook.com")

        while True:
            try:
                self.driver.find_element_by_xpath("""//*[@id="email"]""")\
                    .send_keys(gmail)
                self.driver.find_element_by_xpath("""//*[@id="pass"]""")\
                    .send_keys(password)
                self.driver.find_element_by_xpath("""//*[@id = "u_0_b"]""")\
                    .click()
                break
            except:
                sleep(3)

    def click_friends(self):
        sleep(1)
        while True:
            try:
                self.driver.get("https://www.facebook.com/?sk=ff")
                break
            except:
                pass

    def clicking_add_friend(self):
        count = 0
        while True:
            print("Im at first")
            try:
                while True:
                    print("Im at while true")
                    list_of_buttons = self.driver.find_elements_by_class_name(
                        "selected")
                    for buttons in list_of_buttons:

                        try:
                            buttons.click()
                            count = 0
                            print(count)
                            random_time = random.randint(800, 1000)/1000
                            sleep(random_time)
                        except:
                            count += 1
                            print("Im at buttons except")

                sleep(random.randint(5000, 10000)/1000)
            except:
                print("Im at facebook.com/?sk=ff")
                count += 1
                print(count)
                if count > 10:
                    self.driver.get(
                        "https://www.facebook.com/?sk=ff")
                    count = 0
                    sleep(3)

    def add_friend(self):
        print("I'm in add_friend")
        while True:
            try:
                while True:
                    list_of_buttons = self.driver.find_elements_xpa(
                        "FriendRequestAdd")
                    for buttons in list_of_buttons:
                        try:
                            buttons.click()
                            random_time = random.randint(800, 1000)/1000
                            sleep(random_time)
                        except:
                            pass

                sleep(random.randint(5000, 10000)/1000)

            except:
                sleep(1)
                self.driver.find_element_by_class_name("layerConfirm").click()

            else:
                sleep(3)
                webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

            finally:
                pass

    def delete_requests(self):
        sleep(3)
        count=0
        self.driver.get(
            "https://www.facebook.com/friends/requests/?fcref=jwl&outgoing=1#")
        while True:
            print("Im at first")
            try:
                while True:
                    print("Im at while true")
                    list_of_buttons = self.driver.find_elements_by_class_name(
                        "outgoingButton")
                    for buttons in list_of_buttons:

                        try:
                            buttons.click()
                            count = 0
                            print(count)
                            random_time = random.randint(800, 1000)/1000
                            sleep(random_time)
                        except:
                            self.driver.find_element_by_xpath(
                                """//*[@id="outgoing_reqs_pager_5ef4a85b1ad525d68180008"]/div/a""").click()
                            print("Im at buttons except")
                            sleep(3)

            except:
                self.driver.find_element_by_xpath(
                    """//*[@id="outgoing_reqs_pager_5ef4a85b1ad525d68180008"]/div/a""").click()
                sleep(3)
            else:
                print("Im at facebook.com/?sk=ff")
                count += 1
                print(count)
                if count > 10:
                    self.driver.get(
                        "https://www.facebook.com/?sk=ff")
                    count = 0
                    sleep(3)

if __name__ == "__main__":
    testing = FacebookAdder()
    testing.run_in_image_off_mode()
    testing.login(gmail='gmail', password='password')
    testing.add_friend()
    # testing.add_friend()
