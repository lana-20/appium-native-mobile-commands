import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APPIUM = "http://localhost:4723"
CAPS = {
    "platformName": "iOS",
    "appium:options": {
        "platformVersion": "17.2",
        "deviceName": "iPhone 15 Pro Max",
        "automationName": "XCUITest",
        "app": "com.apple.Preferences"
    }
}
OPTIONS = AppiumOptions().load_capabilities(CAPS)

driver = webdriver.Remote(
    command_executor=APPIUM,
    options=OPTIONS
)

try:
    wait = WebDriverWait(driver, 3)
    siri_search = wait.until(EC.presence_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, "Siri & Search")))
    siri_search.click()
    wait.until(EC.presence_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, "ASK SIRI")))

    # Scroll down and verify presence of the Shortcuts element at the bottom of the screen
    driver.execute_script("mobile: scroll", {"direction": "down"})
    wda = wait.until(EC.presence_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, "com.apple.shortcuts")))
    assert wda.text == "Shortcuts"
    time.sleep(3)   # for demo only

    # Scroll up and verify presence of the Siri Side Button element at the top of the screen
    driver.execute_script("mobile: scroll", {"direction": "up"})
    siri_side_button = wait.until(EC.presence_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, "ASSISTANT_HARDWARE_BUTTON_ID")))
    assert siri_side_button.text == "Press Side Button for Siri"
    time.sleep(3)   # for demo only
finally:
    if driver is not None:
        driver.quit()
