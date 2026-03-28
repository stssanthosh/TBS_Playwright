
Object_SitePassword="(//*[@id='Passwordfeild'])"
Object_SitePasswordContinue="//em[contains(text(),'Please enter the password to use the testing site')]/parent::p/following-sibling::div/button"
Object_Username="//*[@id='Email_Address_feild']"
Object_Password="//*[@id='Password_feild']"
Object_signin = "//button[@id='SignInbtn']"
Object_IlldoitLater = "//a[contains(text(),'do it later')]"
Object_Login="//span[text()=' Start New']"
Object_DashboardLogo="//div[@aria-label='Logo']"
Object_TwoFactorAuthenticationCode="//*[@id='verificationcodefield']"
Object_VerifyCode="//button[@aria-label='Verify the code']"
Object_ErrorMessageTwoFactor="//div[contains(text(),'Invalid Verification Code. 3 attempts until your account is temporarily locked.')]"
Object_ErrorResult="//div[contains(text(),'Error occured')]"
Object_Signup="//*[@id='SignupLink']"
Object_ForgetPasswordheader="//h1[contains(text(),'Forgot')]"
Object_ForgetPasswordEmailAddress="//*[@id='emailId']"
Object_ForgetPasswordContinue="//*[@id='ForgetPasswordContinue']"
Object_ForgetPasswordReturnToSignin="//*[@id='ReturnToSignIn']"
Object_ForgetPasswordCheckYourInbox="//h1[contains(text(),'Password Reset Link Sent – Check Your Inbox!')]"
Object_ForgetPasswordCheckYourInboxGoToSignin="//*[@id='GoToSignIn']"
Object_ForgetPassword="//a[contains(text(),'Forgot Password?')]"
Object_SignupHeader="//h1/span[contains(text(),'Sign Up')]"
Object_WorkEmail="//*[@id='WorkEmail']"
Object_ContactName="//*[@id='ContactName']"
Object_SignupPassword="//*[@id='Password']"
Object_PhoneNumber="//*[@id='PhoneNumber']"
Object_TaxPrefessional="//*[@id='IsTaxPreparer']"
Object_FirmName="//*[@id='FirmName']"
Object_HowManyClientsDoYouWorkWith="//*[@id='ifselfemployedlabel']/following-sibling::div"
Object_CreateAccount="//*[@id='createAccount']"
Object_OTAHeader="//span[contains(text(),'Verify your Email')]"
Object_OTA="//*[@id='otaverificationfeild']"
Object_Verify="//button[@aria-label='Vefify']"
Object_TwoFAHeader="//h1[contains(text(),'Enable Two-Factor Authentication (2FA)')]"
Object_TwoFAIWillDoItLater="//a[contains(text(),'do it Later')]"
Object_Welcome="//h1[contains(text(),'Welcome')]"
Object_WelcomeTagline="//h1[contains(text(),' Welcome Back ')]"
Object_GoToDashboard="//span[text()='Start ']/parent::button"
Object_DashBoardHeader="//p[contains(text(),'Welcome Back')]"
Object_ErrorOccured = "//*[contains(text(),'Error occured']"
Object_ChangePayer = "//button[@id='changepayer']"
Object_Addnewemployer = "//span[text()=' Add Employer']"
Object_EmployerName = "//input[@id='Employername']"
Object_EIN = "//*[@id='ein']"
Object_Trade_name = "//input[@id='tradename']"
Object_ReferenceNumber = "//input[@id='referencenumber']"
Object_PayerCountryCode = "//*[@id='countrylabel']/following-sibling::div"
Object_PayerAddress1 = "//input[@id='addressline1']"
Object_PayerAddress2 = "//input[@id='addressline2']"
Object_Payercity = "//input[@id='cityortown']"
Object_PayerStateOrProvince = "//label[text()='State']/parent::div/div/div/div[1]/div/div[4]/i"
Object_PayerZipOrPostalCode = "//input[@id='zipcode']"
Object_contacttoggle = "//button[text()=' Contact Person Information ']"
Object_PayerFirstName = "//input[@id='contactfirstname']"
Object_PayerMiddleName = "//input[@id='contactmiddlename']"
Object_PayerLastName = "//input[@id='contactlastname']"
Object_PayerSuffix = "//label[text()='Suffix (Optional) ']/following-sibling::div/div/div/div[2]/following-sibling::div[2]/i"
Object_EmailAddress = "//input[@id='contactemailaddress']"
Object_Phonenumber = "//input[@id='contactphonenumber']"
Object_SigningAuthorityName = "//input[@id='signingauthorityname']"
Object_SigningAuthorityTitle = "//label[text()=' Signing Authority Title (Optional) ']/parent::div/div/div/div/div[4]/i"
Object_saveandcontinue = "//span[text()='Save & Continue ']"
Object_save = "//span[text()='Save ']"
Object_AddressValid = "//span[contains(text(),'Okay')]/parent::span/parent::button"
Object_AddressUSPSRecommended = "//span[contains(text(),'Continue')]/parent::span/parent::button"
Object_IgnoreAndContinue = "//span[contains(text(),'Ignore and Continue')]/parent::span/parent::button"
Object_ignore =  '//span[text()="Ignore and Continue"]'
Object_cont =  '//span[text()="Continue"]'

