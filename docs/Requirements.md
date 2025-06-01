# Team Apache-84: Project Requirements

## Document Overview

This document outlines the requirements and research for Blueprint.VIU.CS system, a course planning tool aimed at improving the experience of students and faculty through course reviewing. The document details the user research conducted through background research and interviews with students and faculty members underlining their goals, expected tasks and needs regarding semester specific course planning.

Additionally, the document presents the functional and non-functional requirements based on gathered data, the proposed features (essential and stretch), and use cases to develop the systems functionality. Use case diagrams are utilized to visualize primary interactions between users and the system. This document also includes a detailed project plan update section to further develop the project's scope and objectives based on feedback.

## Project Updates

- We’re changing the scope of our project to focus on semester-specific course planning rather than the bigger picture graduation path planning. The reason for this is because we got feedback warning us that trying to do both would be too much, which we agree.
- We're working on adding a feature that provides an incentive for students to leave course reviews so that we get more useful information, right now we have a 'review badge feature' in place, which is subject to change.
- One thing we learned from the interviews is that providing a way for faculty to communicate back to students would be useful and would create a more productive communication cycle (rather than students just telling faculty what to do). We added an 'announcement board' feature as we believe it would solve this problem and wouldn't add much time to the development phase.

### Project Plan Updates

Changes to the ProjectPlan.md document:
- Added our team name to the top.
- Made several wording changes to the ‘Project Proposal’ section of the document, to ensure our goals focus on semester-specific planning rather than program planning.
	- Got rid of the ‘easiest path’ terminology, focused less on the big picture and more on semester specific wording.
	- Noted that other factors may cause students to not complete the CS program in 4 years.
	- Noted that the faculty dean is the only one in the faculty who could push for a program change, and they would have to submit a proposal to the Planning and Priorities Standing Committee.
	- Added a blurb that talks about how user input (reviews) will help promote an ongoing information cycle in our system.
- Made changes to the features section of the ‘Project Proposal’ section of the document, to ensure our planned features focus on semester-specific planning rather than program planning.
- Removed ‘institutional bankruptcy’ from our risk list (we will just pretend it doesn’t exist).
- Moved ‘poor time management’ risk to scheduling, as we misinterpreted our team as “the organization”, instead of VIU or CS faculty.
- Added ‘faculty noncooperation’ as an organizational risk to our project. This risk has a medium likelihood with a medium impact.
- We were asked “when does the system need to deploy to be helpful?” We believe the system will need to be deployed right before the academic year begins (i.e.August or Sept.) to collect at least two terms of student review data before course registration for the next year (when students would use the system for planning).
- Updated the risk table to give specific values for monitoring risks, and assigned specific people to monitor those risks. 
- Also addressed how ‘progress with stakeholders’ can be measured.

## Data Collection

### Background Research

After conducting research, we found that the system used for “ratemyprofessor” shares similar characteristics to our proposed system. This was expected as ratemyprofessor was one of the inspirations for our system.

Link to the website: https://www.ratemyprofessors.com/ 

The main feature of the ratemyprofessor system is the review feature (which is a planned core feature for our project). We think this feature is important to our system because it gives the users a better idea of the difficulty of courses and more clarity of what the class will entail once enrolled.

Our system will have a different approach to rating difficulty than ratemyprofessor. We will not be assigning class difficulty based on teachers. We intend to use the rating to reflect how much information will be covered in the course work and how much time per class is required to meet success. For example, CSCI 159 would have listed main topics such as arrays, pointers, loops, etc… We want the rating to reflect the difficulty of learning the topics as new students. In other words, we want reviews to be centred on the material of each class, and have no bias towards certain teachers. We intend to present guidelines of discussion of comments and written review to only focus on material specific discussion rather than the discussion focused on how it was taught. If this becomes a risk, and teachers are being targeted within reviews, then we intend to mitigate these risks by moderating the comments.
Our system will only take into account VIU courses, and our system will also prioritize the user’s anonymity, like ratemyprofessor’s system. We believe there is a need for this system over the ratemyprofessor system as our system will create a feedback loop between the students and faculty about CSCI courses that previously didn’t exist before. Where both students and faculty feel safe to say what’s on their mind. We find this will create a healthier bridge of communication between students and instructors without the need for direct targeting of individuals based on bias.

Additionally, our system will be different from ratemyprofessor because it will give back to the faculty and support more than just one user group. Ratemyprofessor is a third-party website that only serves to help students, meanwhile teachers are put on this website and don’t get anything out of the system. Our system focuses on having two-way support for both sides.

