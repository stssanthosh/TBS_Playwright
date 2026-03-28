BASE_URL = "https://sc.stsuat.com"
Email = "qa.automation@spantechnologyservices.com"
Password = "Spancbeqa58*"
selectors = {
"EFile_GoogleSignin":"//a[@title='google']",
"EFile_Email": "//*[@id='identifierId']",
"EFile_EmailNext":"//span[text()='Next']/parent::button",
"EFile_Password":"//input[@aria-label='Enter your password']",
"EFile_PaswordNext":"//span[text()='Next']/parent::button",
"EFile_Continue":"//span[text()='Continue']/parent::button",
"EFile_OTP": '//*[@id="totpPin"]',
"EFile_OTPNext":"//span[contains(text(),'Next')]/parent::button"
}
