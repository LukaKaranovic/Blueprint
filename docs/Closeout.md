
# Closeout Document

## Document Overview

This document outlines the final state and development done for the Blueprint.VIU.CS.system, a course planning tool aimed at improving the experience of students and faculty through course reviewing. This documeent contains details on features and functionalities, team structure and organization, user engagement reflection, and finally project testing. 

First we go over a brief project overview discussing the state of the project as of A6. Then we discuss features and functionalities which have been implemented as of the final state of the project. Then we outline within our team structure and organization details about potential improvements that could be applied to the system. As for the User Engagement section we discuss details we have gathered from interviews. And finally, we discuss what testing has been done as of A6. 

## Project Update

### Design Models Update
**ER Diagram changes:**
- We recognize that our ER diagram needs to include association tables as they were left out before. We didn’t have enough time so just pretend they were added.
- Yes, facultyID should be a FK for the Announcements table, this change has been reflected. Only one faculty member can create an announcement and no other faculty members can update it - for our system.
  - What courses faculty teach does not impact what courses they can put announcements on. Any faculty member can make announcements for any course.
  - The ‘courses taught’ attribute is strictly tied to **faculty user accounts** so faculty members can quickly and easily access the courses they will likely be looking at (because they are teaching them) on the client side. 
  - Each course won’t have faculty assigned to them as the VIU sites already present that and we are focused on presenting information unique from that so that people can use our system in combination with VIU’s (in our current scope).
- The only time a student interacts with a course (other than viewing) is to leave a review for it, or to select it for their semester data, which is represented in the ER diagram.

**Schema changes:**
- The reason for why these association tables were added to the schema were added.
- More than one announcement can be posted on the same date as announcementDate is not part of the primary key, we just won’t store/display the exact time.

**Design Class Diagram:**
- You are absolutely right about missing navigation visibility! We honestly thought we didn’t have to do navigation visibility outside of the domain layer, so we didn’t do it. We would go back and do it now but it’s too late in the phase to do it and would take too much time.
- All recent announcements will be viewable on the main page. Otherwise, what controls what reviews/announcements are viewed is based on what course you are viewing. When you view a course, it will have a reviews tab and an announcements tab which will display all of the reviews/announcements for that course.
- I don’t know if review or announcement classes need more methods as they are just objects to unravel as boxes of text, all of the operations done on them will be done in the data layer and triggered by other domain classes.
- In our system, review objects don’t need a courseID as domain objects are used to construct entities on our front end and reviews are already going to be on the course’s page (so the courseID is implied). The database does store a courseID under each review and getReviewData() in CourseData gets all the reviews for a course using this attribute.

**Integration Tests:**
- We saw a pattern in class where integration test components normally consisted of integrating one method/function with an entire module, so we changed the integration tests to reflect that. Updated the descriptions to be a bit more clear as well.

## Overview of Project

For Blueprint.VIU.CS, our original intention was to have a course review system which handled user reviews of topics which could be stored in a database and allow faculty members to update courses based on reviews made by our system. Its objective was to let students review what aspects of topics in classes they found either easy or difficult to understand. To which faculty could later use these suggestions to mold classes later on into a more balanced and digestible load for students. We also wanted to let students be able to calculate their own versions of semesters by creating a difficulty calculator which could determine how difficult a semester could be by selecting various classes offered during a term. 

In its final state, almost all main aspects of this project had been fully implemented (with no frontend display). Our database is entirely working as well as all of the business logic. We also got some functionalities of the frontend to work. Our frontend has no connection to our backend however, as routing to the database via a functional API was not achievable within the development time frame.

In terms of design, we for the most part stuck to what was originally intended. Only major changes which were made were mostly design philosophy as development started. 

What led to some subtle differences in development was mostly to accommodate factors in team structure and necessary adaptations which needed to be made in order to complete certain sections lacking resources.  

## Features and Functionalities

For our features and functionalities, the functionalities and features that were required for the base of the program to work are all there. The user can log in depending on if they are either a student or faculty member, in which they are then prompted to choose an action based on which user group they fall under. We are lacking a true verification process, as we intended on referencing against a log in with VIU’s student record, we didn't have the time to fully implement this.

