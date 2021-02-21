from POM.routes.routes import Routes

class approvals(Routes):


    _checkBoardXpath="//tr[{0}]/td[1]/span[1]/mat-checkbox[1]"      # #BY ORDER
    _checkAllXpath="//th[1]/span[1]/mat-checkbox[1]/label[1]/div[1]"
    _ApproveBtnXpath="//button[contains(text(),' Approve ')]"
    _RejectBtnXpath="//button[contains(text(),' Reject ')]"
    _ConfirmBtnXpath="//button[contains(@class,'save-button')]"
    _CancelBtnXpath="//button[contains(@class,'cancel-button')]"
    _CloseBtnXpath="//span[contains(@class,'material-icons close-icon')]"
    _RejectionReasonXpath="//input[@placeholder='Rejection Reason']"
    _DetailsXpath="//tr[{0}]/td[2]/div[1]/div[3]/a[1]"  #BY ORDER
    _CommentBtnXpath="//tr[{0}]//span[contains(@class,'comment-icon')]" #BY ORDER
    _WriteCommentXpath="//textarea[@placeholder='Write Comment']"
    _sendCommentBtnXpath="//button[@class='sent-button']"
    _viewmembers="//tr[{0}]/td[6]//img"  #BY ORDER

    # FILTER
    _filterBtn = "//span[contains(@class,'icon-filter')]"
    _FilterBoardXpath="//div[1]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"
    _FilterMemberXpath = "//div[2]/ng-select[1]/div[1]/div[1]/div[2]"
    _MemberOptionXpath="//ng-dropdown-panel[1]/div[1]/div[2]/div[{0}]" #BY ORDER
    _BoardsOptionXpath="//span[contains(text(),'{0}')]" #BY LABEL

    _filterStartDateXpath = "//input[contains(@formcontrolname,'startDataSearch')]"
    _filterEndDateXpath = "//input[contains(@formcontrolname,'endDataSearch')]"


    def CheckAll(self):
        self.validate.get_web_element(self._checkAllXpath).click()


    def CheckBoards(self,ordergroup):
        for order in ordergroup:
          self.validate.get_web_element(self._checkBoardXpath.format(order)).click()


    def Approve_Boards(self):
        self.validate.get_web_element(self._ApproveBtnXpath).click()

    def Reject_Boards(self):
        self.validate.get_web_element(self._RejectBtnXpath).click()


    def set_RejectionReason(self,text):
        self.validate.get_web_element(self._RejectionReasonXpath).send_keys(text)

    def view_Details(self,order):
        self.validate.get_web_element((self._DetailsXpath).format(order)).click()

    def click_comment(self,order):
        self.validate.get_web_element((self._CommentBtnXpath).format(order)).click()

    def set_comment(self,text):
        self.validate.get_web_element(self._WriteCommentXpath).send_keys(text)

    def send_comment(self):
        self.validate.get_web_element(self._sendCommentBtnXpath).click()

    def view_members(self,order):
        self.validate.get_web_element(self._viewmembers.format(order)).click()

    def click_filter(self):
        self.validate.get_web_element(self._filterBtn).click()

    def filter_Boards(self, name):
        self.validate.get_web_element(self._FilterBoardXpath).click()
        self.validate.get_web_element((self._BoardsOptionXpath).format(name)).click()

    def filter_Members(self,order):
        self.validate.get_web_element(self._FilterMemberXpath).click()
        self.validate.get_web_element((self._MemberOptionXpath).format(order)).click()

    def set_date(self, start, end):
        self.validate.get_web_element(self._filterStartDateXpath).send_keys(start)
        self.validate.get_web_element(self._filterEndDateXpath).send_keys(end)

    def click_confirm(self):
        self.validate.get_web_element(self._ConfirmBtnXpath).click()