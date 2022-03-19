from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import argv
import multiprocessing
import random
from selenium.webdriver.support.ui import WebDriverWait
import time
from sys import exit
from selenium.webdriver.common.by import By
import os.path
from selenium.webdriver.support import expected_conditions as EC

'''
Programmed by Z3NTL3 ( Efdal )
Very useful anonymous uploader supports unlimited file upload at once!
'''
class Browser():
    def __init__(self): 
        self.obj = webdriver.Firefox()
    def Driver(self):
        return self.obj

# Z3NTL3
def Run(*, file_list):
    driver.get("https://anonfiles.com/")
    WebDriverWait(driver,10).until(
            lambda x: x.find_element(By.TAG_NAME,"input"))
    
    upload = driver.find_element(By.TAG_NAME,'input')
    upload.send_keys(f'{os.path.abspath(f"{file_list}")}')
    
    
    urlresponse = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control upload-file-input']")))
    file_at = urlresponse.get_attribute('value')
    print()
    print(f"\033[38;5;206mYour F\033[38;5;207mile i\033[38;5;219ms \033[38;5;207mat: \033[38;5;219m{file_at} \n\033[38;5;207mChec\033[38;5;206mk \033[38;5;219m'uploads.txt'\033[38;5;206m\033[0m")
    print()
    with open('uploads.txt','a')as file:
        file.write(f'Upload: "{file_list}" at "{file_at}"\n')
    driver.quit()

def List():
    with open('list.txt','r')as f:
        files = f.read().strip(' ').split('\n')
    return files

def list_amount():
    r = List()
    return len(r)

filelist = List()
amount = list_amount()

if amount < 1:
    print(LOGO)
    exit('\033[31mMinimum 1 filename in list.txt\033[0m')
LOGO = """
 {}╔═╗╔═╗╔╗╔╔╦╗╦  ╔═╗  
 {}╔═╝║╣ ║║║ ║ ║  ║╣   
 {}╚═╝╚═╝╝╚╝ ╩ ╩═╝╚═╝  
    {}  AnonUp
   {}File Uploader
    {}Anonymously

 {}by Z3NTL3 (Efdal).{}
 Contact: SavageDevs.net

{}CTRL {}+ {}C\033[0m to {}stop\033[0m
""".format(
    '\033[38;5;205m',
'\033[38;5;206m',
'\033[38;5;207m',
'\033[38;5;219m',
'\033[38;5;207m',
'\033[38;5;219m',
'\033[38;5;207m',
'\033[\033[38;5;219m',
'\033[0m',
'\033[38;5;207m',
'\033[38;5;219m',
'\033[38;5;207m',
'\033[\033[38;5;219m'
)


if __name__ == '__main__':
    print(LOGO)      
    for files in filelist:
        if os.path.exists(f'{os.path.abspath(f"{files}")}'):
            print(f"\033[32mValid file found: \033[0m\'{files}\'\033[32m starting auto-upload\033[0m")
            print()
            driver = Browser().Driver()
            th = multiprocessing.Process(target=Run(file_list=f'{files}'))
            th.start()
            th.join()
        else:
           print(f"\033[31mThis file does not exist in the current directory: \'\033[0m{files}\033[31m\'\033[0m")
        
 