#DGE Page

Object_DGE = "//button[text()='Designated Government Entity (DGE)']"
Object_DGEcheckbox = "//input[@id='governmentalentity']"
Object_DGEBusinessname = "//input[@id='entitybusinessname']"
Object_DGETradename = "//input[@id='entitytradename']"
Object_DGEEIN = "//input[@id='entityein']"
Object_DGEAddressline1 = "//input[@id='entityaddressline1']"
Object_DGEAddressline2 = "//input[@id='entityaddressline2']"
Object_DGECity = "//input[@id='entitycityortown']"
Object_DGEstate = "(//label[text()='State'])[2]/parent::div/div/div/div[1]/div/div[4]/i"
Object_DGEZipcode = "//input[@id='entityzipcode']"
Object_DGEFN = "//input[@id='entityfirstname']"
Object_DGEMN = "//input[@id='entitymiddlename']"
Object_DGELN = "//input[@id='entitylastname']"
Object_DGEPN = "//input[@id='entityphonenumber']"
Object_DGEsuffix = "//label[text()='Suffix (Optional) ']/following-sibling::div/div/div/div[2]/following-sibling::div[2]/i"

#Welcome Page


Object_toggle = "//span[text()='Transmit all the 1095-C forms as single return']"
Object_continue = "//button[@aria-label='Continue to Form 1095']"


#Employee Page
Object_newemployee = "//span[text()='Add New Employee']"
Object_newrecipient = "//span[text()='Add New Recipient']"
Object_Businessname = "//input[@id ='input-611']"
Object_DOB = "//input[@aria-label ='DOB']"
Object_Subs = "//input[@aria-label ='Subscription Number']"
Object_firstname = "//label[text()=' First name ']/parent::div/div/div/div/div[3]/input"
Object_middlename = "//label[text()='Middle name (Optional) ']/parent::div/div/div/div/div[3]/input"
Object_lastname = "//label[text()='Last name ']/parent::div/div/div/div/div[3]/input"
Object_emailaddress1095c = "//label[text()=' Email address (Optional)']/parent::div/div/div/div/div[3]/input"
Object_phonenumber1095C = "//label[text()=' Phone number (Optional)']/parent::div/div/div/div/div[3]/input"
Object_Addressline11095C = "//label[text()='Address line 1 ']/parent::div/div/div/div/div[3]/input"
Object_Addressline21095C = "//label[text()=' Address line 2 (Optional) ']/parent::div/div/div/div/div[3]/input"
Object_city1095C = "//label[text()='City or town ']/parent::div/div/div/div/div[3]/input"
Object_state1095C = "//label[text()='State']/parent::div/div/div/div/div/div[3]/following-sibling::div/i"
Object_zipcode1095C = "//label[text()='ZIP code']/parent::div/div/div/div/div[3]/input"
Object_ssn1095C = "//label[text()='SSN ']/parent::div/div/div/div/div[3]/input"
Object_ein1095B = "(//input[@aria-label = 'SSN'])[3]"
Object_dobfield = "(//input[@aria-label='DOB'])[1]"
Object_dob1095B = "//span[contains(text(),'DOB')]"
Object_RecipientEIN = "//span[contains(text(),'EIN')]"
Object_ResponsibleIndividual = "//input[@aria-label='First name']"
Object_saveandcontinue1095C = "//*[text()='Save & Continue ']/parent::button"
Object_saveandcontinue1095B = "(//span[contains(normalize-space(.), 'Save & Continue')])[1]"
Object_ignore1095C = "(//i[@class='mdi-close mdi v-icon notranslate v-theme--TBSCustomTheme v-icon--size-default me-1'])[2]"
Object_changerecipient = "//*[text()='Change Employee ']/parent::button"

