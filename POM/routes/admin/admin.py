

from POM.routes.routes import Routes


class admin(Routes):

    _PageNameXpath = "//p[contains(text(), '{0}')]"  # BY LABEL


    #CATEGORIES_OF_USERS_PAGE

    _AddCategoryBtnXpath= "//span[@title='Add']"
    _CategoryNameXpath="//input[@placeholder='Category Name']"
    _SaveNewBtnXpath="//mat-icon[contains(text(),'save')]"
    _CancelBtnXpath="//mat-icon[contains(text(),'cancel')]"
    _SaveEditNbtnXpath="//td[1]/mat-icon[1]"
    _EditBtnXpath="//tr[{0}]/td[2]/mat-icon[1]"   #BY ORDER
    _EditNameXpath="//div[3]/input[@formcontrolname='categoryValue']"   #BY ORDER
    _LanguageBtnXpath="//div[@class='col-md-2 pl-0 pr-0']"
    _Language_choice="//div[3]/div[2]//span[contains(text(),'{0}')]"  #BY LABEL

    #JOB_TITELS

    _AddJobBtnXpath="//span[@title='Add']"
    _JobTitleXpath="//input[@placeholder='Job title']"
    _IntCodeXpath="//input[@formcontrolname='code']"
    _NewCategoryDDLXpath="//th[3]/mat-form-field[1]/div[1]"
    _DDLOptionXpath= "//mat-option[{0}]"   #BY ORDER      #"//span[contains(text(),'{0}')]" #BY LABEL
    _DefuatRoleDDLXpath="//span[contains(text(),'Default Role')]"
    _SaveNewJobXpath="//mat-icon[contains(text(),'save')]"
    _CloseNewJobXpath="//mat-icon[contains(text(),'cancel')]"
    _EditJobBtnXpath="//tr[{0}]//mat-icon[contains(text(),'edit')]"  #BY ORDER TODO : CALL IT BY INTEGRATION CODE INSTEAD OF OREDR
    _DeleteJobBtnXpath="//tr[{0}]//mat-icon[contains(text(),'delete')]"   #BY ORDER TODO : CALL IT BY INTEGRATION CODE INSTEAD OF OREDR
    _EditJobTitleXpath="//td[1]//div[3]/input[1]"
    _EditIntCodeXpath="//td[2]//div[3]/input[1]"
    _EditCategoryXpath=""
    _EditRoleXpath=""
    _SaveEditBtnXpath="//tr[{0}]/td[5]/mat-icon[1]"  #BY ORDER
    _CancelEditBtnXpath="//tr[{0}]/td[6]/mat-icon[1]" #BY ORDER

    #DEPARTMENT_HIERARCHY

    _ExportChartDDlXpath="//div[@class='mat-form-field-infix']"
    _ExportChartOptionXpath="//span[contains(text(),'{0}')]"  #BY LABEL
    _DirectionXpath="//span[contains(text(),'{0}')]"  #BY LABEL

    #NON_WORKING_DAYS
    _AddBtnXpath="//span[@title='Add']"
    _LanguageDDLXpath="//mat-select[@placeholder='language']"
    _LanguageXpath="//span[contains(text(),'{0}')]" #BY LABEL
    _TemplateNameXpath="//input[@placeholder='Template Name']"
    _ApplyOnDDLXpath="//ng-select[@formcontrolname='applyOn']"
    _ApplyonOptionsXpath="//ng-dropdown-panel[1]/div[1]/div[2]/div[{0}]"  #BY ORDER
    _CheckDaysXpath="//mat-checkbox[{0}]"  #BY ORDER
    _NewExceptionBtnXpath="//div[@class='plus-hightlight']"
    _HolidayNameXpath="// input[ @ placeholder = 'Name']"
    _StartDateXpath="//input[@formcontrolname='startDate']"
    _EndDateXpath="//input[@formcontrolname='endDate']"
    _TypeDDlXpath="//mat-select[@formcontrolname='typeId']"
    _TypeDDLOption="//span[contains(text(),'{0}')]"  #BY LABEL (CASE SENSITIVE)
    _SaveNewHolidayBtnXpath="//span[text()='Save ']"
    _EditHolidayXpath = "//td[contains(text(),'{0}')]//..//td[3]/mat-icon"  # BY LABEL
    _deleteHolidayeXpath = "//td[contains(text(),'{0}')]//..//td[4]/mat-icon"  # BY LABEL
    _Applyonholiday="//td[contains(text(),'{0}')]//..//div[@class='mat-select-value']" #BY LABEL
    _ApplyonholidayOption="//div[3]/div[2]//mat-option[{0}]/span[1]" #BY ORDER

    #delete

    #COMPLETION_STATUS

    _newcCompletionStatusXpath="//span[@class='add-icon-task icon-blue-add']"
    _CompletionStatusnameXpath="//input[@placeholder='Category Name']"
    _CancelNewCompletionXpath="//mat-icon[contains(text(),'cancel')]"
    _SaveNewCompletionXpath="//mat-icon[contains(text(),'save')]"
    _extendStatusXpath="//tr[{0}]//mat-icon[contains(text(),'keyboard_arrow_right')]"  #BY ORDER
    _AddchildstatusBtnXpath="//div[contains(text(),'{0}')]//..//span[contains(@class,'add-icon-task')]" #BY LABEL
    _EditStatusBtnXpath="//tr[{0}]/td[3]/mat-icon[1]" #BY ORDER
    _DeleteStatusBtnXpath="//tr[{0}]/td[4]/mat-icon[1]" #BY ORDER


    #TODO: COMPLETE COMPLETION SCREEN

    #REPORTS_SCREEN
    _ByBoardSupervisorXpath="//p[text()=' By Board Supervisor ']"
    _CustomReportFlowXpath="//p[text()=' Create Custom Report Flow ']"
    _SourceDepDDLXpath="//ng-select[@formcontrolname='srcDirectorate']"
    _SourceDDLOptionXpath="//span[contains(text(),' Business Development Unit')]" #BY LABEL

    _SourceTitleDDLXpath="//mat-select[@formcontrolname='srcTitle']"
    _DestDepDDLXpath="//ng-select[@formcontrolname='destDirectorate']"
    _DestTitleDDLXpath="//mat-select[@formcontrolname='destTitle']"
    _UsersDDLXpath="//ng-select[@formcontrolname='employees']"
    _ReportsApplyOnDDLXpath="//ng-select[@formcontrolname='applyOn']"
    _SaveReportsBtnXpath="//span[text()='Save ']"
    _DeleteReportBtnXpath=""





    def __init__(self, driver):
        Routes.__init__(self, driver)
        self.htmlInfo += "<h3> ADMIN PAGE </h3>"
        self.htmlP = "<p class='Admin validation {0}'> {1} </p>"

    def click_Page(self,name):
        self.validate.get_web_element(self._PageNameXpath.format(name)).click()  #Case sensitive
        self.htmlInfo += self.htmlP.format("", "PAGE:{0}".format(name))

    def add_category(self):
        self.validate.get_web_element(self._AddCategoryBtnXpath).click()

    def set_newcategory(self,name):
        self.validate.get_web_element(self._CategoryNameXpath).send_keys(name)

    def save_newcategory(self):
        self.validate.get_web_element(self._SaveNewBtnXpath).click()
        self.htmlInfo += self.htmlP.format("", "ADDING NEW CATEGORY")

    def cancelnewcategory(self):
        self.validate.get_web_element(self._CancelBtnXpath).click()
        self.htmlInfo += self.htmlP.format("", "CANCEL ADDING NEW CATEGORY")

    def edit_category(self,order):
        self.htmlInfo += self.htmlP.format("", "EDIT CATEGORY")

        self.validate.get_web_element(self._EditBtnXpath.format(order)).click()
        self.validate.get_web_element(self._EditNameXpath).clear()
    def set_editname(self,name):
        self.validate.get_web_element(self._EditNameXpath).send_keys(name)


    def save_editcategory(self):
        self.validate.get_web_element(self._SaveEditNbtnXpath).click()
        self.htmlInfo += self.htmlP.format("", "SAVE CATEGORY")

    def change_language(self, language):
        self.validate.get_web_element(self._LanguageBtnXpath).click()
        self.validate.get_web_element(self._Language_choice.format(language)).click()
        self.htmlInfo += self.htmlP.format("", " :{0}".format("CHANGE LANGUAGE"))

    #********************************************************************************************

    def click_new_jobtitle(self,):
        self.validate.get_web_element(self._AddJobBtnXpath).click()

    def set_JobTitle(self,title):
        self.validate.get_web_element(self._JobTitleXpath).send_keys(title)
        self.htmlInfo += self.htmlP.format("", " :{0}".format("NEW JOB TITLE "))

    def set_JobCode(self,code):
        self.validate.get_web_element(self._IntCodeXpath).send_keys(code)
        self.htmlInfo += self.htmlP.format("", " :{0}".format("NEW JOB INTEGRATION CODE"))

    def set_new_jobcategory(self,category):
        self.validate.get_web_element(self._NewCategoryDDLXpath).click()
        self.validate.get_web_element(self._DDLOptionXpath.format(category)).click()
        self.htmlInfo += self.htmlP.format("", " :{0}".format("NEW JOB CATEGORY"))

    def set_newjobrole(self,role):
        self.validate.get_web_element(self._DefuatRoleDDLXpath).click()
        self.validate.get_web_element(self._DDLOptionXpath.format(role)).click()
        self.htmlInfo += self.htmlP.format("", " :{0}".format("NEW JOB ROLE"))

    def save_newJob(self):
        self.validate.get_web_element(self._SaveNewJobXpath).click()
        self.htmlInfo += self.htmlP.format("", " :{0}".format("SAVE NEW JOB"))

    def exit_newJob(self):
        self.validate.get_web_element(self._CloseNewJobXpath).click()
        self.htmlInfo += self.htmlP.format("", " :{0}".format("CANCEL NEW JOB"))

    def click_edit(self,order):
        self.validate.get_web_element(self._EditJobBtnXpath.format(order)).click()
        self.htmlInfo += self.htmlP.format("", " :{0}".format("EDIT JOB"))

    def edit_name(self,name ):
        self.validate.get_web_element(self._EditJobTitleXpath).clear()
        self.validate.get_web_element(self._EditJobTitleXpath).send_keys(name)

    def edit_intcode(self,code):
        self.validate.get_web_element(self._EditIntCodeXpath).clear()
        self.validate.get_web_element(self._EditIntCodeXpath).send_keys(code)

    def save_edit(self,order):
        self.validate.get_web_element(self._SaveEditBtnXpath.format(order)).click()
        self.htmlInfo += self.htmlP.format("", " :{0}".format("SAVE EDIT JOB"))


    def delete_job(self,order):
        self.validate.get_web_element(self._DeleteJobBtnXpath.format(order)).click()
        self.htmlInfo += self.htmlP.format("", " :{0}".format("DELETE JOB"))


    def cancel_edit(self,order):
        self.validate.get_web_element(self._CancelEditBtnXpath.format(order)).click()
        self.htmlInfo += self.htmlP.format("", " :{0}".format("CANCEL EDIT"))


    #******************************************************************************************

    def export_chart(self,option):
        self.validate.get_web_element(self._ExportChartDDlXpath).click()
        self.validate.get_web_element(self._ExportChartOptionXpath.format(option)).click()
        self.htmlInfo += self.htmlP.format("", " :{0}".format("EXPORT CHART"))


    def change_direction(self,direction):
        if direction.lower().contains("horizontal"):
            self.validate.get_web_element(self._DirectionXpath.format("vertical"))
            self.htmlInfo += self.htmlP.format("", " :{0}".format("SET CHART'S DIRECTION TO HORIZONTAL"))

        else:
            self.validate.get_web_element(self._DirectionXpath.format("horizontal"))
            self.htmlInfo += self.htmlP.format("", " :{0}".format("SET CHART'S DIRECTION TO VERTICAL"))



    #***********************************************************************************************

    def click_add(self,):
        self.validate.get_web_element(self._AddBtnXpath)
        self.htmlInfo += self.htmlP.format("", " :{0}".format("ADD NEW HOLIDAY"))

    def select_Language(self,language):
        self.validate.get_web_element(self._LanguageDDLXpath).click()
        self.validate.get_web_element(self._LanguageXpath.format(language)).click()
        self.htmlInfo += self.htmlP.format("", " :{0}".format("CHANGE LANGUAGE"))

    def set_templateName(self,name):
        self.validate.get_web_element(self._TemplateNameXpath).send_keys(name)
        self.htmlInfo += self.htmlP.format("", " :{0}".format("SET TEMPLATE NAME"))

    def new_apply_on(self,ordergroup):
        self.htmlInfo += self.htmlP.format("", " :{0}".format("APPLY HOLIDAY ON PROJECTS"))
        for order in ordergroup:
            self.validate.get_web_element(self._ApplyOnDDLXpath).click()
            self.validate.get_web_element(self._ApplyonOptionsXpath.format(order)).click()


    def check_days(self,daygroup):
        self.htmlInfo += self.htmlP.format("", " :{0}".format("APPLY HOLIDAY ON DAYS"))
        for day in daygroup:
          self.validate.get_web_element(self._CheckDaysXpath.format(day)).click()

    def new_HolidayAndException(self):
        self.htmlInfo += self.htmlP.format("", " :{0}".format("ADD NEW HOLIDAY"))
        self.validate.get_web_element(self._NewExceptionBtnXpath).click()

    def set_HolidayName(self,name):
        self.htmlInfo += self.htmlP.format("", " :{0}".format("SET NEW HOLIDAY NAME"))
        self.validate.get_web_element(self._HolidayNameXpath).send_keys(name)

    def set_HolidayDate(self,start,end):
        self.htmlInfo += self.htmlP.format("", " :{0}".format("SET HOLIDAY DATE"))
        self.validate.get_web_element(self._StartDateXpath).send_keys(start)
        self.validate.get_web_element(self._EndDateXpath).send_keys(end)

    def set_HolidayType(self,type):
        self.htmlInfo += self.htmlP.format("", " :{0}".format("SET HOLIDAY TYPE"))
        self.validate.get_web_element(self._TypeDDlXpath).click()
        self.validate.get_web_element(self._TypeDDLOption.format(type)).click()

    def Save_Holiday(self):
        self.htmlInfo += self.htmlP.format("", " :{0}".format("SAVE HOLIDAY"))
        self.validate.get_web_element(self._SaveNewHolidayBtnXpath).click()

    def deleteHoliday(self,HolidayName):
        self.htmlInfo += self.htmlP.format("", " :{0}".format("DELETE HOLIDAY"))
        self.validate.get_web_element(self._deleteHolidayeXpath.format(HolidayName)).click()

    def edit_Holiday(self, name):
        self.htmlInfo += self.htmlP.format("", " :{0}".format("EDIT HOLIDAY"))
        self.validate.get_web_element(self._EditHolidayXpath.format(name)).click()

    def editApplyonholiday(self,name,boardsgroup):
        self.htmlInfo += self.htmlP.format("", " :{0}".format("APPLY HOLIDAY ON BOARDS"))
        self.validate.get_web_element(self._Applyonholiday.format(name)).click()
        for board in boardsgroup:
          self.validate.get_web_element(self._ApplyonholidayOption.format(board)).click()


