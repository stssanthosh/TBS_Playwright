import os, sys
from openpyxl import load_workbook
from Support.Generic.TBS import *
from Support.Generic.Common import *
from Support.Generic.Reports import *
from Support.Generic.Support import *
from Support.Generic.email import *


def testcase_1095b(page, start, end, title, region="STAGING"):
    os.environ["Title"] = title
    form = "NEC"
    sheet_name = form
    file_sheet_index("TBS", sheet_name)
    env_vars, max_row = file_sheet_index("TBS", sheet_name)

    business_type = "Employer"
    recipient_type = "Employee"

    if str(end) == "2":
        end = 2
    elif str(end).upper() == "ALL":
        end = max_row
    else:
        end = int(end)
        
    

    test_data = None  



    for row in range(int(start), end + 1):
        start_time = current_time()

        Scenario_ID = read_excel(sheet_name, row, "Scenario_ID")
        Scenario_Description = read_excel(sheet_name, row, "Scenario_Description")
        type_val = read_excel(sheet_name, row, "Type")
        module = read_excel(sheet_name, row, "Module")
        result = ""

        test_data = {
            "Scenario_ID": Scenario_ID,
            "Scenario_Description": Scenario_Description,
            "type": type_val,
            "start_time": start_time,
            "Form": form,
            "module": module,
            "Result": result,
            "Row": row,
            "PayerType": business_type,
            "RecipientType": recipient_type,
            "Status": False
        }
        try:
            go_to_1095B_form(page, test_data)
            add_employer(page, test_data)
            add_recipient(page, test_data)
            form_b(page, test_data)
            review_summary(page, test_data)
            card_payment(page, test_data)
            status = test_data.get("Status")
            result = test_data.get("Result")
            generate_report(page, status, result, test_data)

        except Exception as e:
            print(f"Error in Scenario ID {Scenario_ID}: {e}")
            Result = test_data.get("Result")
            test_data["Result"] = f"{Result}; Script failed due to exception"
            test_data["Status"] = False
            fail_message(page, test_data)
    return test_data

