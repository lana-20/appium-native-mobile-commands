from appium import webdriver

APP = 'https://github.com/appium/android-apidemos/releases/download/v3.1.0/ApiDemos-debug.apk'
APPIUM = 'http://localhost:4723'
CAPS = {
    "platformName": "Android",
    "appium:options": {
        "platformVersion": "14.0",      # optional
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        'app': APP
    }
}
driver = webdriver.Remote(APPIUM, CAPS)
try:
    print(driver.execute_script("mobile: shell", {"command": "service list"}))
    print(driver.execute_script("mobile: shell", {"command": "dumpsys battery"}))
    print(driver.execute_script("mobile: shell", {"command": "dumpsys cpuinfo"}))
    print(driver.execute_script("mobile: shell", {"command": "dumpsys meminfo io.appium.android.apis"}))
finally:
    if driver:
        driver.quit()
