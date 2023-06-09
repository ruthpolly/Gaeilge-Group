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

quiz_data = [
    {"Question": "1. What does 'Go tobann! mean?",
     "Answers": {"a": "Suddenly",
                 "b": "No!",
                 "c": "Get out!",
                 "d": "Amazing!"},
     "correct_answer": "a"},
    {"Question": "2. How would you say 'the weather is lovely'?",
     "Answers": {"a": "Sea sea sea",
                 "b": "Is maith liom tae.",
                 "c": "Tá an ghrian ag scoilteadh na gcloch.",
                 "d": "Ní thuigim."},
     "correct_answer": "c"},
    {"Question": "3. Finish this line of Géibheann by Caitlín Maude,\n"
                 "Ainmhí mé, ainmhí allta as __________",
     "Answers": {"a": "Port Láirge",
                 "b": "an Aifric",
                 "c": "an abhainn",
                 "d": "na teochreasa"},
     "correct_answer": "d"},
    {"Question": "4. Who wrote the book A Tigh ná Tit Orm?",
     "Answers": {"a": "Caitlín Maude",
                 "b": "Des Bishop",
                 "c": "Daithí Ó Sé",
                 "d": "Maidhc Dainín Ó Sé"},
     "correct_answer": "a"},
    {"Question": "5. What is 'craic agus ruaille buaille'?",
     "Answers": {"a": "Controlled substances",
                 "b": "Fun and excitement",
                 "c": "dinner and drinks", 
                 "d": "cats and dogs"},
     "correct_answer": "b"},
    {"Question": "6. How do you say 'Hi, how are you?'",
     "Answers": {"a": "Ciúnas bóthar cailín bainne?",
                 "b": "Conas atá tú?",
                 "c": "Póg mo thón", 
                 "d": "Ní thuigim"},
     "correct_answer": "b"},
    {"Question": "7. What is cácá milis",
     "Answers": {"a": "A sweet cake",
                 "b": "A movie about a blind man on a train eating cake.",
                 "c": "A bird",
                 "d": "Ribena"},
     "correct_answer": "b"},
    {"Question": "8. How would you say St. Patrick's Day as Gaeilge?",
     "Answers": {"a": "Lá Féile Pádraig",
                 "b": "St Patty's Day",
                 "c": "Ag imirt peile",
                 "d": "Ag feachaint ar an teilifís"},
     "correct_answer": "a"},
    {"Question": "9. What does 'ar meisce' mean?",
     "Answers": {"a": "Drunk",
                 "b": "Happy",
                 "c": "Silly", 
                 "d": "Mean"},
     "correct_answer": "a"},
    {"Question": "10. Which of these sentences is correct",
     "Answers": {"a": "Is é Corcaigh príomhchathair na hÉireann",
                 "b": "Ní maith linn tae"
                      "Is fuath linn teigh amach go dtí an tigh tabhairne",
                 "c": "Bíonn an ghrian ag taitneamh go minic",
                 "d": "Is breá linn na Sasanaigh"},
     "correct_answer": "a"},
]


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

    while ready_to_begin != "y":
        enter_username()

    if ready_to_begin == "y":
        load_questions()


def load_questions():
    """
    Runs through the questions
    """


def main():
    """
    Runs all program functions
    """
    enter_username()


main()