# Review Return Federal Filing
# Object_DraftAndErrors = "//button[@id='DraftAndErrors']"
# Object_CreateNewForm = "//button[@id='CreateNewForm']"
# Object_ContinueToStateFiling = "//button[@id='ContinueToState']"
# Object_FederalFilingBack = "//button[@id='Back']"

# Review Return State Filing
# Object_ContinueToFormDistribution = "//button[@id='ContinueToDistribution']"

# Review Return Form Distribution
# Object_PrintEmail = "//p[@id='PrintMail']"
# Object_OnlineAccess = "//p[@id='OnlineAccess']"
# Object_PostalMailing = "//p[@id='Postalmailing']"
# Object_BanditComplete = "//p[@id='BanditComplete']"
# Object_ContinueToFormSumary = "//button[@id='ContinueToSummary']"

# Cart Page
# Object_CompleteFiling = "//span[contains(text(),'Continue filing')]"
# Object_CompleteYourOrder = "(//span[contains(text(),'Complete your order')])[2]"

# Acknowledgement PopUp
Object_IAgreeToProceedWithThePayment = "//*[text()='Agree and Continue ']"
Object_AcknowledgementContinue = "//input[@id='checkbox-11']"
Object_Addnewcard = "//span[text()=' Add New Card ']"

# Card PopUp
Object_CreditCardNameOnCard = "//label[contains(text(),'Name on card')]/following-sibling::div/div/div/div/input"
Object_CreditCardCardNumber = "//label[text()='Card number']/parent::div/div"
Object_CreditCardExpirationDate = "//label[text()='Expiration date']/parent::div/div"
Object_CreditCardCVV = "//input[@name='cvc']"
Object_CreditCardAcknowledgement = "//*[contains(text(),' I confirm that I have the authority to use this credit card, and I authorize TaxBandits to charge my credit card. ')]"
Object_PayAndTransmit = "//span[text()='Pay and Transmit ']"
 
# Final Summary
Object_GoToDashboard = "//button[@class='v-btn v-btn--elevated v-theme--light bg-primary v-btn--density-default v-btn--size-large v-btn--variant-elevated text-initial elevation-0']/span/following-sibling::span/following-sibling::span"

# Summary
Object_continuetostate = "//span[text()='Continue to State ']"
Object_continuetostate1095b = "//span[text()='Continue to State']"
Object_formdistribution = "//span[text()='Continue to Form Distribution']"
Object_stateformdistribution = "//span[text()='Continue to Form Distribution ']"

# Form Distribution
Object_printmail = "//input[@id='PrintAndMail']"
Object_BanditComplete = "//input[@id='Advanced']/parent::div"
Object_Onlineacess = "//input[@id='Online']"
Object_Postalmailing = "//input[@id='postal']"
Object_Reviewforms = "//span[text()='Continue to Review Forms']"

Object_Formsummary = "//*[text()='Continue to Filing Summary']"
Object_proceedtocheckout = "//span[text()='Proceed to Checkout']"

# Payment
Object_payment = "//span[text()='Complete Your Order ']"
Object_creditstransmit = "//span[text()='Confirm and Transmit ']"
Object_gotodashboard = "//span[contains(normalize-space(.), 'Go To Dashboard')]"

