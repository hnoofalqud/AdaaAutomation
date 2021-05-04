import time

import pyautogui
from POM.routes.routes import Routes
from selenium.webdriver import ActionChains


class Boards(Routes):
    """
    Boards Page

    - New Board
    -- Each Field has a set function
    """

    # PROJECTS
    _allProjectsCssSelector = "span.ng-star-inserted > p"
    _projectByOrderCssSelector = "span.ng-star-inserted:nth-child({0}) > p "
    _projectByNameXpath = "//span//p[contains(text(),'{0}')]"
    _searchProjectsXpath = "//input[@id='mat-input-0']"

    # FILTER
    _filterBtn = "//span[contains(@class,'icon-filter')]"
    _filterMemberDDLXpath = "//ng-select[1]/div[1]/div[1]/div[2]"
    _filterPriorityDDLXpath = "//div[3]/mat-select[1]/div[1]/div[1]"
    _filterStartDateXpath = "//input[contains(@formcontrolname,'startDataSearch')]"
    _filterEndDateXpath = "//input[contains(@formcontrolname,'endDataSearch')]"
    _MemberOptionXpath = "//ng-dropdown-panel[1]/div[1]/div[2]/div[{0}]"  # BY ORDER
    _PriorityOptionXpath = "//span[contains(text(),'{0}')]"  # BY LABEL

    # --- NEW BOARD --- START
    _newBoardBtnXpath = "//div[@class='new-button ng-star-inserted']"

    # DIV 1
    _boardNameXpath = "//input[contains(@formcontrolname,'productName')]"
    _boardCodeXpath = "//input[contains(@placeholder,'Code')]"

    # DIV 2
    _boardDepartmentsDropDownXpath = "//div[2]/div[3]//input"
    _boardDepartmentsDropDownOptionByOrderXpath = "(//div[@class='ng-dropdown-panel-items scroll-host']//*[contains(text(),' ')])[{0}]"

    _boardSupervisorDropDownXpath = "//div[2]/div[4]//input"
    _boardSupervisorDropDownOptionByOrderXpath = "(//div[@class='ng-dropdown-panel-items scroll-host']//*[contains(text(),' ')])[{0}]"

    _boardStatusDropDownXpath = "//div[@class='col-md-4 margin-zero-form']//mat-form-field "  # //div[@class='mat-select-value']
    _boardStatusDropDownOptionXpath = "(//mat-option//span[@class='mat-option-text'])[{0}]"  # OPTION ORDER

    _boardAppColorXpath = "//app-color-control"
    _boardAppColorOptionXpath = "//div[@class='product-color ng-star-inserted'][{0}]"  # "//div[contains(@class,'color')]//div[{0}]" #BY ORDER

    # DIV 3 (Resource Pool)
    _boardDepartmentsResourcePoolDropDownXpath = "//div[2]/ng-select//input"
    _boardDepartmentsResourcePoolDropDownOptionXpath = "(//div[3]/div[2]//div[contains(@class,'ng-option')])[{0}]"

    _membersResourcePoolDropDownXpath = "//div[3]/div[3]//div[contains(@class,'mat-select-value')] "
    _membersResourcePoolDropDownOptionXpath = "//mat-optgroup[{0}]/mat-option[{1}]/span"

    # DIV 4(copy from)

    _copyfromBtnXpath = "//mat-slide-toggle[@formcontrolname='copyFromToggle']"
    _copyfromoptionxpath = "//div[text()='{0}']"
    _firstDDLXpath = "//div[1]/div[6]/div[1]/ng-select"
    _FirstDDLOptionXpath = "//ng-dropdown-panel[1]//div[2]/div[{0}]"  # BY ORDER
    _copyTaskstartDate = "//input[@formcontrolname='StartDate']"

    # DIV 6 (BOARD DESCRIPTION)
    _boardDescriptionXpath = "//div[6]/div//div//textarea"

    # DIV 7 (BOARD ATTRIBUTES)
    _addAttributesBtnXpath = "//div[1]/div[7]//mat-icon[1]"
    _AttributeNameXpath = "//input[@placeholder='Attribute Name']"
    _SelectAttributeDDLXpath = "//mat-select[@formcontrolname='TypeId']"
    _SeletAttributeOptionsXpath = "//span[contains(text(),'{0}')]"  # BY LABEL
    _attributeValueXpath = "//input[@formcontrolname='value']"
    _yesNoDDlXpath = "//mat-select[@formcontrolname='value']"
    _yesNoOptionDDL = "//span[text()='{0}']"
    _deleteAttributeXpath = "//mat-icon[contains(text(),'delete')]"
    # SAVE (SUBMIT) BUTTON
    _saveBoardBtnXpath = "//button[@type='submit']"

    # CLOSE (EXIT) BUTTON
    _closeBoardBtnXpath = "//span[contains(text(),'close')]"

    # --- NEW BOARD --- END

    # ----------------------

    # --- NEW TASK --- START
    _newTaskBtnXpath = "//thead/tr[1]/th[1]/span[1]"
    _newchildtaskBtnXpath = "//tr[{0}]/td[1]/div[1]/div[3]/span[1]"

    # DIV 1
    _taskNameXpath = "//app-task-details//input[contains(@placeholder,'Name')]"
    _taskDescriptionXpath = "//app-task-details//textarea[contains(@formcontrolname,'taskDesc')]"

    # DIV 2
    _taskStartDateXpath = "//app-task-details//input[contains(@formcontrolname,'startDate')]"
    _taskEndDateXpath = "//app-task-details//input[contains(@formcontrolname,'endDate')]"
    _taskDurationXpath = "//app-task-details//input[contains(@placeholder,'Duration')]"

    # DIV 3
    _taskMakingRecurringThumb = "//app-task-details//div[contains(@class,'mat-slide-toggle-thumb')]"
    _RecurringOccurrences = "//input[@formcontrolname='RecurringOccurrences']"
    _RecurringStartDate = "//input[@formcontrolname='RecurringStartDate']"
    _RecurringEndDate = "//input[@formcontrolname='RecurringEndDate']"
    _repeateType = "//mat-label[contains(text(),'Repeat')]"
    _RepeatTyeOptionXpath="//span[contains(text(),'{0}')]" #BY LABEL


    # DIV 4
    _taskProgressType = "//div[6]/div[1]//mat-select[1]/div[1]"

    _progresstypeoptionxpath ="//mat-select[@formcontrolname='taskStatusDetailId']"
    _taskProgressTypeOptionByOrder = "(//mat-option//span)[{0}]"  # ORDER
    _progresstypeoptiondetails = "//span[contains(text(),'{0}')]" #by label
    _taskProgressRatio = "//input[contains(@placeholder,'Progress ratio')]"
    _taskPriorityDDLXpath = "//div[6]/div[3]//mat-select"
    _taskPriorityOptionXpath = "//mat-option[{0}]/span[1]"  # ORDER
    _taskPriorittyDetailsDDLXpath = "//mat-select[@formcontrolname='taskStatusDetailId']"
    _taskPriorityDetailsOptionXpath = "//mat-option[{0}]/span[1]"
    _DependancyDDLXpath = "//mat-select[@formcontrolname='dependencyType']"
    _DependancyOptionXpath = "//mat-option[{0}]/span[1]"
    _dependOnTaskDDLXpath = "//ng-select[@formcontrolname='predcessorTaskId']"
    _dependOnTaskOptionXpath = "//div[@class='ng-dropdown-panel-items scroll-host']//div//div[{0}]"
    # DIV 5

    # DIV 7
    _taskDepartmentsDropDownXpath = "//ng-select[@formcontrolname='taskDirectorates']"  # "(//div[8]//input)[1]"
    _taskDepartmentsDropDownOptionXpath = "(//div[@class='ng-dropdown-panel-items scroll-host']//*[contains(text(),' ')])[{0}]"

    _taskMembersDropDownXpath = "//ng-select[@formcontrolname='assignedEmployees']"  # "(//div[8]//input)[2]"
    _taskMembersDropDownOptionXpath = "(//div[@class='ng-dropdown-panel-items scroll-host']//*[contains(text(),' ')])[{0}]"

    # SAVE (SUBMIT) BUTTON
    _saveTaskBtnXpath = "//button[contains(text(),'Save')]"
    # CANCEL BUTTON
    _cancelTaskBtnXpath = "//button[contains(text(),'Cancel')]"

    _closeTaskBtnXpath="//div[1]/div[2]/app-task-details[1]/p[1]/span[1]"           #"//span[@class='task-details-close icon-baseline-clear-24px']"     #"//app-task-details[1]/p[1]/span[1]"
    # --- NEW TASK --- END
    _tasksListXpath = "//div[@class='task-name'][1]"
    _BoardDDLOptionXpath = "//div[contains(@class,'mat-menu-cont')]//p[contains(text(),'{0}')]"  # by label
    _templateXpath = "//p[@title='{0}']"
    _BoardStatusDDLXpath = "//mat-select[1]/div[1]/div[1]"
    _BoardStatusDDLOptionXpath = "//div[contains(@class,'panel')]//span[contains(text(),'{0}')]"  # by label
    _BoardDDLBtnXpath = "//div/div[contains(@class,'project-name')]"
    _DuplicateNameXpath = "//input[@formcontrolname='name']"  # "//mat-label[@class='ng-star-inserted']"
    _OKBtnXpath = "//button[contains(@class,'save-button')]"
    _ConvertToNameXpath = "//input[@formcontrolname='name']"
    _DeleteBtnXpath = "//button[contains(@class,'save-button')]"
    _progressRatioBtnXpath = "//tr[{0}]/td[8]/div[1]"  # By ORDER
    _ProgressRatioXpath = "//input[contains(@placeholder,'Progress ratio')]"
    _ApprovedIconXpath = "//tbody/tr[{0}]/td[5]/div[1]/mat-icon[1]"
    _ClosedStatusValidation = "//tr[{0}]//mat-icon[contains(text(),'close')]"
    _CheckedStatusValidationXpath = "//tr[{0}]//mat-icon[contains(text(),'check')]"
    # ----------------------

    _TaskDetailsBtnXpath = "//tr[{0}]//a[1]"  # By order
    _CommentBtnXpath = "//span[contains(text(),'Comments')]"
    _SetCommentXpath = "//textarea[@formcontrolname='noteTxt']"
    _sendcommentBtnXpath = "//button[@class='sent-button']"
    _EditCommentBtnXpath = "//app-comments-tab[1]/div[1]/div[3]/div[{0}]/div[3]/span[1]"
    _DeleteCommentEditDDLXpath = "//p[@class='edit-profile' and text()=' Delete']"
    _CommentXpath="//p[contains(text(),'where')]"

    _EditCommentOptionXpath = "//p[@class='edit-profile' and text()='Edit Comment']"
    _deleteTaskBtnXpath="//tbody/tr[{0}]/td[1]/div[1]/div[3]/span[2]"
    _BoardSettingsBtnXpath = "//div[5]/div[2]/span[3]"
    _DetailsActivityLogxpath = "//span[contains(text(),'Activity Log')]"

    # FILTER ACTIVITY LOGS

    _activitymemberfilter = "//div[contains(text(),'Members')]"
    _activitymemberoptionfilter = "//div[2]/div[{0}]"  # by order    #"//span[text()=' user user']" #by label
    _activityactionfilter = "//div[contains(text(),'Action')]"
    _activityactionoptionfilter = "//ng-dropdown-panel[1]/div[1]/div[2]/div[{0}]"  # by order
    _bookmarkedFilterXpath = "//button[@class='bookmark-button bookmark-button-left-radius']"
    _notbookmarkedfilterxpath = "//button[@class='bookmark-button bookmark-button-right-radius']"
    _activitylogfromdatefilter = "//input[@formcontrolname='from']"
    _activitylogtodatefilter = "//input[@formcontrolname='to']"
    _activitylogrows = "//app-log-page[1]//table[1]/tbody/tr[1]"

    # calendar view
    _CalendarViewXpath = "//span[text()='Calendar']"
    _calendarWeekViewXpath = "//div[text()=' Week ']"
    _calendarDayViewXpath = "//div[text()=' Day ']"
    _calendarMonthViewXpath = "//div[text()=' Month ']"
    _TaskinweekCalendar= "//span[contains(text(),'{0}')]"  #BY LABEL
    _DayinCalendar="//div[contains(@aria-label,'{0}')]"   #ex:Saturday April 3
    _TaskXpath="//span[contains(text(),'{0}')]"  #by label
    _tasksListInCalendar="//mwl-calendar-open-day-events[1]/div[1]"


    # Gant View
    _gantweekview = "//span[text()='Week']"
    _gantdayview = "//span[text()='Day']"
    _gantQuarterview = "//span[text()='Quarter']"
    _gantmonthview = "//span[text()='Month']"
    _viewganttask ="//div[contains(text(),'{0}')]"     #BY LABEL
    _clickganttab = "//span[text()='Gant']"
    _expandgant = "//div[2]//tr[{0}]/td[2]//span[1]"


    _addfilexpath = "//mat-icon[contains(text(),'cloud_upload')]"
    _BoardNameXpath = "//div[3]//p[contains(text(),'{0}')]"  # By label

    def __init__(self, driver):
        Routes.__init__(self, driver)
        self.htmlInfo += "<h3> BOARDS PAGE </h3>"
        self.htmlP = "<p class='board validation {0}'> {1} </p>"

    def get_number_of_projects(self):
        return len(self.webDriver.find_elements_by_css_selector(self._allProjectsCssSelector))

    def click_project(self, projectName):
        # element = self.validate.is_element_found_by_xpath(self._projectByNameXpath.format(projectName))
        webElement=self.validate.get_web_element(self._projectByNameXpath.format(projectName))

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "open {0} > PASS".format(projectName))
        except:
            self.htmlInfo += self.htmlP.format("false", "open {0} > PASS".format(projectName))

    def search_project(self, searchField):
        self.validate.get_web_element(self._searchProjectsXpath).clear()
        webElement=self.validate.get_web_element(self._searchProjectsXpath)
        try:
            webElement.send_keys(searchField)
            self.htmlInfo += self.htmlP.format("true", "SEARCH FOR {0} PROJECT > PASS".format(searchField))

        except:
            self.htmlInfo += self.htmlP.format("false", "SEARCH FOR {0} PROJECT > FAIL".format(searchField))


    # NEW BOARD

    def get_new_board_btn(self, notes=""):
        self.htmlInfo += "<hr class='board validation'>"
        element2 = self.validate.get_web_element(self._newBoardBtnXpath)
        element2.click()
        # print(element2.click())
        try:
            element2.click()
            self.htmlInfo += self.htmlP.format("true", "NEW BOARD {0} > PASS".format(notes))
        except:
            self.htmlInfo += self.htmlP.format("false", "NEW BOARD {0} > FAIL".format(notes))

    def set_board_name(self, name):
        # element = self.validate.is_element_found_by_xpath(self._boardNameXpath)
        webElement=self.validate.get_web_element(self._boardNameXpath)
        try:
            webElement.send_keys(name)
            self.htmlInfo += self.htmlP.format("true", "SET BOARD NAME: {0} > PASS".format(name))
        except:
            self.htmlInfo += self.htmlP.format("false", "SET BOARD NAME: {0} > FAIL".format(name))

    def set_board_code(self, code):
        # element = self.validate.is_element_found_by_xpath(self._boardCodeXpath)
        webElement=self.validate.get_web_element(self._boardCodeXpath)
        try:
            webElement.send_keys(code)
            self.htmlInfo += self.htmlP.format("true", "SET BOARD CODE: {0} > PASS".format(code))
        except:
            self.htmlInfo += self.htmlP.format("false", "SET BOARD CODE: {0} > FAIL".format(code))

    def set_board_department_drop_down(self, option):
        self.validate.get_web_element(self._boardDepartmentsDropDownXpath).click()
        webElement = self.validate.get_web_element(self._boardDepartmentsDropDownOptionByOrderXpath.format(option))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true",
                                               "BOARD DEPARTMENT: OPTION#{0} - {1} > PASS".format(option, "{0}"))
        except:
            self.htmlInfo += self.htmlP.format("false",
                                               "BOARD DEPARTMENT: OPTION#{0} - {1} > FAIL".format(option, "{0}"))

    def set_board_supervisor_drop_down(self, option):
        self.validate.get_web_element(self._boardSupervisorDropDownXpath).click()
        webElement = self.validate.get_web_element(self._boardSupervisorDropDownOptionByOrderXpath.format(option))
        try:
            webElement.click()
            self.htmlInfo = self.htmlInfo.format("true", "BOARD SUPERVISOR: OPTION#{0} > PASS".format(option))
        except:
            self.htmlInfo = self.htmlInfo.format("false", "BOARD SUPERVISOR: OPTION#{0} > FAIL".format(option))

    def set_Newboard_status(self, option):
        self.validate.get_web_element(self._boardStatusDropDownXpath).click()
        webElement = self.validate.get_web_element(self._boardStatusDropDownOptionXpath.format(option))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "SET BOARD STATUS TO {0} > PASS".format(option))
        except:
            self.htmlInfo += self.htmlP.format("false", "SET BOARD STATUS TO {0} > FAIL".format(option))

    def edit_color(self, colorOrder):
        webElement=self.validate.get_web_element(self._boardAppColorOptionXpath.format(colorOrder))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "EDIT BOARD COLOR > PASS")

        except:
            self.htmlInfo += self.htmlP.format("false", "EDIT BOARD COLOR > FAIL")


    def set_board_color(self, option):
        self.validate.get_web_element(self._boardAppColorXpath).click()
        webElement = self.validate.get_web_element(self._boardAppColorOptionXpath.format(option))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "SET BOARD COLOR {0} > PASS".format(option))
        except:
            self.htmlInfo += self.htmlP.format("false", "SET BOARD COLOR {0} > FAIL".format(option))

    def set_board_departments_resource_pool(self, option):
        # [1,2,3]
        for optionItem in option:
            self.validate.get_web_element(self._boardDepartmentsResourcePoolDropDownXpath).click()
            webElement = self.validate.get_web_element(
                self._boardDepartmentsResourcePoolDropDownOptionXpath.format(optionItem))
            try:
                webElement.click()
                self.htmlInfo += self.htmlP.format("true ",
                                                   "BOARD DEPARTMENT RESOURCE POOL:{0} > PASS".format(optionItem))
            except:
                self.htmlInfo += self.htmlP.format("false ",
                                                   "BOARD DEPARTMENT RESOURCE POOL:{0} > FAIL".format(optionItem))

    def set_board_members_resource_pool(self, group, option):
        self.validate.get_web_element(self._membersResourcePoolDropDownXpath).click()
        for groupItem, optionItem in zip(group, option):
            currentOption = self.validate.get_web_element(
                self._membersResourcePoolDropDownOptionXpath.format(groupItem, optionItem))
            try:
                currentOption.click()
                self.htmlInfo += self.htmlP.format("true",
                                                   "BOARD MEMBERS RESOURCE POOL:GROUP{0} OPTION {1} > PASS".format(
                                                       groupItem, optionItem))
            except:
                self.htmlInfo += self.htmlP.format("false",
                                                   "BOARD MEMBERS RESOURCE POOL:GROUP{0} OPTION {1} > FAIL".format(
                                                       groupItem, optionItem))
        # TO CLICK OUTSIDE
        size = currentOption.size
        x = (int(size['width']) * 2)
        ActionChains(self.webDriver).move_to_element(currentOption).move_by_offset(-x, 0).click().perform()

        # self.validate.get_web_element("//body[1]/div[2]/div").click()  # CLOSE DIALOG

    def set_board_description(self, text):
        webElement = self.validate.get_web_element(self._boardDescriptionXpath)
        try:
            webElement.send_keys(text)
            self.htmlInfo += self.htmlP.format("true", "BOARD DESCRIPTION: {0} > PASS".format(text))
        except:
            self.htmlInfo += self.htmlP.format("false", "BOARD DESCRIPTION: {0} > FAIL".format(text))

    def get_save_new_board_btn(self):
        imgHTML = self.validate.takeScreenshot(name="save_board")
        self.htmlInfo += imgHTML
        webElement = self.validate.get_web_element(self._saveBoardBtnXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLICK SAVE NEW BOARD > PASS")
            imgHTML = self.validate.takeScreenshot(name="save_board")
            self.htmlInfo += imgHTML
        except:
            self.htmlInfo += self.htmlP.format("false", "CLICK SAVE NEW BOARD > FAIL")

    def get_close_new_board_btn(self):
        webElement = self.validate.get_web_element(self._closeBoardBtnXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLOSE NEW BOARD > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLOSE NEW BOARD > FAIL")


    def get_close_Task_Details(self):
        webElement = self.validate.get_web_element(self._closeTaskBtnXpath)

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLOSE TASK DETAILS > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLOSE TASK DETAILS > FAIL")


    def CopyfromBtn(self, option):
        self.validate.get_web_element(self._copyfromBtnXpath).click()
        webElement = self.validate.get_web_element(self._copyfromoptionxpath.format(option))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "COPY FROM {0} > PASS".format(option))
        except:
            self.htmlInfo += self.htmlP.format("false", "COPY FROM {0} > FAIL".format(option))

    def copyfromDDL(self, option, date):
        self.validate.get_web_element(self._firstDDLXpath).click()
        webElement = self.validate.get_web_element(self._FirstDDLOptionXpath.format(option))
        try:
            webElement.click()
            self.validate.get_web_element(self._copyTaskstartDate).send_keys(date)
            self.htmlInfo += self.htmlP.format("true", "COPY FROM {0} PROJECT ,START DATE: {1}> PASS".format(option,date))
        except:
            self.htmlInfo += self.htmlP.format("false", "COPY FROM {0} PROJECT ,START DATE: {1}> FAIL".format(option,date))

    # --------------------------------

    def get_new_task_btn(self):
        webElement = self.validate.get_web_element(self._newTaskBtnXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLICK NEW TASK > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLICK NEW TASK > FAIL")

    def new_childTask_btn(self, order):
        _TaskXpath="//tr[{0}]/td[1]/div[1]"
        element_to_hover_over = self.validate.get_web_element(_TaskXpath.format(order))
        hover = ActionChains(self.webDriver).move_to_element(element_to_hover_over)
        hover.perform()
        webElement = self.validate.get_web_element(self._newchildtaskBtnXpath.format(order))

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLICK NEW CHILD TASK > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLICK NEW CHILD TASK > FAIL")

    def set_task_name(self, name):
        webElement = self.validate.get_web_element(self._taskNameXpath)
        webElement.send_keys(name)
        if webElement:
            self.htmlInfo += self.htmlP.format("true", "NEW TASK -> TASK NAME: {0} > PASS".format(name))
        else:
            self.htmlInfo += self.htmlP.format("false", "NEW TASK -> TASK NAME: {0} > PASS ".format(name))

    def set_task_description(self, description):
        webElement = self.validate.get_web_element(self._taskDescriptionXpath)
        try:
            webElement.send_keys(description)
            self.htmlInfo += self.htmlP.format("true", "TASK DESCRIPTION: {0} > PASS ".format(description))
        except:
            self.htmlInfo += self.htmlP.format("false", "TASK DESCRIPTION: {0} > PASS".format(description))

    def set_task_start_end_date(self, startDate, endDate):
        webElement1 = self.validate.get_web_element(self._taskEndDateXpath)
        try:
            webElement1.send_keys(endDate)
            self.htmlInfo += self.htmlP.format("true", "END DATE: {0} > PASS".format(endDate))
        except:
            self.htmlInfo += self.htmlP.format("false", "END DATE: {0}  > FAIL".format(endDate))

        webElement2 = self.validate.get_web_element(self._taskStartDateXpath)

        try:
            webElement2.send_keys(startDate)
            self.htmlInfo += self.htmlP.format("true", "START DATE: {0} > PASS".format(startDate))
        except:
            self.htmlInfo += self.htmlP.format("false", "START DATE: {0}  > FAIL".format(startDate))

    def set_task_duration(self, duration):
        webElement = self.validate.get_web_element(self._taskDurationXpath)

        try:
            webElement.send_keys(duration)
            self.htmlInfo += self.htmlP.format("true", "DURATION: {0} > PASS".format(duration))
        except:
            self.htmlInfo += self.htmlP.format("false", "DURATION: {0} > FAIL".format(duration))

    def set_task_departments(self, options):
        for optionItem in options:
            self.validate.get_web_element(self._taskDepartmentsDropDownXpath).click()
            webElement = self.validate.get_web_element(self._taskDepartmentsDropDownOptionXpath.format(optionItem))
            try:
                webElement.click()
                self.htmlInfo += self.htmlP.format("true", "TASK DEPARTMENTS: {0} > PASS".format(str(options)))
            except:
                self.htmlInfo += self.htmlP.format("false", "TASK DEPARTMENT: {0} > FAIL".format(str(optionItem)))

    def set_task_members(self, options):
        for optionItem in options:
            self.validate.get_web_element(self._taskMembersDropDownXpath).click()
            webElement = self.validate.get_web_element(self._taskMembersDropDownOptionXpath.format(optionItem))
            try:
                webElement.click()
                self.htmlInfo += self.htmlP.format("true", "TASK MEMBERS: {0} > PASS".format(optionItem))
            except:
                self.htmlInfo += self.htmlP.format("false", "TASK MEMBERS: {0} > FAIL".format(optionItem))

    def set_task_progress(self, Option,option2):
        self.validate.get_web_element(self._taskProgressType).click()
        webElement = self.validate.get_web_element(self._taskProgressTypeOptionByOrder.format(Option))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "TASK PROGRESS TYPE: {0} > PASS".format(Option))
        except:
            self.htmlInfo += self.htmlP.format("false", "TASK PROGRESS TYPE: {0} > FAIL".format(Option))
        self.validate.get_web_element(self._progresstypeoptionxpath).click()
        self.validate.get_web_element(self._progresstypeoptiondetails.format(option2)).click()




    def set_task_progress_ratio(self, ratio):
        self.validate.get_web_element(self._taskProgressRatio).clear()
        webElement = self.validate.get_web_element(self._taskProgressRatio)

        try:
            webElement.send_keys(ratio)
            self.htmlInfo += self.htmlP.format("true", "TASK PROGRESS RATIO: {0} > PASS".format(ratio))
        except:
            self.htmlInfo += self.htmlP.format("false", "TASK PROGRESS RATIO: {0} > FAIL".format(ratio))

    def set_task_priority(self, priority):
        self.validate.get_web_element(self._taskPriorityDDLXpath).click()
        webElement = self.validate.get_web_element(self._taskPriorityOptionXpath.format(priority))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "TASK PRIORITY {0} > PASS".format(priority))
        except:
            self.htmlInfo += self.htmlP.format("false", "TASK PRIORITY {0} > FAIL".format(priority))

    def set_task_priority_details(self, option):
        self.validate.get_web_element(self._taskPriorittyDetailsDDLXpath).click()
        webElement = self.validate.get_web_element(self._taskPriorityDetailsOptionXpath.format(option))

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "PRIORITY DETAILS {0} > PASS".format(option))
        except:
            self.htmlInfo += self.htmlP.format("false", "PRIORITY DETAILS {0} > FAIL".format(option))

    def set_depndancy(self, option, task):
        self.validate.get_web_element(self._DependancyDDLXpath).click()
        webElement = self.validate.get_web_element(self._DependancyOptionXpath.format(option))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", " TASK DEPNDANCY TYPE {0} > PASS".format(option))
        except:
            self.htmlInfo += self.htmlP.format("false", " TASK DEPNDANCY TYPE {0} > FAIL".format(option))

        self.validate.get_web_element(self._dependOnTaskDDLXpath).click()
        webElement2= self.validate.get_web_element(self._dependOnTaskOptionXpath.format(task))
        try:
            webElement2.click()
            self.htmlInfo += self.htmlP.format("true", " DEPENDS ON TASK: {0} > PASS".format(task))
        except:
            self.htmlInfo += self.htmlP.format("false", "TASK DEPNDANCY {0} > FAIL".format(task))

    def save_new_task(self):
        webElement = self.validate.get_web_element(self._saveTaskBtnXpath)

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "SAVE TASK > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "SAVE TASK > FAIL")

    def cancel_task(self):
        webElement = self.validate.get_web_element(self._cancelTaskBtnXpath)

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CANCEL TASK > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CANCEL TASK > FAIL")

    def Board_DDL(self, option):
        self.validate.get_web_element(self._BoardDDLBtnXpath).click()
        webElement = self.validate.get_web_element(self._BoardDDLOptionXpath.format(option))
        # webElement.click()
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "BOARD {0} > PASS".format(option))
        except:
            self.htmlInfo += self.htmlP.format("false", "BOARD {0} > FAIL".format(option))

    def set_Convert_To_name(self, text):
        webElement = self.validate.get_web_element(self._ConvertToNameXpath)

        try:
            webElement.send_keys(text)
            self.htmlInfo += self.htmlP.format("true", "CONVERT TO TEMPLATE {0} > PASS".format(text))
        except:
            self.htmlInfo += self.htmlP.format("false", "CONVERT TO TEMPLATE {0} > FAIL".format(text))



    def validate_Tasks_number(self):
        if self.validate.is_element_found_by_xpath(self._taskslistXpath):
            self.htmlInfo += self.htmlP.format("true", "VALIDATE TASKS LIST: LIST APPEARED > PASS")
        else:
            self.htmlInfo += self.htmlP.format("false", "VALIDATE TASKS LIST: LIST DID NOT APPEAR > FAIL")

    def set_Board_status(self, status):
        self.validate.get_web_element(self._BoardStatusDDLXpath).click()
        webElement= self.validate.get_web_element(self._BoardStatusDDLOptionXpath.format(status))

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "BOARD STATUS {0} > PASS".format(status))
        except:
            self.htmlInfo += self.htmlP.format("false", "BOARD STATUS {0} > FAIL".format(status))



    def set_Duplicate_name(self, text):
        webElement=self.validate.get_web_element(self._DuplicateNameXpath)
        try:
            webElement.send_keys(text)
            self.htmlInfo += self.htmlP.format("true", "SET DUPLICATE NAME {0} > PASS".format(text))
        except:
            self.htmlInfo += self.htmlP.format("false", "SET DUPLICATE NAME {0} > FAIL".format(text))


    def click_OK(self):
        webElement=self.validate.get_web_element(self._OKBtnXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLICK OK > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLICK OK > FAIL")



    def Confirm_Delete(self):
        webElement=self.validate.get_web_element(self._DeleteBtnXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CONFIRM DELETE > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CONFIRM DELETE > FAIL")


    # def validate_template(self,expected):
    # return self.is_element_found_by_xpath(self._templatexpath.format(expected))

    def set_progress(self, progress):
        self.validate.get_web_element(self._ProgressRatioXpath).clear()
        webElement=self.validate.get_web_element(self._ProgressRatioXpath)
        try:
            webElement.send_keys(progress)
            self.htmlInfo += self.htmlP.format("true", "BOARD PROGRESS RATIO:{0} > PASS".format(progress))
        except:
            self.htmlInfo += self.htmlP.format("false", "BOARD PROGRESS RATIO:{0} > FAIL".format(progress))


    def click_progress_ratio(self, order):
        actionChains = ActionChains(self.webDriver)
        progress = self.validate.get_web_element(self._progressRatioBtnXpath.format(order))
        actionChains.move_to_element(progress)
        actionChains.double_click(progress).perform()

    def Validate_Approved_status(self, order, status):
        if (status == "disapproved"):
            webElement=self.validate.is_element_found_by_xpath((self._ApprovedIconXpath).format(order))
            if webElement :
                self.htmlInfo += self.htmlP.format("true", "APPROVAL STATUS:{0} > PASS".format(status))
            else:
                self.htmlInfo += self.htmlP.format("false", "APPROVAL STATUS:{0} > FAIL".format(status))

        else:
            webElement2=self.validate.is_element_found_by_xpath((self._CheckedStatusValidationXpath).format(order))
            if webElement2:
                self.htmlInfo += self.htmlP.format("true", "APPROVAL STATUS:{0} > PASS".format(status))
            else:
                self.htmlInfo += self.htmlP.format("false", "APPROVAL STATUS:{0} > FAIL".format(status))

    def click_addAttributes(self):
        webElement=self.validate.get_web_element(self._addAttributesBtnXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLICK ADD ATTRIBUTE > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLICK ADD ATTRIBUTE > FAIL")



    def validate_boardName_Edit(self, name):
        if self.validate.is_element_found_by_xpath(self._BoardNameXpath.format(name)):
            self.htmlInfo += self.htmlP.format("true", "Board name is {0} > PASS".format(name))
        else:
            self.htmlInfo += self.htmlP.format("false", "Board name is {0} > FAIL".format(name))


    def set_attributesName(self, name):
        webElement=self.validate.get_web_element(self._AttributeNameXpath)
        try:
            webElement.send_keys(name)
            self.htmlInfo += self.htmlP.format("true", "SET ATTRIBUTE NAME {0} > PASS".format(name))
        except:
            self.htmlInfo += self.htmlP.format("false", "SET ATTRIBUTE NAME {0} > FAIL".format(name))


    def select_attribures(self, option, value):
        self.validate.get_web_element(self._SelectAttributeDDLXpath).click()
        webElement=self.validate.get_web_element(self._SeletAttributeOptionsXpath.format(option))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "SELECT ATTRIBUTE : {0}> PASS".format(option))
        except:
            self.htmlInfo += self.htmlP.format("false", "SELECT ATTRIBUTE : {0} > FAIL".format(option))

        if str(option).lower() == "yes/no":
            self.validate.get_web_element(self._yesNoDDlXpath).click()
            webElement2=self.validate.get_web_element(self._yesNoOptionDDL.format(value))
            try:
                webElement2.click()
                self.htmlInfo += self.htmlP.format("true", "SELECT OPTION : {0}> PASS".format(value))

            except:
                self.htmlInfo += self.htmlP.format("false", "SELECT OPTION : {0}> FAIL".format(value))

        else:
            webElement3=self.validate.get_web_element(self._attributeValueXpath)
            try:
                webElement3.send_keys(value)
                self.htmlInfo += self.htmlP.format("true", "SELECT OPTION : {0}> PASS".format(value))
            except:
                self.htmlInfo += self.htmlP.format("false", "SELECT OPTION : {0}> FAIL".format(value))



    def delete_attribute(self):
        webElement=self.validate.get_web_element(self._deleteAttributeXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLICK DELETE ATTRIBUTE> PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLICK DELETE ATTRIBUTE> FAIL")


    # def set_attributeValue(self,value):
    # type=self.validate.get_web_element(self.)
    # self.validate.get_web_element(self._attributeValueXpath).send_keys(value)

    def click_Task_Details(self, order):
        _TaskXpath="//tr[{0}]/td[1]/div[1]"
        element_to_hover_over = self.validate.get_web_element(_TaskXpath.format(order))
        hover = ActionChains(self.webDriver).move_to_element(element_to_hover_over)
        hover.perform()
        webElement = self.validate.get_web_element(self._TaskDetailsBtnXpath.format(order))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLICK TASK DETAILS> PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLICK TASK DETAILS> FAIL")



    def delete_Task(self,order):
        _TaskXpath = "//tr[{0}]/td[1]/div[1]"
        element_to_hover_over = self.validate.get_web_element(_TaskXpath.format(order))
        hover = ActionChains(self.webDriver).move_to_element(element_to_hover_over)
        hover.perform()
        webElement=self.validate.get_web_element(self._deleteTaskBtnXpath.format(order))
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "DELETE TASK > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "DELETE TASK> FAIL")



    def commentINdetails(self):
        webElement=self.validate.get_web_element(self._CommentBtnXpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "GO TO COMMENT TAB> PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "GO TO COMMENT TAB> FAIL")


    def Set_Comment(self, type ,comment):
        if str(type).lower().__contains__("new"):
            webElement=self.validate.get_web_element(self._SetCommentXpath)
        elif str(type).lower().__contains__("edit"):
            self.validate.get_web_element("//textarea[@placeholder='Write Note']").clear()
            webElement=self.validate.get_web_element("//textarea[@placeholder='Write Note']")
        try:
            webElement.send_keys(comment)
            self.htmlInfo += self.htmlP.format("true", "SET COMMENT: {0}> PASS".format(comment))
        except:
            self.htmlInfo += self.htmlP.format("false", "SET COMMENT: {0}> FAIL".format(comment))
    def send_comment(self):
        webElement2=self.validate.get_web_element(self._sendcommentBtnXpath)
        try:
            webElement2.click()
            self.htmlInfo += self.htmlP.format("true", "CLICK SEND COMMENT> PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLICK SEND COMMENT> FAIL")

    def save_comment(self):
        webElement=self.validate.get_web_element("//button[@class='task-details-save']")
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLICK SAVE COMMENT> PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLICK SAVE COMMENT> FAIL")


    def EditComment(self, order,option):
        self.validate.get_web_element(self._EditCommentBtnXpath.format(order)).click()
        if str(option).lower().__contains__("delete"):
            webElement1=self.validate.get_web_element(self._DeleteCommentEditDDLXpath)
            try:
                webElement1.click()
                self.htmlInfo += self.htmlP.format("true", "CLICK DELETE COMMENT> PASS")
            except:
                self.htmlInfo += self.htmlP.format("false", "CLICK DELETE COMMENT> FAIL")

        else:
            webElement2=self.validate.get_web_element(self._EditCommentOptionXpath)
            try:
                webElement2.click()
                self.htmlInfo += self.htmlP.format("true", "CLICK EDIT COMMENT> PASS")
            except:
                self.htmlInfo += self.htmlP.format("false", "CLICK EDIT COMMENT> FAIL")


    def validate_comments(self,comment):
        webElement=self.validate.is_element_found_by_xpath(self._CommentXpath.format(comment))
        if webElement:
            self.htmlInfo += self.htmlP.format("true", "COMMENT: {0} ->APPEARED > PASS  ".format(comment))
        else:
            self.htmlInfo += self.htmlP.format("false", "COMMENT: {0} ->DIDN'T APPEAR > FAIL  ".format(comment))


    def activityindetails(self):
        webElement=self.validate.get_web_element(self._DetailsActivityLogxpath)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "GO TO ACTIVITY LOG TAB> PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "GO TO ACTIVITY LOG TAB> FAIL")


    def activity_logMembers(self, option):
        self.validate.get_web_element(self._activitymemberfilter).click()

        try:
            self.validate.get_web_element(self._activitymemberoptionfilter.format(option)).click()
            self.htmlInfo += self.htmlP.format("true", "FILTER MEMBERS :{0}> PASS".format(option))
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER MEMBERS :{0}> FAIL".format(option))

    def activity_logAction(self, option):
        self.validate.get_web_element(self._activityactionfilter).click()
        try:
            self.validate.get_web_element(self._activityactionoptionfilter.format(option)).click()
            self.htmlInfo += self.htmlP.format("true", "FILTER ACTION :{0}> PASS".format(option))
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER ACTION :{0}> FAIL".format(option))

    def bookmarkfilter(self, option):
        if str(option).lower() == "bookmark":
            try:
                self.validate.get_web_element(self._bookmarkedFilterXpath).click()
                self.htmlInfo += self.htmlP.format("true", "FILTER BOOKMARKED TASKS :{0}> PASS".format(option))
            except:
                self.htmlInfo += self.htmlP.format("false", "FILTER BOOKMARKED TASKS :{0}> FAIL".format(option))

        else:
            try :
                self.validate.get_web_element(self._notbookmarkedfilterxpath).click()
                self.htmlInfo += self.htmlP.format("true", "FILTER NOT BOOKMARKED TASKS :{0}> PASS".format(option))
            except:
                self.htmlInfo += self.htmlP.format("false", "FILTER NOT BOOKMARKED TASKS :{0}> FAIL".format(option))

    def activitylogfromdate(self, fdate):
        try:
            self.validate.get_web_element(self._activitylogfromdatefilter).send_keys(fdate)
            self.htmlInfo += self.htmlP.format("true", "FILTER TASKS FROM DATE :{0}> PASS".format(fdate))
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER TASKS FROM DATE :{0}> FAIL".format(fdate))

    def activiylogtodate(self, todate):
        try:
            self.validate.get_web_element(self._activitylogtodatefilter).send_keys(todate)
            self.htmlInfo += self.htmlP.format("true", "FILTER TASKS TO DATE :{0}> PASS".format(todate))
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER TASKS TO DATE :{0}> FAIL".format(todate))


    def gantview(self, view):
        try:
            if str(view).lower() == "week":
                self.validate.get_web_element(self._gantweekview).click()
            elif str(view).lower() == "day":
                self.validate.get_web_element(self._gantdayview).click()
            elif str(view).lower() == "month":
                self.validate.get_web_element(self._gantmonthview).click()
            else:
                self.validate.get_web_element(self._gantQuarterview).click()
            self.htmlInfo += self.htmlP.format("true", "VIEW GANT CHART :{0} VIEW> PASS".format(view))
        except:
            self.htmlInfo += self.htmlP.format("false", "VIEW GANT CHART :{0} VIEW> FAIL".format(view))




    def click_gantview(self):
        try:
            self.validate.get_web_element(self._clickganttab).click()
            self.htmlInfo += self.htmlP.format("true", "GO TO GANT CHART > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "GO TO GANT CHART > FAIL")


    def expandgant(self, order):
        self.validate.get_web_element(self._expandgant.format(order))

    def viewtaskingant(self, task):
        try:
            self.validate.get_web_element(self._viewganttask.format(task)).click()
            self.htmlInfo += self.htmlP.format("true", "VIEW TASK DETAILS > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "VIEW TASK DETAILS > FAIL")

    def click_Calendar_view(self):
        try:
            self.validate.get_web_element(self._CalendarViewXpath).click()
            self.htmlInfo += self.htmlP.format("true", "GO TO CALENDAR VIEW > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "GO TO CALENDAR VIEW > FAIL")


    def opentasklist_DayinCalendar(self, date):
        try:
            self.validate.get_web_element(self._DayinCalendar.format(date)).click()
            self.htmlInfo += self.htmlP.format("true", "OPEN TASKS LIST IN {0} > PASS".format(date))
        except:
            self.htmlInfo += self.htmlP.format("false", "OPEN TASKS LIST IN {0} > FAIL".format(date))

    def open_Taskincalendar(self,name):
        try:
            self.validate.get_web_element(self._TaskXpath.format(name)).click()
            self.htmlInfo += self.htmlP.format("true", "OPEN TASK {0} > PASS".format(name))
        except:
            self.htmlInfo += self.htmlP.format("false", "OPEN TASK {0} > FAIL".format(name))


    def CalendarView(self, view):
        try:
            if str(view).lower() == "week":
                self.validate.get_web_element(self._calendarWeekViewXpath).click()
            elif str(view).lower() == "day":
                self.validate.get_web_element(self._calendarDayViewXpath).click()
            elif str(view).lower() == "month":
                self.validate.get_web_element(self._calendarMonthViewXpath).click()
            self.htmlInfo += self.htmlP.format("true", "OPEN CALENDAR IN {0} VIEW > PASS".format(view))
        except:
            self.htmlInfo += self.htmlP.format("false", "OPEN CALENDAR IN {0} VIEW > FAIL".format(view))


    def Move_RightLeft(self,dir):
        try:
            if str(dir).lower().__contains__("right"):
                self.validate.get_web_element("//mat-icon[contains(text(),'keyboard_arrow_right')]").click()
            elif str(dir).lower().__contains__("left"):
                self.validate.get_web_element("//mat-icon[contains(text(),'keyboard_arrow_left')]").click()
            else:
                print("the button is not recognized")
            self.htmlInfo += self.htmlP.format("true", "MOVE TO THE {0} > PASS".format(dir))
        except:
            self.htmlInfo += self.htmlP.format("false", "MOVE TO THE {0} > FAIL".format(dir))

    def click_recurringThumb(self):
        webElement=self.validate.get_web_element(self._taskMakingRecurringThumb)
        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "CLICK RECURRING THUMB BUTTON> PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLICK RECURRING THUMB BUTTON > FAIL")


    def set_recurringOccurrences(self,occ):
        webElement=self.validate.get_web_element(self._RecurringOccurrences)
        try:
            webElement.send_keys(occ)
            self.htmlInfo += self.htmlP.format("true", "SET RECURRING OCCURRENCES TO {0}> PASS".format(occ))
        except:
            self.htmlInfo += self.htmlP.format("false", "SET RECURRING OCCURRENCES TO {0}> FAIL".format(occ))



    def set_RecurringStartdate(self,date):
        webElement= self.validate.get_web_element(self._RecurringStartDate)
        try:
            webElement.send_keys(date)
            self.htmlInfo += self.htmlP.format("true", "SET RECURRING START DATE:{0}> PASS".format(date))
        except:
            self.htmlInfo += self.htmlP.format("true", "SET RECURRING START DATE: {0}> PASS".format(date))

    def set_RecurringEnddate(self,date):
        webElement= self.validate.get_web_element(self._RecurringEndDate)
        try:
            webElement.send_keys(date)
            self.htmlInfo += self.htmlP.format("true", "SET RECURRING END DATE:{0}> PASS".format(date))
        except:
            self.htmlInfo += self.htmlP.format("true", "SET RECURRING END DATE: {0}> PASS".format(date))

    def set_repeatType(self,option):
        self.validate.get_web_element(self._repeateType).click()
        webElement=self.validate.get_web_element(self._RepeatTyeOptionXpath.format(option))

        try:
            webElement.click()
            self.htmlInfo += self.htmlP.format("true", "SET REPEAT TYPE TO : {0}> PASS".format(option))

        except:
            self.htmlInfo += self.htmlP.format("false", "SET REPEAT TYPE TO : {0}> FAIL".format(option))


    def boardsettings(self):
        self.validate.get_web_element(self._BoardSettingsBtnXpath).click()

    def click_filter(self):
        try :
            self.validate.get_web_element(self._filterBtn).click()
            self.htmlInfo += self.htmlP.format("true", "CLICK FILTER > PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "CLICK FILTER > FAIL")


    def filter_Prioruty(self, name):
        self.validate.get_web_element(self._filterPriorityDDLXpath).click()
        try:
            self.validate.get_web_element((self._PriorityOptionXpath).format(name)).click()
            self.htmlInfo += self.htmlP.format("true", "FILTER TASKS WITH {0} PRIORITY > PASS".format(name))
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER TASKS WITH {0} PRIORITY > FAIL".format(name))


    def filter_Members(self, order):
        self.validate.get_web_element(self._filterMemberDDLXpath).click()
        try:
            self.validate.get_web_element((self._MemberOptionXpath).format(order)).click()
            self.htmlInfo += self.htmlP.format("true", "FILTER TASKS MEMBERS> PASS")
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER TASKS MEMBERS> FAIL")

    def set_startdate(self, start):
        try:
            self.validate.get_web_element(self._filterStartDateXpath).send_keys(start)
            self.htmlInfo += self.htmlP.format("true", "FILTER TASKS START FROM : {0}> PASS".format(start))
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER TASKS START FROM : {0}> FAIL".format(start))

    def set_Enddate(self, end):
        try:
            self.validate.get_web_element(self._filterEndDateXpath).send_keys(end)
            self.htmlInfo += self.htmlP.format("true", "FILTER TASKS END FROM : {0}> PASS".format(end))
        except:
            self.htmlInfo += self.htmlP.format("false", "FILTER TASKS END FROM : {0}> FAIL".format(end))

    def validate_boardsactivitylogs(self):
        if self.validate.is_element_found_by_xpath(self._activitylogrows):
            self.htmlInfo += self.htmlP.format("true", "ACTIVITY LOG APPEARED> PASS")
        else:
            self.htmlInfo += self.htmlP.format("false", "ACTIVITY LOG APPEARED> FAIL")



    def validate_tasksListInCalendar(self):
        webElement= self.validate.is_element_found_by_xpath(self._tasksListInCalendar)
        if webElement :
            print("Tasks list Displayed")
            self.htmlInfo += self.htmlP.format("true", "TASKS LIST DISPLAYED> PASS")

        else:
            self.htmlInfo += self.htmlP.format("false", "TASKS LIST DISPLAYED> FAIL")


    def validate_TaskDetails(self):
        WebElement=self.validate.is_element_found_by_xpath("//app-task-details[1]")
        if WebElement:
            self.htmlInfo += self.htmlP.format("true", "TASK DETAILS OPENED> PASS")
        else:
            self.htmlInfo += self.htmlP.format("false", "TASK DETAILS OPENED> FAIL")

    def takeScreenshot(self, name):
        self.validate.takeScreenshot(name)

    def copycsv(self):
        self.validate.get_web_element(self._addfilexpath).click()
        time.sleep(4)
        pyautogui.click()
        pyautogui.write(r'C:\Users\Hanoof.Alqadeh\Downloads')
        pyautogui.hotkey('enter')
        x, y = pyautogui.locateCenterOnScreen('filename.png', confidence=0.7)
        pyautogui.click(x, y)
        pyautogui.write('Illiteracy rate by region')
        pyautogui.hotkey('enter')
        # pyautogui.write('AdaaAutomation')
        # pyautogui.hotkey('enter')
        # pyautogui.write('111704')
        # pyautogui.hotkey('enter')

        # pyautogui.doubleClick(x, y)
    # self.webDriver.find_elements_by_css_selector("input[type='files']").SendKeys(r"C:\Users\Hanoof.Alqadeh\Desktop\AdaaAutomation")
