from ObjectRepository.Forms.Object_FormNEC import *
from ObjectRepository.Forms.Object_FormDIV import *
from ObjectRepository.Forms.Object_Form1098T import *
from ObjectRepository.Forms.Object_FormLTC import *
from ObjectRepository.Forms.Object_FormMISC import *
from ObjectRepository.Forms.Object_FormG import *
from ObjectRepository.Forms.Object_Form1098T import *
from ObjectRepository.Forms.Object_Form1042S import *
from ObjectRepository.Forms.Object_Form1098 import *

from ObjectRepository.Generic.Login import *
from Support.Generic.Support import *
from Support.Generic.Reports import *
from Support.Generic.Common import *
from faker import Faker
import time

fake = Faker()

def login(page):
    env = get_config()
    page.goto(env['url'])
    time.sleep(5)
    if page.locator("//input[@id='Passwordfeild']").is_visible():
        page.fill("//input[@id='Passwordfeild']", "spanqatesting")
        page.click("//span[contains(normalize-space(.), 'Continue')]")
        time.sleep(5)
    page.fill(Object_Username, env['username'])
    page.fill(Object_Password, env['password'])
    page.click(Object_signin)
    time.sleep(5)
        
    try:
        page.wait_for_selector(
            "//span[contains(text(),'Two-Factor Authentication')]",
            timeout=5000
        )

        print("2FA detected → skipping")

        page.locator(Object_IlldoitLater).click()
        page.locator("//span[normalize-space()='Yes, I want to skip']").click()

        # wait until 2FA modal disappears
        page.wait_for_selector(
            "//span[contains(text(),'Two-Factor Authentication')]",
            state="detached",
            timeout=10000
        )

    except:
        print("2FA not shown → continuing")

    popup = page.locator("//div[text()=' PRODUCTS ']/parent::div/button")
    try:
        popup.wait_for(state="visible", timeout=10000)
        popup.wait_for(state="attached")
        popup.wait_for(state="enabled")

        popup.click(timeout=30000, force=True)

    except Exception as normal_click_error:
        print("Normal click failed → Trying JS click...")

        try:
            handle = popup.element_handle(timeout=5000)
            if handle:
                page.evaluate_handle("(el) => el.click()", handle)
            else:
                print("Element not found for JS click")
        except Exception as js_error:
            print("JS click failed:", js_error)
    # if popup.is_visible():
        # try:
        #     popup.click(timeout=30000, force=True)
        # except:
        #     handle = popup.element_handle()
        #     if handle:
        #         page.evaluate("(el) => el.click()", handle)
        #     else:
        #         print("Unable to get popup element handle")
   
def go_to_form(page, test_data):
    form = test_data.get("Form")
    row = test_data.get("Row")
    scenario_id = test_data.get("Scenario_ID")
    result = test_data.get("Result", "")
    time.sleep(10)
    page.click("(//span[@class='TBS-arrow-down ms-1 fs-10px mt-1'])")
    page.click("//p[contains(text(),'1099/W-2 Dashboard')]")

    form_details = read_excel(form, row, "FormSelection")


    # Click Start New Form
    # page.click("(//span[contains(text(),'Start New')])[2]")
    page.click("//span[text()=' 1099/W-2 ']")
    page.click("//p[contains(text(),'Start New Form')]")

    # Handle form selection
    if form_details == "NEC":
        page.click(Object_FormNEC_Navigation)
        page.click(Object_FormNEC_Navigation_2025)
    elif form_details == "DIV":
        page.click(Object_select1095CCAstate)
        page.click(Object_Form1095CCAstate)
    

    # Screenshot
    add_screenshot(page, scenario_id)

    # Update test data
    test_data["Status"] = True
    test_data["Result"] = f"{result}Navigated to Form "
    return test_data


def go_to_1099HC_form(page, test_data):
    form = test_data.get("Form")
    row = test_data.get("Row")
    scenario_id = test_data.get("Scenario_ID")
    result = test_data.get("Result", "")
    time.sleep(5)
    page.click("(//span[@class='TBS-arrow-down ms-1 fs-10px mt-1'])[4]")
    page.click("//p[contains(text(),'ACA Dashboard')]")

    form_details = read_excel(form, row, "FormSelection")
    page.click("//span[text()=' ACA ']")
    page.click("//p[contains(text(),'Start New Form')]")

    if form_details == "MA State":
        page.click(Object_Form1099HC)
        page.click(Object_select1099HCform)
    else:
        print("MA form not Selected")
    
    add_screenshot(page,scenario_id)

    test_data["Status"] = True
    test_data["Result"] = f"{result}Navigated to Form "
    return test_data


