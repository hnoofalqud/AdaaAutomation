from POM.routes.routes import Routes

class Calendar(Routes):


    _RightArrowBtnXpath="//mat-icon[contains(text(),'keyboard_arrow_right')]"
    _LeftArrowBtnXpath="//mat-icon[contains(text(),'keyboard_arrow_left')]"
    _WeekBtnXpath="//div[@class='btn-group direction']//..//div[text()=' Week ']"                  #"//div[@class='btn btn-calender' and contains(text(),'Week')]"     #"//div[contains(text(),'Week')]"       #"div.col-md-3 > div > div:nth-child(2)"
    _DayBtnXpath="//div[@class='btn-group direction']//..//div[text()=' Day ']"       #"//div[contains(text(),'Day')]"          #"//div[@class='btn btn-calender' and contains(text(),'Day')]"
    _MonthBtnXpath="//div[@class='btn-group direction']//..//div[text()=' Month ']"               #"//div[@class='btn btn-calender' and contains(text(),'Month')]"
    _CalendarDayXpath="//div[contains(@aria-label,'{0}')]"   #ex:Saturday April 3
    _TaskNameBtnXpath="//span[contains(text(),'{0}')]"  #By name
    _taskslistxpath="//div[1]/div[1]/mwl-calendar-event-title[1]"
    _taskdetailsXpath="//app-task-details[@class='app-task-details']"
    _closeDetails="//span[contains(@class,'task-details-close')]"



    #Filter
    _filterBtn = "//span[contains(@class,'icon-filter')]"
    _FilterMemberXpath="//div[2]/ng-select[1]/div[1]/div[1]/div[2]"
    _MemberOptionXpath="//ng-dropdown-panel[1]/div[1]/div[2]/div[{0}]" #BY ORDER
    _BoardsOptionXpath="//span[contains(text(),'{0}')]" #BY LABEL

    _FilterBoardXpath="//div[1]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"
    _PriortyXpath="//div[3]/mat-form-field[1]/div[1]/div[1]/div[3]"
    _PriorityOptionXpath = "//span[contains(text(),'{0}')]"  # BY LABEL

    def __init__(self, driver):
        Routes.__init__(self, driver)
        self.htmlInfo += "<h3> CALENDAR PAGE </h3>"
        self.htmlP = "<p class='calendar validation {0}'> {1} </p>"

    def click_Right(self):
        #self.htmlInfo += self.htmlP.format("", "go next")
        webElement=self.validate.get_web_element(self._RightArrowBtnXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "MOVE RIGHT > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "MOVE RIGHT > FAIL")


    def click_Left(self):
        #self.htmlInfo += self.htmlP.format("", "go back")

        webElement=self.validate.get_web_element(self._LeftArrowBtnXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "MOVE LEFT > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "MOVE LEFT > FAIL")

    def Week_View(self):
        webElement=self.validate.get_web_element(self._WeekBtnXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "GO TO WEEK VIEW > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "GO TO WEEK VIEW  > FAIL")
        # self.webDriver.execute_script("document.querySelector('div.col-md-3 > div > div:nth-child(2)').click()")

    def Day_view(self):
        webElement=self.validate.get_web_element(self._DayBtnXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "GO TO DAY VIEW > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "GO TO DAY VIEW  > FAIL")


    def Month_View(self):
        webElement=self.validate.get_web_element(self._MonthBtnXpath)

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "GO TO DAY VIEW > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "GO TO DAY VIEW  > FAIL")

    def view_tasks(self,date):
        webElement=self.validate.get_web_element(self._CalendarDayXpath.format(date))

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "VIEW TASKS > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "VIEW TASKS > FAIL")


    def close_details(self):
        webElement=self.validate.get_web_element(self._closeDetails)

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLOSE DETAILS> PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLOSE DETAILS > FAIL")


    def open_task(self,name):
        webElement=self.validate.get_web_element(self._TaskNameBtnXpath.format(name))

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "open task : {0} > PASS".format(name))
        except:
            self.htmlInfo += self.htmlP.format("false", "open task : {0} > FAIL".format(name))

    def click_filter(self):
        webElement=self.validate.get_web_element(self._filterBtn)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLICK FILTER > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLICK FILTER  > FAIL")

    def filter_Boards(self, name):
        self.validate.get_web_element(self._FilterBoardXpath).click()
        webElement=self.validate.get_web_element((self._BoardsOptionXpath).format(name))

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "FILTER BOARD : {0} > PASS".format(name))
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER BOARD : {0} > FAIL".format(name))

    def filter_Members(self,order):
        self.validate.get_web_element(self._FilterMemberXpath).click()
        try:
            self.validate.get_web_element((self._MemberOptionXpath).format(order)).click()
            self.htmlInfo += self.htmlP.format("true", "FILTER MEMBERS > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER MEMBERS > FAIL")



    def Filter_Priority(self,name):
        self.validate.get_web_element(self._PriortyXpath).click()
        try:
            self.validate.get_web_element((self._PriorityOptionXpath).format(name)).click()
            self.htmlInfo += self.htmlP.format("true", "FILTER PRIORITY : {0} > PASS".format(name))
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER PRIORITY : {0} > FAIL".format(name))


    def validate_tasklist(self):
      if self.validate.is_element_found_by_xpath(self._taskslistxpath):
          self.htmlInfo += self.htmlP.format("true", "VALIDATE TASKS LIST : TASKS DETAILS APPEARED > PASS")
          print("TASKS LIST APPEARED")
      else:
          self.htmlInfo += self.htmlP.format("false", "VALIDATE TASKS LIST : TASKS DETAILS APPEARED > FAIL")
          print("NOTHING APPEARED")

    def validate_taskdetails(self):
       if self.validate.is_element_found_by_xpath(self._taskdetailsXpath):
           self.htmlInfo += self.htmlP.format("true", "VALIDATE TASKS DETAILS : TASKS DETAILS APPEARED > PASS")
           print("TASKS DETAILS APPEARED")
       else:
           self.htmlInfo += self.htmlP.format("false", "VALIDATE TASKS LIST : TASKS DETAILS APPEARED > FAIL")
           print("NOTHING APPEARED")

    # def editHoliday(self,holiday):
    #     self.validate.get_web_element(self._EditHoliday.format(holiday)).click()
    #
    # def deleteHoliday(self,holiday):
    #     self.validate.get_web_element(self._deleteHolidayeXpath.format(holiday)).click()