### Interviews 

For users, we have two main groups, students and faculty. The way we identified these users was by discussing who was contributing to the system and who was getting value out of the system. For our interview process, we decided to get two of each group to get a larger sample size to see if we can detect similarities between their answers. We made sure to pick students that some group members have an established relationship with, so we can easily contact them for follow ups. For the faculty, we decided to select instructors who were teaching some of our group members, so they would also be easy to contact later in the term. Their years of hands-on experience with both instruction and the creation of academic programs are invaluable to getting initial, professional assessments of our system and whether there’s an actual need for it. These users were selected because of their exposure to the system's primary problem statement and how the use of the system is directed to solving specific users' issues. 

#### Table 1: Interview Process

| Interviewee ID | User Type | Interviewer | Date/Time |
| --- | --- | --- | --- |
|  1   |  Faculty  | Christopher and Casey    |  Feb 6, 2025, 4PM  |
|  2  | Student    | Lachlan    | Feb  11, 2025, 9PM  |
|  3   | Faculty    | Luka    | Feb  12, 2025, 4PM  |
|  4   | Student    | Casey    | Feb  12, 2025, 10PM  |

### Interview Data

**All interview scripts and notes are kept in a separate [appendix document](/A3/Appendix:%20User%20Interviews.md).**

#### Faculty:

**Primary Goal:** Gathering a wide variety of student course reviews to assist in making productive changes for specific courses and the CSCI program as a whole. As well as providing feedback to students.

**Benefits of using the system:** Faculty can get a clear idea of the students’ perception of courses. They can use this feedback to improve the computer science program at VIU. 

**3 primary tasks:** 
1. Faculty will add and edit course information to the system.
2. Faculty will be able to view reviews and come to conclusions based on student feedback.
3. Faculty will be able to communicate back to students based on feedback.

#### Student:
**Primary Goal:** Gain the ability to plan for a specific semester and gain information on the workload of that particular semester before registering.

**Benefits of using the system:** Students will be able to make judgments about their course selections for future semesters thanks to the functionality built into our system. Students will be able to see which courses are more work intensive and which ones are less intensive.

**3 primary tasks:**
1. Students will be able to select courses and make an observation of difficulty for a semester.
2. Students can view specific course data which pertains to difficulty, topics, and workload.
3. Students will be able to submit reviews for courses they have taken to help future students.

After our extensive interview processes, we gained some key insights of each user type. For faculty interviews, it is evident that the main thing that would help them accomplish applying feedback effectively would be having a large data set. A problem that they identified with a review system is that students will only leave reviews if they have had a polarizing experience (very good or bad). This means that we would have to incentivize the bulk of students to leave frequent reviews on the courses they’ve taken in order to build a larger and more accurate data set. Ways to boost student engagement would be enforcing anonymity, allowing students to feel safe being honest, and to reward students for contributing to the system with their reviews in some way. One faculty member mentioned that with existing systems like ratemyprofessor, individual teachers are targeted and biases are formed, which is something to be avoided in a system focused on course material, not professors. Additionally, the need for two-way communication was clearly expressed as faculty pointed out that students would just be telling faculty what to do, with no way to communicate back. For student interviews, we learned that students want to do the least work possible, so making the system as easy as possible to use for students will be a main priority. Students are also not happy with the current state of the computer science program, they don’t like how many courses are offered only once per year and often are unbalanced in difficulty. For what differed from expectations, faculty was surprisingly enthusiastic about the idea of this system. While students shared that support, they were very pessimistic about the use of the system to enhance the CSCI program in the future.

## Users

Our main user types for this system are VIU computer science students and the VIU computer science faculty and staff. Students will take advantage of the review system by being able to look at class difficulty and reviews left by previous students that have used the system as well as leave their own reviews after taking the course themselves. The faculty and staff will be able to see how classes are received by students via reviews, and will be able to provide feedback back to the students, or update the available classes and schedules in the system. We chose these two user groups for our system because the system was designed with the intent to give a productive feedback loop between these two user groups that didn’t exist before. We also have plans for the future to extend potential users to other types of departments. 

## Use Cases

#### Table 3: Use Cases

