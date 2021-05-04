from datetime import time

import pyautogui
from selenium.webdriver import ActionChains

from POM.routes.routes import Routes


class Inbox(Routes):
    _InboxTabBtnXpath="//mat-drawer[1]//p[text()='Inbox']"
    _OutboxTabBtnXpath="//mat-drawer[1]//p[text()=' Outbox']"
    # NEW MESSAGE
    _newMsgBtnXpath = "//button[contains(text(),'New Message')]"

    # INBOX BOARD NAME
    _inboxBoardNameDropDownXpath = "(//ng-select)[4]"
    _inboxBoardNameDropDownOptionXpath = "//ng-dropdown-panel/div/div[2]/div[{0}]/span"

    # TASK
    _inboxTaskDropDownXpath = "(//ng-select)[5]"
    _inboxTaskDropDownOptionXpath = "//ng-dropdown-panel/div/div[2]/div[{0}]/span"

    # Description
    _InboxDescription = "//textarea"

    # FILE UPLOAD
    _upload = "//file-upload"

    # SEND BTN
    _sendBtnXpath = "(//button)[4]"

    # CLOSE BTN
    _closeInboxMsgBtnXpath = "//span[contains(text(),'close')]"

    # FILTER
    _filterBtn ="//mat-expansion-panel-header/span[2]"             #"//span[contains(@class,'icon-filter')]"
    _filterTypeXpath = "//div[1]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"
    _TypeOptionXpath="//span[contains(text(),'{0}')]" #BY LABEL
    _filterBoardXpath = "//div[2]/ng-select[1]/div[1]/div[1]/div[2]"
    _filterUsersXpath = "//ng-select[@formcontrolname='member']"
    _StartDateXpath = "//input[contains(@formcontrolname,'from')]"
    _EndDateXpath = "//input[contains(@formcontrolname,'to')]"
    _BoardsOptionXpath="//span[contains(text(),'{0}')]" #BY LABEL
    _UsersOptionXpath="//div[1]/div[2]/div[{0}]/span[1]"  #BY ORDER

    _ConfirmDeleteBtnXpath="//p[contains(text(),'Delete')]"
    _inboxNumber="//span[contains(text(),'{0}')]"
    _UploadFileBtnXpath="//file-upload[@formcontrolname='files']"


    #MORE OPTIONS
    _moreBtnXpath="//mat-icon[contains(text(),'more_horiz')]"

    #READ/UNREAD
    _ReadMsgBtnXpath="//section[1]/div[{0}]/div[4]/div[1]"

    def __init__(self, driver):
        Routes.__init__(self, driver)
        self.htmlInfo += "<h3> INBOX PAGE </h3>"
        self.htmlP = "<p class='inbox validation {0}'> {1} </p>"

    def get_new_inbox_msg_btn(self, notes=""):
        webElement = self.validate.get_web_element(self._newMsgBtnXpath)

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "NEW INBOX MESSAGE {0} > PASS".format(notes))
        except:
            self.htmlInfo += self.htmlP.format("false", "NEW INBOX MESSAGE {0} > FAIL".format(notes))



    def set_inbox_board_name_drop_down(self, order):
        self.validate.get_web_element(self._inboxBoardNameDropDownXpath).click()
        webElement = self.validate.get_web_element(self._inboxBoardNameDropDownOptionXpath.format(order))

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "INBOX BOARD: OPTION#{0} > PASS".format(order))
        except:
            self.htmlInfo += self.htmlP.format("false", "INBOX BOARD: OPTION#{0} > FAIL".format(order))


    def set_inbox_task_drop_down(self, order):
        self.validate.get_web_element(self._inboxTaskDropDownXpath).click()
        webElement = self.validate.get_web_element(self._inboxTaskDropDownOptionXpath.format(order))

        try:
            webElement.click()
            self.htmlInfo += self.htmlInfo.format("true", "INBOX TASK: OPTION#{0} > PASS".format(order))
        except:
            self.htmlInfo += self.htmlInfo.format("false", "INBOX TASK: OPTION#{0} > FAIL".format(order))

    def set_msg_description(self, text):
        webElement = self.validate.get_web_element(self._InboxDescription)

        try:
            webElement.send_keys(text)
            self.htmlInfo += self.htmlInfo.format("true", "MESSAGE DESCRIPTION {0} > PASS".format(text))
        except:
            self.htmlInfo += self.htmlInfo.format("false", "MESSAGE DESCRIPTION {0} > FAIL".format(text))

    def upload_file(self, path=""):
        errorMsg = "UPLOAD NOT AVAILABLE YET ... PLEASE UPLOAD THE FILE MANUALLY"
        self.htmlInfo += "<p class='inbox validation error'> {0} </p>".format(errorMsg)
        print(errorMsg)

    def get_send_btn(self):
        webElement = self.validate.get_web_element(self._sendBtnXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "SEND MESSAGE > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "SEND MESSAGE > FAIL")

    # def get_filter_btn(self):
    #     self.htmlInfo += self.htmlP.format("", "FILTER")
    #     return self.validate.get_web_element(self._filterBtn)

    def get_close_new_inbox_msg_btn(self):
        webElement =self.validate.get_web_element(self._closeInboxMsgBtnXpath)

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLOSE NEW MESSAGE > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLOSE NEW MESSAGE > FAIL")

    def click_more_btn(self,tab,option):
        self.validate.get_web_element(self._moreBtnXpath).click()
        if str(tab).lower().__contains__("outbox"):
            if str(option).lower().__contains__("edit"):
                webElement=self.validate.get_web_element("//div[1]/div[1]/div[1]/div[1]/p[1]")
                try:
                    webElement.click()
                    self.htmlInfo += self.htmlP.format("true", "EDIT OUTBOX > PASS")
                except:
                    self.htmlInfo += self.htmlP.format("false", "EDIT OUTBOX > FAIL")
            elif str(option).lower().__contains__("copy"):
                webElement =self.validate.get_web_element("//div[1]/div[1]/div[1]/div[1]/p[2]")

                try:
                    webElement.click()
                    self.htmlInfo += self.htmlP.format("true", "COPY OUTBOX > PASS")
                except:
                    self.htmlInfo += self.htmlP.format("false", "COPY OUTBOX > FAIL")
            elif str(option).lower().__contains__("share"):
                webElement=self.validate.get_web_element("//div[1]/div[1]/div[1]/div[1]/p[3]")
                try:
                    webElement.click()
                    self.htmlInfo += self.htmlP.format("true", "SHARE OUTBOX > PASS")
                except:
                    self.htmlInfo += self.htmlP.format("false", "SHARE OUTBOX > FAIL")
            elif str(option).lower().__contains__("delete"):
                webElement=self.validate.get_web_element("//div[1]/div[1]/div[1]/div[1]/p[4]")

                try:
                    webElement.click()
                    self.htmlInfo += self.htmlP.format("true", "DELETE OUTBOX > PASS")
                except:
                    self.htmlInfo += self.htmlP.format("false", "DELETE OUTBOX > FAIL")
        else:
            if str(option).lower().__contains__("copy"):
                webElement=self.validate.get_web_element("//div[1]/div[1]/div[1]/div[1]/p[1]")

                try:
                    webElement.click()
                    self.htmlInfo += self.htmlP.format("true", "COPY INBOX > PASS")
                except:
                    self.htmlInfo += self.htmlP.format("false", "COPY INBOX > FAIL")
            elif str(option).lower().__contains__("share"):
                webElement=self.validate.get_web_element("//div[1]/div[1]/div[1]/div[1]/p[2]")

                try:
                    webElement.click()
                    self.htmlInfo += self.htmlP.format("true", "SHARE INBOX > PASS")
                except:
                    self.htmlInfo += self.htmlP.format("false", "SHARE INBOX > FAIL")



    def confirm_delete(self):
        webElement=self.validate.get_web_element(self._ConfirmDeleteBtnXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CONFIRM DELETE > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CONFIRM DELETE > FAIL")


    def read_Message(self,order):
        _inboxorderXpath = "//form[1]/div[2]/div[1]/section[1]/div[{0}]"
        currentOption = self.validate.get_web_element(_inboxorderXpath.format(order))
        self.webDriver.execute_script("arguments[0].scrollIntoView();", currentOption)
        element_to_hover_over = self.validate.get_web_element(_inboxorderXpath.format(order))
        hover = ActionChains(self.webDriver).move_to_element(element_to_hover_over)
        hover.perform()
        webElement = self.validate.get_web_element(self._ReadMsgBtnXpath.format(order))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "READ/UNREAD MESSAGE {0}> PASS".format(order))
        except:
            self.htmlInfo += self.htmlP.format("false", "READ/UNREAD MESSAGE {0}> FAIL".format(order))


    def validate_inboxNum(self,number):
        if self.validate.is_element_found_by_xpath(self._inboxNumber.format(number)):
            print("INBOX NUMBER IS CORRECT")
            self.htmlInfo += self.htmlP.format("true", "INBOX NUMBER IS {0}> PASS".format(number))
        else:
            print("INBOX NUMBER ID NOT CORRECT")
            self.htmlInfo += self.htmlP.format("false", "INBOX NUMBER IS {0}> FAIL".format(number))


    def uploade_file(self,path):
        self.validate.get_web_element(self._UploadFileBtnXpath).click()
        time.sleep(4)
        pyautogui.click()
        pyautogui.write(r'C:\Users\Hanoof.Alqadeh\Desktop\pics')
        pyautogui.hotkey('enter')
        x, y = pyautogui.locateCenterOnScreen('filename.png', confidence=0.7)
        pyautogui.click(x, y)
        pyautogui.write('download')
        pyautogui.hotkey('enter')

    def Set_BoxType(self, BoxType):
        if BoxType == "Inbox":
            webElement=self.validate.get_web_element(self._InboxTabBtnXpath)

            try:
                webElement.click()
                self.htmlInfo += self.htmlP.format("true", "GO TO: {0} > PASS".format(BoxType))
            except:
                self.htmlInfo += self.htmlP.format("false", "GO TO: {0} > FAIL".format(BoxType))

        elif BoxType == "Outbox":
            webElement=self.validate.get_web_element(self._OutboxTabBtnXpath)

            try:
                webElement.click()
                self.htmlInfo += self.htmlP.format("true", "GO TO: {0} > PASS".format(BoxType))
            except:
                self.htmlInfo += self.htmlP.format("false", "GO TO: {0} > FAIL".format(BoxType))



    def click_Filter(self):
        # self.validate.get_web_element(self._filterBtn).click()
        # webElement = self.validate.get_web_element(self._filterBtn)
        # webElement.click()
        # element_to_click = self.validate.get_web_element(self._filterBtn)
        # click = ActionChains(self.webDriver).move_to_element(element_to_click).click(on_element=element_to_click)
        # click.perform()
        try:
            self.webDriver.execute_script("document.querySelector('mat-expansion-panel-header').click()")
            self.htmlInfo += self.htmlP.format("true", "CLICK FILTER > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLICK FILTER > FAIL")



    def filter_Type(self,name):
        self.validate.get_web_element(self._filterTypeXpath).click()
        webElement=self.validate.get_web_element((self._TypeOptionXpath).format(name))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "FILTER ON {0} TYPE> PASS".format(name))
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER ON {0} TYPE> FAIL".format(name))




    def filter_Boards(self, name):
        self.validate.get_web_element(self._filterBoardXpath).click()
        webElement=self.validate.get_web_element((self._BoardsOptionXpath).format(name))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "FILTER BOARDS {0}> PASS".format(name))
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER BOARDS {0}> FAIL".format(name))


    def filter_users(self,order):
        self.validate.get_web_element(self._filterUsersXpath).click()
        webElement=self.validate.get_web_element((self._UsersOptionXpath).format(order))

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "FILTER USERS {0}> PASS".format(order))
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER USERS {0}> FAIL".format(order))


    def set_date(self,start,end):
        webElement=self.validate.get_web_element(self._StartDateXpath)

        try:
            webElement.send_keys(start)
            self.htmlInfo += self.htmlP.format("true", "SET STARTS DATE {0}> PASS".format(start))
        except:
            self.htmlInfo += self.htmlP.format("false", "SET START DATE {0}> FAIL".format(start))

        webElement2=self.validate.get_web_element(self._EndDateXpath)

        try:
            webElement2.send_keys(end)
            self.htmlInfo += self.htmlP.format("true", "SET END DATE {0}> PASS".format(end))
        except:
            self.htmlInfo += self.htmlP.format("false", "SET END DATE {0}> FAIL".format(end))



    def validate_filterbyUser(self,user):
        webElement=self.validate.get_web_element("//p[@class='name-mail'] | //p[@text()='{0}']".format(user))
        if webElement:
            print("List contains user {0}".format(user))
            self.htmlInfo += self.htmlP.format("true", "VALIDATE USERS{0}> PASS".format(user))

        else:
            print("couldn't find the user {0}".format(user))
            self.htmlInfo += self.htmlP.format("false", "VALIDATE USERS{0}> FAIL".format(user))
