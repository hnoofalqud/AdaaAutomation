import os

from ExcelToCode.ExcelToCode import ExcelToCode
from POM.login import Login
from POM.routes.Activity_log_page.activitylog import Activitylog
from POM.routes.admin.admin import admin
from POM.routes.boards_page.boards import Boards
from POM.routes.calendar_page.calendar import Calendar
from POM.routes.contacts_page.contacts import Contacts
from POM.routes.escalation_page.escalation import Escalation
from POM.routes.inbox_page.inbox import Inbox
from POM.routes.navigation import Navigation
from POM.routes.reports_page.reports import Reports
from POM.routes.myprofile.myprofile import myprofile
from browser.browser import Browser
from POM.routes.approvals_page.Approvals import approvals
from input_output.Excel import ReadExcel
from POM.routes.mytasks_page.mytasks import Mytasks
from validate.toastMsg import ToastMsg
from validate.validateElement import ValidateElement
from POM.routes.home_page.home import Home
from Files.utilities import Utilities
from datetime import datetime, date


#  TEST 1

startTime = str(str(date.today()) + " " + str(datetime.now().time())[:8])
d1 = str(datetime.now().time())[:8]
htmlInfo = ""
mainHtmlInfo = " "

print(Utilities.welcome)  # PRINTS THE WELCOME MESSAGE

readExcel = ReadExcel()  # Open The Excel File
url = "https://realsoftapps.com/Adaa_New/external/login"  # SET URL
browserChoice = readExcel.getCellFromSheet(sheet="Setup", cell="C2")  # TEST BROWSER
testCase = readExcel.getCellFromSheet(sheet="Setup", cell="C3")  # LIST OF TEST CASES

testCaseList = str(testCase).split(",")
browserObj = Browser()

browserObj.launch(url=url, browser=browserChoice)  # LAUNCH BROWSER + LOAD URL

loginPage = Login(driver=browserObj.driver)
validate = ValidateElement(driver=browserObj.driver)

login = loginPage.login(email="Hanoof.alqadeh@realsoft-me.com", password="Hanoof@123")
# login = loginPage.login(email="Mohammed.aljezawi@mobisoft-me.com", password="Mohammed@123")


if login:
    navigationControls = Navigation(driver=browserObj.driver)
    boardsPage = Boards(driver=browserObj.driver)
    inboxPage = Inbox(driver=browserObj.driver)
    reports = Reports(driver=browserObj.driver)
    toastMsg = ToastMsg(driver=browserObj.driver)
    escalation = Escalation(driver=browserObj.driver)
    approvalsPage = approvals(driver=browserObj.driver)
    activitylogPage = Activitylog(driver=browserObj.driver)
    contactsPage = Contacts(driver=browserObj.driver)
    calendarPage=Calendar(driver=browserObj.driver)
    adminPage = admin(driver=browserObj.driver)
    mytasks= Mytasks(driver=browserObj.driver)
    myprofile=myprofile(driver=browserObj.driver)
    homepage=Home(driver=browserObj.driver)




    for singleTestCase in testCaseList:
        print(singleTestCase)
        excelToCode = ExcelToCode(browserObj, readExcel, str(singleTestCase), navigationControls, boardsPage, inboxPage , toastMsg , reports,calendarPage, escalation ,approvalsPage,activitylogPage,contactsPage,adminPage,mytasks,myprofile,homepage,validate)
        result = excelToCode.read_rows()

        if result == False:
            print("BREAK FROM MAIN")
            mainHtmlInfo = "<p class='general-validation false'> {0} </p>".format(
                "SUDDEN STOP FROM MAIN - TEST NOT COMPLETED")

    htmlInfo += loginPage.htmlInfo + boardsPage.htmlInfo + inboxPage.htmlInfo + validate.htmlInfo + toastMsg.htmlInfo + reports.htmlInfo + excelToCode.htmlInfo + str(mainHtmlInfo)


else:
    htmlInfo += loginPage.htmlInfo
    print("LOGIN FAILED------")

counterTrue = str(htmlInfo).lower().count("true")
counterTrue2 = str(htmlInfo).lower().count("truefinalstep")
counterFalse = str(htmlInfo).lower().count("false")

