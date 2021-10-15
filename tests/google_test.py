from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

import platform

def test_site():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = None
        if platform.system() == "darwin":
            driver = webdriver.Chrome(
                executable_path="driver/macos/chromedriver",
                options=chrome_options
            )
        else:
            driver = webdriver.Chrome(
                executable_path="driver/linux/chromedriver",
                options=chrome_options
            )
        driver.get("https://www.google.com")
        title = driver.title
        assert title == "Google"
        print("Test end ....")
    except WebDriverException as e:
        print(e)

test_site()