def add_employer(page, test_data):
    # --- Get values from test_data dict ---
    Form = test_data.get("Form")
    row = test_data.get("Row")
    Scenario_ID = test_data.get("Scenario_ID")
    Result = test_data.get("Result", "")
    PayerType = test_data.get("PayerType")
    sheet_name = Form
    Payer = read_excel(sheet_name, row, PayerType)
    PayerTIN = read_excel(sheet_name, row, f"{Payer} TIN")
    Country = read_excel(sheet_name, row, f"{Payer} Country")
    Form_Action = read_excel(sheet_name, row, "Form_Action")
    type = read_excel(sheet_name, row, "Type")
    ErrorMessage = read_excel(sheet_name, row, "Error Message")
    Module = read_excel(sheet_name, row, "Module")
    Type = test_data.get("Type")

    #----> Need to ask Sruthi
    
    PayerName = "TBS TESTING"
    FirstName = "Sruthi"
    LastName = "test"
    Tin = fake_ein()
    Email = "davidrajan.a@spantechnologyservices.com"
    PhoneNumber = "8685961234"
    Address = {
    "AddressLine1": "123 Main St",
    "City": "Anytown",
    "State": "California (CA)",
    "Zipcode": "90011",
    "Country": "United States"
    }

    AddressLine1 = Address["AddressLine1"]
    City = Address["City"]
    State = Address["State"]
    Zipcode = Address["Zipcode"]
    Country = Address["Country"]


    # Other Excel values
    MaxChar_Employer = read_excel(sheet_name, row, "Max char - Employer")
    TradeName_Employer = read_excel(sheet_name, row, "Trade Name")
    ReferenceNumber = read_excel(sheet_name, row, "Reference Number")
    AddressLine1_Employer = read_excel(sheet_name, row, "Address Line 1")
    AddressLine2_Employer = read_excel(sheet_name, row, "Address Line 2")
    City_Employer = read_excel(sheet_name, row, "City")
    State_Employer = read_excel(sheet_name, row, "StateEmployer")
    Zipcode_Employer = read_excel(sheet_name, row, "ZIPcodeEmployer")
    FirstNameValid = read_excel(sheet_name, row, "First Name")
    MiddleNameValid = read_excel(sheet_name, row, "Middle Name")
    LastNameValid = read_excel(sheet_name, row, "Last Name")
    Suffix = read_excel(sheet_name, row, "Suffix")
    EmailAddress = read_excel(sheet_name, row, "Email Address")
    PhoneNumberValid = read_excel(sheet_name, row, "Phone Number")
    SigningAuthorityName = read_excel(sheet_name, row, "Signing Authority Name")
    SigningAuthorityTitle = read_excel(sheet_name, row, "Signing Authority Title")

    # DGE Details
    DGEBA = read_excel(sheet_name, row, "DGEBA")
    DGETradeName = read_excel(sheet_name, row, "DGETradeName")
    DGEAL1 = read_excel(sheet_name, row, "DGEAL1")
    DGEAL2 = read_excel(sheet_name, row, "DGEAL2")
    DGECity = read_excel(sheet_name, row, "DGECity")
    DGEState = read_excel(sheet_name, row, "DGEState")
    DGEZIP = read_excel(sheet_name, row, "DGEZIP")
    DGEFN = read_excel(sheet_name, row, "DGEFN")
    DGEMN = read_excel(sheet_name, row, "DGEMN")
    DGELN = read_excel(sheet_name, row, "DGELN")
    DGEPhonenumber = read_excel(sheet_name, row, "DGEPhonenumber")

    # BusinessName = PayerName

    # --- Start automation logic ---
    
    if Payer == "CHOOSE":
        page.click('//span[text()=" Select Employer from Address Book "]')
        page.click('(//*[text()="Select Employer"])[1]')
        page.fill(Object_totalno, "20")

        if Form == "1099HC":
            page.click("//span[text() = 'Continue to Form 1099-HC ']")
        else:
            page.click('//span[text()="Continue to Form 1095-C "]')

    elif Payer == "NULL":
        page.click(Object_Addnewemployer)
        page.click(Object_saveandcontinue)
        page.fill(Object_EIN, Tin)
        page.fill(Object_EmployerName, PayerName)
        page.click(Object_PayerCountryCode)
        page.click(f"//*[contains(text(),'{Country}')]")
        page.fill(Object_PayerAddress1, AddressLine1)
        page.fill(Object_Payercity, City)
        time.sleep(5)
        page.click(Object_PayerStateOrProvince)
        time.sleep(3)
        page.click(f"//*[contains(text(),'{State}')]")
        page.fill(Object_PayerZipOrPostalCode, Zipcode)
        page.fill(Object_EmailAddress, Email)
        page.fill(Object_Phonenumber, PhoneNumber)
        page.fill(Object_PayerFirstName, FirstName)
        page.fill(Object_PayerLastName, LastName)
        page.click(Object_saveandcontinue)
        page.click(Object_ignore)
        page.fill(Object_totalno, "20")
        page.click(Object_continue)
    
    elif Payer == "ADD":
        # if PayerTIN == "EIN":
        #     print("Payer TIN is EIN")
        if sheet_name == "1095B":
            page.click("//span[text()=' Add Filer']") 
            page.fill(Object_EIN, Tin)  
        elif sheet_name == "1094_1095C":
            page.click(Object_Addnewemployer)  
            page.fill(Object_EIN, Tin)  
        elif sheet_name == "1099HC":
            page.click(Object_Addnewemployer) 
            page.fill(Object_EIN, Tin)
        else:
            print("Form is other than 1095B, 1094_1095C and 1099HC")
            page.fill(Object_EIN, Tin)
        page.fill(Object_EmployerName, PayerName)
        page.click(Object_PayerCountryCode)
        page.click(f"//*[contains(text(),'{Country}')]")
        page.fill(Object_PayerAddress1, AddressLine1)
        page.fill(Object_Payercity, City)
        page.click(Object_PayerStateOrProvince)
        time.sleep(3)
        page.click(f"//*[contains(text(),'{State}')]")
        page.fill(Object_PayerZipOrPostalCode, Zipcode)
        page.fill(Object_EmailAddress, Email)
        page.fill(Object_Phonenumber, PhoneNumber)
        page.fill(Object_PayerFirstName, FirstName)
        page.fill(Object_PayerLastName, LastName)
        page.click(Object_saveandcontinue)
        page.click(Object_ignore)
        time.sleep(5)
        if Form == "1095B":
            page.click("//span[text()='Continue to Form 1095-B ']")
        elif Form == "1099HC":
            page.click("//span[text() = 'Continue to Form 1099-HC ']")
        else:
            page.fill(Object_totalno, "20")
            page.click(Object_continue)
        # page.click('(//button[@id="save"])[1]')
        # page.click('(//button[@id="save"])[2]')
        # if Country == "United States of America (US)":
        #     page.click(Object_AddressValid)
        #     page.click(Object_AddressUSPSRecommended)   
        #     page.click(Object_IgnoreAndContinue)
        # if type == "Negative":
        #     status = page.locator(f"//*[contains(text(),'{ErrorMessage}')]").is_visible()
        #     if status:
        #         Result = "Correct Alert" 
        #     else:
        #         Result = "Alert Issue"
        #     if Module == "PAYER":
        #         generate_report(page, status, Result,test_data)
        #     else: 
        #         pass
        # else:
        # form_status = page.locator(Object_ChangePayer).is_visible() or \
        #                 page.locator("//*[contains(text(),'Error occured')]").is_visible()
        # add_screenshot(page, Scenario_ID)
        # if form_status:
        #     Result = f"{PayerType} Saved" 
        # else:
        #     Result = "Payer Not Saved"
        # test_data["Result"] = Result    
        # print(f"Final Result: {Result}")
        return test_data

            

    elif Payer == "CHANGE":
        page.click(Object_Addnewemployer)
        if PayerTIN == "EIN":
            page.click(Object_EIN)
        if PayerTIN == "SSN":
            page.click(Object_SSN)
        page.click(Object_EmployerName)
        page.fill(Object_PayerTIN, Tin)
        page.click(Object_PayerCountryCode)
        page.click(f"//*[contains(text(),'{Country}')]")
        page.fill(Object_PayerAddress1, AddressLine1)
        page.fill(Object_Payercity, City)
        page.click(Object_PayerStateOrProvince)
        page.click(f"//*[contains(text(),'{State}')]")
        time.sleep(5)
        page.fill(Object_PayerZipOrPostalCode, Zipcode)
        page.fill(Object_EmailAddress, Email)
        page.fill(Object_Phonenumber, PhoneNumber)
        page.click('(//button[@id="save"])[1]')
        page.click('(//button[@id="save"])[2]')

    elif Payer == "Valid":
        page.click(Object_Addnewemployer)
        page.fill(Object_EmployerName, MaxChar_Employer)
        page.fill(Object_Trade_name, TradeName_Employer)
        page.fill(Object_EIN, Tin)
        page.fill(Object_PayerAddress1, AddressLine1_Employer)
        page.fill(Object_PayerAddress2, AddressLine2_Employer)
        page.fill(Object_Payercity, City_Employer)
        page.click(Object_PayerStateOrProvince)
        page.click(f"//*[contains(text(),'{State_Employer}')]")
        page.fill(Object_PayerZipOrPostalCode, Zipcode_Employer)
        page.fill(Object_PayerFirstName, FirstNameValid)
        page.fill(Object_PayerMiddleName, MiddleNameValid)
        page.fill(Object_PayerLastName, LastNameValid)
        page.click(Object_PayerSuffix)
        page.click(f"//*[contains(text(),'{Suffix}')]")
        page.fill(Object_EmailAddress, EmailAddress)
        page.fill(Object_Phonenumber, PhoneNumberValid)
        page.click(Object_SigningAuthorityName)
        page.click(Object_SigningAuthorityTitle)
        # DGE Details
        page.click(Object_DGE)
        page.click(Object_DGEcheckbox)
        page.fill(Object_DGEBusinessname, DGEBA)
        page.fill(Object_DGETradename, DGETradeName)
        page.fill(Object_DGEEIN, Tin)
        page.fill(Object_DGEAddressline1, DGEAL1)
        page.fill(Object_DGEAddressline2, DGEAL2)
        page.fill(Object_DGECity, DGECity)
        page.click(Object_DGEstate)
        page.click(f"//*[contains(text(),'{DGEState}')]")
        page.fill(Object_DGEZipcode, DGEZIP)
        page.fill(Object_DGEFN, DGEFN)
        page.fill(Object_DGEMN, DGEMN)
        page.fill(Object_DGELN, DGELN)
        page.fill(Object_DGEPN, DGEPhonenumber)
        page.click(Object_saveandcontinue)
        time.sleep(5)
        page.click(Object_ignore)
        page.fill(Object_totalno, "20")
        page.click(Object_continue)

    elif Payer == "Invalid":
        # Same as Valid but add screenshot and exception handling
        pass

    test_data["Result"] = f"{Result}; Employer Added"
    return test_data

