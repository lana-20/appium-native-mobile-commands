import time
from pprint import pprint
from appium import webdriver

APPIUM = "http://localhost:4723"
CAPS = {
    "platformName": "Android",
    "appium:options": {
        "platformVersion": "14.0",  # optional
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings"
    }
}
driver = webdriver.Remote(APPIUM, CAPS)
app = "ApiDemos.apk"
app_id = "io.appium.android.apis"
app_act1 = ".view.DateWidgets2"
app_act2 = ".app.FragmentAlertDialog"
try:
    driver.remove_app(app)
    driver.install_app(app)
    driver.activate_app(app_id)
    driver.execute_script("mobile: startActivity", {"component": f"{app_id}/{app_act1}"})
    time.sleep(3)   # for demo only -  to observe the activity launch
    driver.execute_script("mobile: startActivity", {"component": f"{app_id}/{app_act2}"})
    time.sleep(3)  # for demo only -  to observe the activity launch
    driver.terminate_app(app_id)
    pprint(driver.execute_script("mobile: deviceInfo"))
finally:
    if driver is not None:
        driver.quit()
