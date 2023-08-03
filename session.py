import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
import random
import time


class Session:

    def __init__(self,args):
        self.args = args
        self.id = args.id
        self.pw = args.pw
        self.driver = None
        self.home_url = args.home_url
        self.theme = args.theme
        self.letter_link = args.letter_link
        self.notice_link = args.notice_link
        self.bob_link = args.bob_link


    def go_main(self):
        self.start_session()
        self.driver.get(self.home_url)
        self.login()
        self.get_menu()
    
    def get_menu(self):
        if self.theme == "가정통신문":
            self.driver.get(self.letter_link)
        elif self.theme == "공지사항":
            self.driver.get(self.notice_link)
        elif self.theme == "학교급식":
            self.driver.get(self.bob_link)
    
    def login(self):
        login_id = self.driver.find_element(By.ID,"userId")
        login_id.send_keys(self.id)
        login_pw = self.driver.find_element(By.ID,"password")
        login_pw.send_keys(self.pw)
        self.driver.find_element(By.CLASS_NAME,'member_join').click()
    
    def start_session(self):
        try:
            shutil.rmtree(r"c:\chrometemp")  #쿠키 / 캐시파일 삭제
        except FileNotFoundError:
            pass

        subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') #

        option = Options()
        # option.add_experimental_option("prefs", {"download.default_directory": r"C:\\github\\ajax_crawler\\data"})
        option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # user-agent 설정 #
        option.add_argument('User_Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36') 
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0] 
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option) 
        driver.execute_script('return navigator.userAgent')
        self.driver = driver

    