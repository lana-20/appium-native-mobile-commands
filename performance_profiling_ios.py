from appium import webdriver
from appium.webdriver.common.mobileby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import base64

trace_zip = "trace.zip"
msg_input = (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='messageInput']")
saved_msg = (AppiumBy.ACCESSIBILITY_ID, "savedMessage")
save_msg_btn = (AppiumBy.ACCESSIBILITY_ID, "messageSaveBtn")
echo_box = (AppiumBy.ACCESSIBILITY_ID, "Echo Box")
TEST_MESSAGE = "Hello World"

APP = "https://github.com/appium-pro/TheApp/releases/download/v1.12.0/TheApp.app.zip"
APPIUM = 'http://localhost:4723'
CAPS = {
        'platformName': 'iOS',
        'platformVersion': '17.2',
        'deviceName': 'iPhone 15 Pro Max',
        'automationName': 'XCUITest',
        'app': APP,
    }

driver = webdriver.Remote(APPIUM, CAPS)

try:
    args = {
        'timeout': 60000,
        'pid': 'current',
        'profileName': 'Time Profiler'
    }
    driver.execute_script("mobile: startPerfRecord", args)

    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located(echo_box)).click()
    wait.until(EC.presence_of_element_located(msg_input)).send_keys(TEST_MESSAGE)
    wait.until(EC.presence_of_element_located(save_msg_btn)).click()
    saved_text = wait.until(EC.presence_of_element_located(saved_msg)).text
    assert saved_text == TEST_MESSAGE
    driver.back()

    args = {
        'profileName': 'Time Profiler'
    }
    b64_zip = driver.execute_script("mobile: stopPerfRecord", args)
    bytes_zip = base64.b64decode(b64_zip)
    with open(trace_zip, 'wb') as stream:
        stream.write(bytes_zip)
except TimeoutException:
    # Handle timeout exception as needed
    pass
finally:
    driver.quit()