from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from validate.validateElement import ValidateElement


class Login:
    _logoImg = "//img[contains(@src,'Logo.svg')]"

    _emailField = "//input[contains(@type,'email')]"
    _passwordField = "//input[contains(@type,'password')]"
    _loginBtn = "//form//button"
    _loginBtn2 = "//form//button//span"

    _wrongCredentials = "//div[contains(text(),'Wrong Username or password')]"

    def __init__(self, driver):
        self.webDriver = driver
        self.validate = ValidateElement(driver=self.webDriver)
        self.htmlInfo = "<h3> LOGIN PAGE </h3>"
        self.htmlP = "<p class='login validation {0}'> {1} </p>"

    def fill_login_credentials(self, email, password):
        # Login Page
        try:
            self.htmlInfo += "<p class='login validation'> EMAIL: {0} // PASSWORD: {1} </p>".format(email, password)
            self.webDriver.find_element_by_xpath(self._emailField).send_keys(email)
            self.webDriver.find_element_by_xpath(self._passwordField).send_keys(password)
        except Exception as E:
            errorMsg = "LOGIN CREDENTIALS FAILED -> {0}".format(E)
            self.htmlInfo += "<p class='login validation false'> {0} </p>".format(errorMsg)
            print(errorMsg)

    def login(self, email="huda.alazzeh@realsoft-me.com", password="Huda@123", code="000001"):
        try:
            self.validate.wait_for_loader()  # WAIT FOR THE PAGE LOADER TO FINISH LOADING

            # BUNCH OF VALIDATION STEPS
            isLogoVisible = self.validate.is_element_found_by_xpath(self.get_logo_img_xpath())
            isLoginBtnDisabled = self.validate.is_disabled_by_xpath(self.get_login_btn_xpath())

            validationMsg1 = "IS LOGO IMG FOUND? {0}".format("PASS" if isLogoVisible else "FAIL")
            validationMsg2 = "IS DISABLED LOGIN BTN (CREDENTIALS EMPTY)? -> {0}".format(
                "PASS" if isLoginBtnDisabled else "FAIL")
            # FILL THE LOGIN CREDENTIALS (EMAIL & PASSWORD)
            self.fill_login_credentials(email=email, password=password)

            isLoginBtnEnabled = self.validate.is_enabled_by_xpath(self._loginBtn)
            validationMsg3 = "IS ENABLED LOGIN BTN (CREDENTIALS FILLED)? -> {0}".format(
                "PASS" if isLoginBtnEnabled else "FAIL")

            # WAIT FOR THE LOGIN BUTTON TO BE ENABLED
            loginBtn = WebDriverWait(self.webDriver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self._loginBtn)))

            self.htmlInfo += self.htmlP.format(str(isLogoVisible).lower(), validationMsg1)
            self.htmlInfo += self.htmlP.format(str(isLoginBtnDisabled).lower(), validationMsg2)
            self.htmlInfo += self.htmlP.format(str(isLoginBtnEnabled).lower(), validationMsg3)



            # CLICK ON THE LOGIN BUTTON
            try:
                loginBtn.click()
            except:
                print("LOGIN BTN BLOCKED...")
                loginBtn = WebDriverWait(self.webDriver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self._loginBtn)))
                loginBtn.click()
            self.validate.wait_for_loader()

            if not str(self.webDriver.current_url).__contains__("confirm-login"):
                import time
                time.sleep(3)

            if str(self.webDriver.current_url).__contains__("confirm-login"):
                self.authenticate(code=code)
                self.htmlInfo += "<p class='login validation true'> AUTHENTICATION SUCCESS </p>"
                return True
            else:
                errorMsg = "AUTHENTICATION PAGE NOT LOADED"
                self.htmlInfo += "<p class='login validation false'> {0} </p>".format(errorMsg)
                print(errorMsg)

        except Exception as E:
            errorMsg = "LOGIN FAILED -> {0}".format(E)
            self.htmlInfo += "<p class='login validation false'> {0} </p>".format(errorMsg)
            print(errorMsg)
            return False

    def authenticate(self, code):
        # Authentication Page
        self.validate.wait_for_loader()
        try:
            self.webDriver.find_element_by_xpath("//input[1]").send_keys(code)
            self.webDriver.find_element_by_xpath("//div//button[@type='submit']").click()
        except Exception as E:
            errorMsg = "AUTHENTICATION FAILED -> {0}".format(E)
            self.htmlInfo += "<p class='login validation false'> {0} </p>".format(errorMsg)
            print(errorMsg)
        self.validate.wait_for_loader()

    def get_logo_img_xpath(self):
        return self._logoImg

    def get_wrong_credentials_xpath(self):
        return self._wrongCredentials

    def get_login_btn_xpath(self):
        return self._loginBtn
