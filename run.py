import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('gaeilge_group')

NAME = ""
SCORE = 0


def enter_username():
    """
    Welcome message and asks user for username before beginning.
    """
    global NAME
    NAME = input("Hello! Enter your name and click the enter key to begin:\n")
    if NAME == "":
        print("Name is required to begin.")
        enter_username()
    else:
        start_quiz()	

def start_quiz():
    """
    Provides instructions and loads quiz if user agrees, or else returns to 
    name input.
    """
    print(f"Hello {NAME}! Welcome to the Gaeilge quiz, just do your best.")



def main():
    """
    Runs all program functions
    """
    enter_username()
    start_quiz()

main()