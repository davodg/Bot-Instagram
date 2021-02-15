from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt, pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile=firefoxProfile, executable_path=r"geckodriver")

    def login(self):
        driver = self.driver
        driver.get("https://instagram.com")
        time.sleep(3)
        time.sleep(3)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comments()

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        print('Digitando comentário...')
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 3))

    def comments(self):
        a = 0
        while 1:
            sorteio_url = 'colocar a url do sorteio aqui'
            sorteios = [
                sorteio_url
            ]

            sorteio_vez = random.choice(sorteios)
            driver = self.driver
            time.sleep(5)
            driver.get(sorteio_vez)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                users = [
                    #Colocar o @ dos usuarios aqui                   
                 ]
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(1, 20))
                user_1 = random.choice(users)
                user_2 = random.choice(users)
                user_3 = random.choice(users)
                marcar = user_1
                marcar_2 = user_1 + " " + user_2
                marcar_3 = user_1 + " " + user_2 + " " + user_3

                if sorteio_vez == sorteio_url:
                    self.type_like_a_person(marcar, comment_input_box)
                    print('Comentei: ', marcar, ' no post: ', sorteio_vez, '')
                    # repetir o if para comentar em mais de um sorteio

                    time.sleep(random.randint(1, 15))
                    driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                    a = a + 1
                    print('Vezes comentadas:')
                    print(a)
                    for i in range(1, 3): driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(random.randint(60, 90))
            except Exception as e:
                print(e)
                time.sleep(5)



davidBot = InstagramBot("usuario", "senha")
davidBot.login()
