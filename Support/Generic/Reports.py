import os
import sys
import time
import shutil
from datetime import datetime
import datetime as dt
from pathlib import Path
from dotenv import load_dotenv
import base64
from Support.Generic.email import *
from Support.Generic.Support import *





def login_environment_variables():
    
    env = get_config()

    os.environ["site"] = env["Site"]
    os.environ["Region"] = env["Region"]
    os.environ['username'] = env["username"]
    os.environ['password'] = env["password"]
    os.environ['url'] = env["url"]
    os.environ['Userrole'] = env["UserRole"]
    os.environ['Browser'] = env["Browser"]

    # os.environ["Region"] = "SandBox"
    # os.environ["site"] = "TBS"
    os.environ["logid"] = "Log_" + datetime.now().strftime("%Y%m%d%H%M%S")
    os.environ['start_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # os.environ['username'] = "murali.r+sandbox_test@spantechnologyservices.com"
    # os.environ['password'] = "Span@1234"
    # os.environ['Browser'] = "CHROME"
    # os.environ['Userrole'] = "BO"
    # os.environ['url'] = "https://testapp1.taxbandits.com/login/"
    


def generate_test_report():
    project_directory = os.environ["PROJECT_DIRECTORY"]
    form_folder = os.getcwd()
    logid = os.environ['logid']
    start_time_str = os.environ["start_time"]  # stored earlier
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    t1 = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    t2 = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    delta = t2 - t1
    duration_seconds = delta.total_seconds()
    duration_minutes = round(duration_seconds / 60, 2)

    duration = f"{duration_minutes} Mins"

    scenario_results_value = scenario_results()

    run_status = ""
    print("419")
    if scenario_results_value.__contains__("passed_testcase"):
        run_status = "Fail"
    else:
        run_status = "Pass"
    date = reportDate()
    day = reportDay()
    print("426")
    total_tc = scenario_results_value.count("scenario_result")
    pass_tc = scenario_results_value.count("failed_testcase")
    fail_tc = scenario_results_value.count("passed_testcase")

    total_tc = str(total_tc)
    pass_tc = str(pass_tc)
    fail_tc = str(fail_tc)

    run_summary_value = run_summary(logid, run_status, total_tc, pass_tc, fail_tc, date, day, start_time_str, end_time,
                                    duration)
    button = buttons()
    button = str(button)

    report = """
<!DOCTYPE html>
<html lang="en">
    """ + head + """
 <body>
 <div class="container mt-6">
    """ + header + run_summary_value + scenario_results_value + scripts + """
    </body>
  </html>
    """

    file = open(form_folder + "//Report//Report.html", "w")

    file.write(report)
    file.close()
    print("454")




def reportDate():
    MM = datetime.now().strftime('%m')
    MM = datetime.now().strftime('%h')
    MM = datetime.now().strftime('%B')
    MM = MM[0:3]
    DD = datetime.now().strftime('%d')
    YYYY = datetime.now().strftime('%Y')
    YYYY = YYYY[2:4]
    date = DD + "-" + MM + "-" + YYYY
    return date


def reportDay():
    day = datetime.now().strftime('%a')
    return day

def run_summary(logid, run_status, total_tc, pass_tc, fail_tc, date, day, start_time, end_time, duration):
    color = "green" if run_status == "Pass" else "red"

    run_summary = """
      <h3> Run Summary </h3>
      <table cellspacing="5" width="100%" border="1" >
          <tr>
            <th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Log ID</th>
            <th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Run Status</th>
            <th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Total TC</th>
            <th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Pass TC</th>
            <th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Fail TC </th>
            <th style="background-color:#FFA500;text-align: center;border: 1px solid black;" >Date</th>
            <th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Day</th>
            <th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Start Time</th>
            <th style="background-color:#FFA500;text-align: center;border: 1px solid black;">End Time</th>
            <th style="background-color:#FFA500;text-align: center;border: 1px solid black;">Duration</th>
          </tr>
          <tr>
            <td style="text-align: center; border: 1px solid black;">""" + str(logid) + """</td>
            <td style="color: """ + color + """;text-align: center;border: 1px solid black;">""" + str(run_status) + """</td>
            <td style="text-align: center;border: 1px solid black;">""" + str(total_tc) + """</td>
            <td style="text-align: center;border: 1px solid black;">""" + str(pass_tc) + """</td>
            <td style="text-align: center;border: 1px solid black;">""" + str(fail_tc) + """</td>
            <td style="text-align: center;border: 1px solid black;">""" + str(date) + """</td>
            <td style="text-align: center;border: 1px solid black;">""" + str(day) + """</td>
            <td style="text-align: center;border: 1px solid black;">""" + str(start_time) + """</td>
            <td style="text-align: center;border: 1px solid black;">""" + str(end_time) + """</td>
            <td style="text-align: center;border: 1px solid black;">""" + str(duration) + """</td>
          </tr>
      </table> <br>
      """

    return run_summary


def buttons():
    buttons = """<br><table  >  
                  <tr> 

                    <td WIDTH=50><button onclick="window.location.reload();" class="btn btn-primary" >TOTAL </button></td>
                    <td WIDTH=50><button onclick="PassTestCase()" class="btn btn-success" >PASS </button></td>
                    <td WIDTH=50><button onclick="FailTestCase()" class="btn btn-danger" >FAIL </button>  </td>

                    <td WIDTH=50> </td>
                    <td WIDTH=150><a><button onclick="location.href = 'https://id.atlassian.com/';" id="myButton"  target="_blank"  class="btn btn-success">Raise an issue?</button> </a> </td>


                  </tr>
                </table>
                <br>"""

    return buttons

head = """<head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </head>"""

scripts = """ 
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

  <script>
    function PassTestCase() {
      var x = document.getElementById("passed_testcase");
      if (x.style.display === "none") {
        x.style.display = "block";
      } else {
        x.style.display = "none";
      }
    }

    function FailTestCase() {
      var x = document.getElementById("failed_testcase");
      if (x.style.display === "none") {
        x.style.display = "block";
      } else {
        x.style.display = "none";
      }
    }
    </script>
"""

header = """  <table>
        <tr>
          <td>
            <img src="data:image/png;base64,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" alt="" width="336" height="105"/>
          <td><h1>SPAN TECHNOLOGY SERVICES PRIVATE LIMITED</h1></td>
        </tr>
      </table>"""


def scenario_results():
    print("326")
    form_folder = os.getcwd()

    ScenarioDetail = os.listdir(form_folder + "//Report//Report//Logs//Output//ScenarioDetail")

    ScenarioDetails = ""
    for i in ScenarioDetail:
        file = open(form_folder + "//Report//Report//Logs//Output//ScenarioDetail//" + i, "r")
        value = file.read()
        ScenarioDetails = ScenarioDetails + value
    print("336")
    try:
        os.makedirs(form_folder + "//Report//Log")
    except:
        pass
    print("341")
    file = open(form_folder + "//Report//Log//ScenarioDetail.txt", "a")
    file.write(ScenarioDetails)
    file.close()
    print("345")
    region = os.environ['Region']
    site = os.environ['site']
    username = os.environ['username']
    password = os.environ['password']
    logid = os.environ['logid']
    browser = os.environ['Browser']
    Userrole = os.environ['Userrole']
    url = os.environ['url']
    credentials = """<h3> Credential </h3>
      <table cellspacing="5" width=90%" border="1" >

          <tr>
            <th WIDTH=100 style="background-color:#FFA500;text-align: center;border: 1px solid black;">Site</th>
            <th WIDTH=100 style="background-color:#FFA500;text-align: center;border: 1px solid black;">Region</th>
            <th WIDTH=100 style="background-color:#FFA500;text-align: center;border: 1px solid black;">User Type</th>
            <th WIDTH=350 style="background-color:#FFA500;text-align: center;border: 1px solid black;">URL</th>
            <th WIDTH=400 style="background-color:#FFA500;text-align: center;border: 1px solid black;">Username</th>
            <th WIDTH=100 style="background-color:#FFA500;text-align: center;border: 1px solid black;">Password</th>
            <th WIDTH=100 style="background-color:#FFA500;text-align: center;border: 1px solid black;">Browser</th>
          </tr>
          <tr>
            <td  style="text-align: center;border: 1px solid black;">""" + site + """</td>
            <td  style="text-align: center;border: 1px solid black;">""" + region + """</td>
            <td  style="text-align: center;border: 1px solid black;">""" + Userrole + """</td>
            <td  style="text-align: center;border: 1px solid black;">""" + url + """</td>
            <td  style="text-align: center;border: 1px solid black;">""" + username + """</td>
            <td  style="text-align: center;border: 1px solid black;">""" + password + """</td>
            <td  style="text-align: center;border: 1px solid black;">""" + browser + """</td>
          </tr>    
      </table>"""

    print("377")
    scenario_results_total = """<div class="accordion accordion-flush" >
        <div class="accordion-item">
                <h2 class="accordion-header ">
                  """ + credentials + """<br>
                  <table>  
                    <tr> 
                      <td WIDTH=50><button onclick="window.location.reload();" class="btn btn-primary" >TOTAL </button></td>
                      <td WIDTH=50><button onclick="PassTestCase()" class="btn btn-success" >PASS </button></td>
                      <td WIDTH=50><button onclick="FailTestCase()" class="btn btn-danger" >FAIL </button>  </td>
                      <td WIDTH=50> </td>
                      <td WIDTH=150><a><button onclick="location.href = 'https://id.atlassian.com/';" id="myButton"  target="_blank"  class="btn btn-success">Raise an issue?</button> </a> </td>
                    </tr>

                  </table> <br>
                  <h3> Run Details</h3>
                  <table  cellspacing="3" width=100%" border="1" >
                    <tr style="height:50px">
                    <td WIDTH=200 style="border: 1px solid black;text-align: center;background-color:#FFA500;text-align: center;"><h6>Scenario ID</h6></td>
                      <td WIDTH=300 style="border: 1px solid black;background-color:#FFA500;text-align: center;"><h6>Scenario Description</h6></td>
                      <td WIDTH=300 style="border: 1px solid black;background-color:#FFA500;text-align: center;"><h6>Actual Result</h6></td>
                      <td WIDTH=100 style="border: 1px solid black;background-color:#FFA500;text-align: center;"><h6>Duration</h6></td>
                      <td WIDTH=50 style="border: 1px solid black;background-color:#FFA500;text-align: center;"><h6>Type</h6></td>
                      <td WIDTH=100 style="border: 1px solid black;background-color:#FFA500;text-align: center;"><h6>Status</h6></td>
                      <td WIDTH=100 style="border: 1px solid black;background-color:#FFA500;text-align: center;"><h6>Screenshot</h6></td>
                    </tr>
                  </table>""" + ScenarioDetails + """
                </h2>
        </div>
      """
    print("396")
    return scenario_results_total


def strptime(date_string, format):
        'string, format -> new datetime parsed from a string (like time.strptime()).'
        import _strptime
        return _strptime._strptime_datetime(date_string, format)


def image_to_binary(file):
    binary_fc = open(file, 'rb').read()
    base64_utf8_str = base64.b64encode(binary_fc).decode('utf-8')
    ext = file.split('.')[-1]
    dataurl = f'data:image/{ext};base64,{base64_utf8_str}'
    return dataurl

def delete_file(file_path):
    path = Path(file_path)
    if path.is_file():
        try:
            path.unlink()
            print(f"✅ Deleted file: {path}")
        except Exception as e:
            print(f"⚠ Failed to delete file {path}: {e}")


def create_folder(directory):
    path = Path(directory)
    if not path.exists():
        try:
            path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"⚠ Failed to create folder {path}: {e}")




