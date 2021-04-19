import pyautogui

from POM.routes.routes import Routes


class myprofile(Routes):

    _myprofileXpath="//span[@class='icon-Myprofile tab-icon']"                   #"//div[3]/div[2]/div/div/div/p[1]"
    _logoutBtnXpath="//div[3]/div[2]/div/div/div/p[2]"
    _editBtnXpath="//mat-icon[contains(text(),'create')]"
    _changephoto="//p[@class='edit-profile profile-icon']"
    _deleteimgXpath="//p[@class='edit-profile']"
    _PermessionXpath="//span[contains(text(),'Permissions')]"
    _NotificationXpath="//span[contains(text(),'Notifications')]"
    _mobilenumXpath="//input[@formcontrolname='mobile']"
    _CountryCodeDDLXpath="//div[contains(text(),'Country Code')]"
    _CountryCodeDDLOptionXpath="//span[contains(text(),'{0}')]"    #BY LABEL
    _ProductionNotificatinBtnXpath="//mat-tab-body/div/div/div[1]/div/mat-slide-toggle[{0}]"  #BY ORDER
    _TasksNotificationBtnXpath="//mat-tab-body/div/div/div[2]/div/mat-slide-toggle[{0}]"  #BY ORDER
    _GeneralNotificationBtnXpath="//mat-tab-body/div/div/div[3]/div/mat-slide-toggle[1]"
    _EmailNotificationBtnXpath="//mat-tab-body/div/div/div[4]/div/mat-slide-toggle[1]"
    _SaveBtnXpath="//span[text()='Save ']"
    _ConfirmBtnXpath="//mat-icon[contains(text(),'save')]"
    _CancelBtnXpath="//p[contains(text(),'Cancel')]"


    def permession_tab(self):
        self.validate.get_web_element(self._PermessionXpath).click()
    def notification_tab(self):
        self.validate.get_web_element(self._NotificationXpath).click()

    def checknotification(self,group,grouporder):
        if str(group).lower()== "production":
            for order in grouporder:
                self.validate.get_web_element(self._ProductionNotificatinBtnXpath.format(order)).click()
        elif str(group).lower() == "tasks" :
            for order in grouporder:
                self.validate.get_web_element(self._TasksNotificationBtnXpath.format(order)).click()
        elif str(group).lower() == "general" :
            self.validate.get_web_element(self._GeneralNotificationBtnXpath).click()
        else:
            self.validate.get_web_element(self._EmailNotificationBtnXpath).click()



    def delete_image(self):
        self.validate.get_web_element(self._editBtnXpath).click()

        self.validate.get_web_element(self._deleteimgXpath)


    def openmyprofile(self):
        self.validate.get_web_element(self._myprofileXpath).click()

    def change_image(self,dir, name):
        self.validate.get_web_element(self._editBtnXpath).click()
        self.validate.get_web_element(self._changephoto).click()
        x, y = pyautogui.locateCenterOnScreen('file_path.png', confidence=0.5)
        pyautogui.click(x, y)
        pyautogui.write(str(dir))
        pyautogui.hotkey('enter')
        x, y = pyautogui.locateCenterOnScreen('file_name.png', confidence=0.5)
        pyautogui.click(x, y)
        pyautogui.write(str().format(name))
        pyautogui.hotkey('enter')

    def set_mobileNum(self,num):
        self.validate.get_web_element(self._mobilenumXpath).clear()
        self.validate.get_web_element(self._mobilenumXpath).send_keys(num)





    def setCountryCode(self,code):
        self.validate.get_web_element(self._CountryCodeDDLXpath).click()
        self.validate.get_web_element(self._CountryCodeDDLOptionXpath.format(code)).click()





        # pyautogui.doubleClick(x, y)
