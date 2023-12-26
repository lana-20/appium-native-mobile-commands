import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APPIUM = "http://localhost:4723"
CAPS = {
    "platformName": "Android",
    "appium:options": {
        "platformVersion": "14.0",  # optional
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        "appPackage": "io.appium.android.apis",
        "appActivity": ".app.AlertDialogSamples"
    }
}
driver = webdriver.Remote(APPIUM, CAPS)
wait = WebDriverWait(driver, 5)
try:
    alert_acceptance = wait.until(EC.presence_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, 'OK Cancel dialog with a message')))
    alert_acceptance.click()
    time.sleep(1)
    driver.execute_script("mobile:acceptAlert")

    alert_dismissal = wait.until(EC.presence_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, 'OK Cancel dialog with a long message')))
    alert_dismissal.click()
    time.sleep(1)
    driver.execute_script("mobile:dismissAlert")
finally:
    if driver is not None:
        driver.quit()