| Use Case | Description | User(s) associated with it |
| --- | --- | --- |
| Verify User | User can verify their identity through VIU's system to access certain features. | Students and Faculty |
| Submit Review | User leaves review of a class.  |  Students  |
| Edit Review | Edit an existing review if errors are present. | Students |
| View Review | Users can view the user reviews for a class.  |  Students and Faculty   |
| View Course Data | User selects a course and views its contents.  | Students and Faculty |
| View Semester Data   |  User has selected courses for the semester and can view the calculated data for the semester.   | Students  |
| Find Course |  Users can search for specific courses.  | Students and Faculty  |
| Filter Courses | Filters courses by their assigned attributes. | Students and Faculty |
| Select Course | User selects a course for their semester schedule.   |  Students  |
| Edit Course |  Edit an existing course’s information and/or course availability.  |  Faculty   |
| Add Course | Add a course to the system and its dates/info. | Faculty |
| Make Announcement | Create an announcement for a course to be posted on the announcement board and the course. | Faculty |
| Rate Announcement | Users can upvote or downvote announcements to give feedback. | Students |

### Use Case Diagrams

#### Student Use Case Diagram

For our Student Use Case Diagram, we decided our main Use Cases would be the following: Select Course, View Course Data, View Semester Data. The system is designed in a way for student users to build semesters based on difficulty using these Use Cases. 

![StudentUseCase](./images/SUC.png)

#### Faculty Use Case Diagram

For our Faculty Use Case Diagram, we decided our main Use Cases would be the following: Edit Course, Add Course, Find Course. The system is designed in a way for faculty users to change aspects of classes based on feedback using these Use Cases. 

![FacultyUseCase](./images/FUC.png)

#### Student and Faculty Use Case Diagram

For our Student and Faculty Use Case Diagram, we decided the main Use Cases would be the following: View Reviews, Find Course, with students having a Use Case for Submit Review, and both Students and Faculty having a filter course Use Case. The system is designed to have reviews submitted by students be addressed by faculty via our system with these Use Cases.   

![StudentFacultyUseCase](./images/SFUC.png)

## Product Requirements

This section outlines the product requirements.

### Product Summary

A big problem for students in the VIU computer science program is being caught off guard by the drastic difference in workload each semester throughout the program. This can be harmful as students are often working a job outside of school (or have other responsibilities) and cannot handle the sudden change in workload. At the moment, there is no easy or accessible way to determine a course's difficulty. The unawareness of course difficulties causes students to take several time consuming and/or difficult courses at once. This leads to failure of courses, which costs students a lot of extra money and time. Our system, Blueprint.VIU.CS, is designed with the goal of helping CS students minimize the chance of this happening to them, by giving them a tool to help plan their semesters around course difficulty that is calculated from past student experiences.

Additionally, many computer science teachers and faculty often forget what it is like to be a beginner, so they do not know what is too much or too little content for a course. Our system may provide the information needed to help remind them what it is like to be a student. This way, faculty could make changes to the CS program that help balance the workload in each semester. 

The target audience for our system is anyone involved in the VIU computer science program. We have two distinct main user types, the first being the students, and the second being the faculty. We decided on these two user types through group discussion in our project proposal phase. Blueprint hopes to create a feedback loop between students and faculty. Students create reviews for courses, providing the difficulty, workload, and comments about the course. Faculty can then make changes to the program based on this feedback, and can post thoes updates to the announcements board, where students can give feedback through upvoting/downvoting. 

