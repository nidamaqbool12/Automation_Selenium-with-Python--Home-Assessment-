import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Firefox()
driver.get("https://services.itspk.com/admin-login")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.ID, "email").send_keys("admin@gmail.com")

driver.find_element(By.ID, "password").send_keys("12345678")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-secondary']").click()
time.sleep(3)

                                                    #Edit Role
driver.get("https://services.itspk.com/listusers")

action=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/button")
action.click()
time.sleep(2)
edit_role = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/ul/li[2]/a")
edit_role.click()

remove_icon=driver.find_element(By.XPATH,"(//span[@aria-hidden='true'][normalize-space()='×'])[2]")
remove_icon.click()
time.sleep(2)

box=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/h2")
box.click()
time.sleep(5)

update_btn=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/form/div[2]/button")
update_btn.click()
time.sleep(3)

                                                       #Edit User
action=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/button")
action.click()
time.sleep(2)
Edit_User= driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/ul/li[3]/a")
Edit_User.click()
time.sleep(3)

f_name = driver.find_element(By.ID,"first_name")
f_name.clear()
f_name.send_keys("NIDA")
time.sleep(2)

l_name= driver.find_element(By.ID,"last_name")
l_name.clear()
l_name.send_keys("MAQBOOL")
time.sleep(2)

update_btn_edit =driver.find_element(By.XPATH,"(//button[normalize-space()='Update'])[1]")
update_btn_edit.click()

time.sleep(4)


                                                       #Delete User
action=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/button")
action.click()
time.sleep(2)
Delete_User = driver.find_element(By.XPATH,"(//button[@type='button'][normalize-space()='Delete'])[1]")
Delete_User.click()
time.sleep(3)

Delete_1= driver.find_element(By.XPATH,"(//button[@type='submit'][normalize-space()='Delete'])[1]")
Delete_1.click()
time.sleep(4)