#************************************************************************

    # REPORTS_SCREEN
    _ByBoardSupervisorXpath = "//p[text()=' By Board Supervisor ']"
    _CustomReportFlowXpath = "//p[text()=' Create Custom Report Flow ']"
    _SourceDepDDLXpath = "//ng-select[@formcontrolname='srcDirectorate']"
    _SourceDDLOptionXpath="//span[contains(text(),' Business Development Unit')]" #BY LABEL
    _SourceTitleDDLXpath = "//mat-select[@formcontrolname='srcTitle']"
    _SourceTitleOptionXpath="//span[contains(text(),'{0}')]"  #BY LABEL
    _DestDepDDLXpath = "//ng-select[@formcontrolname='destDirectorate']"  #//app-reports-management/form/div[2]/div[3]/div/div[3]/ng-select
    _DestTitleDDLXpath = "//mat-select[@formcontrolname='destTitle']"     #//app-reports-management/form/div[2]/div[4]/div/div[3]/ng-select
    _UsersDDLXpath = "//ng-select[@formcontrolname='employees']"
    _ReportsApplyOnDDLXpath = "//ng-select[@formcontrolname='applyOn']"
    _SaveReportsBtnXpath = "//span[text()='Save ']"
    _DeleteReportBtnXpath = ""

    #TODO: change the DDL'S xpath , it's not working when there is multiple rows


    def select_reportsType(self,type):
        if str(type).lower().__contains__("supervisor"):
            self.validate.get_web_element(self._ByBoardSupervisorXpath).click()
        else:
            self.validate.get_web_element(self._CustomReportFlowXpath).click()

    def set_sourcedep(self,name):
        self.validate.get_web_element(self._SourceDepDDLXpath).click()
        self.validate.get_web_element(self._SourceDDLOptionXpath.format(name)).click()

    def set_sourceTitle(self,title):
        self.validate.get_web_element(self._SourceTitleDDLXpath).click()
        self.validate.get_web_element(self._SourceTitleOptionXpath.format(title)).click()


