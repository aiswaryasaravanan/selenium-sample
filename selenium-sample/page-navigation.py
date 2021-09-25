from selenium import webdriver
import time

def testPageNavigation():
    url = 'https://example.cypress.io'
    driver.get(url)

    typePage = driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[3]/ul/li[1]/a')
    typePage.click()

    navigatedPage = driver.current_url
    retryCount = 5
    while str(navigatedPage) != "https://example.cypress.io/commands/actions" and retryCount:
        time.sleep(2)
        retryCount = retryCount-1
    
    if str(navigatedPage) == "https://example.cypress.io/commands/actions":
        print("Success")
    else:
        print("Page navigation failed")

if __name__ == '__main__':

    driver = webdriver.Chrome()
    testPageNavigation()