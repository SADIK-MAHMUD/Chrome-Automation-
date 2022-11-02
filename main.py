import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By
from undetected_chromedriver.options import ChromeOptions as Options


def main():
    options = Options()
    options.add_argument("--user-data-dir=C:\\Users\\SADIK\\Desktop\\Data")
    driver = uc.Chrome(options=options)
    driver.get('https://accounts.google.com/')
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys("Mail")
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    sleep(6)
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("Pass")
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    sleep(10)


if __name__ == "__main__":
    main()