def setup_project_environment():

    load_dotenv()
    project_name = os.getenv("PROJECT_NAME")
    if not project_name:
        raise ValueError("PROJECT_NAME not set in environment or .env file.")

    current_path = os.path.abspath(__file__)
    while True:
        current_path = os.path.dirname(current_path)
        if os.path.basename(current_path).lower() == project_name.lower():
            break
        if current_path == os.path.dirname(current_path):  # reached root
            raise FileNotFoundError(f"Project root '{project_name}' not found.")

    os.environ["PROJECT_DIRECTORY"] = current_path

    if current_path not in sys.path:
        sys.path.append(current_path)

    return current_path

def delete_all_files_in_directory(directory):
    path = Path(directory)
    if path.is_dir():
        for file in path.iterdir():
            if file.is_file():
                delete_file(file)

def delete_all_folders_in_folder(directory):
    path = Path(directory)
    if path.is_dir():
        for folder in path.iterdir():
            if folder.is_dir():
                try:
                    shutil.rmtree(folder)
                except Exception as e:
                    print(f"⚠ Failed to delete folder {folder}: {e}")



def folder_configuration(exec_dir):
    report_folder = Path(exec_dir) / "Report"

    # Remove existing files and folders
    delete_all_files_in_directory(report_folder)
    delete_all_folders_in_folder(report_folder)
    if report_folder.exists():
        try:
            shutil.rmtree(report_folder)
        except Exception as e:
            print(f"⚠ Failed to remove Report folder: {e}")

    # Create required folders
    create_folder(report_folder / "Screenshot")
    create_folder(report_folder / "Log")
    create_folder(report_folder / "Report" / "Logs" / "Email")
    create_folder(report_folder / "Report" / "Logs" / "Output" / "EmailReportDetail")
    create_folder(report_folder / "Report" / "Logs" / "Output" / "ScenarioDetail")

    # Remove specific files
    delete_file(report_folder / "Webhook.json")
    delete_file(report_folder / "Log" / "ScenarioDetail.txt")
    delete_file(report_folder / "Report" / "Logs" / "Email" / "EmailReportDetail.txt")
    delete_file(report_folder / "Report" / "Output" / "Report.html")
    delete_file(report_folder / "Report" / "Output" / "EmailReport.html")
    delete_file(report_folder / "Report" / "Report.html")
    delete_file(report_folder / "Report" / "Email.html")

    # Remove files inside specific directories
    delete_all_files_in_directory(report_folder / "Report" / "Logs" / "Output" / "ScenarioDetail")
    delete_all_files_in_directory(report_folder / "Report" / "Logs" / "Output" / "EmailReportDetail")
    delete_all_folders_in_folder(report_folder / "Screenshot")


