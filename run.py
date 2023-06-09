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
    print(f"Hello {NAME}! Welcome to the Gaeilge quiz, just do your best.\n")
    print("This is a multiple choice quiz with 10 questions, and 4 answer"
          " options. When you are ready to answer, you can enter either 'a',"
          " 'b', 'c', or 'd' and click the enter key to submit your answer.\n"
          "You will be asked at the end of each question if you would like "
          "to proceed to the next question. Click 'y' and enter for yes, or"
          " 'n' and enter for no.")
    
    ready_to_begin = input(f"OK {NAME}, are you ready to try it? (y/n):")


def main():
    """
    Runs all program functions
    """
    enter_username()


main()
