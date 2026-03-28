import sys
import os


# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from Support.Generic.Reports import *
from Support.Generic.TBS import *
from Support.Generic.Common import *
from Support.Generic.Support import *
from Support.Forms.NEC import *
from ObjectRepository.Generic.Login import *


setup_project_environment()
login_environment_variables()
execution_directory = os.getenv("execution_directory", os.getcwd())
os.environ['execution_directory'] = execution_directory
folder_configuration(execution_directory)


def test_run(page):
    start = 2
    end = 3
    title = "NEC"
    login(page)
    testcase_NEC(page, start=start, end=end, title=title)
