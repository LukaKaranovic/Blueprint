# Team Roles and Technology Document

## 1. Technological Skills

After surveying our entire group about their technical skills, we have determined the following:

#### Table 1: Survey of team technological skills

| **Area** | **Technology** | **\# of Proficient Members** | **\# of Members Willing to Learn** |
| --- | --- | --- | --- |
| Programming languages | C++ |  5   |  0  |
| | Bash scripting |  1   |  3   |
| | Java |  0  |  1   |
| | PHP |  1   |  1   |
| | Perl |  0   |  0   |
| | JavaScript |  0   |  2   |
| | Python |  2   |  3   |
| RDBMS or file storage | MySQL (MariaDB) |  1   |  4   |
| | Oracle |  0   |  3   |
| | SQLite |  0   |  4  |
| | Flat file (no db) |  2   |  0   |

## 2. Preliminary Technology Choice

Based on the results from table 1, our group has chosen to use **Python** as our main programming language and **SQLite** as our database.

If learning and using Python becomes too difficult, we all have a strong background in C++ to fall back on to complete the programming side of things. Additionally, half of us are taking CSCI 370 and will be gaining experience in Oracle before the implementation phase of the project.

#### Table 2: Preliminary Technology Choice

|     | First Choice | Back-up plan |
| --- | --- | --- |
| Programming language(s) | Python  |   C++  |
| File management |  SQLite  |   Oracle  |

Note: Because we have a 3 week development cycle, we have decided to use SQLite as our database, with future migration to MySQL if the project development extends past this term.

## 3. Preliminary Technical Roles

Our team has decided on this preliminary breakdown of team roles.

#### Table 3: Team member technical roles

| **Team member** | **Primary role** | **Secondary role** |
| --- | --- | --- |
| Luka Karanovic | Software Designer | Database Developer |
| Brandon Tobin |   Software Designer  |  Programmer   |
| Christopher Nilssen | Database Designer | Database Developer |
| Lachlan Dyer | Programmer | Software Designer |
| Casey Adams | Front-end Developer |  Software Designer    |

**Here is a breakdown of each role’s responsibilities:**
- **Software Designer**: responsible for creating specifications for code.
  - Setting up file/folder structures.
  - Describing classes (visibility, methods, responsibilities).
  - Writing classes to model how specs get translated into classes.
  - Will work directly with the Database Designer to ensure the database and software can connect correctly.
- **Programmer**: responsible for writing code based on given specifications.
  - Coming up with algorithms to solve the problem.
  - Working with the Software Designer to ensure the code is doing what it’s supposed to.
- **Front-end Developer**: similar to a programmer, but focusing more on the graphical/user interface side of things.
  - Describing interfaces between classes.
  - Creating the graphical user interface (GUI) for the product.
  - Ensuring a seamless user-end experience.
- **Database Designer**: responsible for creating the database and ensuring tables are created correctly.
  - Will need to work directly with the Software Designer to ensure the database and software can connect correctly.
- **Database Developer**: responsible for implementing tables in the database and inserting data.
  - Will need to work with the Database Designer to ensure the database has been implemented correctly.
