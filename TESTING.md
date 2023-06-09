# Title -  Testing

![Title](filepath)

Visit the deployed site: [Title](filepath)

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

Testing was ongoing throughout the build. Printing to the console was used to make sure everything was functioning correctly and to help troubleshooting when something went wrong, and to test functions along the way.

- - -

## AUTOMATED TESTING

### PEP8 Validator

[PEP8](link) was used to validate the code. 

* [Results](filepath) - No errors or warnings.
- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website. 

### Desktop Results

* [Index Page](/documentation/lighthouse-desktop-home.png)

### Mobile Results

* [Index Page](/documentation/lighthouse-mobile-home.png)
- - -

## MANUAL TESTING

### Testing User Stories

| Goals | How are they achieved? |  |
| :--- | :--- | :--- |
| `First Time Visitors` |
|  |  |  |
| Understand what the site is for and how to navigate the site. | Instructions on how to play the game are displayed. |  |
| Submit a username. |  |
| Play a quiz | Users get to take part in a quiz to learn about Irish phrases. |  |
|`Returning Visitors`|
|  |  |  |
| Play a quiz | Find new quizes/games |  |
| Learn more about other cultures slang/phrases | When playing the quiz the user will learn the correct answer. |  |

- - -

### Full Testing

Full testing was performed on the following devices:

* Laptop:
  * HP laptop
* Mobile Devices:
  * iPhone 13.
  * iPhone 11.
  * Samsung devices.

Each device tested the site using the following browsers:

* Google Chrome
* Safari
* Firefox

Additional testing was taken by friends and family on a variety of devices and screen sizes. 

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `Start` |
|   |   |   |   |
| Username field | User should be able to enter username. | Enter username  | Username entered | Pass |
| Username field | User should not be able to continue without entering username. | Click return key with input blank  | Message tells user input cannot be blank | Fail |
| Start quiz | When button is clicked the user will be redirected to the quiz. | Clicked Start Quiz | Redirected to quiz | Pass |
| `Quiz` |
| Select Correct Answer | When correct key is entered, congratulations message should load | Correct answer entered | Message loaded | Pass |
| Select correct answer | When correct option is clicked, button clicked should turn green | Clicked correct answer | Field turns green |  Pass |
| Select incorrect answer | When incorrect option clicked, button clicked should turn red, and correct green. | Clicked incorrect answer | Button clicked turned red and correct answer button turned green | Pass |
| Next button | Next question should appear | Next button clicked | Next question appears | Pass |
| Home button | User will be redirected to home page | Home button clicked | Redirected to the home page | Pass |
| Score increase | Score incremente by one with correct answer | Correct answer selected | Score incremented | Pass |
| Score increment | Score should not increment with incorrect answer. | Incorrect answer selected | Score did not increase | Pass |
| `Results Page` |
| Next Button | Results page should be displayed | Clicked next on last question | Results page displayed | Pass |
| Final Score | Final score should be displayed | Clicked next on last question | Final score displayed | Pass |
| Home button | Should redirect user back to home page | Clicked home button | Home page displayed | Pass |

 - - -

## BUGS

### Solved Bugs

| No | Bug | How I solved the issue |
| :--- | :--- | :--- |
| 1 | The final score would not display on the results page | This proved difficult to solve, ans was taking up a lot of time for a small issue, so I worked around this by deleting the p element in the html results area. I inserted the text on the results page through the JavaScript file and updated the score from there.  |
| 2 | The quiz was skipping questions, I turned to tutor support for this and they suggested the event listener within the function was the issue. I texted this in Chrome Developer using the console log, it was not the issue. | I continued to test the issue using the console log and realised I had called the function to show a new phrase twice some how. After more testing, and no progress, I checked my html file and saw I had called it there also. So I just deleted it. Problem solved.|
| 3 | The hover pseudo class was still applied to the buttons after clicking an option, the button diabled but it still transformed when hovered over, which could give the user the impression it was still possible to click. | Having looked on stack overflow, the best option seemed to be to add a new class in js when the button was clicked, and remove the hover effect. I felt this made the quix more static and less interactive. I checked for the rgba values of the disabled buttons in chrome developer and changed them slightly, so there would still be an effect when hovering over the buttons. |

- - -

### Known Bugs

| No | Bug | |
| :--- | :--- | :--- |
| 1 | When viewing on a mobile, the selected answer in the quiz does not turn green/red when selected. This could probably be resolved with a media query however due to time restraints I did not explore this | |
| 2 | The user can skip questions without selecting an answer, this is not so much a bug but something I had planned on implementing, but again due to time restaints I did not explore the option. |
| 3 | The username is not required as it was intended to be. I was advised on slack that I would need to validate it manually through Javascript but after about half an hour I decided to give up on it as I did not have the time to spend ensuring it worked. |