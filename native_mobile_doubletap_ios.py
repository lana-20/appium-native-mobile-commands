import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APPIUM = "http://localhost:4723"
CAPS = {
    "platformName": "iOS",
    "appium:options": {
        "platformVersion": "17.2",
        "deviceName": "iPhone 15 Pro Max",
        "automationName": "XCUITest",
        "app": "com.apple.Maps",
        "autoAcceptsAlerts": True
    }
}
driver = webdriver.Remote(APPIUM, CAPS)
try:
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "Not Now"))).click()
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "Allow Once"))).click()

    driver.execute_script("mobile: doubleTap", {"x": 100, "y": 100})
    time.sleep(1)   # for demo only
    driver.execute_script("mobile: doubleTap", {"x": 100, "y": 100})
    time.sleep(1)
    driver.execute_script("mobile: doubleTap", {"x": 100, "y": 100})
    time.sleep(3)
finally:
    if driver is not None:
        driver.quit()