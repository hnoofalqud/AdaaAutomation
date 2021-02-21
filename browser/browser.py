import os
from datetime import datetime
from selenium import webdriver



class Browser:
    driver = None  # HOLDS THE BROWSER (to call all the driver'TestCase associated methods directly)

    def __init__(self):
        # CONSTRUCTOR
        pass

    def launch(self, browser="F", url=""):
        # Instantiate the browser Command
        if browser.lower() == "firefox" or browser.lower() == "f":
            print("LAUNCHING FIREFOX...")
            self.driver = webdriver.Firefox()  # Starts webElement new local session of Firefox.

        elif browser.lower() == "chrome" or browser.lower() == "c":
            print("LAUNCHING CHROME...")
            self.driver = webdriver.Chrome()  # Creates webElement new instance of the chrome drive

        elif browser.lower() == "edge" or browser.lower() == "e":
            print("LAUNCHING EDGE...")
            self.driver = webdriver.Edge()  # Creates webElement new instance of the chrome drive

        elif browser.upper() == "CHROME (TABLET SIZE)":
            print("LAUNCHING CHROME (TABLET SIZE)...")
            from selenium.webdriver.chrome.options import Options
            mobile_emulation = {

                "deviceMetrics": {"width": 660, "height": 540, "pixelRatio": 3.0},

                "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

            chrome_options = Options()
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
            #  self.driver = webdriver.Ie()  # Creates webElement new instance of the chrome drive

        elif browser.upper() == "GHOST MODE":
            print("GHOST MODE...")
            from selenium.webdriver.chrome.options import Options
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            self.driver = webdriver.Chrome(chrome_options=chrome_options)

        self.driver.get(url)

        self.driver.implicitly_wait(1)

    def navigate(self, command):
        if command.upper() == "BACK" or command.upper() == "B" \
                or command.upper() == "PREVIOUS" or command.upper() == "P":
            self.driver.back()
        elif command.upper() == "FORWARD" or command.upper() == "F" \
                or command.upper() == "NEXT" or command.upper() == "N":
            self.driver.forward()
        elif command.upper() == "REFRESH" or command.upper() == "RELOAD" or command.upper() == "R":
            self.refreshPage()
        elif command.__contains__("http"):
            self.launchURL(command)

    def takeScreenshot(self, name):
        directory = os.path.abspath('.')
        now = (str(datetime.now().time()).replace(":", "_"))[:5]
        path = directory + "\\Files\\Log\\screenshot_" + name + "_" + now + ".png"
        self.driver.save_screenshot(path)
        return path
        print("SCREENSHOT SAVED [{0}]".format(path))

    def getPageTitle(self):
        pageTitle = self.driver.title
        return pageTitle

    def getPageURL(self):
        pageURL = self.driver.current_url
        return pageURL

    def refreshPage(self):
        self.driver.refresh()
        self.driver.find_element_by_id().send_keys()

