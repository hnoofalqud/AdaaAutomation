import time
from Files.utilities import Utilities

from POM.routes.boards_page.boards import Boards
from POM.routes.inbox_page.inbox import Inbox
from POM.routes.navigation import Navigation
from validate import validateElement
from validate.toastMsg import ToastMsg


class ExcelToCode(Utilities):
    webDriver = None  # TO ACCESS THE DOM ELEMENTS IN THE BROWSER
    readExcel = None  # THE EXCEL FILE OBJECT
    sheet = None  # THE CURRENT EXCEL FILE SHEET NAME

    def __init__(self, browserObject, readExcel, sheet, navigationControls, boardsPage, inboxPage, toastMsg , reportsPage, calendarPage, escalationPage, approvalsPage, activitylogPage, contactsPage, adminPage, mytasksPage, myprofile, homepage,validate):
        self.browserObject = browserObject
        self.webDriver = browserObject.driver  # OBJECT THAT HOLDS THE DESIRED BROWSER
        self.readExcel = readExcel  # OBJECT THAT HOLDS THE EXCEL FILE
        self.sheet = sheet  # CURRENT TEST CASE
        self.htmlInfo = ""

        # GET TEST CASE ID + DESCRIPTION
        testCaseID = self.readExcel.getCellFromSheet(sheet=sheet, cell="J3")
        testCaseDesc = self.readExcel.getCellFromSheet(sheet=sheet, cell="J4")

        # LOG & PRINT THE TEST CASE ID + DESCRIPTION
        print("TEST CASE ID: {0}".format(testCaseID))
        print("TEST CASE DESCRIPTION: {0} \n".format(testCaseDesc))

        self.navigationControls = navigationControls
        self.boardsPage = boardsPage
        self.inboxPage = inboxPage
        self.toastMsg = toastMsg
        self.reportsPage=reportsPage
        self.escalationPage=escalationPage
        self.calendarPage=calendarPage
        self.approvalsPage=approvalsPage
        self.activitylogPage=activitylogPage
        self.contactsPage=contactsPage
        self.validate= validate
        self.admin=adminPage
        self.mytasks= mytasksPage
        self.myprofile= myprofile
        self.homepage=homepage



        self.currentPage = "boards"

    def read_rows(self):
        lastRow = self.readExcel.getMaxRow(sheet=self.sheet) + 1  # NUMBER OF STEPS (IN THE EXCEL FILE)
        for rowNumber in range(2, lastRow):  # SKIP THE FIRST ROW (CONTAINS THE HEADER)

            # SPLIT QUESTIONS - ANSWERS & CALL EXECUTE FUNCTION
            if self.get_function_from_row(rowNumber) is None:
                continue

            errorStatus = self.execute_function(rowNumber)  # RETURNS TRUE IF AN ERROR (EXCEPTION) IS FOUND FOUND
            if errorStatus:  # ERROR FOUND (STOP TEST CASE)
                print("<><><><><><><><> SUDDEN STOP - TEST NOT COMPLETED <><><><><><><><>")
                print(self.error)  # PRINTS A BIG ERROR MASSAGE ON THE SCREEN
                self.htmlInfo += "<p class='general-validation false'> {0} - ROW #{1} </p>".format("SUDDEN STOP - TEST NOT COMPLETED" , rowNumber)
                return False
                break

    def execute_function(self, rowNumber):
        try:
            # THIS METHOD SPECIFIES WHICH FUNCTION TO EXECUTE
            function = self.get_function_from_row(rowNumber)  # GET DATA FROM EXCEL
            if str(function).lower().__contains__('navigate'):
                self.navigate_functions(rowNumber)

            if str(function).lower().__contains__('click') or str(function).lower().__contains__('button'):
                self.button_functions(rowNumber)

            if str(function).lower().__contains__('set'):
                self.set_functions(rowNumber)

            if str(function).lower().__contains__('validate'):
                self.validate_functions(rowNumber)

        except Exception as e:
            print(e)
            return True

    def validate_functions(self, rowNumber):
        getParameter = self.get_parameter_from_row(rowNumber)  # GET DATA FROM EXCEL
        getInputData = self.get_input_data_from_row(rowNumber)
        getExtraData = self.get_extra_data_from_row(rowNumber)

        if str(getParameter).lower().__contains__("toast"):
            self.toastMsg.toast_msg_visible(msg=getInputData, notes="ROW #{0} - {1}".format(rowNumber, getExtraData))
        if str(self.currentPage).lower().__contains__("board"):
            self.validate_Boards(rowNumber,getParameter)
        if str(self.currentPage).lower().__contains__("activity"):
            self.validate_activity(rowNumber,getParameter)
        if str(self.currentPage).lower().__contains__("contacts"):
            self.validate_contact(rowNumber,getParameter)
        if str(self.currentPage).lower().__contains__("calendar"):
            self.validate_calendar(rowNumber,getParameter)
        if str(self.currentPage).lower().__contains__("inbox"):
            self.validate_Inbox(rowNumber,getParameter)
        if str(self.currentPage).lower().__contains__("my tasks"):
            self.validate_mytasks(rowNumber,getParameter)

    def navigate_functions(self, rowNumber):
        getParameter = self.get_parameter_from_row(rowNumber)  # GET DATA FROM EXCEL

        self.currentPage = str(getParameter).lower()
        # print(self.currentPage)
        self.navigationControls.navigate_to_page(page=self.currentPage)

    def button_functions(self, rowNumber):
        getParameter = self.get_parameter_from_row(rowNumber)  # GET DATA FROM EXCEL

        if str(self.currentPage).lower().__contains__("board"):
            self.board_buttons(rowNumber, getParameter)
        elif str(self.currentPage).lower().__contains__("inbox"):
            self.inbox_buttons(rowNumber, getParameter)
        elif str(self.currentPage).lower().__contains__("reports"):
            self.reports_buttons(rowNumber, getParameter)
        elif str(self.currentPage).lower().__contains__("escalation"):
            self.escalation_buttons(rowNumber, getParameter)
        elif str(self.currentPage).lower().__contains__("calendar"):
            self.calendar_buttons(rowNumber,getParameter)
        elif str(self.currentPage).lower().__contains__("approvals"):
            self.approvals_button(rowNumber,getParameter)
        elif str(self.currentPage).lower().__contains__("activity"):
            self.activity_buttons(rowNumber,getParameter)
        elif str(self.currentPage).lower().__contains__("contacts"):
            self.contact_buttons(rowNumber,getParameter)
        elif str(self.currentPage).lower().__contains__("admin"):
            self.admin_buttons(rowNumber,getParameter)
        elif str(self.currentPage).lower().__contains__("my tasks"):
            self.mytasks_buttons(rowNumber,getParameter)
        elif str(self.currentPage).lower().__contains__("my profile"):
            self.myprofile_buttons(rowNumber,getParameter)
        elif str(self.currentPage).lower().__contains__("home"):
            self.homepage_buttons(rowNumber,getParameter)






    def set_functions(self, rowNumber):
        getParameter = self.get_parameter_from_row(rowNumber)  # GET DATA FROM EXCEL
        getInputData = self.get_input_data_from_row(rowNumber)
        getExtraData = self.get_extra_data_from_row(rowNumber)

        if str(self.currentPage).lower().__contains__("board"):
            self.set_board(getParameter, getInputData, getExtraData)
        elif str(self.currentPage).lower().__contains__("inbox"):
            self.set_inbox(getParameter, getInputData, getExtraData)
        elif str(self.currentPage).lower().__contains__("users") :
            self.set_users(getParameter,getInputData,getExtraData)
        elif str(self.currentPage).lower().__contains__("reports"):
            self.set_report(getParameter, getInputData, getExtraData)
        elif str(self.currentPage).lower().__contains__("escalation"):
            self.set_escalation(getParameter, getInputData, getExtraData)
        elif str(self.currentPage).lower().__contains__("approvals"):
            self.set_approvals(getParameter, getInputData, getExtraData)
        elif str(self.currentPage).lower().__contains__("contacts"):
            self.set_contacts(getParameter, getInputData, getExtraData)
        elif str(self.currentPage).lower().__contains__("activity"):
            self.set_activiyLogs(getParameter, getInputData, getExtraData)
        elif str(self.currentPage).lower().__contains__("admin"):
            self.set_admin(getParameter, getInputData, getExtraData)
        elif str(self.currentPage).lower().__contains__("my profile"):
            self.set_myprofile(getParameter, getInputData, getExtraData)
        elif str(self.currentPage).lower().__contains__("home"):
            self.set_homepage(getParameter,getInputData,getExtraData)





    def board_buttons(self, rowNumber, getParameter):
        if str(getParameter).lower().__contains__('new board'):
            self.boardsPage.get_new_board_btn()
        elif str(getParameter).lower().__contains__('calendar view'):
            self.boardsPage.CalendarView(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('add attributes'):
            self.boardsPage.click_addAttributes()
        elif str(getParameter).lower().__contains__('delete attribute'):
            self.boardsPage.delete_attribute()
        elif str(getParameter).lower().__contains__('delete task'):
            self.boardsPage.delete_Task(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('save board'):
            self.boardsPage.get_save_new_board_btn()
        elif str(getParameter).lower().__contains__('close') or str(getParameter).lower().__contains__('exit'):
            self.boardsPage.get_close_new_board_btn()
        elif str(getParameter).lower().__contains__('project'):
            self.boardsPage.click_project(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('ok'):
            self.boardsPage.click_OK()
        elif str(getParameter).lower().__contains__('new task'):
            self.boardsPage.get_new_task_btn()
        elif str(getParameter).lower().__contains__("new child task"):
            self.boardsPage.new_childTask_btn(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('save task'):
            self.boardsPage.save_new_task()
        elif str(getParameter).lower().__contains__('confirm delete'):
            self.boardsPage.Confirm_Delete()
        elif str(getParameter).lower().__contains__('search project'):
            self.boardsPage.search_project(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('day'):
            self.boardsPage.opentasklist_DayinCalendar(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("task details"):
            self.boardsPage.click_Task_Details(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("close task details"):
            self.boardsPage.get_close_Task_Details()
        elif str(getParameter).lower().__contains__("comment tab"):
            self.boardsPage.commentINdetails()
        elif str(getParameter).lower().__contains__("save comment"):
            self.boardsPage.save_comment()
        elif str(getParameter).lower().__contains__("send comment"):
            self.boardsPage.send_comment()
        elif str(getParameter).lower().__contains__("activity logs"):
            self.boardsPage.activityindetails()
        elif str(getParameter).lower().__contains__("add file"):
            self.boardsPage.copycsv()
        elif str(getParameter).lower().__contains__("gant view"):
            self.boardsPage.gantview(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("edit comment"):
            self.boardsPage.EditComment(self.get_input_data_from_row(rowNumber),self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('progress ratio'):
            self.boardsPage.click_progress_ratio(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('gant chart'):
            self.boardsPage.click_gantview()
        elif str(getParameter).lower().__contains__('take screenshot'):
            self.boardsPage.takeScreenshot(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('calendar'):
            self.boardsPage.click_Calendar_view()
        elif str(getParameter).lower().__contains__('open task in gant'):
            self.boardsPage.viewtaskingant(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('move'):
            self.boardsPage.Move_RightLeft(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('open task'):
            self.boardsPage.open_Taskincalendar(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("copy from"):
            self.boardsPage.CopyfromBtn(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('filter'):
            self.boardsPage.click_filter()
        elif str(getParameter).lower().__contains__('priority'):
            self.boardsPage.filter_Prioruty(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('members'):
            self.boardsPage.filter_Members(self.get_input_data_from_row(rowNumber))
        else:
            print("{0} NOT A BOARD BUTTON".format(getParameter))


    def validate_mytasks(self,rowNumber,getParameter):
        if str(getParameter).lower().__contains__('members'):
            self.mytasks.loop_over_members(self.get_input_data_from_row(rowNumber))

    def mytasks_buttons(self, rowNumber, getParameter):
        if str(getParameter).lower().__contains__("task details"):
            self.mytasks.open_task_details(self.get_input_data_from_row(rowNumber),self.get_extra_data_from_row(rowNumber))
        # elif str(getParameter).lower().__contains__("")


    def set_mytasks(self, getParameter, getInputData, getExtraData):
        if str(getParameter).lower().__contains__("task name"):
            self.mytasks.editname(getInputData)
        elif str(getParameter).lower().__contains__("description"):
            self.mytasks.editDescription(getInputData)
        elif str(getParameter).lower().__contains__("start date"):
            self.mytasks.edit_startdate(getInputData)
        elif str(getParameter).lower().__contains__("end date"):
            self.mytasks.edit_enddate(getInputData)
        elif str(getParameter).lower().__contains__("recurring"):
            self.mytasks.select_Recurring(getInputData)
        elif str(getParameter).lower().__contains__("duration"):
            self.mytasks.edit_duration(getInputData)
        elif str(getParameter).lower().__contains__("weekly every"):
            self.mytasks.weekly_everyrecurring(getInputData)
        elif str(getParameter).lower().__contains__("weekly day"):
            self.mytasks.set_weeklyDay(getExtraData)
        elif str(getParameter).lower().__contains__("weekly occerunce"):
            self.mytasks.set_weklyoccurrenc(getInputData)
        elif str(getParameter).lower().__contains__("monthly every"):
            self.mytasks.monthly_recurring(getInputData,getExtraData)
        # if str(getParameter).lower().__contains__("")


    def homepage_buttons(self,rowNumber,getParmeter):
        if str(getParmeter).lower().__contains__("expand"):
            self.homepage.expand_tabs(self.get_input_data_from_row(rowNumber))
        elif str(getParmeter).lower().__contains__("open task"):
            self.homepage.open_Task(self.get_input_data_from_row(rowNumber))
        elif str(getParmeter).lower().__contains__("open members"):
            self.homepage.open_Members(self.get_input_data_from_row(rowNumber))
        elif str(getParmeter).lower().__contains__("open board"):
            self.homepage.openBoards(self.get_input_data_from_row(rowNumber))
        elif str(getParmeter).lower().__contains__("tasks"):
            self.homepage.tasks(self.get_input_data_from_row(rowNumber),self.get_extra_data_from_row(rowNumber))

    def inbox_buttons(self, rowNumber, getParameter):
        if str(getParameter).lower().__contains__('new'):
            self.inboxPage.get_new_inbox_msg_btn()
        elif str(getParameter).lower().__contains__('send'):
            self.inboxPage.get_send_btn()
        elif str(getParameter).lower().__contains__('close') or str(getParameter).lower().__contains__('exit'):
            self.inboxPage.get_close_new_inbox_msg_btn()
        elif str(getParameter).lower().__contains__('read'):
            self.inboxPage.read_Message(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("outbox") or str(getParameter).lower().__contains__("inbox"):
            self.inboxPage.Set_BoxType(getParameter)
        elif str(getParameter).lower().__contains__('more'):
            self.inboxPage.click_more_btn(self.get_input_data_from_row(rowNumber),self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('filter'):
            self.inboxPage.click_Filter()
        elif str(getParameter).lower().__contains__('type'):
            self.inboxPage.filter_Type(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('boards'):
            self.inboxPage.filter_Boards(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('users'):
            self.inboxPage.filter_users(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('confirm'):
            self.inboxPage.confirm_delete()
        else:
            print("{0} NOT A INBOX BUTTON".format(getParameter))

    def validate_Inbox(self,rowNumber,getParameter):
        if str(getParameter).lower().__contains__("inbox number"):
            self.inboxPage.validate_inboxNum(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("user list"):
            self.inboxPage.validate_filterbyUser(self.get_input_data_from_row(rowNumber))

    def set_board(self, getParameter, getInputData, getExtraData):
        if str(getParameter).lower().__contains__("board name"):
            self.boardsPage.set_board_name(getInputData)
        elif str(getParameter).lower().__contains__("board code"):
            self.boardsPage.set_board_code(getInputData)
        elif str(getParameter).lower().__contains__("board") and str(getParameter).lower().__contains__("department"):
            self.boardsPage.set_board_department_drop_down(getInputData)
        elif str(getParameter).lower().__contains__("board") and str(getParameter).lower().__contains__("supervisor"):
            self.boardsPage.set_board_supervisor_drop_down(getInputData)
        elif str(getParameter).lower().__contains__("resource pool") and str(getParameter).lower().__contains__(
                "departments"):
            self.boardsPage.set_board_departments_resource_pool(str(getInputData).split(","))
        elif str(getParameter).lower().__contains__("resource pool") and str(getParameter).lower().__contains__(
                "members"):
            self.boardsPage.set_board_members_resource_pool(group=str(getInputData).split(","),
                                                            option=str(getExtraData).split(","))
        elif str(getParameter).lower().__contains__("new board status"):
            self.boardsPage.set_Newboard_status(getInputData)
        elif str(getParameter).lower().__contains__("board status"):
            self.boardsPage.set_Board_status(getInputData)
        elif str(getParameter).lower().__contains__("attributes name"):
            self.boardsPage.set_attributesName(getInputData)
        elif str(getParameter).lower().__contains__("attributes ddl"):
            self.boardsPage.select_attribures(getInputData,getExtraData)
        elif str(getParameter).lower().__contains__('new board color'):
            self.boardsPage.set_board_color(getInputData)
        elif str(getParameter).lower().__contains__('edit color'):
            self.boardsPage.edit_color(getInputData)
        elif str(getParameter).lower().__contains__("copy from details"):
            self.boardsPage.copyfromDDL(getInputData,getExtraData)
        elif str(getParameter).lower().__contains__('board ddl'):
            self.boardsPage.Board_DDL(getInputData)
        elif str(getParameter).lower().__contains__("duplicate name"):
            self.boardsPage.set_Duplicate_name(getInputData)
        elif str(getParameter).lower().__contains__("convert to template"):
            self.boardsPage.set_Convert_To_name(getInputData)
        elif str(getParameter).lower().__contains__("task name"):
            self.boardsPage.set_task_name(getInputData)
        elif str(getParameter).lower().__contains__("task description"):
            self.boardsPage.set_task_description(getInputData)
        elif str(getParameter).lower().__contains__("date"):
            self.boardsPage.set_task_start_end_date(startDate=str(getInputData),endDate=str(getExtraData))
        elif str(getParameter).lower().__contains__("duration"):
            self.boardsPage.set_task_duration(getInputData)
        elif str(getParameter).lower().__contains__("task") and str(getParameter).lower().__contains__("department"):
            print(str(getInputData).split(","))
            self.boardsPage.set_task_departments(str(getInputData).split(","))
        elif str(getParameter).lower().__contains__("task") and str(getParameter).lower().__contains__("member"):
            self.boardsPage.set_task_members(str(getInputData).split(","))
        elif str(getParameter).lower().__contains__("task priority"):
            self.boardsPage.set_task_priority(getInputData)
        elif str(getParameter).lower().__contains__("details"):
            self.boardsPage.set_task_priority_details(getInputData)
        elif str(getParameter).lower().__contains__("tasks number"):
            self.boardsPage.validate_Tasks_number()
        elif str(getParameter).lower().__contains__("comment"):
            self.boardsPage.Set_Comment(getInputData,getExtraData)
        elif str(getParameter).lower().__contains__("progress type"):
            self.boardsPage.set_task_progress(getInputData,getExtraData)
        elif str(getParameter).lower().__contains__("task ratio"):
            self.boardsPage.set_task_progress_ratio(getInputData)
        elif str(getParameter).lower().__contains__("task dependency"):
            self.boardsPage.set_depndancy(getInputData,getExtraData)
        elif str(getParameter).lower().__contains__("progress ratio"):
            self.boardsPage.set_progress(getInputData)
        elif str(getParameter).lower().__contains__("attributes value"):
            self.boardsPage.set_attributeValue(getInputData)
        elif str(getParameter).lower().__contains__("filter start date"):
            self.boardsPage.set_startdate(getInputData)
        elif str(getParameter).lower().__contains__("filter end date"):
            self.boardsPage.set_Enddate(getInputData)

    def validate_Boards(self,rowNumber,getParameter):
        if str(getParameter).lower().__contains__("approve status"):
            self.boardsPage.Validate_Approved_status(self.get_input_data_from_row(rowNumber) ,self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("board name"):
            self.boardsPage.validate_boardName_Edit(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("tasks list"):
            self.boardsPage.validate_tasksListInCalendar()
        elif str(getParameter).lower().__contains__('take screenshot'):
            self.boardsPage.takeScreenshot(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__('comment'):
            self.boardsPage.validate_comments(self.get_input_data_from_row(rowNumber))

    def set_inbox(self, getParameter, getInputData, getExtraData):
        if str(getParameter).lower().__contains__("board"):
            self.inboxPage.set_inbox_board_name_drop_down(getInputData)
        elif str(getParameter).lower().__contains__("task"):
            self.inboxPage.set_inbox_task_drop_down(getInputData)
        elif str(getParameter).lower().__contains__("description"):
            self.inboxPage.set_msg_description(getInputData)
        elif str(getParameter).lower().__contains__("filter date"):
            self.inboxPage.set_date(getInputData, getExtraData)

    def myprofile_buttons(self,rowNumber,getParameter):
        if str(getParameter).lower().__contains__("permission"):
            self.myprofile.permession_tab()
        if str(getParameter).lower().__contains__("my profile"):
            self.myprofile.openmyprofile()
        elif str(getParameter).lower().__contains__("notifications"):
            self.myprofile.notification_tab()
        elif str(getParameter).lower().__contains__("delete img"):
            self.myprofile.delete_image()
        elif str(getParameter).lower().__contains__("change img"):
            self.myprofile.change_image(self.get_input_data_from_row(rowNumber),self.get_extra_data_from_row(rowNumber))
        # elif str(getParameter).lower().__contains__("")
    def set_myprofile(self,getParameter, getInputData, getExtraData):
        if str(getParameter).lower().__contains__("mobile"):
            self.myprofile.set_mobileNum(getInputData)
        if str(getParameter).lower().__contains__("notificattion"):
            self.myprofile.checknotification(getInputData, str(getExtraData).split(","))

    def reports_buttons(self, rowNumber, getParameter):
       if str(getParameter).lower().__contains__("new report"):
           self.reportsPage.get_new_Report_btn()
       elif str(getParameter).lower().__contains__("urgent"):
           self.reportsPage.click_urgent()
       elif str(getParameter).lower().__contains__("send report"):
           self.reportsPage.get_send_new_Report_btn()
       elif str(getParameter).lower().__contains__("close"):
           self.reportsPage.get_close_new_Report_btn()
       elif str(getParameter).lower().__contains__("comment"):
           self.reportsPage.get_comment_btn()
       elif str(getParameter).lower().__contains__("forward button"):
           self.reportsPage.get_forward_Report_btn()
       elif str(getParameter).lower().__contains__("more"):
           self.reportsPage.get_more_menu_btn()
       elif str(getParameter).lower().__contains__("option"):
           self.reportsPage.get_menu_option(self.get_input_data_from_row(rowNumber))
       elif str(getParameter).lower().__contains__("confirm"):
           self.reportsPage.Confirm_Delete_Report()
       elif str(getParameter).lower().__contains__("outbox") or str(getParameter).lower().__contains__("inbox") :
            self.reportsPage.Set_BoxType(getParameter)
       elif str(getParameter).lower().__contains__("list"):
           self.reportsPage.get_Report(self.get_extra_data_from_row(rowNumber))
       elif str(getParameter).lower().__contains__("send comment"):
           self.reportsPage.send_comment()
       elif str(getParameter).lower().__contains__("send copy"):
           self.reportsPage.send_copy()
       elif str(getParameter).lower().__contains__("send forward"):
           self.reportsPage.send_forward()
       elif str(getParameter).lower().__contains__("filter"):
           self.reportsPage.click_filter()
       elif str(getParameter).lower().__contains__("boards"):
           self.reportsPage.filter_Boards(self.get_extra_data_from_row(rowNumber))
       elif str(getParameter).lower().__contains__("members"):
           self.reportsPage.filter_Members(self.get_extra_data_from_row(rowNumber))

       else:
           print("{0} NOT A REPORT BUTTON".format(getParameter))



    def set_report(self,getParameter, getInputData, getExtraData):
        if str(getParameter).lower().__contains__("board"):
            self.reportsPage.set_board_Name_drop_down(getInputData)
        elif str(getParameter).lower().__contains__("subject"):
            self.reportsPage.set_report_subject(getInputData)
        elif str(getParameter).lower().__contains__("description"):
            self.reportsPage.set_report_Description(getInputData)
        elif str(getParameter).lower().__contains__("list"):
            self.reportsPage.get_Report(getInputData)
        elif str(getParameter).lower().__contains__("task"):
            self.reportsPage.set_task_drop_down(getInputData)
        elif str(getParameter).lower().__contains__("comment"):
            self.reportsPage.set_new_Comment(getInputData)
        elif str(getParameter).lower().__contains__("filter date"):
            self.reportsPage.set_date(startDate=str(getInputData), endDate=str(getExtraData))


    def escalation_buttons(self, rowNumber, getParameter):
        if str(getParameter).lower().__contains__("new escalation"):
            self.escalationPage.get_new_escalation_btn()
        elif str(getParameter).lower().__contains__("send esclataion"):
            self.escalationPage.get_send_new_Escalation_btn()
        elif str(getParameter).lower().__contains__("close comment"):
            self.escalationPage.Close_new_comment()
        elif str(getParameter).lower().__contains__("terminate"):
            self.escalationPage.click_close()
        elif str(getParameter).lower().__contains__("close new"):
            self.escalationPage.get_close_new_Report_btn()
        elif str(getParameter).lower().__contains__("comment"):
            self.escalationPage.get_comment_btn()
        elif str(getParameter).lower().__contains__("more"):
            self.escalationPage.get_more_menu_btn()
        elif str(getParameter).lower().__contains__("option"):
            self.escalationPage.get_menu_option(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("confirm"):
            self.escalationPage.Confirm_Button()
        elif str(getParameter).lower().__contains__("outbox") or str(getParameter).lower().__contains__("inbox"):
            self.escalationPage.Set_BoxType(getParameter)
        elif str(getParameter).lower().__contains__("list"):
            self.escalationPage.get_escalation(self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("send comment"):
            self.escalationPage.send_comment()
        elif str(getParameter).lower().__contains__("filter"):
            self.escalationPage.click_filter()
        elif str(getParameter).lower().__contains__("boards"):
            self.escalationPage.filter_Boards(self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("members"):
            self.escalationPage.filter_Members(self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("send copy"):
            self.escalationPage.Send_copy()
        else:
            print("{0} NOT A ESCALATION BUTTON".format(getParameter))

    def set_escalation(self, getParameter, getInputData, getExtraData):
        if str(getParameter).lower().__contains__("board"):
            self.escalationPage.set_board_Name_drop_down(getInputData)
        elif str(getParameter).lower().__contains__("subject"):
            self.escalationPage.set_Escalation_subject(getInputData)
        elif str(getParameter).lower().__contains__("description"):
            self.escalationPage.set_Escalation_Description(getInputData)
        elif str(getParameter).lower().__contains__("comment"):
            self.escalationPage.set_new_Comment(getInputData)
        elif str(getParameter).lower().__contains__("task"):
            self.escalationPage.set_task_drop_down(getInputData)
        elif str(getParameter).lower().__contains__("list"):
            self.escalationPage.get_escalation(getInputData)
        elif str(getParameter).lower().__contains__("filter date"):
            self.escalationPage.set_date(startDate=str(getInputData), endDate=str(getExtraData))

    def calendar_buttons(self, rowNumber, getParameter):
        if str(getParameter).lower().__contains__("right"):
            self.calendarPage.click_Right()
        elif str(getParameter).lower().__contains__("left"):
            self.calendarPage.click_left()
        elif str(getParameter).lower().__contains__("week"):
            self.calendarPage.Week_View()
        elif str(getParameter).lower().__contains__("day"):
            self.calendarPage.Day_view()
        elif str(getParameter).lower().__contains__("month"):
            self.calendarPage.Month_View()
        elif str(getParameter).lower().__contains__("view"):
            self.calendarPage.view_tasks(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("close"):
            self.calendarPage.close_details()
        elif str(getParameter).lower().__contains__("open"):
            self.calendarPage.open_task(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("filter"):
            self.calendarPage.click_filter()
        elif str(getParameter).lower().__contains__("boards"):
            self.calendarPage.filter_Boards()
        elif str(getParameter).lower().__contains__("members"):
            self.calendarPage.filter_Members(self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("priority"):
            self.calendarPage.Filter_Priority(self.get_extra_data_from_row(rowNumber))

    def approvals_button(self,rowNumber ,getParameter):

        if str(getParameter).lower().__contains__("all"):
            self.approvalsPage.CheckAll()

        elif str(getParameter).lower().__contains__("approve"):
            self.approvalsPage.Approve_Boards()

        elif str(getParameter).lower().__contains__("reject"):
            self.approvalsPage.Reject_Boards()
        elif str(getParameter).lower().__contains__("details"):
            self.approvalsPage.view_Details(self.get_extra_data_from_row(rowNumber))

        elif str(getParameter).lower().__contains__("comment"):
            self.approvalsPage.click_comment(self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("send"):
            self.approvalsPage.send_comment()
        elif str(getParameter).lower().__contains__("filter"):
            self.approvalsPage.click_filter()
        elif str(getParameter).lower().__contains__("boards"):
            self.approvalsPage.filter_Boards(self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("members"):
            self.approvalsPage.filter_Members(self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("confirm"):
            self.approvalsPage.click_confirm()



    def set_approvals(self, getParameter, getInputData, getExtraData):
        if str(getParameter).lower().__contains__("single") or str(getParameter).lower().__contains__("multi"):
            print(str(getInputData).split(","))
            self.approvalsPage.CheckBoards(str(getInputData).split(","))

        elif str(getParameter).lower().__contains__("reason"):
            self.approvalsPage.set_RejectionReason(getInputData)
        elif str(getParameter).lower().__contains__("comment"):
            self.approvalsPage.set_comment(getInputData)
        elif str(getParameter).lower().__contains__("date"):
            self.approvalsPage.set_date(startDate=str(getInputData), endDate=str(getExtraData))

    def activity_buttons(self,rowNumber ,getParameter):
        if str(getParameter).lower().__contains__("project"):
            self.activitylogPage.click_project(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("bookmark"):
            self.activitylogPage.Click_Bookmark(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("filter"):
            self.activitylogPage.click_filter()
        elif str(getParameter).lower().__contains__("tasks"):
            self.activitylogPage.filter_Tasks(self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("edited by"):
            self.activitylogPage.filter_EditedBy(self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("action"):
            self.activitylogPage.Filter_Action(self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("bookmark filter"):
            self.activitylogPage.Filter_Bookmark(self.get_extra_data_from_row(rowNumber))

    def set_activiyLogs(self, getParameter, getInputData, getExtraData):
        if str(getParameter).lower().__contains__("date"):
            self.activitylogPage.set_date(startDate=str(getInputData), endDate=str(getExtraData))


    def contact_buttons(self,rowNumber ,getParameter):
        if str(getParameter).lower().__contains__("filter"):
            self.contactsPage.click_filter()
        elif str(getParameter).lower().__contains__("name"):
            self.contactsPage.Filter_Name(self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("job"):
            self.contactsPage.Filter_Job(self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("department"):
            self.contactsPage.Filter_Dep(self.get_extra_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("email"):
            self.contactsPage.send_email(self.get_input_data_from_row(rowNumber))

    def validate_activity(self,rowNumber,getParameter):
        print("logs")
        if str(getParameter).lower().__contains__("logs"):
            self.activitylogPage.validate_logs()

    def validate_contact(self,rowNumber,getParameter):
        if str(getParameter).lower().__contains__("contacts list"):
            self.contactsPage.contacts_list()
        elif str(getParameter).lower().__contains__("mailto"):
            self.contactsPage.validate_attribute(self.get_parameter_from_row(rowNumber))

    def validate_calendar(self,rowNumber,getParameter):
        if str(getParameter).lower().__contains__("list"):
            self.calendarPage.validate_tasklist()
        elif str(getParameter).lower().__contains__("details"):
            self.calendarPage.validate_taskdetails()

    def admin_buttons(self, rowNumber, getParameter):
        if str(getParameter).lower().__contains__("page"):
            self.admin.click_Page(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("confirm delete"):
            self.admin.confirm_delete()
        elif str(getParameter).lower().__contains__("save category"):
            self.admin.save_newcategory()
        elif str(getParameter).lower().__contains__("cancel new category"):
            self.admin.cancelnewcategory()
        elif str(getParameter).lower().__contains__("edit category"):
            self.admin.edit_category(self.get_input_data_from_row(rowNumber))


        elif str(getParameter).lower().__contains__("new job"):
                self.admin.click_new_jobtitle()
        elif str(getParameter).lower().__contains__("save new job"):
                self.admin.save_newJob()
        elif str(getParameter).lower().__contains__("exit new job"):
                self.admin.exit_newJob()
        elif str(getParameter).lower().__contains__("edit job"):
                self.admin.click_edit(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("save job edit"):
                self.admin.save_edit(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("delete job"):
                self.admin.delete_job(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("cancel edit"):
                self.admin.cancel_edit(self.get_input_data_from_row(rowNumber))


        elif str(getParameter).lower().__contains__("chart"):
                self.admin.export_chart(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("direction"):
                self.admin.change_direction(self.get_input_data_from_row(rowNumber))


        elif str(getParameter).lower().__contains__("add holiday"):
                self.admin.click_add()
        elif str(getParameter).lower().__contains__("new holiday and exception"):
                self.admin.new_HolidayAndException()
        elif str(getParameter).lower().__contains__("save holiday"):
                self.admin.Save_Holiday()
        elif str(getParameter).lower().__contains__("delete holiday"):
                self.admin.deleteHoliday(self.get_input_data_from_row(rowNumber))
        elif str(getParameter).lower().__contains__("edit holiday"):
                self.admin.edit_Holiday(self.get_input_data_from_row(rowNumber))





    def set_admin(self, getParameter, getInputData, getExtraData):
        if str(getParameter).lower().__contains__("new category"):
            self.admin.set_newcategory(getInputData)
        elif str(getParameter).lower().__contains__("edit category name"):
            self.admin.set_editname(getInputData)
        elif str(getParameter).lower().__contains__("category language"):
            self.admin.change_language(getInputData)


        elif str(getParameter).lower().__contains__("new job"):
            self.admin.set_JobTitle(getInputData)
        elif str(getParameter).lower().__contains__("new job code"):
            self.admin.set_JobCode(getInputData)
        elif str(getParameter).lower().__contains__("new job category"):
            self.admin.set_new_jobcategory(getInputData)
        elif str(getParameter).lower().__contains__("new job role"):
            self.admin.set_newjobrole(getInputData)
        elif str(getParameter).lower().__contains__("edit job name"):
            self.admin.edit_name(getInputData)
        elif str(getParameter).lower().__contains__("job integration code"):
            self.admin.edit_intcode(getInputData)


        elif str(getParameter).lower().__contains__("holiday language"):
            self.admin.select_Language(getInputData)
        elif str(getParameter).lower().__contains__("template name"):
            self.admin.set_templateName(getInputData)
        elif str(getParameter).lower().__contains__("apply on"):  # list
            self.admin.new_apply_on(getInputData)
        elif str(getParameter).lower().__contains__("days"):  # list
            self.admin.check_days(getInputData)
        elif str(getParameter).lower().__contains__("holiday name"):
            self.admin.set_HolidayName(getInputData)
        elif str(getParameter).lower().__contains__("holiday date"):
            self.admin.set_HolidayDate(getInputData,getExtraData)
        elif str(getParameter).lower().__contains__("holiday type"):
            self.admin.set_HolidayType(getInputData)
        elif str(getParameter).lower().__contains__("apply on boards"):
            self.admin.editApplyonholiday(getInputData)







   