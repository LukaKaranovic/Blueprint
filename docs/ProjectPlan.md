# Team Apache 84: Project Plan

## Document Overview

This document outlines the development  of Blueprint.VIU.CS, a tool designed to assist VIU Students with semester-specific course planning. Beginning with a detailed proposal for the project's purpose and objectives, followed by a detailed discussion of its features, such as course flash cards, course difficulty ratings, and overall semester difficulty ratings.

Subsequent sections cover the management of tasks, the planned technical implementation of key functionalities, and risk analysis. This document also highlights how the tool can positively impact students and faculty, along with suggested future enhancements to elevate its usefulness. 

## Project Update

* Added core features to preliminary proposal in A1 document.
* Updated preliminary proposal section in `TeamFormation.md` to include two types of users.
* Updated our main technology to be Python and SQLite, instead of Python and Oracle.
* Addressed all feedback for `TeamContract.md` given to us from discussion posts and A1 evaluation. Several changes were made to all sections.

## Project Proposal

We decided on the name Blueprint.VIU.CS for our name. We chose this name because we want our project to function as a blueprint for picking the optimal class combination for each semester, with our focus on the computer science program.

### Product Overview:
Our plan for the project is to have a user-friendly interface that helps computer science students manage their workloads on a per semester basis, focusing on helping them plan the easiest class combination possible to achieve that goal. The idea is that students can select the courses they want for a particular semester, and it will come up with course specific information and an overall semester difficulty score, which tells students whether or not they should change their courses. The target audience of our project will be VIU CS students who want to ensure success in a specific semester and minimize the chance of failing classes due to a high semester workload. It will also be made for the VIU CS teachers and faculty, so they can see which semesters have a much higher workload than others in order to alter the program to be more balanced across all semesters. We intend to have a list of cards of each required course in the CS program, sorted by the year the course is in, and the semester(s) the course is offered (fall or spring). These cards will function like flashcards, which hold all of the course data, and will present information once clicked. Each card will contain the difficulty, time recommended per week, importance, and main topics of the course. We will have a search feature which allows you to look up classes through filters. As a stretch goal we will have a planning feature which allows students to plan future semester course selections and save them.

### What problem the product will solve:
Not many people have completed the 4-year VIU CS program in 4 years. This is partly due to not prioritizing the correct courses or having to retake classes because of failure. The biggest contributor to this problem is the drastic difference in workload in each semester throughout the program. This can be harmful as others work a job outside of school and can not handle the sudden change in workload, with no easy way to tell. Understanding the difficulty and the time required for specific classes is confusing and requires self research to fully understand. Many classes lack information about how much work outside of scheduled class times is required to succeed, which often leads to students taking on too heavy of a workload at once. 

Many students do not like the current VIU goal planning system (GPS), and often get caught in the trap of missing courses they need (pre-reqs for other courses). While this system doesn't plan on replacing the VIU GPS, it hopes to serve as an additional tool to be used in combination with it. Students also end up not knowing which classes require more work than others, and end up not being prepared to put in the time for those courses. Having this knowledge will be beneficial to student mental health as they will not be caught off guard by the workload of certain courses. 

Most students avoid these heavy workloads (or are warned about them) from other students rather than from instructors or the program itself. The goal of our information system is to encourage current students to leave reviews and a difficulty rating for each course they have taken, to give pass this valuable information on to future students.

Additionally, many computer science teachers and faculty often forget what it is like to be a beginner, so they do not know what is too much or too little content for a course. Our system may provide the information needed to help remind them what it is like to be a student. The hope is that faculty dean could submit a proposal to the Planning and Priorities Standing Committee make adjustments by spreading out more difficult courses or by reducing the content in them to make it easier on future students.

This product will help students avoid missing important but difficult courses with our course importance rating (sometimes taking a hard, but key class is more efficient than taking two easier, less important ones), which is based on how many courses the course is a prerequisite for. It will also benefit students’ mental health by helping them avoid heavy workload semesters (such as taking MATH 223, CSCI 260, 261, 265 all at once), offering them a more manageable and balanced lifestyle. The system will also give a brief description of each class, which can eliminate confusion on what classes cover which material. This product will help the CS teachers and faculty locate which courses are too difficult or too easy, as the data is provided by students. They can then look at these courses and change the curriculum(s) of them to adjust their difficulty, split up the more difficult courses across different semesters, or offer the harder courses more frequently.

### Preliminary Prioritized Features List

**Core Features:** 
* Flashcards containing course data, which includes: 
	* A tag of what year the course is normally taken in (1-4), and whether it is offered in the fall, spring, or both.
* Course difficulty (0-5 rating)
* Time recommended per week to spend on the course (hours)
* Importance (low, medium, or high -> based on how many courses this course is a prerequisite for, and if it is a graduation requirement)
* The main topics/description of the course.
* All current sections and their times (for the next year)
* Search feature which allows you to look up courses by:
	* Course code (e.g. CSCI 260)
	* Year (1-4)
	* Terms offered (fall, spring, summer, both)
	* More search options would be a stretch goal.
