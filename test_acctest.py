# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAcctest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_acctest(self):
    self.driver.get("http://qa-test.klika-tech.com/")
    self.driver.set_window_size(1072, 824)
    self.driver.find_element(By.CSS_SELECTOR, ".digits > li:nth-child(7)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".digits > li:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".digits > li:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".operations > li:nth-child(6)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(8)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".double:nth-child(7)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".operations > li:nth-child(2)").click()
    assert self.driver.find_element(By.ID, "display").text == " "
  