Faculty members are able to view courses, add/edit courses, as well as make announcements for courses that will be associated with the corresponding course.
Faculty are also able to have a list of courses associated with them, essentially being used to have all of their courses they are teaching there for easy access. This really doesn't serve much of a purpose as we are running in a command line but it was supposed to be on a webpage and be easily accessible through a singular click.

Student users are also able to view courses, add/edit reviews for courses as well as create a semester that calculates their overall semester data, giving an overall difficulty score and recommended hours for all the selected courses. 

One of our key use cases was the ability to filter search courses, this is lacking in the release version of our program and instead there will be the ability to list all the available courses in the database for now.

Another functional requirement that is lacking is the moderation of comments and reviews made. This also prevents our system for focusing reviews less on the professor and more on the class content. This would be essential for a full release of this program to the public but as time has come to the very end, it has been omitted to instead spend resources on functionality of the system itself.

As stated earlier, the verification process was never implemented, this also has disabled the ability to get a lot of the non-functional requirements working, such as restricting students from writing reviews for courses they have not actually taken and the ability to give students a badge on their reviews that shows they are a trusted student reviewer.

The main feature lacking is the front end that we first proposed, having a fully interactive UI that communicates with the business layer to display real time data from the database. Due to a lack of time and resource management this had to be cut for the final product and instead is replaced by a command line user interface instead.

Something which the team could have done differently to achieve the original goal is to have worked to complete the database functionality as a team during the initial stages rather than subdividing the team into sections. This would have ensured that we could build up from the database design to the front end rather than having to align one portion of the project with another. This also would mean potentially having a team dedicated to either function development or testing, which could've offset having a dedicated member do both.

## Team Structure and Organization

At the initial stages of our project, our intentions were to have a divided team of 3 working on the back-end and having 2 dedicated members working on the front-end portion of the project. Our original intention was to have a dedicated 2-2-1 approach of having 2 work on the View Layer, 2 working on the business layer, and 1 working on the data layer. Unfortunately due to a loss in a team member, adaptations needed to be made in order to accomplish goals between each layer accordingly. Originally we had planned to have Christopher and Luka and Brandon working on the business and data layers. However, to accommodate for the loss of Christopher during the development process, it became a whole team effort to develop functionality in the database. This meant that Casey and Lachlan needed to be pulled away from the front-end portion of the project to help mediate loss of time. As of the current state, we have decided to prioritize pushing more development resources into the back-end. 

Time management and prioritizing development of features could have been improved. A more generalized structure of how and when certain functionalities needed to be implemented would have benefited the development cycle. However, busy semesters and other priorities can get in the way of this. Another potential benefit would have been to research technologies ahead of time, as we started searching implementation strategy at the start of phase 6, having the advantage of already knowing a basic idea of connecting layers (such as API knowledge and development stack which could be abstracted) could’ve sped up the process of testing sooner than later. We experienced this approach making a big change with Christopher’s SQLite to Python communication proof of concept, as it saved us a lot of time during development.

Amongst all of us, we have each had to learn and adapt to new frameworks and technology. We originally assessed that all of us were willing to learn new skills. However, taking the time to learn these skills and sync all of our layers together proved to be quite the challenge compared to what was originally predicted.

If development were to continue after our A6, what would most likely be required is to display everything on a web front end. This would require replacing each of our command line interface functionalities with a UI and then connecting them one by one. Afterwards, implementing more unit tests and reviewing that all of our use cases have been successfully implemented would ensure there are no bugs.

In the case of starting over again, one potential change could be having a less condensed functionality list and prioritising having our back-end section done with more members dedicated. This way, worrying about having all of our functionalities working and connected would be less of a hassle when shifting focus to other sections of the project. Some other potential things to consider would be potentially shifting away from SQLite and considering other options for databases (such as MySQL or Oracle), or possibly considering other Python web frameworks such as Django and Spring Boot.

## User Engagement Reflection

After an interview with one of our faculty users, we received various types of feedback on the current state of our project. Some well received aspects were design of the front-end and grabbing data from API objects, as well as the functionality design choice for each of our data files. Some criticisms that were addressed was the philosophy of both the data layer and the view layer. Our faculty user addressed that the view layer should have reviews for each topic, rather than a general review for the entire course. Our data layer should implement a way to insert data which already exists from other sources (such as the VIU database) through some sort of “bulk insert” through some XML file approach. Both of these criticisms are something we cannot fully adapt to due to time constraints. So we will accept circumstances moving forward with development. 