* Semester average difficulty rating (based on courses selected)
* Review system or system for collecting data
	* Allow students to submit difficulty rating and time recommended for a course 
* The ability for faculty to add official course data (such as schedules, main topics, credits, instructors)

**Stretch / Additional Features:**
* Account system for saving selections/schedules for current or future semesters, and for keeping track of your reviews (reviews are anonymous to others)
* A planning feature, which allows students to plan future semesters and save them somewhere.
* Built in course timetable maker (like VIU student record, but with customizable colours)
* Timetable integration:
	* Warning popup if you select courses with conflicting times
* Optimization of classes and suggested feedback based on course selections (such as giving you recommended courses to add or drop)
* Expansion to other faculties/programs, ideally math courses would be the place we expand to first.
* Additional search options: 
	* Course name (e.g. Data Structures and Algorithms)
	* Difficulty range (0-5)
	* etc.
* A verification system to verify a student has taken that course before submitting a review (inputting student number is an option)
* A verification system to verify that a user is an instructor/faculty member before they can change certain course information.
* A feature that creates an announcement automatically if a faculty member makes a change to the course information.

## Management Plan

### Task Tracking

The issues board will be used to track the individual pieces of our development and documentation. The boards have been separated into multiple different processes in our projects design and implementation such as documentation, development, modeling, testing and updates. For this phase, we have added all sections of documentation that were needed to be completed and assigned them to members based on what they were chosen to do by our group meeting. The overall process of setting up the issues board was convenient and useful, the only challenge was being able to assign multiple project members to individual tasks which may give us trouble further down development.

### Technical Processes

#### Version Control Procedures

**Note:** The lack of branch protection in our version control procedures is due to the fact that we only have a 3 week development cycle. We want to keep things moving at a fast pace, and not have people waiting for code reviews as we don’t have much time. 

##### Development

For development, we will be using a separate GitLab branch to hold our codebase, named `Blueprint`. This branch will act as our ‘main’ branch for our codebase. There will be individual branches for each component of the system. Once the individual component’s implementation is deemed complete, it will be pushed to a `testing` branch, where it will be tested for integration with the main code (all of the other components).

Once everything works on the `testing` branch, it will be pushed to`Blueprint`. Only code that works properly and is currently in the testing branch will be allowed on the Blueprint branch (more on that below).

* The `testing` branch remains the total integration branch for all playtesting and beta build distribution.
* Codebase changes being merged into `Blueprint` from `testing` must run through all of our tests (to be determined) successfully on a VIU CSCI machine (pup, cub, or kit).
* When applicable, branch protection will be applied (to Blueprint only), requiring code reviews by at least **two other members** before a merge can continue from `testing` to `Blueprint` (described later in the coding standards section).

The branch protection process for merging the `testing` branch to `Blueprint` is as follows:

1. The code writer creates a pull request when they are ready to commit changes. A comment is left on the pull-request describing the changes.
2. The code writer must then request a review officially on GitHub, where a reviewer must accept this request and look at the changes.
3. After the review, if the code is deemed to be up to standard, the changes will be merged into the Blueprint branch.

A single commit ideally should never modify more than 200 lines. Commit message titles should be clear, and commit messages should be clearly descriptive about the changes made. Separate commits should be made to resolve separate issues.

##### Documentation

Documentation will be kept in the `main` branch on GitLab. It will contain all of the documentation required for the course project, organized in folders for each deliverable (A1 to A6).

Documentation is mainly worked on in a shared team Google Drive, as Google Docs allows for live collaboration among the group for in-class work. At least every weekend, documentation will be moved from the Google Drive to the GitLab repository. Minor changes and edits (mainly due to proofreading) will be made directly to the repository.

No branch protection will be applied to the `main` branch, since only documentation is in here. If a big mistake is made, we rollback the commits on the `main` branch.

#### Development Environment and Tools

Please note that these are **preliminary and subject to change** if the tools do not work well in combination with one another.

For main code development, we will use VSCode as our IDE when developing our backend in Python and our frontend in HTML, CSS, and JavaScript.

For our databases, we plan on using SQLite on the command line, with future migration to MySQL. 

We also plan to use Flask for backend database interaction with Python and SQLite.

We switched to SQLite for our database as we only have a 3 week development cycle, we are using it as a proof of concept with future migration to MySQL.

#### Code Standards

Methods and functions should be kept short whenever possible – never more than a screen. If something is done repeatedly, it should be refactored into its own method. Avoid the use of global variables when practicable.

For in-code documentation: When creating new classes, methods, members, etc., Doxygen-style comments will be added to those objects.

**Code Reviews:** Before merging code into the testing branch, it is required at least one other member does a code review before a merge can continue. This mechanism is done via a 'pull request' (more context on this in the version control section).

