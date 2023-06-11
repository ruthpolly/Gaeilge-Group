# Gaeilge Group

The Gaeilge Group is an Irish speaking group with the intention of improving their quality of Irish. It is not so much a casual speaking group, but with tests to gauage how much their skill has improved. This quiz was designed to assess the members level of Irish when they join, and project their expected score after a a short course has been completed.

![Range of devices image](/assets/documentation/am-i-responsive.png)

[Website deployed on Heroku](https://gaeilgegroup.herokuapp.com/)

## CONTENTS

- [Title](#Title)
  - [CONTENTS](#contents)
  - [User Experience (UX)](#user-experience-ux)
    - [Initial Discussion](#initial-discussion)
      - [Key information for the site](#key-information-for-the-site)
    - [User Stories](#user-stories)
      - [Client Goals](#client-goals)
      - [First Time Visitor Goals](#first-time-visitor-goals)
      - [Returning Visitor Goals](#returning-visitor-goals)
      - [Frequent Visitor Goals](#frequent-visitor-goals)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Wireframes](#wireframes)
    - [Features](#features)
    - [Accessibility](#accessibility)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
  - [Deployment \& Local Development](#deployment--local-development)
    - [Deployment](#deployment)
    - [Local Development](#local-development)
    - [Testing User Stories](#testing-user-stories)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
      - [Images](#images)
    - [Acknowledgments](#acknowledgments)

- - -

## User Experience (UX)

### Initial Discussion

The site is for members of the Gaeilge Group in order to asses their level of Irish before joining the group, to monitor their progress and project their expected score after a few weeks of learning. The site updates a google sheet the teacher has access to so the scores can be monitored.

### User Stories

#### Client Goals

- For users to be able to navigate the quiz
- Users can easily answer questions and understand instructions
- User names and scores are tracked in a google sheet
- Projected scores are calculated and communicated to user and teacher


#### First Time Visitor Goals

- Easily understand what the quiz contains
- Easily understand how the quiz works
- Receive feedback if incorrect key was used
- Receive feedback if incorrect answer was selected
- Receive feedback on completion of the quiz, get final score

#### Returning Visitor Goals

- Easily retake the quiz
- Easily understand and follow instructions of the quiz
- Receive feedback if incorrect key was used
- Receive feedback for incorrect answers

- - -

## Design

### Colour Scheme

Termcolor was import and used to add some colour to the quiz. This was solely for readability and to highligh important messages to the user. Red is used to communicate a mistake or an incorrect answer. Green is used to cmmunicate a correct answer and when the scores are sent to the teacher successfully.

### Flow Chart

- LucidChart was used to create a flow chart to plan the project. 

[Flow Chart](filepath)

## Structure

### Stages

- The first section is welcoming the user to the quiz and requesting a username. This is validated so that no whitespace, special characters or digits can be entered.

![Username Entry](/assets/documentation/username-entry.png)

- The next section gives the user information and instructions on how many questions/answers there are and how to answer the questions.

![Instructions Section](/assets//documentation/instructions-section.png)

- When the user proceeds with the quiz, the terminal clears and the first question is loaded.

![Questions](/assets//documentation/questions.png)

- If the user gets a question correct or incorrect, they are given feedback.

![Correct-Question-Feedback](/assets/documentation/correct-answer-feedback.png)
![Incorrect-Answer-Feedback](/assets//documentation/incorrect-answer-feedback.png)

- When the quiz is finished, the user is told that the score is being sent to the teacher. They are given their score, and the score they should achieve soon when they ahev finished learning.

![Final-feedback](/assets/documentation/result-and-feedback.png)

### Accessibility

It is important to make websites as accessible as possible. This was achieved by:

- Using semantic code.
- Giving regular feedback to the user, especially if they are using the quiz incorrectly
- Using coloured text to improve readability
- Using sleep timers to improve readability

- - -

## Technologies Used

### Languages Used

Python was used to create this website.

### Frameworks, Libraries & Programs Used

Google docs with lucid - Used to create flow chart.

Git - For version control.

Github - To save and store the files for the website.

Heroku - For deployment.

PEP8 - To troubleshoot and test features, solve

Stack Overflow 
- [Validation for text input](https://stackoverflow.com/questions/74211093/trying-to-validate-a-text-input-so-it-allows-characters-in-the-alphabet-only-as)
- [Validation for whitespace](https://stackoverflow.com/questions/9895775/how-to-check-for-white-space-input-in-python)
- [Termcolor and time](https://stackoverflow.com/questions/55958822/how-do-i-type-one-letter-at-a-time-for-an-input-in-python)

[PEP8](/assets/documentation/pep8-validation.png)



- - -

## Deployment & Local Development

### Deployment

Heroku was used to deploy the website. The instructions to achieve this are:

1. 
2. 
3. 
4. 
5. 
6. 

### Testing
- All testing can be found in this file:
![Testing](/TESTING.md)

- - -

## Credits

### Content

Content for the website was written Ruth O Sullivan.
Guidance/tutorials on how to achieve this site was found on the following websites/videos
-[aaa](filepath)
-[bbb](filepath)
I also searched on slack and stack overflow for any issues I came across and found almost all solutions there.

### Acknowledgments

I would like to acknowledge the following people who helped me along the way in completing my second portfolio project:

- The Code Institute Slack Community for constant support and guidance.
- [Jubril Akolade](https://github.com/Jubrillionaire), my Code Institute Mentor, for his advice, and endless patience.
- Alan Bushell, our cohort facilitator for his guidance along the way.