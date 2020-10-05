from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

path = '/home/runner/work/git-action-test/git-action-test/chromedriver'
options = Options()
options.headless = True
driver = Chrome(executable_path=path, options=options)

driver.get('http://localhost:5000/slate_portal')
driver.set_window_size(1920, 1080)
print(driver.title)
driver.quit()