* The reviewer must be able to understand the code and must ensure the code writer has provided proper in-code documentation.
* If the reviewer does not understand part of the code, it must be described in the in-code documentation. If not, the code writer must go back and edit the comments to explain said parts before merging.
* Both the reviewer and code writer must ensure the code works as intended with the rest of the system before merging into the `Blueprint` branch.

All code must be finalised and ready for testing two days before a submission, to allow time for testing, documentation of bugs, and patching.

#### Documentation Standards

Documents are to, as closely as possible, follow the organization/layout structure provided by the skeletal versions of the documents provided by Sarah. If additional sections are needed within the documents, the heading and layout choices will be the same as the rest of the document to look and feel consistent. Documents are expected to have proper grammar and spelling.

## Risk Analysis

### Risk Framework

**Organizational:**
- Faculty noncooperation. The CS faculty may not think our system is useful and may just ignore it or not use it altogether. Our team (as system admins) can't update course offerings and changes to the program forever, so we will no one to maintain these things. Additionally, we lose an entire user group.

**Technological:** 
- Broken software interoperability. The team lacks the technical proficiency to establish a working data pipeline from backend to frontend and vice versa. A moderately likely risk given the overall skill level of the team, but can be worked around by preparing alternative software solutions ahead of time.

**Scheduling:** 
- Poor time management and task prioritization. Team members are unable to adapt to the proposed schedules or set unrealistic expectations of themselves and each other. This would cause uneven progress toward goals at the minimum, and complete derailing of objectives at the worst.
- Lack of time to add core features. Due to the short time frame allotted for actual development time, there is a large risk of failure to meet our core features due to time constraints. This will also be amplified by the use of new languages and technologies and the need to get an understanding of how they work correctly and efficiently. Our backup plan of using a foundation we are all knowledgeable in will help us alleviate this risk.

**Resource:** 
- Insufficient data gathering. The team is unable to gather enough or high quality data from the stakeholders to establish a worthwhile database. While this risk will not impede the team's ability to produce a working proof-of-concept, it will hamper the assessment of the value of the product. It may be possible to generate realistic data sets in lieu of "genuine" data to offset this risk.

#### Table 1: Risk Management Framework

|               | Low Impact | Med Impact                  | High Impact                                            | Critical Impact          |
| :------------ | :--------- | :-------------------------- | :----------------------------------------------------- | :----------------------- |
| Low Risk      |            |                             | Broken Software Interoperability   |  						   |
| Med Risk      |            | Insufficient Data Gathering, Faculty Noncooperation | 		|                          |
| High Risk     |            | Poor Time Management and Task Prioritization, Lack of Time to Add Core Features  	|   |                          |
| Critical Risk |            |                             |                                                        |                          |

---

### Risk Plan

#### Table 2: Risk Plan Table
|     | Risk Name               | Risk Description               | How to monitor                          | Plan         |Description  		        |
| --- | -------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| 1   | Poor Time Management | Team members fail to adhere to schedules or set unrealistic expectations, causing uneven progress or delays. | Brandon will track task completion in GitLab each week, and will check that an appropriate portion of work is done each week (1/3 of work for a 3 week assignment) | Mitigate     | Set clear milestones, define roles, and allocate buffer time in the schedule to account for delays.                          |
| 2   | Faculty Noncooperation | CS faculty doesn't like our system and doesn't want to use it, causing us to lose an entire user group and have no one to maintain program/course changes in the long-term. | Christopher regularly check with instructors/CS faculty members (especially those interviewed) to get their opinions on the system. If there are negative opinions, we will have to act on this risk. | Mitigate | Interview faculty to see what they would want out of the system and add those features. |
| 3   | Broken Software Interoperability | Team lacks the skills to integrate backend and frontend systems effectively.                                 | Lachlan will review technical implementation progress each week in the development phase, ensuring that we are on pace with the development timeline. | Mitigate     | Build a prototype early in the implementation stage to identify gaps. Consult external resources or mentors for troubleshooting. |
| 4   | Lack of Time to Add Core Features | Failure to meet our core features due to time constraints.       | Casey will organize and lead weekly meetings to ensure we're on track, based on our development timeline and issues board (checking if we are behind or not). | Mitigate     | Develop a clearly defined and agreed upon development timeline for each feature and make a prioritization list of each core feature. Adjust plans if we can't keep up with the timeline by reducing core features or increasing work time.   |
| 5   | Insufficient Data Gathering      | Inability to collect enough quality data from stakeholders, impacting the database and app functionality.    | Luka will set thresholds for stakeholder engagement/activity with the system (Ex. 20 reviews a month expected, faculty updates courses by {date}), and will watch to see if this goal is met. | Share    | Use simulated datasets to offset data deficiencies. Increase stakeholder engagement through surveys or interviews.           | 
