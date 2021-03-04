from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ValidateElement:

    def __init__(self, driver):
        self.driver = driver
        self.htmlInfo = "<h3> GENERAL VALIDATIONS </h3>"

    def takeScreenshot(self, name):
        import os
        from datetime import datetime
        directory = os.path.abspath('.')
        now = (str(datetime.now().time()).replace(":", "_"))[:5]
        name = "screenshot_" + name + "_" + now + ".png"
        path = directory + "\\Files\\Log\\" + name
        self.driver.save_screenshot(path)
        print("SCREENSHOT SAVED [{0}]".format(path))
        #
        imgHTML = "<img class='validation screenshot' src = './Files/Log/{0}' width = '100px' style = 'margin: auto 25 %;'> ".format(
            name)
        return imgHTML

    def is_element_found_by_xpath(self, xpath):
        self.wait_for_loader()
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException as E:
            errorMsg = ">>EXCEPTION<< {0}".format(E)
            self.htmlInfo += "<p class='general-validation error false'> {0} </p>".format(errorMsg)
            print(errorMsg)
            return False
        return True

    def wait_for_loader(self, waitTime=20):
        _loaderXpath = "//app-custom-loader"
        # Wait for the loader to disappear
        WebDriverWait(self.driver, waitTime).until(
            EC.invisibility_of_element_located((By.XPATH, _loaderXpath)))

    def wait_for_element(self, xpath, waitTime=10):
        try:
            WebDriverWait(self.driver, waitTime).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))

            return True
        except Exception as e:
            print("WAITED TO LONG TO LOAD", str(e))
            return False

    def get_system_massage(self, xpath):
        # RETURN THE TEXT
        return self.is_element_found_by_xpath(xpath)

    def is_enabled_by_xpath(self, xpath):
        if self.is_element_found_by_xpath(xpath):
            return self.driver.find_element_by_xpath(xpath).is_enabled()

    def is_disabled_by_xpath(self, xpath):
        return not self.is_enabled_by_xpath(xpath)

    def get_web_element(self, xpath):
        self.wait_for_loader()
        if self.wait_for_element(xpath=xpath):
            return self.driver.find_element_by_xpath(xpath)
        else:
            print("ELEMENT NOT FOUND")
            return None

    def get_web_elements(self, xpath):
        self.wait_for_loader()
        if self.wait_for_element(xpath=xpath):
            return self.driver.find_elements_by_xpath(xpath)
        else:
            print("ELEMENT NOT FOUND")
            return None
