import os
from datetime import datetime as dt


def reportDate():
    MM = dt.now().strftime('%m')
    MM = dt.now().strftime('%h')
    MM = dt.now().strftime('%B')
    MM = MM[0:3]
    DD = dt.now().strftime('%d')
    YYYY = dt.now().strftime('%Y')
    YYYY = YYYY[2:4]
    date = DD+"-"+MM+"-"+YYYY
    return date

def reportDay():
    day = dt.now().strftime('%a')
    return day


head ="""<head>
		<link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<style type="text/css">
		h1{font-size:56px}
		h2{font-size:28px;font-weight:900}
		p{font-weight:100}
		td{vertical-align:top}
		#email{width:1200px;margin-left: 150px;}
		</style>
	</head>"""


def report_header():
    header = """<table role="presentation" width="100%" >
			<tr>
				<td align="center" style="color: black; ">
					<h2 > ACA </h2>
				</td>
		</table>"""
    return  header
    

def credential(Region,site,username,password,browser):
    credential = """<br> <table role="presentation" width="100%">
			<tr>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Region</th>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">URL</th>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Username</th>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Password</th>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Browser</th>
			</tr>
			<tr>
				<td style="text-align: center;border: 1px solid black;">"""+Region+"""</td>
				<td style="text-align: center;border: 1px solid black;">"""+site+"""</td>
				<td style="text-align: center;border: 1px solid black;">"""+username+"""</td>
				<td style="text-align: center;border: 1px solid black;">"""+password+"""</td>
				<td style="text-align: center;border: 1px solid black;">"""+browser+"""</td>
			</tr>
		</table>"""
    return credential


def run_summary(logid,date):
    form_folder = os.getcwd()
    file1 = open(form_folder+"//Report//Report//Logs//Email//EmailReportDetail.txt","r")
    val = file1.read()
    pass_tc=val.count(""";">Pass</td>""")
    fail_tc=val.count(""";">Fail</td>""")
    total_tc = val.count("""scenarios""")
    file1.close()

    run_status = ""

    if fail_tc>=1:
      run_status="Fail"
    else:
      run_status="Pass"

    value="""<br>
      <table role="presentation" width="100%">
			<tr>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Log ID</th>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Run Status</th>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Total TC</th>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Pass TC</th>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Fail TC</th>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Date</th>
			</tr>
			<tr>
				<td  style="text-align: center;border: 1px solid black;">"""+logid+"""</td>
				<td  style="text-align: center;border: 1px solid black;">"""+run_status+"""</td>
				<td  style="text-align: center;border: 1px solid black;">"""+str(total_tc)+"""</td>
				<td  style="text-align: center;border: 1px solid black;color:green;" >"""+str(pass_tc)+"""</td>
				<td  style="text-align: center;border: 1px solid black;color:red;" >"""+str(fail_tc)+"""</td>
				<td  style="text-align: center;border: 1px solid black;">"""+date+"""</td>
			</tr>
		</table>
      """
    return value
   
def scenario_result_table():
   form_folder = os.getcwd()
   file1 = open(form_folder+"//Report//Report//Logs//Email//EmailReportDetail.txt","r")
   val = file1.read()
   table = """<table role="presentation" width="100%">
			<tr>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Scenario ID</th>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;" >Scenario Description</th>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Actual Result </th>
				<th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Status</th>
			</tr>"""+val+"""</table>"""
   return table

def email_result(scenario_id,scenario_description,result,status):
  print(scenario_id)
  print(scenario_description)
  print(result)
  print(status)
  form_folder = os.getcwd()
  file1 = open(form_folder+"//Report//Report//Logs//Email//EmailReportDetail.txt","a")
  scenario_result = """<tr id="scenarios">
				<td style="text-align: center;border: 1px solid black;">"""+scenario_id+"""</td>
				<td style="text-align: left;border: 1px solid black;"> """+scenario_description+"""</td>
				<td style="text-align: center;border: 1px solid black;"> """+result+"""</td>
				<td style="text-align: center;border: 1px solid black;">"""+status+"""</td>
			</tr>"""
  file1.write(scenario_result)
  file1.close()

  form_folder = os.getcwd()
  