if counterTrue + counterFalse > 0:
    rate = str((counterTrue / (counterTrue + counterFalse) * 100))[:3] + "%"
else:
    rate = 0

testResultsHTML = """
<div class="mainResults"> 
        <div class="results allBox">
          <div>
            TESTS: {0}
            <br>
            <i class="fas fa-vials"></i>
          </div>
        </div>
        
         <div class="results allBox">
          <div>
            RATE: 
            <br>
            {1}
          </div>
        </div>
 
        <div class="results greenBox">
          <div>
            PASS: {2}
            <br>
            <i class="fas fa-check-circle"></i>
          </div>
        </div>

        <div class="results redBox">
          <div>
            FAIL: {3}
            <br>
            <i class="fas fa-times-circle"></i>
         </div>
        </div>
 
  </div>
""".format((counterTrue + counterFalse), rate, counterTrue,
           counterFalse)

endTime = str(str(date.today()) + " " + str(datetime.now().time())[:8])
d2 = str(datetime.now().time())[:8]
duration = datetime.strptime(d2, '%H:%M:%S') - datetime.strptime(d1, '%H:%M:%S')

htmlCode = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">

    <title>PYTHON</title>
    <link rel="stylesheet" href="app.css">
        <script src="app.js" defer></script>

</head>
<body>

<div class="div-center card">

    <div class="mainResults2">
    <img src="http://www.realsoft-me.com/images/LogoSlogan.png" alt="">
  </div>

<div class="headInfo">
 TEST ID: {0} </br>
TEST DESCRIPTION: {1} <hr>
 BROWSER: CHROME <br>
 OS: WINDOWS
 
 </div>

 <div class="mainResults2">

 <div class="results2 allBox2"> START TIME
        <br> {2}
      </div>
      
            <div class="results2 allBox2"> END TIME
        <br> {3}
      </div>
      
                <div class="results2 allBox2"> DURATION
        <br> {4}
      </div>
           

<div style="margin: 0 4%;">
<button onclick="toggleLogin()"> Login Details </button>
<button onclick="toggleBoard()"> Board Details </button>
<button onclick="toggleInbox()"> Inbox Details </button>
<button onclick="toggleCalendar()"> Calendar Details </button>
<button onclick="toggleGeneral()"> General Details </button>
<button onclick="toggleScreenShots()"> Toggle Screenshots </button>
<button onclick="toggleAll()"> Toggle All </button>


</div>

 </div>

<div id="myDIV">

    {5}

</div>    



</div>    
</body>
</html>

