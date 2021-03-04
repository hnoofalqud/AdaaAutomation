from POM.routes.routes import Routes


class Navigation(Routes):
    """
    # --- CLASS NAVIGATION ---
    # INCLUDES THE MAIN NAVIGATION BUTTONS, AND FIXED ELEMENTS:
    ## - SIDE MENU
    ## - NOTIFICATIONS
    ## - AVATAR
    # GETTERS:
    ## - SIDE MENU GETTERS
    ### - USING ORDER
    ### - USING LABEL
    ### - EACH BUTTON BY ITSELF
    """

    # SIDE MENU NAVIGATION
    _navigationBylabelXpath = "//p[contains(text(),'{0}') and contains(@class,'sidemenu')]"
    _navigationByOrderXpath = "//a[{0}]//div"

    # SIDE MENU NAVIGATION
    _boardsXpath = _navigationByOrderXpath.format(3)  # BOARDS ORDER IS 1 WITHIN THE DOM SIDE MENU
    _inboxXpath = _navigationByOrderXpath.format(5)  # INBOX ORDER IS 2 WITHIN THE DOM SIDE MENU
    _calendarXpath = _navigationByOrderXpath.format(6)  # CALENDAR ORDER IS 3 WITHIN THE DOM SIDE MENU
    _logsXpath = _navigationByOrderXpath.format(7)  # LOGS ORDER IS 4 WITHIN THE DOM SIDE MENU
    _approvalXpath = _navigationByOrderXpath.format(8)  # APPROVAL ORDER IS 5 WITHIN THE DOM SIDE MENU
    _escalationXpath = _navigationByOrderXpath.format(9)
    _reportsXpath = _navigationByOrderXpath.format(10)
    _contactsXpath = _navigationByOrderXpath.format(11)
    _mytasksXpath=_navigationByOrderXpath.format(8)
    _adminxpath=_navigationByOrderXpath.format(14)
    # NOTIFICATIONS
    _notificationsIconXpath = "//span[@class='material-icons notif mat-menu-trigger']"
    _notificationsListXpath = "//div[@class='mat-menu-content']/div"

    # AVATAR ICON
    _avatarIconXpath = "//img[@class='avatar']"
    _notificationsIconXpath = "//img[@class='{0}'".format('avatar')

    def get_navigation_by_label(self, label):
        # CHECK IF FOUND
        xpath = self._navigationBylabelXpath.format(label)
        if self.validate.is_element_found_by_xpath(xpath=xpath):
            return self.webDriver.find_element_by_xpath(xpath)
        else:
            return None

    def get_navigation_by_order(self, order):
        return self.get_web_element(xpath=self._navigationByOrderXpath.format(order))

    # INDIVIDUAL SIDE MENU NAVIGATION BUTTONS GETTERS (RETURNS A WEB ELEMENT IF FOUND)
    def get_boards_btn(self):
        return self.validate.get_web_element(xpath=self._boardsXpath)  # RETURNS A WEB ELEMENT IF FOUND

    def get_inbox_btn(self):
        return self.validate.get_web_element(xpath=self._inboxXpath)  # RETURNS A WEB ELEMENT IF FOUND

    def get_calendar_btn(self):
        return self.validate.get_web_element(xpath=self._calendarXpath)  # RETURNS A WEB ELEMENT IF FOUND

    def get_logs_btn(self):
        return self.validate.get_web_element(xpath=self._logsXpath)  # RETURNS A WEB ELEMENT IF FOUND

    def get_approval_btn(self):
        return self.validate.get_web_element(xpath=self._approvalXpath)  # RETURNS A WEB ELEMENT IF FOUND

    def get_mytasks_btn(self):
        return self.validate.get_web_element(xpath=self._mytasksXpath)  # RETURNS A WEB ELEMENT IF FOUND

    def get_escalation_btn(self):
        return self.validate.get_web_element(xpath=self._escalationXpath)  # RETURNS A WEB ELEMENT IF FOUND

    def get_reports_btn(self):
        return self.validate.get_web_element(xpath=self._reportsXpath)  # RETURNS A WEB ELEMENT IF FOUND

    def get_contacts_btn(self):
        return self.validate.get_web_element(xpath=self._contactsXpath)  # RETURNS A WEB ELEMENT IF FOUND

    def get_admin_btn(self):
        return self.validate.get_web_element(xpath=self._adminxpath)

    def get_notifications_btn(self):
        return self.validate.get_web_element(xpath=self._notificationsIconXpath)  # RETURNS A WEB ELEMENT IF FOUND
    def get_myprofileBtn(self):
        return self.validate.get_web_element(self._avatarIconXpath)
    def navigate_to_page(self, page=""):
        navigateTo = None

        if str(page).lower().__contains__("board"):
            navigateTo = self.get_boards_btn()

        if str(page).lower().__contains__("inbox"):
            navigateTo = self.get_inbox_btn()

        if str(page).lower().__contains__("calendar"):
            navigateTo = self.get_calendar_btn()

        if str(page).lower().__contains__("reports"):
            navigateTo = self.get_reports_btn()

        if str(page).lower().__contains__("escalation"):
            navigateTo = self.get_escalation_btn()
        if str(page).lower().__contains__("approvals"):
            navigateTo = self.get_approval_btn()
        if str(page).lower().__contains__("activity log"):
            navigateTo = self.get_logs_btn()
        if str(page).lower().__contains__("contacts"):
            navigateTo=self.get_contacts_btn()
        if str(page).lower().__contains__("admin"):
            navigateTo=self.get_admin_btn()
        if str(page).lower().__contains__("my tasks"):
            navigateTo=self.get_mytasks_btn()
        if str(page).lower().__contains__("my profile"):
            navigateTo=self.get_myprofileBtn()
        navigateTo.click()
