<!---
This guide was developed by Susi Remondi for COHORT NAME / DATE / LOCATION HERE.

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack @susiremondi
--->

![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)

### Instructor Guide
# Python Programming

----

> This course introduces beginners to the Python programming language, with a brief working intro to a special topic: either Data Science (Pandas) or Web Development (Flask).

## Overview
In this Python Programming course, students will walk away with a solid foundation in Python, able to confidently build basic applications. Students will also get an 8 hour dive into of one of two Python libraries -  either Pandas (for Data Science) or Flask (for Web Development), and walk away with a project of their choosing they've built using that library.

## Quick Links
- [About This Guide](#about-this-guide)
- [Contributors](#contributors)
- [Course Details](#course-details)
- [Suggested Pacing Guide](#suggested-pacing-guide)
- [Appendix: Materials and Resources](#appendix-materials-and-resources)
- [Notes for Teaching This Course](python-specific-course.md)
- [Instructions on Slide Delivery](presenting-and-creating-materials)
- Note: All of the decks for this course can be found [here](https://nagale.com/ga-python/). Markdown files will be available September 7.

## About This Guide

This guide contains links to a standard set of high quality resources for your use in teaching this course. But our goal is not to provide you with a script to follow; we hire practitioners at GA because we value what you bring to the classroom and want to encourage you to make adaptations.
Think of this guide as a cookbook. You, as the chef, will use the guidelines provided to craft an amazing meal for your students. But of course, you’ll want to think ahead about the various “dietary restrictions” and preferences of your “diners” as well as the type of “ambience” best suited to the type of experience you want to create.
Adaptations we encourage you to make:
- **Swapping out our generic examples for real-life examples from your industry experience.** The more you can speak to your own experience, the more the content will resonate with students.
- **Adapting suggested projects and activities to better challenge your students,** based on their level of prior knowledge and their interests.
- **Moving faster or slower as needed through the lessons based on the needs of your class.**


Adaptations we encourage you not to make without speaking with your manager first, especially during your first cohort:
- **Skipping over or cutting learning objectives.** Our curriculum is designed specifically to prepare students to a career in your industry. We’ve made a promise to them to get them job ready; when you skip content you’re putting their job readiness at risk.
- **Changing the scope of the course.** Try not to add new topics that distract from the core learning.
- **Radically altering the sequence of the course.** It’s okay to skip around sometimes, but try to follow the order of the units suggesting, especially during your first cohort.

>NOTE: If you haven’t already done so, be sure to complete the Instructor Course on myGA. The self-paced course provides a basic background in key concepts necessary for success leading a GA class.

When in doubt, discuss any planned changes to the curriculum you’d like to make with your manager, your fellow instructors, or a Global team member. Chances are, someone else can learn from or be inspired by your improvements!


## Contributors
General Assembly’s course materials are developed in close collaboration with our global expert network. This guide could not have been possible without the contributions of the following current and former instructors, students and community members:
- Brandi Butler
- Steve Peters
- Joseph Nelson
- Kevin Coyle
- Sonyl Nagale


## Course Details
Python Programming is a 40-hour course, delivered in either 5 day full-time or 10 week part time (two 2-hour sessions a week) format. There is no admittance requirement - this course is open to and encouraged for absolute beginners.

Once enrolled, students complete 2 hours of pre-work on the myGA platform.

>NOTE: As an instructor, you should familiarize yourself with this pre-work so you can incorporate it in to your first lesson.

Your role as an instructor is to facilitate each student’s journey to mastery of the concepts outlined below. This guide will provide you with a suggested pacing guide you can use to ensure you hit all of the required objectives in a sequence that makes sense. **We recommend you follow the suggested pacing guide during your first instance.** Later on, as you become more familiar with the content and your own teaching style, you can remix and extend the lessons provided. Just be sure to cover all of the required topics that follow.

In order to graduate and earn a course completion certificate, every student must complete a final project that meets or exceeds the minimum standards outlined in the project rubric. Your manager will help you track other graduation requirements and make decisions about graduation.

### Learning Objectives
The high-level learning objectives for this course are:

- Create a basic Python app, using control flow, classes, and try/catch statements.
- Incorporate APIs, modules, and user input into a Python app.
- Use Pandas to create a visualization of a dataset **or** use Flask to create and run a Python application (depending on the special topic track).

Students cannot graduate unless they demonstrate mastery of the above learning objectives before the end of the course. Mastery is measured through assessment: homeworks, in-class activities and final projects.

The official course syllabus, available [here](https://drive.google.com/file/d/1G5MxiLnVah4YAoJTzdIYK-8guTYC-Q7u/view), outlines what must be covered in the course.

Optional topics you may consider adding on to extend learning (provided your students are ready) include:
- More intermediate programming, such as decorators, logging, and unit tests.
- More interesting or specialized libraries, such as PyGame, NumPy, or Django.

### Course Format
This course may be taught online or in-person, in a [10-week](#10-week-pacing) or [1-week format](#1-week-pacing).


## Suggested Pacing Guide
The schedules below are provided as examples only. Feel free to create the right pace of lessons and activities for your students in order to ensure the required learning objectives are met. **Note:** These links will be live when the markdown files are available on Sept. 7

#### 1 Week Pacing

You can also view this in a Trello board [here](https://trello.com/invite/b/U7Exj4XJ/cb991c85cedbaa30789098d6d6697470/python-programming-5-day-schedule).

| Day 1: Python Fundamentals                                                         | Day 2: Mostly OOP                                                                               | Day 3: Intermediate Python                                                                                  | Day 4d (*Data Track)*: Pandas                                                       | Day 4w (*Web Dev Track)*: Flask                                          | Day 5: Review and Project                       |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------|
| [1:00] [Welcome](unit-1-variables/instructor-resources/01-welcome)      | [:30] Review Homework                                                                           | [:30] Review Homework                                                                                       | [:30] Review Homework                                                               | [:30] Review Homework                                                    | [:30] Review Homework                                           |
| [1:00] [Variables](unit-1-variables/instructor-resources/02-variables)             | [:45] [Advanced Function Arguments](unit-2-control-flow/instructor-resources/09-args)           | [:30] [Intermediate Variables](unit-4-troubleshooting/instructor-resources/17-intermediate-variables)       | [1:00] [Introduction to Data Science](unit-6-pandas/instructor-resources/01-ds-intro)                    | [:30] [Introduction to Web Dev](unit-6-flask/instructor-resources/01-web-dev-intro)                                           | [:30] Overall Review and Q&A *([Data Track link](unit-7-data-wrap-up/instructor-resources/01-review))* // *([Web Dev Track link](unit-7-web-dev-wrap-up/instructor-resources/01-review))* |
| [:30] [Installing Python3](unit-1-variables/instructor-resources/03-local-python)  | [1:35] [Unit Lab 2: Control Flow](unit-2-control-flow/instructor-resources/10-unit-lab-2)       | [:40] [Debugging Principles and Techniques](unit-4-troubleshooting/instructor-resources/18-debugging)       | [1:00] [Pandas I](unit-6-pandas/instructor-resources/02-pandas-i)                                        | [:30] [Flask Introduction](unit-6-flask/instructor-resources/02-flask)                                                 | [5:00] Project *([Data Track link](unit-7-data-wrap-up/instructor-resources/02-project))*  // *([Web Dev Track link](unit-7-web-dev-wrap-up/instructor-resources/02-project))*             |
| [:30] [Unit Lab 1: Variables](unit-1-variables/instructor-resources/04-unit-lab-1) | [:30] [Dictionaries](unit-3-oop/instructor-resources/11-dictionaries)                           | [:30] [Unit Lab 4: Troubleshooting](unit-4-troubleshooting/instructor-resources/19-unit-lab-4)              | [:45] [Data Visualization](unit-6-pandas/instructor-resources/03-data-viz)                               | [1:15] [HTML, CSS, and Styling Flask](unit-6-flask/instructor-resources/03-styling-flask)                                      | [1:00] Class Summary *([Data Track link](unit-7-data-wrap-up/instructor-resources/03-summary))* // *([Web Dev Track link](unit-7-web-dev-wrap-up/instructor-resources/03-summary))*        |
| [1:00] [Conditionals](unit-2-control-flow/instructor-resources/05-conditionals)    | [:40] [Sets and Tuples](unit-3-oop/instructor-resources/12-sets-tuples)                         | [:20] [Introduction to Intermediate Python](unit-5-intermediate/instructor-resources/20-intermediate-intro) | [1:00] [Plotting with Pandas and Matplotlib](unit-6-pandas/instructor-resources/04-plotting-with-pandas) | [1:00] [Variables and Routing](unit-6-flask/instructor-resources/04-flask-routing)                                       |                                                                 |
| [:30] [Lists](unit-2-control-flow/instructor-resources/06-lists)                   | [:50] [Classes](unit-3-oop/instructor-resources/13-classes)                                     | [:35] [Scripting](unit-5-intermediate/instructor-resources/21-scripting)                                    | [:45] [Pandas II](unit-6-pandas/instructor-resources/05-pandas-ii)                                       | [:30] [Templates](unit-6-flask/instructor-resources/05-flask-templates)                                                    |                                                                 |
| [1:00] [Loops](unit-2-control-flow/instructor-resources/07-loops)                  | [:20] [Inheritance](unit-3-oop/instructor-resources/14-inheritance)                             | [1:00] [Code Abstraction](unit-5-intermediate/instructor-resources/22-code-abstraction)                     | [1:30] [Unit Lab 6: Pandas](unit-6-pandas/instructor-resources/06-pandas-unit-lab)                       | [:30] [APIs and Requests](unit-6-flask/instructor-resources/06-flask-apis)                                            |                                                                 |
| [1:30] [Functions](unit-2-control-flow/instructor-resources/08-functions)          | [1:30] [Unit Lab 3: Object Oriented Programming](unit-3-oop/instructor-resources/15-unit-lab-3) | [:40] [Modules and Libraries](unit-5-intermediate/instructor-resources/23-modules)                          |  [:30] [Next Steps with Data Science](unit-6-pandas/instructor-resources/07-next-steps)                  | [1:30] [Unit Lab 6: Flask](unit-6-flask/instructor-resources/07-flask-unit-lab)                                                 |                                                                 |
|                                                                                    | [:20] [Variable Scope](unit-4-troubleshooting/instructor-resources/16-variable-scope)           | [:45] [APIs](unit-5-intermediate/instructor-resources/24-apis)                                              |                                                                                     | [:45] [Next Steps with Web Dev](unit-6-flask/instructor-resources/08-next-steps)                                    |                                                                 |
|                                                                                    |                                                                                                 | [1:30] [Unit Lab 5: Intermediate Python](unit-5-intermediate/instructor-resources/25-unit-lab-5)            |                                                                                     |                                                                          |                                                                 |
|  [Homework:Using lists, `if/elif/else`, and `for/while`](unit-2-control-flow/instructor-resources/hw-5day-day-1)                             | [Homework: Functions, dictionaries, inheritance, kwargs](unit-4-troubleshooting/instructor-resources/hw-5day-day2)                                          | [Homework: Code Abstraction, APIs, Debugging, Scripting](unit-5-intermediate/instructor-resources/hw-5day-day3)                                                      | [Homework: Basic EDA with Pandas, Visualization with Pandas](unit-6-pandas/instructor-resources/hw-5day-4pandas)                          | [Homework: Rendering templates, Creating an API, Making GET/POST requests](unit-6-flask/instructor-resources/hw-5day-4flask) |                                                                 |


#### 10 Week Pacing

You can also view this in a Trello board [here](https://trello.com/invite/b/SCQ7KxpO/fb313e83958ca787d59ae4a491458125/python-programming-10-week-schedule).

| Lesson # (Week:Day) | In Class |  | Homework |
| ------ | --- | --- |  ------ |
| Lesson 1 (w1:d1) | [Welcome](unit-1-variables/instructor-resources/01-welcome), [Variables](unit-1-variables/instructor-resources/02-variables), and [Installing Python3](unit-1-variables/instructor-resources/03-local-python) || [Homework: Declaring variables in a local file.](unit-1-variables/instructor-resources/hw-10wk-class-1) |
| Lesson 2 (w1:d2) | [Unit Lab 1: Variables](unit-1-variables/instructor-resources/04-unit-lab-1), [Conditionals](unit-2-control-flow/instructor-resources/05-conditionals), [Lists](unit-2-control-flow/instructor-resources/06-lists) || [Homework: Using `if` and `else`](unit-2-control-flow/instructor-resources/hw-10wk-class-2) |
| Lesson 3 (w2:d1) | [Loops](unit-2-control-flow/instructor-resources/07-loops), [Functions](unit-2-control-flow/instructor-resources/08-functions) || [Homework: Using lists, `if/elif/else`, and `for/while`](unit-2-control-flow/instructor-resources/hw-10wk-class-3) |
| Lesson 4 (w2:d2) | [Advanced Function Arguments](unit-2-control-flow/instructor-resources/09-args), [Unit Lab 2: Control Flow](unit-2-control-flow/instructor-resources/10-unit-lab-2) || [Homework: `if`, `for`, and list functions](unit-2-control-flow/instructor-resources/hw-5day-day-1) |
| Lesson 5 (w3:d1) | [Dictionaries](unit-3-oop/instructor-resources/11-dictionaries), [Sets and Tuples](unit-3-oop/instructor-resources/12-sets-tuples) || [Homework: Dictionaries, tuples, sets](unit-3-oop/instructor-resources/hw-10wk-class-5) |
| Lesson 6 (w3:d2) | [Classes](unit-3-oop/instructor-resources/13-classes), [Inheritance](unit-3-oop/instructor-resources/14-inheritance), [Unit Lab 3: Object Oriented Programming](unit-3-oop/instructor-resources/15-unit-lab-3) || [Homework: Functions, dictionaries, inheritance, kwargs](unit-3-oop/instructor-resources/hw-10wk-class-5) |
| Lesson 7 (w4:d1) | [Variable Scope](unit-4-troubleshooting/instructor-resources/16-variable-scope), [Intermediate Variables](unit-4-troubleshooting/instructor-resources/17-intermediate-variables), [Debugging Principles and Techniques](unit-4-troubleshooting/instructor-resources/18-debugging) || [Homework: Type Conversion, String Formatting, Debugging, Scope](unit-4-troubleshooting/instructor-resources/hw-10wk-class-7) |
| Lesson 8 (w4:d2) | [Unit Lab 4: Troubleshooting](unit-4-troubleshooting/instructor-resources/19-unit-lab-4), [Introduction to Intermediate Python](unit-5-intermediate/instructor-resources/20-intermediate-intro), [Scripting](unit-5-intermediate/instructor-resources/21-scripting), [Code Abstraction](unit-5-intermediate/instructor-resources/22-code-abstraction) || [Homework: Scripting and Code Abstraction](unit-5-intermediate/instructor-resources/hw-10wk-class-8) |
| Lesson 9 (w5:d1) | [Code Abstraction, Continued](unit-5-intermediate/instructor-resources/22-code-abstraction), [Modules and Libraries](unit-5-intermediate/instructor-resources/23-modules) || [Homework: Modules and Libraries](unit-5-intermediate/instructor-resources/hw-10wk-class-9) |
| Lesson 10 (w5:d2) | [APIs](unit-5-intermediate/instructor-resources/24-apis), Review || [Homework: APIs and String Formatting](unit-5-intermediate/instructor-resources/hw-10wk-class-10) |
| Lesson 11 (w6:d1) | [Unit Lab 5: Intermediate Python](unit-5-intermediate/instructor-resources/25-unit-lab-5) || [Homework: Code Abstraction, APIs, Debugging, Scripting](unit-5-intermediate/instructor-resources/hw-5day-day3) |
| Lesson 12d (w6:d2) | *Data Track*: [Introduction to Data Science](unit-6-pandas/instructor-resources/01-ds-intro), [Pandas I](unit-6-pandas/instructor-resources/02-pandas-i) || [Homework: Reading datasets into Pandas,  Filtering, manipulating, and sorting datasets, Basic exploratory data analysis with Pandas](unit-6-pandas/instructor-resources/hw-10wk-12d) |
| Lesson 12w (w6:d2) | *Web Dev Track*: [Introduction to Web Dev](unit-6-flask/instructor-resources/01-web-dev-intro), [Flask Introduction](unit-6-flask/instructor-resources/02-flask), [HTML, CSS, and Styling Flask](unit-6-flask/instructor-resources/03-styling-flask) || [Homework: Writing a basic Flask app](unit-6-flask/instructor-resources/hw-10wk-11) |
| Lesson 13d (w7:d1) | *Data Track*: [Data Visualization](unit-6-pandas/instructor-resources/03-data-viz), [Plotting with Pandas and Matplotlib](unit-6-pandas/instructor-resources/04-plotting-with-pandas) ||  [Homework: Plotting with Pandas, Determining the best plot, given a dataset](unit-6-pandas/instructor-resources/hw-10wk-13d) |
| Lesson 13w (w7:d1) | *Web Dev Track*: [Variables and Routing](unit-6-flask/instructor-resources/04-flask-routing), [Templates](unit-6-flask/instructor-resources/05-flask-templates), [APIs and Requests](unit-6-flask/instructor-resources/06-flask-apis) || [Homework: Variables, Routing, Templates](unit-6-flask/instructor-resources/hw-10wk-12) |
| Lesson 14d (w7:d2) | *Data Track*: [Pandas II](unit-6-pandas/instructor-resources/05-pandas-ii), [Unit Lab 6: Pandas](unit-6-pandas/instructor-resources/06-pandas-unit-lab) || [Homework: Basic EDA with Pandas, Visualization with Pandas](unit-6-pandas/instructor-resources/hw-5day-4pandas) |
| Lesson 14w (w7:d2) | *Web Dev Track*: [Unit Lab 6: Flask](unit-6-flask/instructor-resources/07-flask-unit-lab) || [Homework: Rendering templates, Creating an API, Making GET/POST requests](unit-6-flask/instructor-resources/hw-5day-4flask) |
| Lesson 15d (w8:d1) | *Data Track*: Lab Review, [Next Steps with Data Science](unit-6-pandas/instructor-resources/07-next-steps) || < None > |
| Lesson 15w (w8:d1) | *Web Dev Track*: Lab Review, [Next Steps with Web Dev](unit-6-flask/instructor-resources/08-next-steps) || < None > |
| Lesson 16d (w8:d2) | *Data Track*: [Overall Review and Q&A](unit-7-data-wrap-up/instructor-resources/01-review), [Introduce Project](unit-7-data-wrap-up/instructor-resources/02-project) || < None > |
| Lesson 16w (w8:d2) | *Web Dev Track*: [Overall Review and Q&A](unit-7-web-dev-wrap-up/instructor-resources/01-review), [Introduce Project](unit-7-web-dev-wrap-up/instructor-resources/02-project) || < None > |
| Lesson 17 (w9:d1) | Work on Project || < None > |
| Lesson 18 (w9:d2) | Work on Project || < None > |
| Lesson 19 (w10:d1) | Project Presentations || < None > |
| Lesson 20d (w10:d2) | *Data Track*: Project Presentations, [Class Summary](unit-7-data-wrap-up/instructor-resources/03-summary) || < None > |
| Lesson 20w (w10:d2) | *Web Dev Track*: Project Presentations, [Class Summary](unit-7-web-dev-wrap-up/instructor-resources/03-summary) || < None > |


---

## Appendix: Materials and Resources
- Please read through the [specific course details](python-specific-course.md) for information on the structure of the repos, how to run the unit labs, the projects, and more.
- See the [presenting and creating materials](presenting-and-creating-materials/README.md) directory for instructions on presenting the materials on GA Brand or creating your own.
- All lesson materials, homeworks and projects outlined on the Suggested Pacing Guide are in this repo.
- Standard GA-produced pre-work materials can be accessed on myGA. The pre-work lessons are:
  - **Welcome to Python Programming:** A short lesson giving them an overview of the course.
  - **Introduction to Programming:** Teaches "programming language", "programmatic thinking", and "pseudocode".
  - **Introduction to Python:** Teaches, "open source", `#` comments, and `print` statements in Python3.
  - **Key Concept Review:** Reviews keywords above.
- Tips and templates for instructors are available on the [GA Instructor Blog](http://assemblyrequired.ga.co).
- For help and support, join the GA Instructors Slack Community and post your questions in #SLACKCHANNEL.


*Copyright 2018, General Assembly Space. Licensed under [CC-BY-NC-SA, 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)*
