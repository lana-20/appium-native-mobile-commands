from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
try:
    driver.get('https://appium.readthedocs.io/en/latest/en/commands/mobile-command/')
    els = driver.find_elements(By.XPATH, "//td[starts-with(text(), 'mobile')]")
    print(f'Appium has {len(els)} native mobile commands:')
    for i, el in enumerate(els, start=1):
        print(i, el.text)
    # # The below prints 0-based indexing 0-53:
    # for i in range(len(els)):
    #     print(i, els[i].text)
finally:
    driver.quit()