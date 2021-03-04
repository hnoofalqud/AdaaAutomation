from POM.routes.routes import Routes


class Home(Routes):

    _TasksDueSoonXpath="//p[contains(text(),'Tasks Due Soon ')]"
    _DueTasksXpath="//p[contains(text(),'Due tasks ')]"
    _RecenetBoardsXpath="//mat-panel-title[contains(text(),'Recent Boards')]"
    _TopDashboardsXpath="//mat-panel-title[contains(text(),'Top Dashboards')]"
    _SeeAllMyTasksXpath="//p[contains(text(),'See all my tasks')]"

    _TaskDueSoonOpenTaskXpath="//mat-expansion-panel[1]/div/div/app-home-tasks[1]/table[1]/tbody[1]/tr[{0}]//td[2]" #BY ORDER
    _OpenMembersXpath="//mat-expansion-panel[1]/div/div/app-home-tasks[1]/table[1]/tbody[1]/tr[{0}]//td[4]" #BY ORDER

    _DueSoonOpenTaskXpath="//mat-expansion-panel[2]//app-home-tasks[1]/table[1]/tbody[1]/tr[{0}]/td[2]"
    _OpenBoardXpath="//span[contains(text(),'{0}')]" #BY LABEL

    def expand_tabs(self,option):
        if str(option).lower() == "tasks due soon" :
            self.validate.get_web_element(self._TasksDueSoonXpath).click()
        elif str(option).lower() == "due tasks":
            self.validate.get_web_element(self._DueTasksXpath).click()
        elif str(option).lower()== "recent boards":
            self.validate.get_web_element(self._RecenetBoardsXpath).click()
        elif str(option).lower()== "top dashboards":
            self.validate.get_web_element(self._TopDashboardsXpath).click()
        else:
            print("the tab is not exist")

    def open_Task(self,order):
        self.validate.get_web_element(self._OpenTaskXpath.format(order)).click()
    def open_Members(self,order):
        self.validate.get_web_element(self._OpenMembersXpath.format(order)).click()

    def See_all(self):
        self.validate.get_web_element(self._SeeAllMyTasksXpath).click()

    def openBoards(self,name):
        #RECENT BOARDS
        self.validate.get_web_element(self._OpenBoardXpath.format(name)).click()

    def tasks(self,option,order):
        if str(option).lower()== "tasks due soon":
            self.validate.get_web_element(self._TaskDueSoonOpenTaskXpath.format(order)).click()
        elif str(option).lower() == "due task" :
            self.validate.get_web_element(self._DueSoonOpenTaskXpath.format(order)).click()
        else:
            print("COULDN'T FIND THE TASK")