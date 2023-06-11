# Gaeilge Group -  Testing

![Gaeilge Group](/assets/documentation/am-i-responsive.png)

Visit the deployed site: [Gaeilge Group](https://gaeilgegroup.herokuapp.com/)

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [PEP8 Validator](#javascript-validator)
  * [Lighthouse](#lighthouse)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
* [BUGS](#bugs)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)

Testing was ongoing throughout the build. Printing to the terminal was used to make sure everything was functioning correctly and to help troubleshooting when something went wrong, and to test functions along the way.

- - -

## AUTOMATED TESTING

### PEP8 Validator

[PEP8](https://pep8ci.herokuapp.com/) was used to validate the code. 

* [Results](/assets/documentation/pep8-validation.png) - No errors or warnings.

- - -

## MANUAL TESTING

### Testing User Stories

| Goals | How are they achieved? |  |
| :--- | :--- | :--- |
| `First Time Visitors` |
|  |  |  |
| Understand what the site is for and how to navigate the site. | Instructions on how to play the game are displayed. |  |
| Submit a username. | Users are asked to submit a username when the program runs |
| Play a quiz | Users play the quiz to asses level of skill for self development and for teachers assessment. |  |
|`Returning Visitors`|
|  |  |  |
| Play a quiz | Track improvement/learning by comparing score |  |

- - -

### Full Testing

Full testing was performed on the following devices:

* Laptop:
  * HP laptop

Each device tested the site using the following browsers:

* Google Chrome
* Firefox

Additional testing was taken by friends and family on a variety of browsers.

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `Start` |
|   |   |   |   |
| Username field | User should be able to enter username. | Enter username  | Username entered | Pass |
| Username field | User should not be able to continue without entering username. | Click return key with input blank  | Message tells user name is required | Pass |
| Username field | User should not be able to enter white space and continue | Entered white space and clicked return | Requested to enter a username | Pass |
| Username field | User should not be able to enter special characters/numbers | Entered special character/number and clicked return | Requested to enter a username | Pass |
| Start Quiz | User should not be able to continue without entering 'y''. | Click return key with input blank  | Message reminds user 'y' is needed to continue | Pass |
| Start Quiz | User should not be able to enter white space and continue | Entered white space and clicked return | Requested to enter 'y' to continue | Pass |
| Start Quiz | User should not be able to enter special characters/numbers | Entered special character/number and clicked return | Requested to enter 'y' to continue | Pass |
| `Quiz` |
| Select Correct Answer | When correct key is entered, congratulations message should load | Correct answer entered | Message loaded | Pass |
| Select correct answer | When correct answer chosen, score should increment | Input correct answer | Score increments |  Pass |
| Select incorrect answer | When incorrect option chosen, message stating the answer is incorrect and what correct answer is should appear | Input incorrect answer | Message appeaared | Pass |
| Input letter not in list | Message should prompt user to input letter from list and reqeat question | Input letter not in list | Message appeaared | Pass |
| `Results Page` |
| Finish Quiz | End of quiz message displayed | Finished quiz | Results page displayed | Pass |
| Update Worksheet | Worksheet updated | Finished Quiz | Worksheet updated with score and projected score | Pass |
| Scores | Final score and projected score should be displayed | Finished Quiz | Scores displayed | Pass |

 - - -

## BUGS

### Solved Bugs

| No | Bug | How I solved the issue |
| :--- | :--- | :--- |
| 1 | The projected score would not display on the projected worksheet | I had been trying to access the second colum of a second worksheet to input a calculated projection. It was easier and cleaner code to do the calculation after the final score, within the same function. Then append it to the list to be updated to the worksheet. |
| 2 | The validation was only working if the input was submitted when blank | I searched on stack overflow and found I could use the isspace, isalpha to further the validation. |
| 3 | The terminal was getting congested with text when running the quiz. | My mentor suggested using the os system to clear the terminal at intervals. |
| 4 | When I used the os system to clear the terminal, the terminal cleared before the user would get to read the feedback | I found on Stack Overflow that I could use the time module to slow down the clear function |
| 5 | The terminal had quite a bit of text, and it being all white it can be difficult for some people to read. | Stack Overflow suggested using colour to distinguish/emphasise text. I used termcolor to break up the text to make it easier to read |


- - -

### Known Bugs

| No | Bug | |
| :--- | :--- | :--- |
| 1 | Users can reuse user names. This would make it difficult for the assessor to distinguish between students. | |
| 2 | Students cannot access their previous scores |