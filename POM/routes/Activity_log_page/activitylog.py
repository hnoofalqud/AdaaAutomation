from POM.routes.routes import Routes

class Activitylog(Routes):

    _BookmarkBtnXpath='//tbody/tr[{0}]/td[2]/span[1]' #By Order
    _projectByNameXpath = "//span//p[contains(text(),'{0}')]" #by name
    _logsRecordXpath="//tbody[@role='rowgroup']"
    _filterBtn = "//span[contains(@class,'icon-filter')]"
    _filterTaskXpath = "//div[1]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"
    _FilterTaskOptionXpath="//ng-dropdown-panel[1]/div[1]/div[2]/div[{0}]/span[1]" #BY ORDER
    _FilterEditedByOption=" //ng-dropdown-panel[1]/div[1]/div[2]/div[{0}]/span[1]" #BY ORDER
    _filterActionOption="//span[contains(text(),'{0}')]" #BY LABEL
    _filterEditedByXpath = "//div[2]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"
    _filterActionXpath = "//div[3]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"
    _EmptyBookmarkBtnXpath="//span[@class='icon-bookmarkempty']"
    _BookmarkfilterBtnXpath="//span[@class='icon-bookmarkfill']"
    _StartDateXpat = "//input[contains(@formcontrolname,'from')]"
    _EndDateXpath = "//input[contains(@formcontrolname,'to')]"


    def __init__(self, driver):
        Routes.__init__(self, driver)
        self.htmlInfo += "<h3> ACTIVITY LOGS </h3>"
        self.htmlP = "<p class='Activity logs validation {0}'> {1} </p>"


    def Click_Bookmark(self,order):
        self.validate.get_web_element(self._BookmarkBtnXpath.format(order)).click()
        self.htmlInfo += self.htmlP.format("", "BOOKMARK BUTTON ")


    def click_project(self, projectName):
        self.validate.get_web_element(self._projectByNameXpath.format(projectName)).click()
        self.htmlInfo += self.htmlP.format("", "OPEN PROJECT:{0}".format(projectName))

    def validate_logs(self):
        if self.validate.is_element_found_by_xpath(self._logsRecordXpath):
            print("Activity logs appeared")
            self.htmlInfo += self.htmlP.format("", "ACTIVITY LOGS VALIDATION:{0}".format("Activity logs appeared"))
        else:
            print("nothing appeared")
            self.htmlInfo += self.htmlP.format("", "ACTIVITY LOGS VALIDATION:{0}".format("nothing appeared"))


    def click_filter(self):

        self.validate.get_web_element(self._filterBtn).click()

    def filter_Tasks(self, order):
        self.validate.get_web_element(self._filterTaskXpath).click()
        self.validate.get_web_element((self._FilterTaskOptionXpath).format(order)).click()

    def filter_EditedBy(self,order):
        self.validate.get_web_element(self._filterEditedByXpath).click()
        self.validate.get_web_element((self._FilterEditedByOption).format(order)).click()

    def Filter_Action(self,name):
        self.validate.get_web_element(self._filterActionXpath).click()
        self.validate.get_web_element((self._filterActionOption).format(name)).click()

    def Filter_Bookmark(self,state):
        if state=="empty" :
            self.validate.get_web_element(self._EmptyBookmarkBtnXpath).click()
        else:
            self.validate.get_web_element(self._BookmarkfilterBtnXpath).click()

    def set_date(self,start , end):
        self.validate.get_web_element(self._StartDateXpath).send_keys(start)
        self.validate.get_web_element(self._EndDateXpath).send_keys(end)
