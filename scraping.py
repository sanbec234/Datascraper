#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:21:33 2022

@author: sanbec234
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:21:33 2022

@author: SNEHAN234
"""
from unicodedata import name
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from re import A

rollno = input("enter rollno: ")
password = input("enter password: ")

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False, slow_mo= 500)
    page = browser.new_page()
    page.goto("")
    page.fill('input#txtusercheck', rollno)
    page.fill('input#txtpwdcheck', password)
    page.click('input[name = abcd3]')
    page.goto("")

   


   

    
    

   

    
    
