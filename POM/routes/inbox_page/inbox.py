from POM.routes.routes import Routes


class Inbox(Routes):
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
    _filterBtn = "//span[contains(@class,'icon-filter')]"
    _filterTypeXpath = "//div[1]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"
    _TypeOptionXpath="//span[contains(text(),'{0}')]" #BY LABEL
    _filterBoardXpath = "//div[2]/ng-select[1]/div[1]/div[1]/div[2]"
    _filterUsersXpath = "//div[3]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"
    _StartDateXpath = "//input[contains(@formcontrolname,'from')]"
    _EndDateXpath = "//input[contains(@formcontrolname,'to')]"
    _BoardsOptionXpath="//span[contains(text(),'{0}')]" #BY LABEL
    _UsersOptionXpath="//div[1]/div[2]/div[{0}]/span[1]"  #BY ORDER




    #READ/UNREAD
    _ReadMsgBtnXpath="//section[1]/div[{0}]/div[4]/div[1]"

    def __init__(self, driver):
        Routes.__init__(self, driver)
        self.htmlInfo += "<h3> INBOX PAGE </h3>"
        self.htmlP = "<p class='inbox validation {0}'> {1} </p>"

    def get_new_inbox_msg_btn(self, notes=""):
        self.htmlInfo += self.htmlP.format("", "NEW INBOX MESSAGE {0}".format(notes))
        return self.validate.get_web_element(self._newMsgBtnXpath)

    def set_inbox_board_name_drop_down(self, order):
        self.validate.get_web_element(self._inboxBoardNameDropDownXpath).click()
        self.validate.get_web_element(self._inboxBoardNameDropDownOptionXpath.format(order)).click()
        self.htmlInfo += self.htmlP.format("", "INBOX BOARD: OPTION#{0} - {1}".format(order, "{0}"))

    def set_inbox_task_drop_down(self, order):
        self.validate.get_web_element(self._inboxTaskDropDownXpath).click()
        self.validate.get_web_element(self._inboxTaskDropDownOptionXpath.format(order)).click()
        self.htmlInfo = self.htmlInfo.format("INBOX TASK: OPTION#{0}".format(order))

    def set_msg_description(self, text):
        self.validate.get_web_element(self._InboxDescription).send_keys(text)
        self.htmlInfo += self.htmlP.format("","MESSAGE DESCRIPTION {0}".format(text))

    def upload_file(self, path=""):
        errorMsg = "UPLOAD NOT AVAILABLE YET ... PLEASE UPLOAD THE FILE MANUALLY"
        self.htmlInfo += "<p class='inbox validation error'> {0} </p>".format(errorMsg)
        print(errorMsg)

    def get_send_btn(self):
        self.htmlInfo += self.htmlP.format("", "SEND MESSAGE")
        return self.validate.get_web_element(self._sendBtnXpath)

    def get_filter_btn(self):
        self.htmlInfo += self.htmlP.format("", "FILTER")
        return self.validate.get_web_element(self._filterBtn)

    def get_close_new_inbox_msg_btn(self):
        self.htmlInfo += self.htmlP.format("", "CLOSE NEW MESSAGE")
        return self.validate.get_web_element(self._closeInboxMsgBtnXpath)

    def read_Message(self,order):
        self.validate.get_web_element((self._ReadMsgBtnXpath).format(order)).click()

    def click_Filter(self):
        self.validate.get_web_element(self._filterBtn).click()

    def filter_Type(self,name):
        self.validate.get_web_element(self._filterTypeXpath).click()
        self.validate.get_web_element((self._TypeOptionXpath).format(name)).click()

    def filter_Boards(self, name):
        self.validate.get_web_element(self._filterBoardXpath).click()
        self.validate.get_web_element((self._BoardsOptionXpath).format(name)).click()

    def filter_users(self,order):
        self.validate.get_web_element(self._filterUsersXpath).click()
        self.validate.get_web_element((self._UsersOptionXpath).format(order)).click()

    def set_date(self,start , end):
        self.validate.get_web_element(self._StartDateXpath).send_keys(start)
        self.validate.get_web_element(self._EndDateXpath).send_keys(end)