def Selecting_Employee_from_Address_Book(page):
    page.click('//*[text()=" Select Employee from Address Book "]')
    page.click('(//span[text()="Select Employee"])[1]')

def add_employee(page, TestData):
    Form = TestData.get("Form")
    Row = TestData.get("Row")
    Scenario_ID = TestData.get("Scenario_ID")
    Result = TestData.get("Result")
    RecipientType = TestData.get("RecipientType")
    Sheet = Form

    Recipient = read_excel(Sheet, Row, RecipientType)
    RecipientTIN = read_excel(Sheet, Row, f"{RecipientType} TIN")
    Country = read_excel(Sheet, Row, f"{RecipientType} Country")
    Form_Action = read_excel(Sheet, Row, "Form_Action")
    Type = read_excel(Sheet, Row, "Type")
    ErrorMessage = read_excel(Sheet, Row, "ErrorMessage")
    Module = read_excel(Sheet, Row, "Module")


    Line14_All12Months = read_excel(Sheet, Row, "Line14_All12Months")
    Plan_Start_month = read_excel(Sheet, Row, "Plan_Start_month")

    FirstName = fake.first_name()
    TestData["FirstName"] = FirstName
    LastName = fake.last_name()
    TIN = fake.ssn()
    Email = f"davidrajan.a+{FirstName}@spantechnologyservices.com"
    PhoneNumber = "8300520076"
    DBA = fake.company()

    AddressLine1 = fake.street_address()
    City = fake.city()
    State, Zipcode = random_us_state_zip()
    Country = Country[0:2]
    TestData[State] = State

    if Recipient == "CHOOSE":
        page.click("(//*[text()=' Select Employee from Address Book '])")
        page.click("(//span[text() ='Select Employee'])[1]")
        time.sleep(5)
        if Form == "1099HC":
            page.click(Object_Subs)
            page.fill(Object_Subs, "999999999")
            time.sleep(5)
            page.click("(//input[@aria-label ='DOB'])[3]")
            time.sleep(5)
            page.fill("(//input[@aria-label ='DOB'])[3]", "01/07/2002")  
            time.sleep(5)

            page.click("(//button[.//span[contains(normalize-space(.), 'Save') and contains(., 'Continue')]])[2]")   
            page.click(Object_ignore)
            page.click("//label[text()='Full-year minimum creditable coverage?']/following-sibling::div/div/div/span[1]")
            page.click("//span[text() ='Save & Continue ']")
            page.click(Object_formdistribution)

        print("inside Choose")

    elif Recipient == "ADD":
        page.click(Object_newemployee)
        if RecipientTIN == "SSN":
            page.fill(Object_ssn1095C, TIN)
            page.fill(Object_firstname, FirstName)
            page.fill(Object_lastname, LastName)

        elif RecipientTIN == "TIN Not Provide":
            page.fill(Object_ssn1095C, TIN)

        page.click("//*[text()=' Country ']/parent::div/div")

        #Country Have to Ask with Sruthi -- now IM bypaasing this step
        # page.fill(f"//input[@aria-label='Country' and @value='{Country}']") 


        page.fill(Object_Addressline11095C, AddressLine1)
        page.fill(Object_city1095C, City)
        page.click("//*[text()='State']/parent::div/div")
        page.click(f"//*[contains(text(),'{State}')]")
        if Form == "LTC":
            page.fill("(//input[@id='zipcode'])[2]", Zipcode)
        else:
            page.fill(Object_zipcode1095C, Zipcode)
        page.fill(Object_emailaddress1095c, Email)
        page.fill(Object_phonenumber1095C, PhoneNumber)
        page.click(Object_saveandcontinue)
        page.click(Object_ignore)
        time.sleep(5)   
        TestData["Recipient_TIN"] = TIN
        TestData["Result"] = f"{Result}; Employee Added"
        return TestData
    
    elif Recipient == "NO":
        page.click(Object_newemployee)
        DOB = fake.date_of_birth(minimum_age=18, maximum_age=120).strftime("%m/%d/%Y")
        Subs = random.randint(99999999, 99999999999)
        page.fill("(//input[@aria-label ='DOB'])[3]", DOB)    

        page.fill(Object_firstname, FirstName)
        page.fill(Object_lastname, LastName)
        page.fill(Object_Addressline11095C, AddressLine1)
        page.fill(Object_city1095C, City)
        page.click(Object_Subs)
        page.fill(Object_Subs, "999999999")
        page.click("//*[text()='State']/parent::div/div")
        page.click(f"//*[contains(text(),'Massachusetts (MA)')]")
        if Form == "LTC":
            page.fill("(//input[@id='zipcode'])[2]", "02115")
        else:
            page.fill(Object_zipcode1095C, "02115")
        # page.fill(Object_emailaddress1095c, Email)
        # page.fill(Object_phonenumber1095C, PhoneNumber)
        page.click("(//button[.//span[contains(normalize-space(.), 'Save') and contains(., 'Continue')]])[2]")   
        page.click(Object_ignore)
        # page.click("//span[normalize-space(text())='Yes']")
        page.click("//input[@id ='ein']")
        page.click("(//button[.//span[contains(normalize-space(.), 'Save') and contains(., 'Continue')]])")
        TestData["Result"] = f"{Result}; Employee Added"

    elif Recipient == "NULL":
        page.click(Object_newemployee)
        page.click(Object_saveandcontinue1095C)
        page.click('//span[text()="Add Employee"]/parent::div/button')
        Selecting_Employee_from_Address_Book(page)

    elif Recipient == "CHANGE":
        if RecipientTIN == "SSN":
            page.fill(Object_ssn1095C, TIN)
            page.fill(Object_firstname, FirstName)
            page.fill(Object_lastname, LastName)
        # elif RecipientTIN == "EIN":
        # elif RecipientTIN == "DOB":
        else: 
            pass

        page.fill(Object_Trade_name, DBA)
        page.click('//*[@id="countrycode"]/parent::div')
        page.fill(f"//*[contains(text(),'{Country}')]")
        page.fill(Object_Addressline11095C, AddressLine1)
        page.fill(Object_city1095C, City)
        page.click('//*[@id="statecode"]/parent::div')
        page.fill(f"//*[contains(text(),'{State}')]")
        page.fill(Object_zipcode1095C, Zipcode)
        page.wait_for_timeout(5000)
        page.fill(Object_emailaddress1095c, Email)
        page.fill(Object_phonenumber1095C, PhoneNumber)
        time.sleep(5)   
        page.click(Object_saveandcontinue)
        page.click(Object_ignore)

    if Recipient == "CHOOSE":
        page.click('//td[text()=" Offer of Coverage (enter required code) "]/following-sibling::td)[1]/div')
        page.click(f"//*[contains(text(),'{Line14_All12Months}')]")
        page.click('//input[@id="planstartmonth"]/parent::div/parent::div/following-sibling::div/i')
        page.click(f"//*[contains(text(),'{Plan_Start_month}')]")
        page.click(Object_saveandcontinue1095Cemployee)
        time.sleep(5)

    else:
        try:
            page.click(Object_saveandcontinue1095C)
        except:
            time.sleep(3)
            page.click('//td[text()=" Offer of Coverage (enter required code) "]/following-sibling::td)[1]/div')
            page.click(f"//*[contains(text(),'{Line14_All12Months}')]")
            page.click('//input[@id="planstartmonth"]/parent::div/parent::div/following-sibling::div/i')
            page.click(f"//*[contains(text(),'{Plan_Start_month}')]")
            page.click(Object_saveandcontinue1095Cemployee)
            time.sleep(5)

    TestData["Recipient_TIN"] = TIN
    TestData["Result"] = Result
    return TestData

