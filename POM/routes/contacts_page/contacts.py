from POM.routes.routes import Routes


class Contacts(Routes):
    _contactsListXpath="//tbody/tr"
    _emailBtnXpath="//td[contains(text(),'{0}')]//..//span"  #BY Email

    #FILTER
    _filterBtn = "//span[contains(@class,'icon-filter')]"
    _NameFilterXpath="//div[1]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"
    _JobFilterXpath="//div[2]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"
    _depFilterXpath="//div[3]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"
    _NameOptionXpath="//div[1]/div[2]/div[{0}]/span[1]" #BY ORDER
    _JobOptionXpath="//span[contains(text(),'{0}')]"  #BY LABEL
    _DepOptionXpath="//div[1]/div[2]/div[{0}]/span[1]"

    def contacts_list(self):
       if self.validate.is_element_found_by_xpath(self._contactsListXpath):
          print("contacts list appeared")
       else:
          print("nothing appeared")

    def click_filter(self):
        self.validate.get_web_element(self._filterBtn).click()

    def Filter_Name(self,order):
        self.validate.get_web_element(self._NameFilterXpath).click()
        self.validate.get_web_element((self._NameOptionXpath).format(order)).click()

    def Filter_Job(self, name):
        self.validate.get_web_element(self._JobFilterXpath).click()
        self.validate.get_web_element((self._JobOptionXpath).format(name)).click()
    def Filter_Dep(self,order):
        self.validate.get_web_element(self._depFilterXpath).click()
        self.validate.get_web_element((self._DepOptionXpath).format(order)).click()

    def send_email(self,email):
        try:
            currentOption = self.validate.get_web_element(self._emailBtnXpath.format(email))
            self.webDriver.execute_script("arguments[0].scrollIntoView();", currentOption)
            self.webDriver.execute_script("arguments[0].click();", currentOption)
            email = self.validate.get_web_element(self._emailBtnXpath.format(email).replace('span','a'))
            print(email.get_attribute('href'))
        except Exception as e:
            print(e)


    def validate_attribute(self,email):
        email = self.validate.get_web_element(self._emailBtnXpath.format(email).replace('span', 'a'))
        attr=(email.get_attribute('href'))
        print(attr)
        if str(attr).lower().__contains__("mailto"):
            print("mail box opened successfully")
        else:
            print("mail box couldn't open")


        # ActionChains(self.webDriver).move_to_element(currentOption).perform()
        # self.webDriver.execute_script("window.scrollBy(0, 200)")