The interface should be as easy as possible for both user types to use. We want our front-end interface to be able to communicate efficient with our backend and our database. The interface for both the faculty and students will look similar, but both user types will have unique functions depending on their use cases. Our interface should allow users to do their primary tasks and achieve their goals by satisfying all of the [use cases](#table-3-use-cases).

We want the system to be run as a website first, and be accessible on any modern PC (prioritizing machines on the VIU campus). For now, we only want our system to be accessible via a website. For students, there are no specific environmental conditions our product must be used in, though having office space and not being in a noisy environment would be largely beneficial depending on the user. A private environment is also recommended in order to maintain anonymity. The same applies for faculty, but it is very strongly recommended and to their best interest to operate in a private environment (away from any students), this is to improve security and to prevent information breaches.

## Requirements

### Functional Requirements:
- The system will let students select courses they want for a particular semester.
- The system must allow students to submit reviews for courses they have taken.
- The system will allow faculty to update certain course information.
- The system will let faculty add courses to a certain semester.
- The system must present overall semester information based on the data of the courses selected.
- The system must be able to filter courses in ways that help both user groups. 
- The system must have a way to moderate reviews to make sure they follow guidelines.
- The system will let faculty communicate back to students based on feedback.
- The system will be able to verify students and faculty identities by an account.
- The system must have a a way to export a semester as a schedule
- The system will filter out hateful/disrespectful language that does not adhere to VIU's policies.

### Non-Functional Requirements:
- The system will reward students who review courses often with a badge. (Usability)
- The system will be formatted for clear and intuitive options for user navigation of both students and faculty. (Usability)
- The system will have guidelines to help reviews focus on courses rather than instructors. (Usability)
- The system will ensure that a course can only be reviewed by students who have taken the course. (Reliability)
- The system will be able to be run without any crashes or bugs which could interrupt user experience (Reliability). 
- The system must be able to handle at least 50 concurrent users, and multiple user types at once. (Performance)
- The system will update live servers to HTML5 on any supported browser during development changes (Performance).
- The system will ensure only faculty/instructors can add or edit course information not gained from review data. (Security)
- The system will ensure that user reviews are anonymous. (Security)
- The backend of the system will need to be able to communicate with the database (Interface).
- The system will present course information to students on flashcards. (Interface)
- The system will work on all VIU campus machines (Windows and Linux) (Implementation). 

## Feature Set

#### Table 4: Essential Features

| Priority | Essential Feature | Reason for priority |
| --- | --- | --- |
| 1 | The Review feature will allow eligible users to create/edit a review for a course and present all written reviews of a course. | We put this as the highest priority because without review data, our system presents no useful or unique information for users. |
| 2 | The Semester Calculator feature will take all of the user’s selected courses for a semester and present summarized data for them. | We prioritize this feature as it helps achieve the main goal for our main user group, the students. |
| 3 |  The Course Editor feature will allow teachers and faculty to update existing course information (schedule, instructors, main topics, etc.) or add new courses to the program. | We prioritize this feature because we want faculty to have accessibility to our system to change any courses, so we don't have to rely on third-party admins to maintain the system for us.  |
| 4 | The Filter Course feature will allow you to filter courses (e.g. by year, difficulty, or # of reviews) so users can find exactly what they are looking for. | This feature is lower priority as the system could function (as a smaller system) without it, but it wouldn't meet requirements without it. |
| 5 | The Announcement Board feature will create two-way communication within our system. It provides a way for faculty to post proposed or official changes to courses based on student feedback, where students can interact with (through upvoting or voting in polls) to show how those changes are being perceived. | This is the lowest priority as it does achieve some of our newly gained requirements but isn't necessary to achieve our main goal with the system. |

#### Table 5: Stretch Features

| Priority | Stretch Feature | Reason for priority |
| --- | --- | --- |
| 1 | The Review Badge feature will encourage more reviews by gamifying the system, granting frequent and good reviewers badges so they can write reviews without authentication.    |  Implementing this feature will help drive user engagement, which will give the system a larger dataset, making it more useful.   |
| 2 | Verification Account feature will allow system to verify (through VIU) that the user is a current faculty member or student, allowing them to make changes to course information and post to the announcement board (if faculty) or leave reviews on taken courses (if student). | Will help with security and integrity of our system, as we don't want anyone to impersonate faculty and present information on behalf of them, have students who haven't taken a course post reviews, or one student post several reviews on a course.  |
| 3 | The Export Schedule feature will provide users with either synchronization to their favorite calendar app or a flat file.  | This is a complex feature that would be nice to have, so students don't have to cross-reference their selections on our system with a schedule from another system. |

## User Engagement Plan

To ensure the Blueprint.VIU.CS system reflects the expectations and needs of the users, a developed plan outlines the plan for receiving feedback based on the projects analysis models.

### Goals
* Increase user satisfaction.
* Gather beneficial data from user feedback.
* Improve features based on feedback.

### Target Audience
* Student user group
* Faculty user group

### Feedback Mapping
* Utilize a domain model for user feedback analysis
* Capture domain-level representations of the data the system will need.

## Engagement Plan Outline
1. Team members will schedule meetings with representative users, at a time convenient for the user.
2. At the beginning of each feedback session a team member will provide an explanation of the analysis model and its intended purpose.
3. Users will be asked for feedback on the clarity and usefulness of the model.
4. Team members will document user feedback from each session.
5. Feedback will be used to further develop models.

#### Table 6: User Engagement Plan

| Model | User ID | Date | Team member | Mode (online/in-person) |
| --- | --- | --- | --- | --- |
| Domain Model | 1 | Feb  | Casey & Christopher  | In-Person  |
| Domain Model | 2  | Feb | Lachlan | Online |
| Domain Model  | 3 | Feb  |  Luka | In-Person  |
| Domain Model  | 4 | Feb  |  Casey | In-Person |