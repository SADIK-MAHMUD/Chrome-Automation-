import undetected_chromedriver as uc
from undetected_chromedriver.options import ChromeOptions as Options
from time import sleep
from selenium.webdriver.common.by import By


# from selenium.webdriver.common.keys import Keys

n = 1
def main():
    while n > 0:
        options = Options()
        options.add_argument("--user-data-dir=C:\\Users\\SADIK\\Desktop\\Data")
        driver = uc.Chrome(options=options)
        driver.get("https://youtube.com/upload")
        sleep(10)
        upload_btn = driver.find_element(By.XPATH, '//input[@type="file"]')
        upload_btn.send_keys("C:\\Users\\SADIK\\Desktop\\Yt Project\\No Bitches.mp4")
        sleep(5)
        "Click Upload!"
        title_box = driver.find_element(By.XPATH, '(//div[@id="textbox"])[1]')
        title_box.send_keys("#Shots #Meme #FYP #ForYouPage")
        sleep(2)
        desc_box = driver.find_element(By.XPATH, '(//div[@id="textbox"])[2]')
        desc_box.send_keys("No Bitches?! \n #SHORTS#Meme#Fun#Comedy#Funny#Sed life#Fyp#foryourpage")
        sleep(3)
        nfk = driver.find_element(By.XPATH, '(//div[@id="offRadio"])[2]')
        nfk.click()
        nxt1 = driver.find_element(By.XPATH, '//div[@class="right-button-area style-scope ytcp-uploads-dialog"]')
        nxt1.click()
        sleep(1)
        nxt2 = driver.find_element(By.XPATH, '//div[@class="right-button-area style-scope ytcp-uploads-dialog"]')
        nxt2.click()
        sleep(1)
        nxt3 = driver.find_element(By.XPATH, '//div[@class="right-button-area style-scope ytcp-uploads-dialog"]')
        nxt3.click()
        sleep(1)
        pub_btn = driver.find_element(By.XPATH, '(//div[@id="offRadio"])[4]')
        pub_btn.click()
        sleep(1)
        save_btn = driver.find_element(By.XPATH, '//ytcp-button[@id="done-button"]')
        save_btn.click()
        input()

        if a link is generated:
            #Copy paste code used before
        else:
            sleep(86400)



if __name__ == "__main__":
    main()
