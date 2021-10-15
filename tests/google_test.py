from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

def test_site():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(
            executable_path="driver/chromedriver",
            options=chrome_options
        )
        driver.get("https://www.google.com")
        title = driver.title
        assert title == "Google"
    except WebDriverException as e:
        print(e)

test_site()
