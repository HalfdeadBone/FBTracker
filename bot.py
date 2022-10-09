from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
from files import *
import time
from datetime import date
from bs4 import BeautifulSoup
import requests
import sys


jsonCfgPath = 'config/config.json'

class Error(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

class Mobile_fbBot():
    def __init__(self):
        self.f = open(jsonCfgPath)
        self.cfg = json.load(self.f)
        self.URL_Mobile_FList= self.cfg['links']['URL_Mobile_FList']
        self.URL_Mobile_Face = self.cfg['links']['URL_Mobile_Face']
        self.URL_Mobile_Active_FList = self.cfg['links']['URL_Mobile_Active_FList']
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.activeUsers = dict()
        self.tempDIR = self.cfg['dirs']['temp']

    def LoadCookie(self):
        cookiePath = self.cfg['dirs']['cookie']
        with open(cookiePath) as cookieFile:
            self.cookies = json.load(cookieFile)
        self.driver.get(self.URL_Mobile_Face)
        time.sleep(4)
        for cookie in self.cookies:
            self.driver.add_cookie(cookie)

    def StartBot(self):
        self.driver.get(self.URL_Mobile_Active_FList)

    def GetAllFriends(self):
        self.driver.get(self.URL_Mobile_FList)
        SCROLL_PAUSE_TIME = 2

        # Prowided by @Cuong Tran, based on feed from stack Overflow user "OWADVL"
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            snew_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        print("end")

    
    def GetUsersId(self, nameList=None ):
        self.driver.get(self.URL_Mobile_Active_FList)
        time.sleep(0.5)
        html = self.driver.page_source
        soup = BeautifulSoup(html)
        buddyList = soup.findAll("div",{"class": "buddylistItem"})
        for item in buddyList:
            print(item.get('id'))
            print(item.find("strong").text)
        if nameList == None:
            print("ok")
        else:
            print("match")

    def LoadSite(self):
        self.driver.get(self.URL_Mobile_Active_FList)

    def NewDataHolding(self):
        t = time.localtime()
        now = time.strftime("%H:%M:%S", t) 
        dataDir = self.cfg['dirs']['collDir']

        html = self.driver.page_source
        soup = BeautifulSoup(html, features="lxml")
        buddyList = soup.findAll("div",{"class": "buddylistItem"})
        keyUsers = list()

        for item in buddyList:
            name = str(item.find("strong").text)
            keyUsers.append(name)

            if name not in self.activeUsers:
                self.activeUsers[name] = now
                #print(self.activeUsers[name], " : ", name)

        diffUser = set(self.activeUsers.keys()).difference(set(keyUsers))

        for person in diffUser:
            userDict = {'name':person, 'start':self.activeUsers.pop(person),'end':now}
            NewAppendCSV(dataDir,str( date.today()),userDict)
    
    def ClosingSequence(self):
        print(InfoMsg("Saving remaining Data. Please wait"))
        t = time.localtime()
        now = time.strftime("%H:%M:%S", t)
        dataDir = self.cfg['dirs']['collDir']
        try:
            for item in self.activeUsers:
                userDict = {'name':item, 'start':self.activeUsers[item],'end':now}
                NewAppendCSV(dataDir,str( date.today()),userDict)
            print(SuccessMsg("Data Has been succesfully Saved"))
            DeleteFile(self.tempDIR,"temp.csv")
        except Exception as e:
            print(ErrorMsg("Unexpected error during Closing Sequence has occured, Some data has been lost"))

    def TempFiles(self):
        t = time.localtime()
        now = time.strftime("%H:%M:%S", t)
        usersList =[] 
        for item in self.activeUsers:
            userDir = {"name":item,'start':self.activeUsers[item],'end':now }
            usersList.append(userDir)
        CreateDIR(self.tempDIR)
        CreateCSV(self.tempDIR, "temp",usersList)

    def RecoverData(self):
        dataDir = self.cfg['dirs']['collDir']
        if not len(os.listdir(self.tempDIR)) == 0:
            users = ReadCSV(self.tempDIR +"temp.csv")
            for item in users:
                NewAppendCSV(dataDir,str(date.today()),item)

