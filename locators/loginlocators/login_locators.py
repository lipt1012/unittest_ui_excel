from selenium.webdriver.common.by import By


class LoginLocator:
   username_loc=(By.CSS_SELECTOR,'input[type=text]')
   password_loc=(By.CSS_SELECTOR,'input[type=password]')
   button_loc=(By.CSS_SELECTOR,'button[type=button]')