One of the most important things we’ve gained thanks to this interview was that development prioritization based around each of layers is an extremely valuable asset which shouldn’t be overlooked. Refining these diagrams can fulfill a lot of the design philosophy during implementation.

Our student users weren’t very helpful in terms of requirements gathering, but being students ourselves, this didn’t hinder our ability to develop something that would help students. However, one of our student users was very helpful in the later stages of the project when we were showing them our prototype. They clearly identified what they liked about our system and how features could be tweaked to be more helpful for students. This was a large help in the later stages of development.

## Project Testing

For testing, we had originally planned on conducting 13 unit tests, 7 integration tests, and 11 user acceptance tests. Since we didn’t have time to get our web front end or Flask communication working, our tests got cut down to 10 unit tests, 6 integration tests, and 9 user acceptance tests.

Of these tests, the following were conducted throughout development:
- Note: the rest of the remaining tests were planned but not conducted, they can be found in our testing section of `DesignModels.md`.
- Another note: we had test scripts initially, but they were removed and replaced with functionalities in `main.py`. The tests can still be conducted and results verified through the use of `main.py`

**Unit Tests: Performed by Luka and Brandon between March 27 - April 3, 2025**

- UTD-1 - Passed, implication is that data does get inserted correctly into the database.
- UTD-2 - Passed, implication is that data can be retrieved from the database.
- UTD-3 - Passed, implication is that the program doesn’t produce errors when querying an empty table.
- UTF-1 - Somewhat passed, (had to change results) - implication is that courses in the database can be searched for.
- UTF-4 - Passed, students can login to existing accounts.
- UTF-5 - Passed, faculty members can login to existing accounts.
- UTB-1 - Passed, implication is that courses have accurate difficulty ratings
- UTB-2 - Passed, implication is that faculty members can post announcements and they are saved.
- UTB-3 - Passed, implication is that courses have accurate recommended hours.
- UTB-4 - Passed, implication is that all reviews for a course get properly associated with that course.

**Integration Tests: Performed by Luka, Brandon, and Casey from April 2 - 5, 2025**

- ITD-1 - Passed, implication is that the database gets set up through a script and tables exist.
- ITD-2 - Passed, implication is that the database returns accurate data even after the program terminates and restarts.
- ITF-1 - Somewhat passed, students can make accounts but no verification of credentials.
- ITF-2 - Somewhat passed, faculty members can make accounts but no verification of credentials.
- ITF-3 - Passed, implication is that faculty members can update courses, edit history gets updated, and course gets updated automatically on front end and database.
- ITF-4 - Passed, implication is that faculty members can post announcements and have them written to the database and displayed on the front end automatically.

**User Acceptance Tests: Performed by Luka, Brandon, and Casey from April 3 - 6, 2025**

Note: we only did UATs for students, so all faculty UATs were not verified by a user.

- Semester Calculator - Passed, implication is that students can calculate their semester info.
- View Courses - Passed, implication is that students can view a course and get meaningful information.
- Filter Courses - Failed, implication is that students cannot search courses by filter.
- View Announcements - Passed, implication is that students can view announcements made by faculty.
- Course Review System - Passed, implication is that students can write reviews for courses.
- Student Account Management - Failed, implication is that students can’t fully customize their accounts with all of the features we promised, only some of them.

For our student UATs, the primary issues the student user identified was that the view courses and current search features are not ideal. The ‘view courses’ option just spews every course at once in a big list, which is hard to look through. The search just prompts for a user to enter a course ID, and doesn’t give any feedback or help the user find a class if they input the wrong course ID, which isn’t very helpful either. This would change our team’s feature prioritization if we were to continue the project as getting a helpful and user-friendly search feature done before moving it to a web interface would be a better approach than moving straight to the web interface.

For our user acceptance tests on the front-end side, we only successfully got one of our requirements tested with a faculty user, that being the LiveUIUpdates. These were done and written by Casey and the outcome was live updates as the server ran and displayed proper routing from Flask as soon as the live server ran. Casey also ran unit tests which displayed dummy data being populated into the UI. Due to the time constraints and shifted focus by the team as a whole. There will most likely be no further unit tests for the front-end portion of the user acceptance testing for the remainder of A6’s development cycle. 