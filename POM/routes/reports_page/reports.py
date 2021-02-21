from POM.routes.routes import Routes


class Reports(Routes):

    _InboxBtnXpath = "//*[contains(text(),'Inbox')]"  # [2]
    # //div[contains(@class,'menu-escalation')]//p[contains(text(),'Inbox')]

    _OutboxBtnXpath = "//*[contains(text(),'Outbox')]"
    # //div[contains(@class,'menu-escalation')]//p[contains(text(),'Outbox')]

    _newReportBtnXpath = "//button[contains(text(),'New Report')]"
    _newCommentBtnXpath = "//*[contains(text(),'Comments')]//*"
    _moreOptionsXpath = "//div[contains(@class,'mat-menu-content')]//p[contains(text(),'{0}')]"
    _WriteCommentXpath="// textarea[contains(@class,'mat-input-element')]"
    _newCommentMenuBtnXpath= "//div[contains(@class,'menu')]//p[contains(text(),'{0}')]" # BY LABE:L
    _MoreBtnXpath = "//mat-icon[contains(text(),'more_horiz')]"#"//div[@class='mat-icon'] "  # //div[contains(@class,'mat-menu-panel')]
    _ForwardBtnXpath = "//*[contains(text(),'Forward')]//*"


    #_ShareBtnXpath = "//*[contains(text(),'Share')]//*"
    # _SaveWordBtnXpath= "//p[@class='edit-profile profile-icon ng-star-inserted']"
    # _SavePdfBtnXpath= "//div[contains(@class,'menu')]//p[contains(text(),'3')]"
    _ReportByOrderXpath="//div[contains(@class,'mail-container')][{0}]"

    # NEW REPORT

    _ReportSubjectXpath = "//input[contains(@placeholder,'Subject')]"
    _BoardNameDropDownXpath = "(//ng-select)[3]"
    _boardNameDropDownOptionByOrderXpath = "//ng-dropdown-panel/div/div[2]/div[{0}]/span"
    _ReportDescriptionXpath = "//textArea"
    _SendReportBtnXpath =  "//span[text()='Send']"   #(//button)[4]"
    _CloseReportBtnXpath = "//span[contains(text(), 'close')]"
    _IsUrgentBtnXpath = "//div[contains(@class,'mat-slide-toggle-thumb')]"
    _CommentRowXpath="//div[contains(@class,'row comments-part-section')]"
    _DeleteReportBtnXpath= "//button[contains(@class,'save-button')]"
    _taskNameDropDownXpath="(//ng-select)[4]"
    _taskNameDropDownOptionXpath="//ng-dropdown-panel/div/div[2]/div[{0}]/span"
    _writeCommentxpath="//textarea[@placeholder='Write Comment']"
    _sendCommentBtnXpath = "//button[@class='sent-button']"
    _sendForward="//div[contains(@class,'action')]//button"
    _sendCopyBtnXpath="//span[contains(text(),'Send')]"
    # Filter
    _filterBtn = "//span[contains(@class,'icon-filter')]"
    _FilterMemberXpath = "//div[2]/ng-select[1]/div[1]/div[1]/div[2]"
    _MemberOptionXpath = "//ng-dropdown-panel[1]/div[1]/div[2]/div[{0}]"  # BY ORDER
    _BoardsOptionXpath = "//span[contains(text(),'{0}')]"  # BY LABEL
    _StartDateXpat = "//input[contains(@formcontrolname,'from')]"
    _EndDateXpath = "//input[contains(@formcontrolname,'to')]"
    _FilterBoardXpath = "//div[1]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"

    def __init__(self, driver):
        Routes.__init__(self, driver)
        self.htmlInfo += "<h3> Reports PAGE </h3>"
        self.htmlP = "<p class='Reports validation {0}'> {1} </p>"

    def get_new_Report_btn(self, notes=""):
        self.htmlInfo += "<hr class='Report validation'>"
        self.htmlInfo += self.htmlP.format("", "NEW Report {0}".format(notes))
        return self.validate.get_web_element(self._newReportBtnXpath).click()

    def set_board_Name_drop_down(self, option):
        self.validate.get_web_element(self._BoardNameDropDownXpath).click()
        webElement = self.validate.get_web_element(self._boardNameDropDownOptionByOrderXpath.format(option))
        webElement.click()
        self.htmlInfo += self.htmlP.format("", "BOARD Name: OPTION#{0}".format(option))

    def set_task_drop_down(self,option):
        self.htmlInfo += self.htmlP.format("", "SET TASKS: {0}".format(option))
        self.validate.get_web_element(self._taskNameDropDownXpath).click()
        self.validate.get_web_element(self._taskNameDropDownOptionXpath.format(option)).click()
    def set_report_subject(self, subject):
        self.validate.get_web_element(self._ReportSubjectXpath).send_keys(subject)
        self.htmlInfo += self.htmlP.format("", "REPORT SUBJECT: {0}".format(subject))

    def set_report_Description(self, Description):
        self.validate.get_web_element(self._ReportDescriptionXpath).send_keys(Description)
        self.htmlInfo = self.htmlP.format("", "REPORT DESCRIPTION: {0}".format(Description))

    def click_Report(self, ReportName):
        self.htmlInfo += self.htmlP.format("", "SET REPORT NAME: {0}".format(ReportName))
        self.validate.get_web_element(self._ReportByNameXpath.format(ReportName)).click()
        # self.webDriver.find_element_by_css_selector(self._ReportByOrderCssSelector.format(ReportName)).click()

    def get_send_new_Report_btn(self):
        imgHTML = self.validate.takeScreenshot(name="Send_Report")
        self.htmlInfo += imgHTML
        return self.validate.get_web_element(self._SendReportBtnXpath).click()

    def get_close_new_Report_btn(self):
        self.htmlInfo += self.htmlP.format("", "CLOSE NEW REPORT:")
        return self.validate.get_web_element(self._CloseReportBtnXpath).click()

    def click_urgent(self, ):
        self.htmlInfo += self.htmlP.format("", "MAKE REPORT URGENT")
        self.validate.get_web_element(self._IsUrgentBtnXpath).click()

    def Set_BoxType(self, BoxType):
        self.htmlInfo += self.htmlP.format("", "GO TO: {0}".format(BoxType))
        if BoxType == "Inbox":
            self.validate.get_web_element(self._InboxBtnXpath).click()
        elif BoxType == "Outbox":
            self.validate.get_web_element(self._OutboxBtnXpath).click()


    def get_forward_Report_btn(self):
        self.htmlInfo += self.htmlP.format("", "FORWARD REPORT")
        self.validate.get_web_element(self._ForwardBtnXpath).click()

    def get_comment_btn(self):
        self.htmlInfo += self.htmlP.format("", "NEW COMMENT ")
        self.validate.get_web_element(self._newCommentBtnXpath).click()

    def get_more_menu_btn(self):
        self.validate.get_web_element(self._MoreBtnXpath).click()

    def get_menu_option(self, menuOption):
        self.htmlInfo += self.htmlP.format("", "GET MORE OPTIONS {0}".format(menuOption))
        self.validate.get_web_element(self._moreOptionsXpath.format(menuOption)).click()

    def send_comment(self):
        self.htmlInfo += self.htmlP.format("", "SEND COMMENT")
        self.validate.get_web_element(self._sendCommentBtnXpath).click()

    def set_new_Comment(self,comment):
        self.htmlInfo += self.htmlP.format("", "SET NEW COMMENT: {0}")
        self.validate.get_web_element(self._writeCommentxpath).send_keys(comment)

    def validate_comment(self):
        self.validate.get_web_element(self._CommentRowXpath)

    def get_Report(self,ReportOrder):
        self.htmlInfo += self.htmlP.format("", "GO TO {0}".format(ReportOrder))
        self.validate.get_web_element(self._ReportByOrderXpath.format(ReportOrder)).click()

    def Confirm_Delete_Report(self):
        self.htmlInfo += self.htmlP.format("", "CONFIRM DELETE")
        self.validate.get_web_element(self._DeleteReportBtnXpath).click()

    def send_forward(self):
        self.htmlInfo += self.htmlP.format("", "FORWARD")
        self.validate.get_web_element(self._sendForward).click()

    def send_copy(self):
        self.htmlInfo += self.htmlP.format("", "Copy")
        self.validate.get_web_element(self._sendCopyBtnXpath).click()


    def click_filter(self):
        self.validate.get_web_element(self._filterBtn).click()

    def filter_Boards(self, name):
        self.validate.get_web_element(self._FilterBoardXpath).click()
        self.validate.get_web_element((self._BoardsOptionXpath).format(name)).click()

    def filter_Members(self, order):
        self.validate.get_web_element(self._FilterMemberXpath).click()
        self.validate.get_web_element((self._MemberOptionXpath).format(order)).click()

    def set_date(self, start, end):
        self.validate.get_web_element(self._StartDateXpat).send_keys(start)
        self.validate.get_web_element(self._EndDateXpath).send_keys(end)