def add_recipient(page, TestData):
    Form = TestData.get("Form")
    Row = TestData.get("Row")
    Scenario_ID = TestData.get("Scenario_ID")
    Result = TestData.get("Result")
    RecipientType = TestData.get("RecipientType")
    Sheet = Form

    Recipient = read_excel(Sheet, Row, RecipientType)
    RecipientTIN = read_excel(Sheet, Row, f"{RecipientType} TIN")
    Country = read_excel(Sheet, Row, f"{RecipientType} Country")
    Form_Action = read_excel(Sheet, Row, "Form_Action")
    Type = read_excel(Sheet, Row, "Type")
    ErrorMessage = read_excel(Sheet, Row, "ErrorMessage")
    Module = read_excel(Sheet, Row, "Module")

    firstName = fake.first_name()
    ResposibleIndividual = fake.company()

    LastName = fake.last_name()
    SSN = fake.ssn()
    EIN = fake_ein()
    if RecipientTIN == "SSN":
        TIN = SSN
        FirstName = firstName
    else:
        TIN = EIN
        FirstName = ResposibleIndividual
    TestData["FirstName"] = FirstName

    # Email = f"davidrajan.a+{FirstName.strip().split()[0]}@spantechnologyservices.com"
    import re
    Email = f"davidrajan.a+{re.sub(r'[^A-Za-z ]', '', FirstName).strip().split()[0]}@spantechnologyservices.com"

    PhoneNumber = "8300520076"
    DBA = fake.company()

    AddressLine1 = fake.street_address()
    City = fake.city()
    State, Zipcode = random_us_state_zip()
    Country = Country[0:2]
    TestData[State] = State

    if Recipient == "CHOOSE":
        page.click("(//*[text()=' Select Employee from Address Book '])")
        page.click("//td/button")
    elif Recipient == "ADD":
        page.click(Object_newrecipient)
        if RecipientTIN == "SSN":
            page.fill(Object_ssn1095C, TIN)
            page.fill(Object_firstname, FirstName)
            page.fill(Object_lastname, LastName)
        elif RecipientTIN == "EIN":
            page.click(Object_RecipientEIN)
            page.fill(Object_ein1095B, TIN)
            page.fill(Object_ResponsibleIndividual, FirstName)
        elif RecipientTIN == "DOB":
            page.click(Object_dob1095B)
            page.fill(Object_dobfield, "01/15/1985")
            page.fill(Object_firstname, FirstName)
            page.fill(Object_lastname, LastName)

        page.click("//*[text()=' Country ']/parent::div/div")

        #Country Have to Ask with Sruthi -- now IM bypaasing this step
        # page.fill(f"//input[@aria-label='Country' and @value='{Country}']") 


        page.fill(Object_Addressline11095C, AddressLine1)
        page.fill(Object_city1095C, City)
        page.click("//*[text()='State']/parent::div/div")
        page.click(f"//*[contains(text(),'{State}')]")
        if Form == "LTC":
            page.fill("(//input[@id='zipcode'])[2]", Zipcode)
        else:
            page.fill(Object_zipcode1095C, Zipcode)
        page.fill(Object_emailaddress1095c, Email)
        page.fill(Object_phonenumber1095C, PhoneNumber)
        page.click(Object_saveandcontinue)
        page.click(Object_ignore)
        time.sleep(5)   
        TestData["Recipient_TIN"] = TIN
        TestData["Result"] = f"{Result}; Employee Added"
        return TestData



