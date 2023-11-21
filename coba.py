from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "dashboard-staging.rekalaba.com"

# Test Case 1: Add Customer
def test_add_customer():
    driver.get(url)
    driver.find_element_by_name("Email").send_keys("pinnuspryandi@gmail.com")
    driver.find_element_by_name("Password").send_keys("admin123456")
    driver.find_element_by_link_text("Login").click()
    driver.find_element_by_link_text("Customer").click()

    driver.find_element_by_link_text("Add Customer").click()

    driver.find_element_by_name("Customer Nama").send_keys("inggar")
    driver.find_element_by_name("Customer Email").send_keys("inggarananto.cv@gmail.com")
    driver.find_element_by_name("Customer Phone Number").send_keys("082122835608")
    driver.find_element_by_name("Customer Address").send_keys("jakarta")
    driver.find_element_by_name("Company Name").send_keys("depok")

    driver.find_element_by_name("Save").click()

    time.sleep(2)

    assert "Customer added successfully" in driver.page_source

# Test Case 2: Update Customer
def test_update_customer():
    driver.get(url)

    driver.find_element_by_link_text("Customer").click()

    driver.find_element_by_css_selector(".customer-list-item:first-child").click()

    driver.find_element_by_link_text("Update Customer").click()
    driver.find_element_by_name("Customer Nama").clear()
    driver.find_element_by_name("Customer Nama").send_keys("ANANTO")

    driver.find_element_by_name("Save").click()

    time.sleep(2)

    assert "Customer updated successfully" in driver.page_source

driver.quit()
