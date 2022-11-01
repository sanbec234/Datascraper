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

rollno = input("enter rollno: ")
password = input("enter password: ")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://ecampus.psgtech.ac.in/studzone2/")
    page.fill('input#txtusercheck', rollno)
    page.fill('input#txtpwdcheck', password)
    page.click('input[name = abcd3]')
    page.goto("https://ecampus.psgtech.ac.in/studzone2/AttWfPercView.aspx")

    name = page.inner_html('#TbStudInfo > tbody > tr:nth-child(1) > td.GenName')
    soup = BeautifulSoup(name, 'html.parser')
    content0 = soup.get_text()
    print("student name: ",content0)

    rno = page.inner_html('#TbStudInfo > tbody > tr:nth-child(2) > td:nth-child(3)')
    soup = BeautifulSoup(rno, 'html.parser')
    content = soup.get_text()
    print("student roll number: ",content)
    
    attendance1 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(2) > td:nth-child(2)')
    soup = BeautifulSoup(attendance1, 'html.parser')
    content1 = soup.get_text()
    th1 = int(content1)
    attended1 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(2) > td:nth-child(5)')
    soup = BeautifulSoup(attended1, 'html.parser')
    content1 = soup.get_text()
    at1 = int(content1)
    p1 = (at1/th1)*100
    print("total hours in 19k312: ",p1)
    print("the classes that can be bunked are: ",int((at1/0.75)-th1))

    attendance2 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(3) > td:nth-child(2)')
    soup = BeautifulSoup(attendance1, 'html.parser')
    content2 = soup.get_text()
    th2 = int(content2)
    attended2 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(3) > td:nth-child(5)')
    soup = BeautifulSoup(attended1, 'html.parser')
    content2 = soup.get_text()
    at2 = int(content2)
    p2 = (at2/th2)*100
    print("total hours in 19O306: ",p2)
    print("the classes that can be bunked are: ",int((at2/0.75)-th2))
   

    attendance3 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(4) > td:nth-child(2)')
    soup = BeautifulSoup(attendance3, 'html.parser')
    content3 = soup.get_text()
    th3 = int(content3)
    attended3 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(4) > td:nth-child(5)')
    soup = BeautifulSoup(attended3, 'html.parser')
    content3 = soup.get_text()
    at3 = int(content3)
    p3 = (at3/th3)*100
    print("total hours in 19Z301: ",p3)
    print("the classes that can be bunked are: ",int((at3/0.75)-th3))
   
    attendance4 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(4) > td:nth-child(2)')
    soup = BeautifulSoup(attendance4, 'html.parser')
    content4 = soup.get_text()
    th4 = int(content4)
    attended4 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(4) > td:nth-child(5)')
    soup = BeautifulSoup(attended4, 'html.parser')
    content4 = soup.get_text()
    at4 = int(content4)
    p4 = (at4/th4)*100
    print("total hours in 19Z302: ",p4)
    print("the classes that can be bunked are: ",(at4/0.75)-th4)
   

    attendance5 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(6) > td:nth-child(2)')
    soup = BeautifulSoup(attendance5, 'html.parser')
    content5 = soup.get_text()
    th5 = int(content5)
    attended5 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(6) > td:nth-child(5)')
    soup = BeautifulSoup(attended5, 'html.parser')
    content5 = soup.get_text()
    at5 = int(content5)
    p5 = (at5/th5)*100
    print("total hours in 19Z303: ",p5)
    print("the classes that can be bunked are: ",int((at5/0.75)-th5))

    attendance6 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(6) > td:nth-child(2)')
    soup = BeautifulSoup(attendance6, 'html.parser')
    content6 = soup.get_text()
    th6 = int(content6)
    attended6 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(6) > td:nth-child(5)')
    soup = BeautifulSoup(attended6, 'html.parser')
    content6 = soup.get_text()
    at6 = int(content6)
    p6 = (at6/th6)*100
    print("total hours in 19Z304: ",p6)
    print("the classes that can be bunked are: ",int((at6/0.75)-th6))

    attendance7 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(6) > td:nth-child(2)')
    soup = BeautifulSoup(attendance6, 'html.parser')
    content7 = soup.get_text()
    th7 = int(content7)
    attended7 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(6) > td:nth-child(5)')
    soup = BeautifulSoup(attended7, 'html.parser')
    content7 = soup.get_text()
    at7 = int(content7)
    p7 = (at7/th7)*100
    print("total hours in 19Z305: ",p7)
    print("the classes that can be bunked are: ",int((at7/0.75)-th7))

    attendance8 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(6) > td:nth-child(2)')
    soup = BeautifulSoup(attendance8, 'html.parser')
    content8 = soup.get_text()
    th8 = int(content8)
    attended8 = page.inner_html('#PDGcourpercView > tbody > tr:nth-child(6) > td:nth-child(5)')
    soup = BeautifulSoup(attended8, 'html.parser')
    content8 = soup.get_text()
    at8 = int(content8)
    p8 = (at8/th8)*100
    print("total hours in 19Z306: ",p8)
    print("the classes that can be bunked are: ",int((at8/0.75)-th8))


   

    
    