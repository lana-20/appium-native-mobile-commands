import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# App provided by https://github.com/giurobrossi/testBiometricAuthentication

APP = "/Users/lanabegunova/Desktop/testByometricAuth.app"
APPIUM = "http://localhost:4723"
CAPS = {
    "platformName": "iOS",
    "appium:options": {
        "platformVersion": "17.2",
        "deviceName": "iPhone 15 Pro Max",
        "automationName": "XCUITest",
        "app": APP
    }
}
driver = webdriver.Remote(APPIUM, CAPS)
try:
    driver.execute_script("mobile: enrollBiometric", {"isEnabled": True})
    authenticate_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Authenticate")
    authenticate_button.click()
    driver.switch_to.alert.accept()

    driver.execute_script("mobile: sendBiometricMatch", {"type": "faceId", "match": True})
    wait = WebDriverWait(driver, 15)
    wait.until(EC.alert_is_present())
    success_alert = driver.switch_to.alert
    assert success_alert.text.__contains__("Login succesful !")
    success_alert.accept()

    app_bundle_id = "eu.unicredit.ubis.testapp2"
    driver.execute_script("mobile: terminateApp", {"bundleId": app_bundle_id})  # driver.terminate_app(app_bundle_id)
    driver.execute_script("mobile: activateApp", {"bundleId": app_bundle_id})   # driver.activate_app(app_bundle_id)
    authenticate_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Authenticate")
    authenticate_button.click()

    driver.execute_script("mobile: sendBiometricMatch", {"type": "faceId", "match": False})
    wait.until(EC.presence_of_element_located(
               (AppiumBy.ACCESSIBILITY_ID, "Abort"))).click()
    wait.until(EC.alert_is_present())
    failure_alert = driver.switch_to.alert
    assert failure_alert.text.__contains__("Authentication cancelled by the user")
    failure_alert.dismiss()

finally:
    if driver is not None:
        driver.quit()