""".format("TC", "THIS TEST AIMS TO TEST THE TEST", startTime, endTime, duration, (htmlInfo + testResultsHTML))

css = """
p.false:hover{background: #ab2222;}
.mainResults{flex-wrap:wrap;display:flex;justify-content:center}
.results{border-radius:20px;color:#fff;width:170px;height:170px;font-size:35px;text-align:center;display:flex;justify-content:center;align-items:center;margin:10px;line-height:65px}
.redBox{background-color:red;background:linear-gradient(to bottom,#9a2b2b 5%,#ad3030 100%)}
.greenBox{background-color:green;background:linear-gradient(to bottom,#72b352 5%,#77b55a 100%)}
.allBox{background-color:green;background:linear-gradient(to bottom,#8f928d 5%,#9aa097 100%)}
h2{color:green;background:#ffffd1;display:inline-block;border-radius:20px;padding:5px;padding-left:20px;padding-right:20px;margin-top:5px;margin-bottom:0}
.validation{color:#000;margin-left:20px}.false{color:white; background: linear-gradient(to bottom,#ca1212 5%,#d81b1b 100%);}.true{color:green}
body{background:#b7b5b2;margin:0;padding:10px}
button{box-shadow:0 10px 14px -7px #6a7188;
background:linear-gradient(to bottom,#343a65 5%,#4f568a 100%);
background-color:#77b55a;border-radius:4px;border:1px solid #171f5f;display:inline-block;cursor:pointer;color:#fff;font-family:Arial;font-size:13px;font-weight:700;padding:6px 12px;text-decoration:none;text-shadow:0 1px 0 #171f5f;margin-bottom:20px;margin-left:auto;margin-right:auto;font-size:12px}button:hover{background: linear-gradient(to bottom,#00185d 5%,#061946 100%);background-color:#72b352}button:active{position:relative;top:1px}a{margin-bottom:15px;display:inline-block;margin-left:20px}a:link{font-size:20px;text-decoration:none;color:#060;background-color:#CF0}a:visited{color:#090}a:hover{color:#9C0}.div-center{margin:auto;width:60%;border:3px solid #778a77;padding:10px}h4{margin:20px}
h3{
border-radius: 13px;
    text-align: center;
    color: #4f568a;
    background: #d8cfc2;
    margin-top: 5px;
    margin-bottom: 10px;
    padding: 6px;
}

.allBox2{background-color:green;background:linear-gradient(to bottom,#b2c3a9 5%,#a2ad9c 100%)}.mainResults2{flex-wrap:wrap;display:flex;justify-content:center}.results2{border-radius:20px;width:240px;height:100px;font-size:20px;text-align:center;display:flex;justify-content:center;align-items:center;margin: 7px;margin-bottom: 15px;}

.card {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    border-radius: 10px;
    background: #f3ece3;}
    
.validation:hover {
    background: #dac7fb;}
    
p{
    padding: 10px;
    margin: 6px;
    border-radius: 15px;
}

.headInfo{
color: #3b416e;
    font-size: 19px;
    background: #aab8a3;
    border-radius: 20px;
    padding: 11px 10px;
    margin: 8px 28px;
    line-height: 30px;
    text-align: center;
    font-weight: 700;
}
"""


js = """
  var list = document.getElementsByClassName("validation")
  for (let x of list){
    x.style.visibility = 'hidden';
        x.style.display = 'none';
  }

function toggleLogin() {
  var list = document.getElementsByClassName("login")

  for (let x of list){
  if (x.style.visibility === 'hidden') {
    x.style.visibility = 'visible';
    x.style.display = 'inherit';
  } else {
    x.style.visibility = 'hidden';
        x.style.display = 'none';

  }

  }
}

function toggleInbox() {
  var list = document.getElementsByClassName("inbox")

  for (let x of list){
  if (x.style.visibility === 'hidden') {
    x.style.visibility = 'visible';
    x.style.display = 'inherit';
  } else {
    x.style.visibility = 'hidden';
        x.style.display = 'none';

  }

  }
}
function toggleCalendar() {
  var list = document.getElementsByClassName("Calendar")

  for (let x of list){
  if (x.style.visibility === 'hidden') {
    x.style.visibility = 'visible';
    x.style.display = 'inherit';
  } else {
    x.style.visibility = 'hidden';
        x.style.display = 'none';

  }

  }
}
function toggleBoard() {
  var list = document.getElementsByClassName("board")

  for (let x of list){
  if (x.style.visibility === 'hidden') {
    x.style.visibility = 'visible';
    x.style.display = 'inherit';
  } else {
    x.style.visibility = 'hidden';
        x.style.display = 'none';

  }

  }
}

function toggleGeneral() {
  var list = document.getElementsByClassName("toast")
  for (let x of list){
  if (x.style.visibility === 'hidden') {
    x.style.visibility = 'visible';
    x.style.display = 'inherit';
  } else {
    x.style.visibility = 'hidden';
        x.style.display = 'none';

  }

  }
}

function toggleAll() {
  var list = document.getElementsByClassName("validation")
  for (let x of list){
  if (x.style.visibility === 'hidden') {
    x.style.visibility = 'visible';
    x.style.display = 'inherit';
  } else {
    x.style.visibility = 'hidden';
        x.style.display = 'none';

  }

  }
}

function toggleScreenShots() {
  var list = document.getElementsByClassName("screenshot")
  for (let x of list){
  if (x.style.visibility === 'hidden') {
    x.style.visibility = 'visible';
    x.style.display = 'inherit';
  } else {
    x.style.visibility = 'hidden';
        x.style.display = 'none';

  }

  }
}
"""

with open("test.html", "w") as with_as_write:
    with_as_write.write(htmlCode)

with open("app.css", "w") as with_as_write:
    with_as_write.write(css)

with open("app.js", "w") as with_as_write:
    with_as_write.write(js)

print(Utilities.done)
