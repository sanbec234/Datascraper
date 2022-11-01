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
    page.goto("https://ecampus.psgtech.ac.in/studzone2/")
    page.fill('input#txtusercheck', rollno)
    page.fill('input#txtpwdcheck', password)
    page.click('input[name = abcd3]')
    page.goto("https://ecampus.psgtech.ac.in/studzone2/FrmEpsStudResult.aspx")

    name = page.inner_html('#Label5')
    soup = BeautifulSoup(name, 'html.parser')
    content0 = soup.get_text()
    print("student name: ",content0)

    rno = page.inner_html('#Label8')
    soup = BeautifulSoup(rno, 'html.parser')
    content = soup.get_text()
    print("student roll number: ",content)
    
    attendance1 = page.inner_html('#DgResult > tbody > tr:nth-child(2) > td:nth-child(4)')
    soup = BeautifulSoup(attendance1, 'html.parser')
    content1 = soup.get_text()
    th1 = float(content1)
    attended1 = page.inner_html('#DgResult > tbody > tr:nth-child(2) > td:nth-child(5)')
    soup = BeautifulSoup(attended1, 'html.parser')
    content1 = soup.get_text()
    content1 = content1[:-2]
    c1 = float(content1)
    cr1 = c1 * th1
   
    

    attendance2 = page.inner_html('#DgResult > tbody > tr:nth-child(3) > td:nth-child(4)')
    soup = BeautifulSoup(attendance2, 'html.parser')
    content2 = soup.get_text()
    th2 = float(content2)
    attended2 = page.inner_html('#DgResult > tbody > tr:nth-child(3) > td:nth-child(5)')
    soup = BeautifulSoup(attended2, 'html.parser')
    content2 = soup.get_text()
    content2 = content2[:-2]
    c2 = float(content2)
    cr2 = c2 * th2
    
   

    attendance3 = page.inner_html('#DgResult > tbody > tr:nth-child(4) > td:nth-child(4)')
    soup = BeautifulSoup(attendance3, 'html.parser')
    content3 = soup.get_text()
    th3 = float(content3)
    attended3 = page.inner_html('#DgResult > tbody > tr:nth-child(4) > td:nth-child(5)')
    soup = BeautifulSoup(attended3, 'html.parser')
    content3 = soup.get_text()
    content3 = content3[:-2]
    c3 = float(content3)
    cr3 = c3 * th3
    
   
    attendance4 = page.inner_html('#DgResult > tbody > tr:nth-child(5) > td:nth-child(4)')
    soup = BeautifulSoup(attendance4, 'html.parser')
    content4 = soup.get_text()
    th4 = float(content4)
    attended4 = page.inner_html('#DgResult > tbody > tr:nth-child(5) > td:nth-child(5)')
    soup = BeautifulSoup(attended4, 'html.parser')
    content4 = soup.get_text()
    content4 = content4[:-2]
    c4 = float(content4)
    cr4 = c4 * th4
    
   

    attendance5 = page.inner_html('#DgResult > tbody > tr:nth-child(6) > td:nth-child(4)')
    soup = BeautifulSoup(attendance5, 'html.parser')
    content5 = soup.get_text()
    th5 = float(content5)
    attended5 = page.inner_html('#DgResult > tbody > tr:nth-child(6) > td:nth-child(5)')
    soup = BeautifulSoup(attended5, 'html.parser')
    content5 = soup.get_text()
    content5 = content5[:-2]
    c5 = float(content5)
    cr5 = c5 * th5
    

    attendance6 = page.inner_html('#DgResult > tbody > tr:nth-child(7) > td:nth-child(4)')
    soup = BeautifulSoup(attendance6, 'html.parser')
    content6 = soup.get_text()
    th6 = float(content6)
    attended6 = page.inner_html('#DgResult > tbody > tr:nth-child(7) > td:nth-child(5)')
    soup = BeautifulSoup(attended6, 'html.parser')
    content6 = soup.get_text()
    content6 = content6[:-2]
    c6 = float(content6)
    cr6 = c6 * th6
    

    attendance7 = page.inner_html('#DgResult > tbody > tr:nth-child(8) > td:nth-child(4)')
    soup = BeautifulSoup(attendance7, 'html.parser')
    content7 = soup.get_text()
    th7 = float(content7)
    attended7 = page.inner_html('#DgResult > tbody > tr:nth-child(8) > td:nth-child(5)')
    soup = BeautifulSoup(attended7, 'html.parser')
    content7 = soup.get_text()
    content7 = content7[:-2]
    c7 = float(content7)
    cr7 = c7 * th7
   

    attendance8 = page.inner_html('#DgResult > tbody > tr:nth-child(9) > td:nth-child(4)')
    soup = BeautifulSoup(attendance8, 'html.parser')
    content8 = soup.get_text()
    th8 = float(content8)
    attended8 = page.inner_html('#DgResult > tbody > tr:nth-child(9) > td:nth-child(5)')
    soup = BeautifulSoup(attended8, 'html.parser')
    content8 = soup.get_text()
    content8 = content8[:-2]
    c8 = float(content8)
    cr8 = c8 * th8

    attendance9 = page.inner_html('#DgResult > tbody > tr:nth-child(2) > td:nth-child(1)')
    soup = BeautifulSoup(attendance9, 'html.parser')
    content9 = soup.get_text()
    th9 = int(content9)
   
    cgpa = (cr1+cr2+cr3+cr4+cr5+cr6+cr7+cr8)/(th1+th2+th3+th4+th5+th6+th7+th8)

    print(content0,"gpa for sem",th9,"is")

    print("%.1f" % cgpa)


   

    
    