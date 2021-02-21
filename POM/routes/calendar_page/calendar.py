from POM.routes.routes import Routes

class Calendar(Routes):


    _RightArrowBtnXpath="//mat-icon[contains(text(),'keyboard_arrow_right')]"
    _LeftArrowBtnXpath="//mat-icon[contains(text(),'keyboard_arrow_left')]"
    _WeekBtnXpath="//div[@class='btn btn-calender' and contains(text(),'Week')]"     #"//div[contains(text(),'Week')]"       #"div.col-md-3 > div > div:nth-child(2)"
    _DayBtnXpath="//div[@class='btn btn-calender' and contains(text(),'Day')]"
    _MonthBtnXpath="//div[@class='btn btn-calender' and contains(text(),'Month')]"
    _CalendarDayXpath="//span[@class='cal-day-number' and text()='{0}']"      #"//span[contains(text(),'13')]"
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



    def click_Right(self):
        #self.htmlInfo += self.htmlP.format("", "go next")

        self.validate.get_web_element(self._RightArrowBtnXpath).click()


    def click_Left(self):
        #self.htmlInfo += self.htmlP.format("", "go back")

        self.validate.get_web_element(self._LeftArrowBtnXpath).click()

    def Week_View(self):
        self.validate.get_web_element(self._WeekBtnXpath).click()
        #self.webDriver.execute_script("document.querySelector('div.col-md-3 > div > div:nth-child(2)').click()")

    def Day_view(self):
        self.validate.get_web_element(self._DayBtnXpath).click()

    def Month_View(self):
        self.validate.get_web_element(self._MonthBtnXpath).click()

    def view_tasks(self,date):
        self.validate.get_web_element(self._CalendarDayXpath.format(date)).click()

    def close_details(self):
        self.validate.get_web_element(self._closeDetails).click()
    def open_task(self,name):
        self.validate.get_web_element(self._TaskNameBtnXpath.format(name)).click()

    def click_filter(self):
        self.validate.get_web_element(self._filterBtn).click()

    def filter_Boards(self, name):
        self.validate.get_web_element(self._FilterBoardXpath).click()
        self.validate.get_web_element((self._BoardsOptionXpath).format(name)).click()

    def filter_Members(self,order):
        self.validate.get_web_element(self._FilterMemberXpath).click()
        self.validate.get_web_element((self._MemberOptionXpath).format(order)).click()

    def Filter_Priority(self,name):
        self.validate.get_web_element(self._PriortyXpath).click()
        self.validate.get_web_element((self._PriorityOptionXpath).format(name)).click()

    def validate_tasklist(self):
      if self.validate.is_element_found_by_xpath(self._taskslistxpath):
          print("TASKS LIST APPEARED")
      else:
          print("NOTHING APPEARED")

    def validate_taskdetails(self):
       if self.validate.is_element_found_by_xpath(self._taskdetailsXpath):
           print("TASKS DETAILS APPEARED")
       else:
           print("NOTHING APPEARED")

    def editHoliday(self,holiday):
        self.validate.get_web_element(self._EditHoliday.format(holiday)).click()

    def deleteHoliday(self,holiday):
        self.validate.get_web_element(self._deleteHolidayeXpath.format(holiday)).click()