def bulk_upload_1095c(page, test_data, projectDirectory):

    Form = test_data.get("Form")
    Row = test_data.get("Row")
    Scenario_ID = test_data.get("Scenario_ID")
    Result = test_data.get("Result", "")
    RecipientType = test_data.get("RecipientType")
    Sheet = Form

    Recipient = read_excel(Sheet, Row, RecipientType)
    RecipientTIN = read_excel(Sheet, Row, f"{RecipientType}TIN")
    Country = read_excel(Sheet, Row, f"{RecipientType}Country")
    Form_Action = read_excel(Sheet, Row, "Form_Action")
    Type = read_excel(Sheet, Row, "Type")
    ErrorMessage = read_excel(Sheet, Row, "ErrorMessage")
    Module = read_excel(Sheet, Row, "Module")
    Scenario = read_excel(Sheet, Row, "Recipient Count")
    TIN = test_data.get("tin", RecipientTIN)

    try:
        page.click(Object_BulkImporttoggle)
        time.sleep(10)

        if Scenario == "Valid 500":
            page.wait_for_selector(Object_Bulkupload, state="enabled", timeout=10000)
            page.set_input_files(Object_Bulkupload, os.path.join(projectDirectory, "TestData", "TBS_1095-C_Employees_Template (500).xlsx"))
            time.sleep(10)
            page.click(Object_Bulkcontinue)
            time.sleep(20)

        elif Scenario == "Allstate":
            page.wait_for_selector(Object_Bulkupload, state="enabled", timeout=10000)
            page.set_input_files(Object_Bulkupload, os.path.join(projectDirectory, "TestData", "1095-C_Employees_Template (all States).xlsx"))
            time.sleep(20)
            page.click(Object_Bulkcontinue)
            time.sleep(15)

        time.sleep(50)
        page.click(Object_continuetoprocess)
        time.sleep(70)
        page.click(Object_previewcontinue)
        time.sleep(5)

        try:
            page.click(Object_skipcontinuefiling)
        except:
            time.sleep(5)
        time.sleep(3)

    except Exception as e:
        time.sleep(2)
        print(f"Bulk upload exception: {e}")


    test_data["Recipient_TIN"] = TIN
    test_data["Result"] = Result
    print(f"{Scenario_ID} - {Result}")
    return test_data

