from selenium import webdriver
import unittest
from public.common.base_page import BasePage
import time
from locators.loginlocators.login_locators import LoginLocator as loc

class Login(BasePage): 
   def __init__(self, driver):
      
       self.driver = driver
   def input_user(self, username):
       self.clear(*loc.username_loc)
       self.type(username,*loc.username_loc)

   def input_psw(self, password):
       self.clear(*loc.password_loc)
       self.type(password,*loc.password_loc) 

   def click_button(self):
       self.click(*loc.button_loc)
       
   def login(self, username, password):
       self.max_window()     
       self.input_user(username)
       self.input_psw(password)
       self.click_button()