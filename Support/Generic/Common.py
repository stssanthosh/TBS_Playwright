from Support.Generic.report import *
from ObjectRepository.Generic.login import *
import random 

def fake_ein():
    import random
    valid_prefixes = [
        "01","02","03","04","05","06","10","11","12","13","14","15","16","20","21","22",
        "23","24","25","26","27","30","31","32","33","34","35","36","37","38","39",
        "40","41","42","43","44","45","46","47","48","50","51","52","53","54","55",
        "56","57","58","59","60","61","62","63","64","65","66","67","68","71","72",
        "73","74","75","76","77","80","81","82","83","84","85","86","87","88","90","91","92","93","94","95","98","99"
    ]

    prefix = random.choice(valid_prefixes)
    body = f"{random.randint(0, 9999999):07d}"
    return f"{prefix}-{body}"


def random_us_state_zip():
    """
    Returns a random U.S. state with a realistic ZIP code.
    Example: ('California', '90210')
    """
    us_states_zip = {
        "Alabama": (35004, 36925),
        "Alaska": (99501, 99950),
        "Arizona": (85001, 86556),
        "Arkansas": (71601, 72959),
        "California": (90001, 96162),
        "Colorado": (80001, 81658),
        "Connecticut": (6001, 6928),
        "Delaware": (19701, 19980),
        "Florida": (32003, 34997),
        "Georgia": (36928, 39901),
        "Hawaii": (96701, 96898),
        "Idaho": (83201, 83877),
        "Illinois": (60001, 62999),
        "Indiana": (46001, 47997),
        "Iowa": (50001, 52809),
        "Kansas": (66002, 67954),
        "Kentucky": (40003, 42788),
        "Louisiana": (70001, 71497),
        "Maine": (3901, 4992),
        "Maryland": (20601, 21930),
        "Massachusetts": (1001, 2791),
        "Michigan": (48001, 49971),
        "Minnesota": (55001, 56763),
        "Mississippi": (38601, 39776),
        "Missouri": (63001, 65899),
        "Montana": (59001, 59937),
        "Nebraska": (68001, 69367),
        "Nevada": (88901, 89883),
        "New Hampshire": (3031, 3897),
        "New Jersey": (7001, 8989),
        "New Mexico": (87001, 88441),
        "New York": (10001, 14975),
        "North Carolina": (27006, 28909),
        "North Dakota": (58001, 58856),
        "Ohio": (43001, 45999),
        "Oklahoma": (73001, 74966),
        "Oregon": (97001, 97920),
        "Pennsylvania": (15001, 19640),
        "Rhode Island": (2801, 2940),
        "South Carolina": (29001, 29945),
        "South Dakota": (57001, 57799),
        "Tennessee": (37010, 38589),
        "Texas": (73301, 88595),
        "Utah": (84001, 84791),
        "Vermont": (5001, 5907),
        "Virginia": (20101, 24658),
        "Washington": (98001, 99403),
        "West Virginia": (24701, 26886),
        "Wisconsin": (53001, 54990),
        "Wyoming": (82001, 83414),
    }

    # Choose a random state
    state = random.choice(list(us_states_zip.keys()))
    # Pick a ZIP code within range
    zip_code = random.randint(us_states_zip[state][0], us_states_zip[state][1])
    # Ensure ZIP is formatted as 5 digits
    zip_code = str(zip_code).zfill(5)

    return state, zip_code

def fail_message(page, test_data):
    Scenario_ID = test_data.get("Scenario_ID")
    Status = test_data.get("Status")
    Result = test_data.get("Result")
    # Result = test_data.get("Result", "Script fail due to exception")
    add_screenshot(page, Scenario_ID)
    generate_report(page, Status, Result, test_data)


     