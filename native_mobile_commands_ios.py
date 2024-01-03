from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APP = "https://github.com/webdriverio/native-demo-app/releases/download/v1.0.8/ios.simulator.wdio.native.app.v1.0.8.zip"
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
    wait = WebDriverWait(driver, 3)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "Swipe"))).click()
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "Or swipe vertical to find what I'm hiding.")))

    # Swipe down and verify presence of the WebdriverIO logo element at the bottom of the screen
    driver.execute_script("mobile: swipe", {"direction": "up"})
    found = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "You found me!!!")))
    assert found.text == "You found me!!!"

    # Swipe up and verify presence of the "Swipe horizontal" element at the top of the screen
    driver.execute_script("mobile: swipe", {"direction": "down"})
    found = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "Swipe horizontal")))
    assert found.text == "Swipe horizontal"
finally:
    driver.quit()