def generate_report(page,status, result, test_data):
    print("Form value:", test_data.get("Form", "-"))
    print("Type value:", test_data.get("type", ""))
    type_ = test_data.get("type", "")
    start_time = test_data.get("start_time", "")
    scenario_id = test_data.get("Scenario_ID", "")
    scenario_description = test_data.get("Scenario_Description", "")
    form = test_data.get("Form", "-")
    result = test_data.get("Result", result)
    # add_screenshot(page,scenario_id)
    # Convert type
    if type_ == "Positive":
        type_ = "+VE"
    else:
        type_ = "-VE"

    # Compute end time + duration
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fmt = "%Y-%m-%d %H:%M:%S"
    start_dt = datetime.strptime(start_time, fmt)
    end_dt = datetime.strptime(end_time, fmt)
    duration = end_dt - start_dt
    duration = str(duration)

    # Clean result string
    result = result.strip()
    result = result.replace(",,", ",")
    result = result.replace(", and Script fail", " and Script fail")
    result = result.replace(", ", ",")
    result = result.strip()

    if len(result) == 0:
        result = " "

    # Normalize result for fail detection
    if result.startswith("and Script fail") or result.startswith(",Script Fail"):
        result = "Script Fail"

    # Take screenshot
    add_screenshot(page, scenario_id)

    # Remove dashes
    result = result.replace("-", "")

    if status:
        # PASS block
        scenario_result(scenario_id, scenario_description, result, start_time, end_time, "Pass", duration, test_data, type_, form)
        email_result(scenario_id,scenario_description,result,"Pass")
    else:
        # FAIL block
        scenario_result(scenario_id, scenario_description, result, start_time, end_time, "Fail", duration, test_data, type_, form)
        email_result(scenario_id,scenario_description,result,"Fail")
    generate_test_report()
    generate_email_report()


