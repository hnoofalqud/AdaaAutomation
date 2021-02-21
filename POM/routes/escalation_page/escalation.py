from POM.routes.routes import Routes


class Escalation(Routes):

    _InboxBtnXpath = "//*[contains(text(),'Inbox')]"
    _OutboxBtnXpath = "//*[contains(text(),'Outbox')]"


    _newEscalationBtnXpath = "//button[contains(text(),'New Escalation')]"
    _newCommentBtnXpath = "//*[contains(text(),'Comments')]//*"
    _moreOptionsXpath = "//div[contains(@class,'mat-menu-panel')]//p[contains(text(),'{0}')]"
    _WriteCommenBoxtXpath= "//textarea[@placeholder='Write Comment']"
    _newCommentMenuBtnXpath= "//div[contains(@class,'menu')]//p[contains(text(),'{0}')]" # BY LABE:L
    _sendCommentBtnXpath="//button[@class='sent-button']"
    _CopyBtnXpath = "//*[contains(text(),'Copy')]//*"
    #_ShareBtnXpath = "//*[contains(text(),'Share')]//*"
    _MoreBtnXpath = "//mat-icon[contains(text(),'more_horiz')]"
    _EscalationByOrderXpath="//div[contains(@class,'mail-container')][{0}]"
    _SendCopyBtnXpath="//button[@class='mat-button mat-button-base']"

    # NEW Escalation

    _EscalationSubjectXpath = "//input[contains(@placeholder,'Subject')]"
    _BoardNameDropDownXpath = "(//ng-select)[3]"
    _boardNameDropDownOptionByOrderXpath = "//ng-dropdown-panel/div/div[2]/div[{0}]/span"
    _EscalationtDescriptionXpath = "//textArea"
    _SendEscalationBtnXpath = "(//button)[4]"
    _CloseEscalationBtnXpath = "//span[contains(text(), 'close')]"
    _IsCloseBtnXpath = "//div[contains(@class,'mat-slide-toggle-thumb')]"  #//div[@class='mat-slide-toggle-bar']
    _taskNameDropDownXpath = "(//ng-select)[4]"
    _taskNameDropDownOptionXpath = "//ng-dropdown-panel/div/div[2]/div[{0}]/span"
    _CommentRowXpath="//div[contains(@class,'row comments-part-section')]"
    _ConfirmBtnXpath= "//button[contains(@class,'save-button')]"
    _CloseNewComment="//span[@class='report-comments-close icon-baseline-clear-24px']"

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
        self.htmlInfo += "<h3> Escalation PAGE </h3>"
        self.htmlP = "<p class='escalation validation {0}'> {1} </p>"

    def get_new_escalation_btn(self):
        self.htmlInfo += "<hr class='Escalation validation'>"
        self.validate.get_web_element(self._newEscalationBtnXpath).click()

    def set_board_Name_drop_down(self, option):
        self.validate.get_web_element(self._BoardNameDropDownXpath).click()
        self.validate.get_web_element(self._boardNameDropDownOptionByOrderXpath.format(option)).click()
        self.htmlInfo += self.htmlP.format("", "BOARD Name: OPTION#{0}".format(option))

    def set_task_drop_down(self, option):
        self.validate.get_web_element(self._taskNameDropDownXpath).click()
        self.validate.get_web_element(self._taskNameDropDownOptionXpath.format(option)).click()


    def set_Escalation_subject(self, subject):
        self.validate.get_web_element(self._EscalationSubjectXpath).send_keys(subject)
        self.htmlInfo += self.htmlP.format("", "Escalation SUBJECT: {0} - {1}".format(subject, '{0}'))

    def set_Escalation_Description(self, Description):
        self.validate.get_web_element(self._EscalationtDescriptionXpath).send_keys(Description)
        self.htmlInfo += self.htmlP.format("", "Escalation DESCRIPTION: {0}".format(Description))


    def get_escalation(self,EscalationOrder):
        self.validate.get_web_element(self._EscalationByOrderXpath.format(EscalationOrder)).click()
        self.htmlInfo += self.htmlP.format("", "OPEN ESCALATION")
        # self.webDriver.find_element_by_css_selector(self._EscalationByOrderCssSelector.format(EscalationName)).click()

    def get_send_new_Escalation_btn(self):
        imgHTML = self.validate.takeScreenshot(name="save_Escalation")
        self.htmlInfo += imgHTML
        return self.validate.get_web_element(self._SendEscalationBtnXpath ).click()

    def get_close_new_Escalation_btn(self):
        self.htmlInfo += self.htmlP.format("", "CLOSE NEW ESCALATION")
        return self.validate.get_web_element(self._CloseEscalationBtnXpath).click()


    def click_close(self):
        self.htmlInfo += self.htmlP.format("", "CLOSE ESCALATION")
        self.validate.get_web_element(self._IsCloseBtnXpath).click()

    def Set_BoxType(self, BoxType):
        self.htmlInfo += self.htmlP.format("", "GO TO : {0}".format(BoxType))
        if BoxType == "Inbox":
            self.validate.get_web_element(self._InboxBtnXpath).click()
        elif BoxType == "Outbox":
            self.validate.get_web_element(self._OutboxBtnXpath).click()

    def get_comment_btn(self):
        self.htmlInfo += self.htmlP.format("", "CLICK COMMENT")
        self.validate.get_web_element(self._newCommentBtnXpath).click()

    def get_more_menu_btn(self):
        self.htmlInfo += self.htmlP.format("", "CLICK MORE MENU")
        self.validate.get_web_element(self._MoreBtnXpath).click()

    def get_menu_option(self, menuOption):
        self.htmlInfo += self.htmlP.format("", "CLICK MORE MENU")
        self.validate.get_web_element(self._moreOptionsXpath.format(menuOption)).click()
    def send_comment(self):
        self.htmlInfo += self.htmlP.format("", "SEND COMMENT")
        self.validate.get_web_element(self._sendCommentBtnXpath).click()

    def set_new_Comment(self,comment):
        self.htmlInfo += self.htmlP.format("", "SET NEW COMMENT")
        self.validate.get_web_element(self._WriteCommenBoxtXpath).send_keys(comment)


    def validate_comment(self):
       return self.validate.get_web_element(self._CommentRowXpath)

    def Confirm_Button(self):
        self.htmlInfo += self.htmlP.format("", "CONFIRM")
        self.validate.get_web_element(self._ConfirmBtnXpath).click()

    def Close_new_comment(self):
        self.validate.get_web_element(self._CloseNewComment).click()

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

    def Send_copy(self):
        self.validate.get_web_element(self._SendCopyBtnXpath).click()

