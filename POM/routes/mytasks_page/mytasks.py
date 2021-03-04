from selenium.webdriver import ActionChains

from POM.routes.routes import Routes


class Mytasks(Routes):

    _TaskDetails="//td[contains(text(),'{0}')]//..//div[contains(text(),'{1}')]//..//a[text()='Details']" #BY BOARD LABEL + TASK LABEL
    _taskMembers="//tr[{0}]/td[6]"  #BY ORDER
    _OwnerName="//p[contains(text(), '{0}')]"  #BY LABEL
    _AssignedToMeXpath="//div//p[contains(text(),'{0}')]"  #BY LABEL
    #EDIT MY TASK
    _TaskNameXpath="//input[@formcontrolname='taskName']"
    _TaskDescXpath="//textarea[@formcontrolname='taskDesc']"
    _TaskStartDateXpath="//input[@formcontrolname='startDate']"
    _TaskEndDateXpath="//input[@formcontrolname='endDate']"
    _TaskDurationXpath="//input[@formcontrolname='duration']"

    #RECURRING
    _MakeRecurring="//mat-slide-toggle[1]/label/div/div"
    _DailyRecurringXpath="//div[contains(text(),'Daily')]"
    _WeeklyRecurringXpath="//div[contains(text(),'Weekly')]"
    _MonthlyRecurringXpath="//div[contains(text(),'Monthly')]"
    _YearlyRecurringXpath="//div[contains(text(),'Yearly')]"
    _RecurringEveryXpath="//input[@formcontrolname='RecurringEvery']"


    _RecurringMonthlyEveryXpath="//mat-radio-button[{0}]/label[1]/div[2]/div[1]//..//input[@formcontrolname='RecurringEvery']"
    _selectMonthlyRrecurringday="//mat-radio-group[1]/mat-radio-button[{0}]/label[1]/div[1]"

    _RecurringMonthDayDDLXpath="//mat-select[@formcontrolname='RecurringPositionId']"
    _RecurringMonthDayDDLOption="//span[contains(text(),'{0}')]"   #BY LABEL
    _Recurringmonthday="//input[@formcontrolname='RecurringMonthDay']"
    _RecurringWeekDayDDLXpath="//mat-select[@formcontrolname='RecurringWeekDayId']"
    _RecurringWeekDayDDlOption="//span[contains(text(),'{0}')]"  #BY LABEL

    _RecurringStartDateXpath="//input[@formcontrolname='RecurringStartDate']"
    _RecurringEndDateXpath="//input[@formcontrolname='RecurringEndDate']"
    _RecurringOccurrencesXpath="//input[@formcontrolname='RecurringOccurrences']"
    _RecurringOnweekDays="//mat-select[@formcontrolname='wDays']"


    _ProgressTypeDDLXpath="//mat-select[@formcontrolname='taskStatusGroupId']"
    _ProgressTypeOptionXpath="//span[contains(text(),'{0}')]"  #BY LABEL
    _TaskProgressRatio="//input[@formcontrolname='currentStatus']"
    _TaskPriorityDDLXpath="//mat-select[@formcontrolname='processType']"
    _TaskPriorityOptionXpath="//mat-option[{0}]/span[1]"   #BY ORDER
    _TaskDependancyDDLXpath="//mat-select[@formcontrolname='dependencyType']"
    _TaskDepandencyOptionXpath="//span[contains(text(),'{0}')]" #By label
    _TaskDepartmentsDDLXpath="//div[contains(text(),'Departments')]"
    _TaskDeparrtmentsOptionXpath="//span[contains(text(),'{0}')]"
    _TaskMembersDDLXpath="//div[contains(text(),'Members')]"
    _TaskMembersOptionXpath="(//div[@class='ng-dropdown-panel-items scroll-host']//*[contains(text(),' ')])[{0}]" #BY ORDER
    _SaveTaskBTNXpath="//button[contains(text(),' Save')]"
    _CancelTaskBTNXpath="//button[contains(text(),' Cancel')]"
    _CommentTabInTask="//span[contains(text(),'Comments')]"
    _ActivityTabINTaskXpath="//span[contains(text(),'Activity Log')]"
    _listOfMembers = "//app-circle-view/div"




    #FILTERATION
    _FilterBoardDDLXpath="//div[contains(text(),'Select Board')]"
    _FilterBoardOptionXpath="//span[contains(text(),'{0}')]" #BY LABEL
    _FilterTaskMemberDDLXpath="//span[contains(text(),'Assigned to me')]"  #TODO : IT HAS TO BE CHANGED

    def open_task_details(self,board,task):
        self.validate.get_web_element(self._TaskDetails.format(board,task)).click()

    # def open_members(self,order):
    #     self.validate.get_web_element(self._taskMembers.format(order)).click()


    def select_Recurring(self,type):
        self.validate.get_web_element(self._MakeRecurring).click()
        if str(type).lower()== "daily" :
            self.validate.get_web_element(self._DailyRecurringXpath)
        elif str(type).lower()== "weekly" :
            self.validate.get_web_element(self._WeeklyRecurringXpath)
        elif str(type).lower()== "monthly" :
            self.validate.get_web_element(self._YearlyRecurringXpath)


    def weekly_recurring(self,every,day,occ):
        self.validate.get_web_element(self._RecurringEveryXpath).send_keys(every)
        self.validate.get_web_element(self._RecurringWeekDayDDLXpath).click()
        self.validate.get_web_element(self._RecurringWeekDayDDlOption.format(day))
        self.validate.get_web_element(self._RecurringOccurrencesXpath).send_keys(occ)

    def monthly_recurring(self,order,every):
        self.validate.get_web_element(self._selectMonthlyRrecurringday.format(order))
        self.validate.get_web_element(self._RecurringMonthlyEveryXpath.format(order)).send_keys(every)


    def monthly_recurringdayORDER(self, day):
        self.validate.get_web_element(self._Recurringmonthday).send_keys(day)
        self.validate.get_web_element(self._RecurringMonthlyEveryXpath.format(1)).send_keys(day)


    def monthlyrecurringweekday(self):
        pass



    def set_recurringDate(self,startDate,endDate):
        self.validate.get_web_element(self._RecurringStartDateXpath).send_keys(startDate)
        self.validate.get_web_element(self._RecurringEndDateXpath).send_keys(endDate)





    #TODO: CHECK ASSIGNEDTOMEXPATH

    def loop_over_members(self ,NAME):
        members=self.validate.get_web_elements(self._listOfMembers)
        count = 0

        for member in members:
            count += 1
            member.click()
            assignedto=self.validate.get_web_element(self._AssignedToMeXpath.format(NAME))
            if assignedto:
                print("task no.{1} is assigned to {0}".format(NAME, count))

            else:
                print("task no.{1} is not assigned to {0}".format(NAME,count))

            # size = member.size
            # x = (int(size['width']) * 2)
            # ActionChains(self.webDriver).move_to_element(member).move_by_offset(-x, 0).click().perform()
            # counter+=100
            self.webDriver.execute_script("arguments[0].scrollIntoView(true);", member)
            self.webDriver.execute_script("arguments[0].click();", member)
            # self.webDriver.execute_script("window.scrollBy(0,{0});".format(counter))
            print('SCROLLING...')




    def Validate_OwnedByMeTasks(self,name):
        #as a previous step u need to open task details
        owner = self.validate.is_element_found_by_xpath(self._OwnerName.format(name))
        if owner:
            print("this task is owned by {0}".format(name))

        else:
            print("this task is not owned by {0}".format(name))