def add_screenshot(page, scenario_id):
    # Get execution directory from environment or default
    exec_folder = os.getenv("execution_directory", os.getcwd())
    exec_folder = os.path.join(exec_folder, "Report", "Screenshot")

    # Create scenario-specific folder
    scenario_folder = os.path.join(exec_folder, scenario_id)
    os.makedirs(scenario_folder, exist_ok=True)

    # Determine screenshot number
    existing_screenshots = [
        f for f in os.listdir(scenario_folder) if f.endswith(".png")
    ]
    number = len(existing_screenshots) + 1

    # Screenshot file path
    screenshot_file = os.path.join(scenario_folder, f"{number}.png")

    # Capture screenshot
    page.screenshot(path=screenshot_file)

    print(f"✅ Screenshot saved: {screenshot_file}")

def current_time():
        current_time = time.localtime()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return current_time


import os
import sys  


def scenario_result(scenario_id, scenario_description, actual_result, start_time, end_time, result, duration, testdata,
                    type, form):
        logid = os.environ["logid"]
        product = "1099/W2"
        region = os.environ['Region']


        a = "153"
        print(a)
        testdata = dict(testdata)

        data = testdata.keys()

        testdata_value = ""

        a = "160"

        for i in data:
            value = """
                          <tr>
							              <td style="text-align: center;border: 1px solid black; width:500px"> <h6>""" + str(
                i) + """</h6></td>
							              <td style="text-align: center;border: 1px solid black; width:500px"> <h6>""" + str(
                testdata[i]) + """</h6></td>
                          </tr>
                       """
            testdata_value = testdata_value + value

        a = "169"
        testdata_value = "<tbody>" + testdata_value + "</tbody>"

        projectDirectory = os.environ['PROJECT_DIRECTORY']

        form_folder = os.getcwd()

        a = "181"

        file1 = open(
            form_folder + "//Report//Report//Logs//Output//ScenarioDetail//ScenarioDetail" + scenario_id + ".txt", "a")

        a = "185"

        result_id = ""
        result_color = ""

        if result == "Pass":
            result_id = "failed_testcase"
            result_color = "success"
        else:
            result_id = "passed_testcase"
            result_color = "danger"

        a = "197"
        scenario_result = """
                  <table  name="scenario_result" id=\"""" + result_id + """\"  cellspacing="3" width=100%" border="1" >
                      <tr style="height:50px">
                        <td WIDTH=200 style="border: 1px solid black;text-align: center;text-align: center;"><h6> """ + scenario_id + """  </h6></td>
                        <td WIDTH=300 style="border: 1px solid black;text-align: left;"><h6> """ + scenario_description + """ </h6></td>
                        <td WIDTH=300 style="border: 1px solid black;text-align: center;"><h6> """ + actual_result + """ </h6></td>
                        <td WIDTH=100 style="border: 1px solid black;text-align: center;"><h6> """ + duration + """ </h6></td>
                        <td WIDTH=50 style="border: 1px solid black;text-align: center;"><h6> """ + type + """ </h6></td>
                        <td WIDTH=100 style="border: 1px solid black;text-align: center;"><h6 class="btn btn-""" + result_color + """"> """ + result + """ </h6></td>
                        <td WIDTH=100 style="border: 1px solid black;text-align: center;" >
                          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-""" + scenario_id + """" aria-expanded="false" aria-controls="flush-""" + scenario_id + """">
                            <div class="d-flex align-items-center justify-content-between">
                            </div>
                          </button>
                        </td>
                      </tr>
                  </table>"""

        a = "217"
        screenshots = os.listdir(form_folder + "//Report//Screenshot//" + scenario_id)
        data_urls = [""]
        for i in range(0, len(screenshots)):
            ss = screenshots[i]
            image = form_folder + "//Report//Screenshot//" + str(scenario_id) + "//" + str(ss)
            data_url = image_to_binary(image)
            data_urls.append(data_url)
        data_urls.pop(0)
        a = "226"
        screens = ""

        default = len(data_urls)
        default = data_urls[default - 1]
        a = "272"
        sno = 1

        ex = ""

        for i in data_urls:
            screen_div = """<td style="background-color:#FFA500;text-align: center;border: 1px solid black;"><button class="btn btn-secondary" onclick="document.getElementById('""" + scenario_id + """screenshot').src='""" + i + """'">""" + str(
                sno) + """</button></td>
              """
            screens = screens + screen_div
            sno = sno + 1

        a = "278"
        sno_table = """ 
  <table  cellspacing="5" ">
                        <tr>
                          <td> <p> <b>SCREENSHOTS: </b> </p> </td>
						  <td> <p> <b> </b> </p> </td>


              """ + screens + """                        </tr>
                      </table>"""

        a = "292"
        default_screenshot = """  <img id=""" + scenario_id + """screenshot""" + """ src=\"""" + i + """\" class="d-block img-fluid w-100">  """

        scenario_screenshots = """

            <div id="flush-""" + scenario_id + """" class="accordion-collapse collapse" >

                <div class="accordion-body border border-1 border-danger">



                      <br>	""" + sno_table + """


                      <div id=\"""" + scenario_id + """\" class="carousel slide">

                          <div class="carousel-inner">

                                 """ + default_screenshot + """

                          </div>

                      </div>

                      <br>

					            <table  cellspacing="5">
                        <thead>
							            <th style="background-color:#FFA500;text-align: center;border: 1px solid black;"> <h6>Data</h6></th>
							            <th style="background-color:#FFA500;text-align: center;border: 1px solid black;"> <h6>Value</h6></th>
                        </thead>""" + testdata_value + """
                      </table>
                </div>
            </div>        
        """

        file1.write(scenario_result + scenario_screenshots)
        file1.close()