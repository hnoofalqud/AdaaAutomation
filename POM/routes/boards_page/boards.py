import time

from selenium.webdriver import ActionChains
from POM.routes.routes import Routes


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

    #FILTER
    _filterBtn = "//span[contains(@class,'icon-filter')]"
    _filterMemberDDLXpath="//ng-select[1]/div[1]/div[1]/div[2]"
    _filterPriorityDDLXpath="//div[3]/mat-select[1]/div[1]/div[1]"
    _filterStartDateXpath="//input[contains(@formcontrolname,'startDataSearch')]"
    _filterEndDateXpath="//input[contains(@formcontrolname,'endDataSearch')]"
    _MemberOptionXpath="//ng-dropdown-panel[1]/div[1]/div[2]/div[{0}]" #BY ORDER
    _PriorityOptionXpath="//span[contains(text(),'{0}')]" #BY LABEL





    # --- NEW BOARD --- START
    _newBoardBtnXpath = "//div[@class='new-button ng-star-inserted']"

    # DIV 1
    _boardNameXpath = "//input[contains(@placeholder,'Board Name')]"
    _boardCodeXpath = "//input[contains(@placeholder,'Code')]"

    # DIV 2
    _boardDepartmentsDropDownXpath = "//div[2]/div[3]//input"
    _boardDepartmentsDropDownOptionByOrderXpath = "(//div[@class='ng-dropdown-panel-items scroll-host']//*[contains(text(),' ')])[{0}]"

    _boardSupervisorDropDownXpath = "//div[2]/div[4]//input"
    _boardSupervisorDropDownOptionByOrderXpath = "(//div[@class='ng-dropdown-panel-items scroll-host']//*[contains(text(),' ')])[{0}]"

    _boardStatusDropDownXpath = "//div[@class='col-md-4 margin-zero-form']//mat-form-field "  #//div[@class='mat-select-value']
    _boardStatusDropDownOptionXpath = "(//mat-option//span[@class='mat-option-text'])[{0}]"  # OPTION ORDER

    _boardAppColorXpath = "//app-color-control"
    _boardAppColorOptionXpath = "(//div[contains(@class,'color')]//div[{0}]" #BY ORDER #//div[@class='product-color ng-star-inserted'][{0i}]

    # DIV 3 (Resource Pool)
    _boardDepartmentsResourcePoolDropDownXpath = "//div[2]/ng-select//input"
    _boardDepartmentsResourcePoolDropDownOptionXpath = "(//div[3]/div[2]//div[contains(@class,'ng-option')])[{0}]"

    _membersResourcePoolDropDownXpath = "//div[3]/div[3]//div[contains(@class,'mat-select-value')] "
    _membersResourcePoolDropDownOptionXpath = "//mat-optgroup[{0}]/mat-option[{1}]/span"

    #DIV 4(copy from)

    _copyfromBtnXpath="//mat-slide-toggle[@formcontrolname='copyFromToggle']"
    _copyfromoptionxpath="//div[text()='{0}']"
    _firstDDLXpath="//div[1]/div[6]/div[1]/ng-select"
    _FirstDDLOptionXpath="//ng-dropdown-panel[1]//div[2]/div[{0}]"  #BY ORDER
    _copyTaskstartDate="//input[@formcontrolname='StartDate']"

    # DIV 6 (BOARD DESCRIPTION)
    _boardDescriptionXpath = "//div[6]/div//div//textarea"

    #DIV 7 (BOARD ATTRIBUTES)
    _addAttributesBtnXpath="//div[1]/div[7]//mat-icon[1]"
    _AttributeNameXpath="//input[@placeholder='Attribute Name']"
    _SelectAttributeDDLXpath="//mat-select[@formcontrolname='TypeId']"
    _SeletAttributeOptionsXpath="//span[contains(text(),'{0}')]"  #BY LABEL
    _attributeValueXpath="//input[@formcontrolname='value']"
    _yesNoDDlXpath="//mat-select[@formcontrolname='value']"
    _yesNoOptionDDL="//span[text()='{0}']"
    _deleteAttributeXpath="//mat-icon[contains(text(),'delete')]"
    # SAVE (SUBMIT) BUTTON
    _saveBoardBtnXpath = "//button[@type='submit']"

    # CLOSE (EXIT) BUTTON
    _closeBoardBtnXpath = "//span[contains(text(),'close')]"

    # --- NEW BOARD --- END

    # ----------------------

    # --- NEW TASK --- START
    _newTaskBtnXpath = "//*[contains(text(),'Tasks')]//*"
    _newchildtaskBtnXpath="//tr[{0}]/td[1]/div[1]/div[3]/span[1]"

    # DIV 1
    _taskNameXpath = "//app-task-details//input[contains(@placeholder,'Name')]"
    _taskDescriptionXpath = "//app-task-details//textarea[contains(@placeholder,'Description')]"

    # DIV 2
    _taskStartDateXpath = "//app-task-details//input[contains(@formcontrolname,'startDate')]"
    _taskEndDateXpath = "//app-task-details//input[contains(@formcontrolname,'endDate')]"
    _taskDurationXpath = "//app-task-details//input[contains(@placeholder,'Duration')]"

    # DIV 3
    _taskMakingRecurringThumb = "//app-task-details//div[contains(@class,'mat-slide-toggle-thumb')]"

    # DIV 4
    _taskProgressType = "//div[6]/div[1]//mat-select[1]/div[1]"
    _taskProgressTypeOptionByOrder = "(//mat-option//span)[{0}]"  # ORDER
    _taskProgressRatio = "//input[contains(@placeholder,'Progress ratio')]"
    _taskPriorityDDLXpath = "//div[6]/div[3]//mat-select"
    _taskPriorityOptionXpath="//mat-option[{0}]/span[1]"  #ORDER
    _taskPriorittyDetailsDDLXpath="//mat-select[@formcontrolname='taskStatusDetailId']"
    _taskPriorityDetailsOptionXpath="//mat-option[{0}]/span[1]"
    _DependancyDDLXpath="//span[@class='mat-select-placeholder ng-tns-c11-1232 ng-star-inserted']"
    _DependancyOptionXpath="//mat-option[{0}]/span[1]"
    # DIV 5

    # DIV 7
    _taskDepartmentsDropDownXpath = "(//div[contains(@class,'ng-input')]//input)[1]"   #"(//div[8]//input)[1]"
    _taskDepartmentsDropDownOptionXpath = "(//div[@class='ng-dropdown-panel-items scroll-host']//*[contains(text(),' ')])[{0}]"

    _taskMembersDropDownXpath ="(//div[contains(@class,'ng-input')]//input)[2]"    #"(//div[8]//input)[2]"
    _taskMembersDropDownOptionXpath = "(//div[@class='ng-dropdown-panel-items scroll-host']//*[contains(text(),' ')])[{0}]"

    # SAVE (SUBMIT) BUTTON
    _saveTaskBtnXpath = "//button[contains(text(),'Save')]"
    #CANCEL BUTTON
    _cancelTaskBtnXpath="//button[contains(text(),'Cancel')]"

    # --- NEW TASK --- END
    _tasksListXpath= "//div[@class='task-name'][1]"
    _BoardDDLOptionXpath= "//div[contains(@class,'mat-menu-cont')]//p[contains(text(),'{0}')]"  #by label
    _templateXpath="//p[@title='{0}']"
    _BoardStatusDDLXpath="//mat-select[1]/div[1]/div[1]"
    _BoardStatusDDLOptionXpath="//div[contains(@class,'panel')]//span[contains(text(),'{0}')]" #by label
    _BoardDDLBtnXpath = "//div/div[contains(@class,'project-name')]"
    _DuplicateNameXpath="//input[@formcontrolname='name']" #"//mat-label[@class='ng-star-inserted']"
    _OKBtnXpath="//button[contains(@class,'save-button')]"
    _ConvertToNameXpath="//input[@formcontrolname='name']"
    _DeleteBtnXpath="//button[contains(@class,'save-button')]"
    _progressRatioBtnXpath="//tr[{0}]/td[8]/div[1]" #By ORDER
    _ProgressRatioXpath= "//input[contains(@placeholder,'Progress ratio')]"
    _ApprovedIconXpath="//tbody/tr[{0}]/td[5]/div[1]/mat-icon[1]"
    _ClosedStatusValidation= "//tr[{0}]//mat-icon[contains(text(),'close')]"
    _CheckedStatusValidationXpath="//tr[{0}]//mat-icon[contains(text(),'check')]"
    # ----------------------

    _TaskDetailsBtnXpath="//tr[{0}]//a[1]" #By order
    _CommentBtnXpath="//span[contains(text(),'Comments')]"
    _SetCommentXpath="//textarea[@formcontrolname='noteTxt']"
    _sendcommentBtnXpath= "//button[@class='sent-button']"
    _EditCommentBtnXpath="//span[@class='icon-comment-arrow time-arrow mat-menu-trigger']"
    _DeleteCommentEditDDLXpath= "//p[@class='edit-profile' and text()=' Delete']"
    _EditCommentOptionXpath="//p[@class='edit-profile' and text()='Edit Comment']"

    _BoardSettingsBtnXpath="//div[5]/div[2]/span[3]"
    _DetailsActivityLogxpath="//span[contains(text(),'Activity Log')]"

    #FILTER ACTIVITY LOGS

    _activitymemberfilter="//div[contains(text(),'Members')]"
    _activitymemberoptionfilter="//div[2]/div[{0}]" #by order    #"//span[text()=' user user']" #by label
    _activityactionfilter="//div[contains(text(),'Action')]"
    _activityactionoptionfilter="//ng-dropdown-panel[1]/div[1]/div[2]/div[{0}]" #by order
    _bookmarkedFilterXpath="//button[@class='bookmark-button bookmark-button-left-radius']"
    _notbookmarkedfilterxpath="//button[@class='bookmark-button bookmark-button-right-radius']"
    _activitylogfromdatefilter="//input[@formcontrolname='from']"
    _activitylogtodatefilter="//input[@formcontrolname='to']"
    _activitylogrows="//app-log-page[1]//table[1]/tbody/tr[1]"


    #calendar view
    _CalendarViewXpath="//span[text()='Calendar']"
    _calendarWeekViewXpath= "//div[text()=' Week ']"
    _calendarDayViewXpath="//div[text()=' Day ']"
    _calendarMonthViewXpath="//div[text()=' Month ']"

    #Gant View
    _gantweekview="//span[text()='Week']"
    _gantdayview="//span[text()='Day']"
    _gantQuarterview="//span[text()='Quarter']"
    _gantmonthview="//span[text()='Month']"
    _viewganttask="//table/tbody/tr[{0}]/td[2]/div[1]"
    _clickganttab="//span[text()='Gant']"
    _expandgant="//div[2]//tr[1]/td[2]//span[1]"

    def __init__(self, driver):
        Routes.__init__(self, driver)
        self.htmlInfo += "<h3> BOARDS PAGE </h3>"
        self.htmlP = "<p class='board validation {0}'> {1} </p>"

    def get_number_of_projects(self):
        return len(self.webDriver.find_elements_by_css_selector(self._allProjectsCssSelector))

    def click_project(self, projectName):
       if self.validate.get_web_element(self._projectByNameXpath.format(projectName)).click():
           self.htmlInfo += self.htmlP.format("true","open {0}".format(projectName))
       else :
           self.htmlInfo += self.htmlP.format("false", "open {0}".format(projectName))


    def search_project(self, searchField):
        self.validate.get_web_element(self._searchProjectsXpath).clear()
        self.validate.get_web_element(self._searchProjectsXpath).send_keys(searchField)


    # NEW BOARD

    def get_new_board_btn(self, notes=""):
        self.htmlInfo += "<hr class='board validation'>"
        self.htmlInfo += self.htmlP.format("", "NEW BOARD {0}".format(notes))
        return self.validate.get_web_element(self._newBoardBtnXpath)

    def set_board_name(self, name):
        if self.validate.get_web_element(self._boardNameXpath).send_keys(name):
            self.htmlInfo += self.htmlP.format("true", "BOARD NAME: {0}".format(name))
        else:
            self.htmlInfo += self.htmlP.format("false", "BOARD NAME: {0}".format(name))


    def set_board_code(self, code):
        self.validate.get_web_element(self._boardCodeXpath).send_keys(code)
        self.htmlInfo += self.htmlP.format("", "BOARD CODE: {0}".format(code))

    def set_board_department_drop_down(self, option):
        self.validate.get_web_element(self._boardDepartmentsDropDownXpath).click()
        webElement = self.validate.get_web_element(self._boardDepartmentsDropDownOptionByOrderXpath.format(option))
        webElement.click()
        self.htmlInfo += self.htmlP.format("", "BOARD DEPARTMENT: OPTION#{0} - {1}".format(option, "{0}"))

    def set_board_supervisor_drop_down(self, option):
        self.validate.get_web_element(self._boardSupervisorDropDownXpath).click()
        webElement = self.validate.get_web_element(self._boardSupervisorDropDownOptionByOrderXpath.format(option))
        webElement.click()
        self.htmlInfo = self.htmlInfo.format("BOARD SUPERVISOR: OPTION#{0}".format(option))

    def set_Newboard_status(self, option):
        self.validate.get_web_element(self._boardStatusDropDownXpath).click()
        self.validate.get_web_element(self._boardStatusDropDownOptionXpath.format(option)).click()
        self.htmlInfo += self.htmlP.format("","set board status to {0}".format(option))
    def set_board_color(self, option):
        self.validate.get_web_element(self._boardAppColorXpath).click()
        self.validate.get_web_element(self._boardAppColorOptionXpath.format(option)).click()
        self.htmlInfo += self.htmlP.format("","BOARD COLOR {0}".format(option))
    def set_board_departments_resource_pool(self, option):
        # [1,2,3]
        for optionItem in option:
            self.validate.get_web_element(self._boardDepartmentsResourcePoolDropDownXpath).click()
            self.validate.get_web_element(self._boardDepartmentsResourcePoolDropDownOptionXpath.format(optionItem)).click()
            self.htmlInfo += self.htmlP.format("", "BOARD DEPARTMENT RESOURCE POOL:{0}".format(optionItem))

    def set_board_members_resource_pool(self, group, option):
        self.validate.get_web_element(self._membersResourcePoolDropDownXpath).click()
        for groupItem, optionItem in zip(group, option):
            currentOption = self.validate.get_web_element(self._membersResourcePoolDropDownOptionXpath.format(groupItem, optionItem))
            currentOption.click()

        # TO CLICK OUTSIDE
        size = currentOption.size
        x = (int(size['width']) * 2)
        ActionChains(self.webDriver).move_to_element(currentOption).move_by_offset(-x, 0).click().perform()

        # self.validate.get_web_element("//body[1]/div[2]/div").click()  # CLOSE DIALOG

    def set_board_description(self, text):
        self.validate.get_web_element(self._boardDescriptionXpath).send_keys(text)
        self.htmlInfo += self.htmlP.format("","BOARD DESCRIPTION {0}".format(text))


    def get_save_new_board_btn(self):
        imgHTML = self.validate.takeScreenshot(name="save_board")
        self.htmlInfo += imgHTML

        return self.validate.get_web_element(self._saveBoardBtnXpath)

    def get_close_new_board_btn(self):
        self.htmlInfo += self.htmlP.format("", "CLOSE NEW BOARD")
        return self.validate.get_web_element(self._closeBoardBtnXpath)




    def CopyfromBtn(self,option):
        self.validate.get_web_element(self._copyfromBtnXpath).click()
        self.validate.get_web_element(self._copyfromoptionxpath.format(option)).click()

    def copyfromDDL(self,option,date):
        self.validate.get_web_element(self._firstDDLXpath).click()
        self.validate.get_web_element(self._FirstDDLOptionXpath.format(option)).click()
        self.validate.get_web_element(self._copyTaskstartDate).send_keys(date)
    # --------------------------------

    def get_new_task_btn(self):
        self.htmlInfo += "<hr class='board validation'>"
        time.sleep(2)
        return self.validate.get_web_element(self._newTaskBtnXpath)

    def new_childTask_btn(self,order):
        self.validate.get_web_element(self._newchildtaskBtnXpath.format(order)).click()


    def set_task_name(self, name):
        self.validate.get_web_element(self._taskNameXpath).send_keys(name)
        self.htmlInfo += self.htmlP.format("", "NEW TASK -> TASK NAME: {0} ".format(name))

    def set_task_description(self, description):
        self.validate.get_web_element(self._taskDescriptionXpath).send_keys(description)
        self.htmlInfo += self.htmlP.format("", "TASK DESCRIPTION: {0} ".format(description))

    def set_task_start_end_date(self, startDate, endDate):
        self.validate.get_web_element(self._taskEndDateXpath).send_keys(endDate)
        self.validate.get_web_element(self._taskStartDateXpath).send_keys(startDate)
        self.htmlInfo += self.htmlP.format("","START DATE: {0} - END DATE: {1} ".format(startDate, endDate, ))

    def set_task_duration(self, duration):
        self.validate.get_web_element(self._taskDurationXpath).send_keys(duration)
        self.htmlInfo = self.htmlInfo.format("DURATION: {0}".format(duration))

    def set_task_departments(self, options):
        for optionItem in options:
            self.validate.get_web_element(self._taskDepartmentsDropDownXpath).click()
            self.validate.get_web_element(self._taskDepartmentsDropDownOptionXpath.format(optionItem)).click()
        self.htmlInfo = self.htmlP.format("", "TASK DEPARTMENTS: {0}".format(str(options)))

    def set_task_members(self, options):
        for optionItem in options:
            self.validate.get_web_element(self._taskMembersDropDownXpath).click()
            self.validate.get_web_element(self._taskMembersDropDownOptionXpath.format(optionItem)).click()
        self.htmlInfo = self.htmlInfo.format("TASK MEMBERS: {0}".format(options))

    def set_task_progress(self,Option):
        self.validate.get_web_element(self._taskProgressType).click()
        self.validate.get_web_element(self. _taskProgressTypeOptionByOrder.format(Option)).click()

    def set_task_progress_ratio(self,ratio):
        self.validate.get_web_element(self._taskProgressRatio).send_keys(ratio)
        self.htmlInfo += self.htmlP.format("","TASK PROGRESS RATIO {0}".format(ratio))
    def set_task_priority(self,priority):
        self.validate.get_web_element(self._taskPriorityDDLXpath).click()
        self.validate.get_web_element(self._taskPriorityOptionXpath.format(priority)).click()
        self.htmlInfo += self.htmlP.format("","TASK PRIORITY {0}".format(priority))

    def set_task_priority_details(self,option):
        self.validate.get_web_element(self._taskPriorittyDetailsDDLXpath).click()
        self.validate.get_web_element(self._taskPriorityDetailsOptionXpath.format(option)).click()
        self.htmlInfo += self.htmlP.format("","PRIORITY DETAILS {0}".format(option))

    def set_depndancy(self,option):
        self.validate.get_web_element(self._DependancyDDLXpath).click()
        self.validate.get_web_element(self._DependancyOptionXpath.format(option)).click()
        self.htmlInfo += self.htmlP.format("", "TASK DEPNDANCY {0}".format(option))

    def save_new_task(self):
        self.validate.get_web_element(self._saveTaskBtnXpath).click()
        self.htmlInfo += self.htmlP.format("", "SAVE TASK")
    def cancel_task(self):
        self.validate.get_web_element(self._cancelTaskBtnXpath).click()
        self.htmlInfo += self.htmlP.format("","CANCEL TASK")
    def Board_DDL(self,option):
        self.validate.get_web_element(self._BoardDDLBtnXpath).click()
        self.validate.get_web_element(self._BoardDDLOptionXpath.format(option)).click()
        self.htmlInfo += self.htmlP.format("", "BOARD {0}".format(option))



    def set_Convert_To_name(self, text):
        self.validate.get_web_element(self._ConvertToNameXpath).send_keys(text)
        self.htmlInfo += self.htmlP.format("","CONVERT TO TEMPLATE {0}".format(text))

    def validate_Tasks_number (self):
       if self.is_element_found_by_xpath(self._taskslistXpath):
           print("tasks list appeared")
       else:
           print("nothing appeared")


    def set_Board_status(self,status):
        self.validate.get_web_element(self._BoardStatusDDLXpath).click()
        self.validate.get_web_element(self._BoardStatusDDLOptionXpath.format(status)).click()
        self.htmlInfo += self.htmlP.format("","BOARD STATUS {0}".format(status))

    def set_Duplicate_name(self,text):
        self.htmlInfo += self.htmlP.format("","DUPLICATE NAME {0}".format(text))
        self.validate.get_web_element(self._DuplicateNameXpath).send_keys(text)

    def click_OK(self):
        self.validate.get_web_element(self._OKBtnXpath).click()
        self.htmlInfo += self.htmlP.format("","CLICK OK ")

    def Confirm_Delete(self):
        self.validate.get_web_element(self._DeleteBtnXpath).click()
        self.htmlInfo += self.htmlP.format("","CONFIRM DELETE")
    # def validate_template(self,expected):
    # return self.is_element_found_by_xpath(self._templatexpath.format(expected))

    def set_progress(self,progress):
        self.validate.get_web_element(self._ProgressRatioXpath).clear()
        self.validate.get_web_element(self._ProgressRatioXpath).send_keys(progress)
        self.htmlInfo += self.htmlP.format("", "BOARD PROGRESS RATIO:{0}".format(progress))

    def click_progress_ratio(self,order):
        actionChains = ActionChains(self.webDriver)
        progress=self.validate.get_web_element(self._progressRatioBtnXpath.format(order))
        actionChains.move_to_element(progress)
        actionChains.double_click(progress).perform()


    def Validate_Approved_status(self,order,status):
        if (status=="disapproved"):
            self.validate.is_element_found_by_xpath((self._ApprovedIconXpath).format(order))
            self.htmlInfo += self.htmlP.format("", "APPROVAL STATUS:{0}".format(status))

        else:
            self.validate.is_element_found_by_xpath((self._CheckedStatusValidationXpath).format(order))
            self.htmlInfo += self.htmlP.format("", "APPROVAL STATUS:{0}".format(status))

    def click_addAttributes(self):
        self.validate.get_web_element(self._addAttributesBtnXpath).click()



    def set_attributesName(self,name):
        self.validate.get_web_element(self._AttributeNameXpath).send_keys(name)

    def select_attribures(self,option,value):
          self.validate.get_web_element(self._SelectAttributeDDLXpath).click()
          self.validate.get_web_element(self._SeletAttributeOptionsXpath.format(option)).click()
          if str(option).lower() == "Yes/No":
              self.validate.get_web_element(self._yesNoDDlXpath).click()
              self.validate.get_web_element(self._yesNoOptionDDL.format(value)).click()
          else:
              self.validate.get_web_element(self._attributeValueXpath).send_keys(value)


    def delete_attribute(self):
        self.validate.get_web_element(self._deleteAttributeXpath).click()

   # def set_attributeValue(self,value):
        #type=self.validate.get_web_element(self.)
       # self.validate.get_web_element(self._attributeValueXpath).send_keys(value)

    def click_Task_Details(self,order):
        self.validate.get_web_element(self._TaskDetailsBtnXpath.format(order)).click()

    def commentINdetails(self):
        self.validate.get_web_element(self._CommentBtnXpath).click()

    def Set_Comment(self,comment):
        self.validate.get_web_element(self._SetCommentXpath).send_keys(comment)
        self.validate.get_web_element(self._sendcommentBtnXpath).click()

    def EditComment(self,option):
        self.validate.get_web_element(self._EditCommentBtnXpath).click()
        if str(option).lower().__contains__("delete"):
            self.validate.get_web_element(self._DeleteCommentEditDDLXpath).click()
        else:
            self.validate.get_web_element(self._EditCommentOptionXpath).click()


    def activityindetails(self):
        self.validate.get_web_element(self._DetailsActivityLogxpath).click()

    def activity_logMembers(self,option):
        self.validate.get_web_element(self._activitymemberfilter).click()
        self.validate.get_web_element(self._activitymemberoptionfilter.format(option)).click()
    def activity_logAction(self,option):
        self.validate.get_web_element(self._activityactionfilter).click()
        self.validate.get_web_element(self._activityactionoptionfilter.format(option)).click()

    def bookmarkfilter(self,option):
        if str(option).lower() == "bookmark" :
            self.validate.get_web_element(self._bookmarkedFilterXpath).click()
        else:
            self.validate.get_web_element(self._notbookmarkedfilterxpath).click()

    def activitylogfromdate(self,fdate):
        self.validate.get_web_element(self._activitylogfromdatefilter).send_keys(fdate)
    def activiylogtodate(self,todate):
        self.validate.get_web_element(self._activitylogtodatefilter).send_keys(todate)

    def gantview(self, view):
        if str(view).lower()=="week":
            self.validate.get_web_element(self._gantweekview).click()
        elif str(view).lower()=="day" :
            self.validate.get_web_element(self._gantdayview).click()
        elif str(view).lower()=="month" :
            self.validate.get_web_element(self._gantmonthview).click()
        else :
            self.validate.get_web_element(self._gantQuarterview).click()

    def click_gantview(self):
        self.validate.get_web_element(self._clickganttab).click()
    def expandgant(self,order):
        self.validate.get_web_element(self._expandgant.format(order))

    def viewtaskingant(self,task):
        self.validate.get_web_element(self._viewganttask.format(task)).click()


    def Calendar_view(self):
        self.validate.get_web_element(self._CalendarViewXpath).click()

    def boardsettings(self):
        self.validate.get_web_element(self._BoardSettingsBtnXpath).click()

    def click_filter(self):
        self.validate.get_web_element(self._filterBtn).click()

    def filter_Prioruty(self, name):
        self.validate.get_web_element(self._filterPriorityDDLXpath).click()
        self.validate.get_web_element((self._PriorityOptionXpath).format(name)).click()

    def filter_Members(self, order):
        self.validate.get_web_element(self._filterMemberDDLXpath).click()
        self.validate.get_web_element((self._MemberOptionXpath).format(order)).click()

    def set_date(self, start, end):
        self.validate.get_web_element(self._filterStartDateXpath).send_keys(start)
        self.validate.get_web_element(self._filterEndDateXpath).send_keys(end)

    def validate_boardsactivitylogs(self):
        self.validate.is_element_found_by_xpath(self._activitylogrows)