def form_c(page, TestData):
    Form = TestData.get("Form")
    Row = TestData.get("Row")
    Sheet = Form
    Scenario_ID = TestData.get("Scenario_ID")
    Result = TestData.get("Result")

    PlanStartMonth = read_excel(Sheet, Row, "Plan_Start_month")
    Line14_All12Months = read_excel(Sheet, Row, "Line14_All12Months")
    Line15_All12Months = read_excel(Sheet, Row, "Line15_All12Months")
    Line16_All12Months = read_excel(Sheet, Row, "Line16_All12Months")
    Line17_All12Months = read_excel(Sheet, Row, "Line17_All12Months")

    page.click(Object_planstartmonth)
    page.click(f"//*[contains(text(),'{PlanStartMonth}')]")
    
    page.click(Object_line14)
    page.click(f"//*[contains(text(),'{Line14_All12Months}')]")
    if Line15_All12Months == "NO":
        pass
    else:
        page.fill(Object_line15, Line15_All12Months)
    page.click(Object_line16)
    page.click(f"//*[contains(text(),'{Line16_All12Months}')]")
    page.fill(Object_line17, Line17_All12Months)
    page.click(Object_saveandcontinue1095Cemployee)
    time.sleep(10)
    Federal = page.query_selector(Object_Federal)

    if Federal:
        TestData["Result"] = f"{Result}; Form C Saved "
        add_screenshot(page, Scenario_ID)
    else:
        TestData["Result"] = f"{Result}; Form C Error Occured "
        add_screenshot(page, Scenario_ID)
    time.sleep(5)

    return TestData

