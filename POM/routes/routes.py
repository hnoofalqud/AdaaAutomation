from validate.validateElement import ValidateElement


class Routes:

    def __init__(self, driver):
        self.webDriver = driver
        self.validate = ValidateElement(driver=self.webDriver)
        self.htmlInfo = ""
