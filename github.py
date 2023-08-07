from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Cài đặt webdriver cho Chrome
webdriver.Chrome(ChromeDriverManager().install())