def form_b(page, TestData):
    Form = TestData.get("Form")
    Row = TestData.get("Row")
    Scenario_ID = TestData.get("Scenario_ID")
    RecipientType = TestData.get("RecipientType")
    Sheet = Form

    form_action = read_excel(Sheet, Row, "Form_Action")
    type = read_excel(Sheet, Row, "Type")
    error_message = read_excel(Sheet, Row, "ErrorMessage")
    module = read_excel(Sheet, Row, "Module")
    origin_of_policy = read_excel(Sheet, Row, "Origin_of_Policy")
    RecipientTIN = read_excel(Sheet, Row, f"{RecipientType} TIN")
    time.sleep(5)
    page.click(Object_Originofpolicy)
    page.click(f"//*[contains(text(),'{origin_of_policy}')]")
    if RecipientTIN == "EIN":
        page.click("//span[normalize-space()='Add Covered Individual']")
        page.fill("//input[@id ='firstname']", "David") 
        page.fill("//input[@id ='lastname']", "James")   
        page.fill("//input[@id = 'dob']", "02/02/2002")
        page.click("//span[contains(@class,'v-btn__content') and normalize-space()='Save']")

    else:
        pass
        
    page.click(Object_coveredall12months)
    page.click(Object_saveandcontinue1095B)
    add_screenshot(page, Scenario_ID)
    return TestData

def transmittal_c(page, TestData):
    Form = TestData.get("Form")
    Result = TestData.get("Result")
    Row = TestData.get("Row")
    Sheet = Form
    Scenario_ID = TestData.get("Scenario_ID")
    AT = read_excel(Sheet, Row, "AT")



    page.click(Object_complete1094C)
    time.sleep(5)

    try:
        page.click(Object_Federal1094Cfiling)
        time.sleep(5)

        if AT == "No":
            page.click(Object_AuthoritiveTransmittalNo)
            page.click(Object_save1094C)
        else:
            page.click(Object_AuthoritiveTransmittalYes)
            time.sleep(5)
            page.fill(Object_line20, "5")
            time.sleep(5)
            page.click(Object_AggregatedgroupYes)
            page.click(Object_page1saveandcontinue)
            page.click(Object_MinimumEssentialCoverageYES)
            page.fill(Object_section4980H, "20")
            page.fill(Object_totalemployeecount, "100")
            page.click(Object_Aggregatedgroupindicator)
            page.click(Object_page2saveandcontinue)
            page.click(Object_employerfromaddressbook)
            page.click(Object_ALEselectemployer)
            page.click(Object_page3saveandcontinue)
            time.sleep(5)
        TestData["Result"] = f"{Result}; Transmittal C Saved "

    except Exception as e:
        time.sleep(1)
        print(f"Form C exception: {e}")
        TestData["Result"] = f"{Result}; Transmittal C Not Saved "

    time.sleep(10)
    add_screenshot(page, Scenario_ID)

    return TestData

def review_summary(page, TestData):
    # --- Extract values from TestData ---
    Payer_TIN = TestData.get("Payer_TIN")
    Recipient_TIN = TestData.get("Recipient_TIN")
    Form = TestData.get("Form")
    Result = TestData.get("Result")
    Row = TestData.get("Row")
    Scenario_ID = TestData.get("Scenario_ID")
    Sheet = Form

    Form_Distribution = read_excel(Sheet, Row, "Form_Distribution")
    Form_details = read_excel(Sheet, Row, "FormSelection")
    time.sleep(10)
    DOB = fake.date_of_birth(minimum_age=18, maximum_age=120).strftime("%m/%d/%Y")
    Subs = random.randint(99999999, 99999999999)
    try:
        if Form == "1095B":
            page.click(Object_continuetostate1095b)
            page.click(Object_formdistribution)
        elif Form_details in ["CA State", "DC State", "NJ State", "RI State"]:
            page.click(Object_stateformdistribution)
        elif Form == "1094_1095C":
            page.click(Object_continuetostate)
            if TestData.get("State") == "Massachusetts":
                page.click(Object_formdistribution)
                page.fill(Object_DOB, DOB)    
                page.fill(Object_Subs, Subs)
                page.click("(//button[.//span[contains(normalize-space(.), 'Save') and contains(., 'Continue')]])[2]")   
                page.click(Object_ignore)
                page.click("//span[normalize-space(text())='Yes']")
                page.click("//button[@id='ContinueToState']")
                page.click(Object_formdistribution)
            else:
                page.click(Object_formdistribution)
                time.sleep(5)





                
    except Exception:
        page.click(Object_formdistribution)

    time.sleep(5)

    # --- Handle form distribution selection ---
    if Form_Distribution == "Self Service Print And Mail":
        page.click(Object_printmail)
    elif Form_Distribution == "OnlineAccess":
        page.click(Object_Onlineacess)
    elif Form_Distribution == "PostalMailing":
        page.click(Object_Postalmailing)
    elif Form_Distribution == "BanditComplete":
        page.click(Object_BanditComplete)

    add_screenshot(page, Scenario_ID)
    page.click(Object_Reviewforms)
    page.click(Object_Formsummary)
    page.click(Object_proceedtocheckout)
    add_screenshot(page, Scenario_ID)
    TestData["Result"] = f"{Result}; Review Summary Completed"

    return TestData

