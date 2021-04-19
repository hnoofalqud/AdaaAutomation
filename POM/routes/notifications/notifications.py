from POM.routes.routes import Routes

class notifications(Routes):
    _selectAllCheckbox="//div[1]/section[1]/div[1]/mat-checkbox[1]/label[1]/div[1]"


    #send_notification_dialog

    _addnotification="//mat-icon[contains(text(),'add')]"
    _languageDDLXpath="//span[contains(text(),'Language')]"
    _LanguageDDLOptionXpath="//span[contains(text(),'{0}')]"   #BY LABEL
    _TitleFieldXpath="//mat-form-field[2]/div/div/div[3]/input[1]"
    _DescreptionXppath="//mat-form-field[3]/div/div/div[3]/input[1]"
    _membersDDLXpath="//mat-dialog-content[1]//ng-select[1]//div[2]/input"
    _SendNotificationBtnXpath="//button[contains(text(),'Send')]"
    _CanelnotificationBtnXpath="//button[contains(text(),'Cancel')]"
    _closenotificationxpath="//span[contains(text(),'close')]"
    _singlecheckboxxpath="//form[1]/section[{0}]/div[1]/mat-checkbox[1]/label[1]/div[1]"  #BY ORDER
    _MorelistXpath="//form[1]/section[{0}]/div[1]/div[1]/div[3]/p[1]/span[2]"   #BY ORDER



    def add_notification(self):
        self.validate.get_web_element(self._addnotification).click()

    def set_notificationDetails(self,title,description):
        self.validate.get_web_element(self._TitleFieldXpath).send_keys(title)
        self.validate.get_web_element(self._DescreptionXppath).send_keys(description)


    def change_notificatiolanguage(self,lan):
        self.validate.get_web_element(self._languageDDLXpath).click()
        self.validate.get_web_element(self._LanguageDDLOptionXpath.format(lan)).click()

    def choose_members(self,member):
        #TODO: ADD MEMBERS OPTION
        self.validate.get_web_element(self._membersDDLXpath).click()

    def send_notification(self):
        self.validate.get_web_element(self._SendNotificationBtnXpath).click()

    def cancel_notification(self):
        self.validate.get_web_element(self._CanelnotificationBtnXpath).click()

    def close_notification(self):
        self.validate.get_web_element(self._closenotificationxpath).click()

    def checknotification(self,grouporder):
        for order in grouporder:
            self.validate.get_web_element(self._singlecheckboxxpath.format(order)).click()

    def selectAll(self):
        self.validate.get_web_element(self._selectAllCheckbox).click()