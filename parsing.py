from session import Session
from options import args

import pandas as pd
import numpy as np
import re   
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class parser:

    def __init__(self,args,session):
        self.driver = session.driver
        self.args = args
        self.theme = args.theme
        self.start_page = args.start_page
        self.end_page = args.end_page
        self.first_button = args.first_button
        self.last_button = args.last_button
        self.prev_button = args.prev_button
        self.next_button = args.next_button


    def crawl_one_theme(self):
        if self.theme == "가정통신문":
            return self.crawl_letter_notice()
        elif self.theme == "공지사항":
            return self.crawl_letter_notice()
        elif self.theme == "학교급식":
            return self.crawl_bob()

    ######## 공지사항, 가정통신문 ########

    def crawl_letter_notice(self):
        iteration, final_page = self.interation()
        data = []
        for all in range(iteration): 
            for index in range(self.start_page,self.next_button):
                
                self.page_controller(index)
                where_end = int(self.driver.find_element(By.XPATH, f'//*[@id="board_area"]/div[5]/a[{index}]').text)
                print('현재 페이지: ', where_end,'총 페이지: ', final_page)
                list_length = len(self.driver.find_elements(By.CLASS_NAME, 'samu'))
                for index in range(list_length,list_length+1):
                    data.append(self.crawl_one_letter_notice(index))
                if final_page == where_end:
                    break            
                
            try:
                self.page_controller(self.next_button)
            except:
                break
        return data    

    def crawl_one_letter_notice(self, index):
        self.driver.find_element(By.XPATH, f'//*[@id="board_area"]/table/tbody/tr[{index}]/td[2]/a').click()
        date, name, title, content = self.get_info()
        self.get_file()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CLASS_NAME,'button_right').click()
        return name, date, title, content

    def get_info(self): 
        date = self.driver.find_element(By.XPATH, '//*[@id="board_area"]/table/tbody/tr[1]/td[2]/div').text #날짜
        name = self.driver.find_element(By.XPATH, '//*[@id="board_area"]/table/tbody/tr[1]/td[1]/div').text #이름
        title = self.driver.find_element(By.XPATH, '//*[@id="board_area"]/table/tbody/tr[2]/td[1]/div').text #제목
        content = self.driver.find_element(By.CLASS_NAME, 'content').text #본문 내용 추출
        return date, name, title, content
        
    def get_file(self): 
        try:
            size = len(self.driver.find_elements(By.CLASS_NAME, 'btn_down'))
            for i in range(size):
                self.driver.find_elements(By.CLASS_NAME, 'btn_down')[i].click()
                self.driver.implicitly_wait(2)
        except:
            pass

    def interation(self):
        tag = self.driver.find_element(By.CSS_SELECTOR, '#board_area > div.board_type01_pagenate > a:nth-child(14)')
        p = re.compile(r'\d+')
        final_page = int(p.search(tag.get_attribute('onclick')).group()) #끝 페이지 추출
        iteration = int(final_page / (self.next_button - self.start_page))
        return iteration, final_page

    def page_controller(self, index):
        if index >= 3 and index <= 12:
            self.driver.find_element(By.XPATH, f'//*[@id="board_area"]/div[5]/a[{index}]').click()
        elif index == self.next_button:
            self.driver.find_element(By.XPATH, f'//*[@id="board_area"]/div[5]/a[{self.next_button}]').click()
        elif index == self.prev_button:
            self.driver.find_element(By.XPATH, f'//*[@id="board_area"]/div[5]/a[{self.prev_button}]').click()
        elif index == self.first_button:
            self.driver.find_element(By.XPATH, f'//*[@id="board_area"]/div[5]/a[{self.first_button}]').click()
        elif index == self.last_button:
            self.driver.find_element(By.XPATH, f'//*[@id="board_area"]/div[5]/a[{self.last_button}]').click()


    ######## 학교 급식 ########

    def crawl_bob(self):
        years, months = self.get_bob_index()
        bob = []
        for year in years:
            for month in months:
                self.driver.implicitly_wait(1)
                self.get_bob_page(year,month)
                bob.append(self.get_bob_month())
            break
        return bob

    def get_bob_month(self):
        row = 2
        col = 7
        bob = []
        for i in range(2,row+1):
            for j in range(1,col+1):
                try:
                    Xpath = f'//*[@id="contents_230702"]/div[2]/div[2]/div/table/tbody/tr[{i}]/td[{j}]/ul/li/a'
                    self.driver.find_element(By.XPATH,  Xpath).click()
                    self.driver.implicitly_wait(1)
                    bob.append(self.get_bob())
                    self.driver.implicitly_wait(1)
                    self.driver.find_element(By.CLASS_NAME,  'popup_bottom').click()
                except:
                    pass
        return bob

    def get_bob_page(self, year,month):
        self.driver.find_element(By.XPATH, '//*[@id="srhMlsvYear"]').send_keys(year)
        self.driver.find_element(By.XPATH, '//*[@id="srhMlsvMonth"]').send_keys(str(month)+'월')
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, '//*[@id="searchForm"]/div/button').click()

    def get_bob(self):
        li = []
        elements = self.driver.find_elements(By.CLASS_NAME, 'ta_l')
        for element in elements:
            li.append(element.text)
        if li == []:
            return None
        return li[:-1]

    def get_bob_index(self):
        options = self.driver.find_elements(By.CSS_SELECTOR, 'option')
        length = len(options)
        tmp = []
        for index, option in enumerate(options):
            if option.text == '1월':
                year_index = index
            tmp.append(option.text)
        return tmp[:year_index], tmp[year_index:]
    

    
