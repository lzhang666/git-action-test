from selenium.webdriver import Chrome

path = '/home/runner/work/git-action-test/git-action-test/chromedriver'
driver = Chrome(path)

driver.get('https://www.uchicago.edu/')
print(driver.title)
driver.quit()

