import time

from POM.routes.routes import Routes


class ToastMsg(Routes):

    # TOAST MSG
    _toastMsg = "//div[contains(text(),'{0}')]"
    _closeToastMsg = "//span[contains(text(),'×')]"
    htmlP = "<p class='toast validation {0}'> {1} </p>"

    def toast_msg_visible(self, msg, notes=""):

        imgHTML = self.validate.takeScreenshot(name=msg)
        self.htmlInfo += imgHTML


        if str(msg).__contains__('required'):
            expectedMsg = 'Please enter the required fields'

        elif str(msg).__contains__('code_defined'):
            expectedMsg = 'Board Code Already Defined'

        elif str(msg).__contains__('name_defined'):
            expectedMsg = 'Arabic Name Already Defined'

        elif str(msg).__contains__('success'):
            expectedMsg = 'Operation completed successfully...'
        elif str(msg).__contains__('Start Date '):
            expectedMsg = 'Start Date must be after dependent Task End Date::updateTask::13'
        elif str(msg).__contains__('File Created'):
            expectedMsg = 'File Created'
        elif str(msg).lower().__contains__('Product Status Can not be Set to Ended While the Progress Is Not 100%'):
            expectedMsg = 'Product Status Can not be Set to Ended While the Progress Is Not 100%'
        elif str(msg).lower().__contains__('Invalid value'):
            expectedMsg="Invalid value(s)"
        else:
            print("CHECK THE CODE FOR THE TOAST MSG -> {0}".format(msg))
            return

        toastMsg = self.validate.get_web_element(self._toastMsg.format(expectedMsg))

        if toastMsg:
            msg = "TOAST MSG IS VISIBLE : {0}".format(toastMsg.text)
            toastMsg.click()
            toastMsg = True

        else:
            msg = "TOAST MSG IS NOT VISIBLE {0}".format(expectedMsg)
            toastMsg = False

        self.htmlInfo += self.htmlP.format(str(toastMsg).lower(), "[{0}] -> {1}".format(notes, msg))