def card_payment(page, TestData):
    Form = TestData.get("Form")
    Row = TestData.get("Row")
    Scenario_ID = TestData.get("Scenario_ID")
    Result = TestData.get("Result")
    Sheet = Form
    FinalPDF = read_excel(Sheet, Row, "FinalPDF")
    CardDetails = read_excel(Sheet, Row, "CardDetails")


    if CardDetails == "New":
        print("Inside No Card Details")

        FirstName = TestData.get("FirstName")
        print(FirstName)

        page.click(Object_payment)
        frame = page.frame_locator("iframe[title='Payment']")
        time.sleep(5)
        frame.locator(Object_IAgreeToProceedWithThePayment).click()
        frame.locator("//input[@id='input-1']").fill(FirstName)
        frame_cardno = frame.frame_locator("//*[@id='number-container']/iframe")
        frame_cardno.locator("//input[@id='number']").fill("4111111111111111")
        frame.locator("//input[@id='input-3']").fill("10/27")
        frame.locator("//input[@id='input-5']").fill("123")
        frame.locator("//span[contains(text(),'I confirm that I have the authority')]").click()
        frame.locator(Object_PayAndTransmit).click()
        time.sleep(10)
    elif CardDetails == "No":
        time.sleep(5)
        page.click(Object_payment)
        frame = page.frame_locator("iframe[title='Payment']")
        frame.locator(Object_IAgreeToProceedWithThePayment).click()
        frame.locator("//input[@id='input-5']").fill("123")
        frame.locator("//span[contains(text(),'I confirm that I have the authority')]").click()
        frame.locator(Object_PayAndTransmit).click()
    elif CardDetails == "Add New":
        page.click(Object_payment)
        page.click(Object_Addnewcard)
        page.fill(Object_CreditCardNameOnCard, FirstName)
        time.sleep(5)
        # Card number
        frame = page.frame_locator("iframe[title='Payment']")
        time.sleep(5)
        frame.locator(Object_IAgreeToProceedWithThePayment).click()
        frame.locator("//input[@id='input-1']").fill(FirstName)
        frame_cardno = frame.frame_locator("//*[@id='number-container']/iframe")
        frame_cardno.locator("//input[@id='number']").fill("4111111111111111")
        frame.locator("//input[@id='input-3']").fill("10/27")
        frame.locator("//input[@id='input-5']").fill("123")
        frame.locator("//span[contains(text(),'I confirm that I have the authority')]").click()
        frame.locator(Object_PayAndTransmit).click()        
    elif CardDetails == "Credits": 
        page.click(Object_payment)
        frame = page.frame_locator("iframe[title='Payment']")
        frame.locator(Object_creditstransmit).click()

    else:
        print("No Payment Details Provided")
    time.sleep(10)
    Status = page.locator("//div[contains(text(), ' Print Forms ')]").is_visible()
    OrderID = page.text_content("//p[contains(text(),'Order ID')]/following-sibling::div")
    time.sleep(8)
    if Status == True:
        TestData["Result"] = f"{Result}; Payment Completed"
        Result = f"{Result}; Order ID - {OrderID}"
        Status = True

    else:
        TestData["Result"] = f"{Result}; Payment failed"
        Status = False  
    add_screenshot(page, Scenario_ID)

    page.click("//span[@class='v-btn__content' and .//span[text()='Home']]")
    page.click("//span[text() = 'Go to Home Dashboard']")

    # page.click(Object_gotodashboard)
    # page.click("//button[@aria-label='Dashboard']")

    return TestData

def final_pdf(page, TestData):
    Result = TestData.get("Result")
    Form = TestData.get("Form")
    Scenario_ID = TestData.get("Scenario_ID")
    Row = TestData.get("Row")
    BusinessName = TestData.get("BusinessName")   # Ensure this key exists
    Sheet = Form
    
    # Read FinalPDF value from Excel
    FinalPDF = read_excel(Sheet, Row, "FinalPDF")
    
    if str(FinalPDF).upper() == "YES":
        
        page.locator("(//button[@aria-label='Collapse Menu'])[2]").click()
        page.locator("(//button[@aria-label='Distribution Center New'])[1]").click()
        page.locator("//*[@id='search']").fill(BusinessName)
        page.wait_for_timeout(5000)
        page.locator("//*[@id='distributionbusinessselect0']").click()
        
        page.locator(
            f"//*[@id='selectallchecklable']/parent::div/parent::th/parent::tr/parent::thead/"
            f"following-sibling::tbody/tr/td/div/div[2][contains(text(),'{Form}')]/"
            f"preceding-sibling::div/div/div/div/div/input"
        ).click()
        
        page.locator(
            f"//*[@id='selectallchecklable']/parent::div/parent::th/parent::tr/parent::thead/"
            f"following-sibling::tbody/tr/td/div/div[2][contains(text(),'{Form}')]/"
            f"parent::div/parent::td/following-sibling::td/div[2]/button"
        ).click()
        
        page.wait_for_selector("//div[contains(text(),'Print Format - Choose the format to print')]")
        
        page.locator("//button[@aria-label='continue']").click()
        
        page.locator(
            f"//span[contains(text(),'{BusinessName}')]/parent::div/parent::td/"
            f"following-sibling::td[5]/div/div"
        ).click()
        
        # Wait for success message
        try:
            page.wait_for_selector(
                "//div[contains(text(),'Success!')]/following-sibling::div[contains(text(),'Downloaded Successfully!')]",
                timeout=60000
            )
            Status = True
            Result = f"{Result};Final Report downloaded"
            add_screenshot(page, Scenario_ID)
        except:
            Status = False
            Result = f"{Result};Final Report not downloaded"
            add_screenshot(page, Scenario_ID)
        
        TestData["Status"] = Status
    
    TestData["Result"] = Result
    return TestData
