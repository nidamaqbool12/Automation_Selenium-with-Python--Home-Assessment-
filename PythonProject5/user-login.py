import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://services.itspk.com/")
driver.maximize_window()

time.sleep(1)

username=driver.find_element(By.ID,"email")
username.send_keys("saya@gmail.com")
print("--------------------PASSED#01-----------------------")
print("Successfully type the  username")
print("                                            ")
time.sleep(3)

password = driver.find_element(By.ID,"password")
password.send_keys("Saya@123")
print("--------------------PASSED#02-----------------------")
print("Successfully type the  password")
print("                                            ")
time.sleep(3)

signIn = driver.find_element(By.XPATH,"//button[@class='btn btn-secondary']")
signIn.click()
print("--------------------PASSED#03--------------------------")
print("Successfully sign in")
time.sleep(3)


