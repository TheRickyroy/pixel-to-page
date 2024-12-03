# Individual Full Stack Project Assessment Guide 
![Learning Objectives](<images/Learning Objectives.webp>)
<p align="center">
| <a href="https://pixel-to-page-b4e4b9d4d8dd.herokuapp.com/">Live Project</a> |
  <a href="https://github.com/users/TheRickyroy/projects/3/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D">Project Board</a> |
  <a href="https://github.com/TheRickyroy/pixel-to-page/blob/main/README.md">README</a> |
  <a href="https://github.com/TheRickyroy/pixel-to-page/blob/main/documentation/testing.md">Testing & Validation</a> |
</p>

Specific learning objectives as provided by [Code Institute - Full Stack Software Developer Skills Bootcamp](https://codeinstitute.net/16-week-skills-bootcamp-lancashire/) as criteria for the individual assessment.\
**NOTE:** Bootcamp is now AI-Augmented


## Table of Contents
- [Individual Full-Stack Project Assessment Guide ](#individual-full-stack-project-assessment-guide)
  - [Table of Contents](#table-of-contents)
- [LO 1](#lo1)
- [LO 2](#lo2)
- [LO 3](#lo3)
- [LO 4](#lo4)
- [LO 5](#lo5)
- [LO 6](#lo6)
- [LO 7](#lo7)

<p align="right"><a href="#individual-full-stack-project-assessment-guide">🔺 Back To Top</a></p>

## LO1:
Learners will be able to apply Agile methodology to effectively plan and design a Full-Stack Web application using Django Web framework and related contemporary technologies.

| Criterion | Assessment Criteria | Expected Performance |
|:-:|:-|:-|
| 1.1 | Front-End Design:<br><br>- Design a front-end that meets accessibility guidelines and follows UX design principles.<br>- Create a responsive full-stack application which meets its given purpose, provides a set of user interactions and uses custom HTML and CSS/CSS frameworks.                                                                          | Semantic use of HTML  <br><br>No Web Content Accessibility Guideline (WCAG) errors  <br><br>A user-friendly interface with consistent styles, clear navigation, and adherence to wireframes/mockups.<br><br>The layout adapts to different screen sizes using CSS media queries, Flexbox, Grid and/or bootstrap without any major errors/loss of functionality |
| 1.2 | Database:<br><br>- Build a database-backed Django web application to manage data records.<br>- Design a database structure with at least one custom model. | A configured Django web application with a connected database.<br><br>At least one custom model that fits the project requirements.<br><br>Correct implementation of Django models with appropriate fields, relationships, and constraints.<br><br>Use of Django’s ORM for data management, ensuring efficient and secure database operations. |
| 1.3 | Agile Methodology:<br><br>- Use an Agile tool to plan and track all major functionality.<br>- Document and implement all user stories, linking them to project goals within an agile tool. | Use of an Agile tool to plan and track project tasks and progress.<br><br>Documentation of user stories, clearly linked to project goals and deliverables within the tool. |
| 1.4 | Code Quality:<br><br>- Include custom Python logic demonstrating proficiency, including compound statements like if-else conditions and loops.<br>- Write code with proper readability, indentation, and meaningful naming conventions.<br>- Name files consistently and descriptively, avoiding spaces and capitalization for cross-platform compatibility. | Inclusion of custom Python logic with clear, well-structured if-else conditions and loops.<br><br>Code that follows readability standards, with proper indentation and meaningful naming conventions.<br><br>Consistent and descriptive file naming, avoiding spaces and capital letters for compatibility.<br><br>Use of comments and docstrings to explain complex logic and functions within the code.<br><br>Adherence to PEP 8 guidelines for Python code style and conventions. |
| 1.5 | Documentation:<br><br>- Document the UX design process, including wireframes, mockups, and diagrams.<br>- Ensure documentation demonstrates that the design process has been followed through to implementation. | Concise documentation of the UX design process, including wireframes, mockups, diagrams as well as reasoning for changes throughout the development process.<br><br>Well-organized README file detailing the UX process, design rationale, and final implementation.

<p align="right"><a href="#individual-full-stack-project-assessment-guide">🔺 Back To Top</a></p>

## LO2:
Learners will be able to develop and implement a data model, application features, and business logic to manage, query, and manipulate data to meet specific needs in a real-world domain.

| Criterion | Assessment Criteria | Expected Performance |
|:-:|:-|:-|
| 2.1 | Database Development:<br><br>- Develop a well-organised and consistent database model. | A well-organised database schema with clearly defined tables and relationships.<br><br>Consistent use of data types and constraints to ensure data integrity.<br><br>Use of migrations to manage schema changes and version control for the database. |
| 2.2 | CRUD Functionality:<br><br>- Implement functionality for users to create, read, update, and delete (CRUD) records. | Implementation of user-friendly interfaces for creating, reading, updating, and deleting (CRUD) records.<br><br>Secure access controls to ensure only authorised users can perform CRUD operations. |
| 2.3 | User Notifications:<br><br>- Ensure that all changes to the data are notified to the relevant user. | Implementation of real-time or near-real-time notifications for relevant data changes.<br><br>Clear and concise notification messages that inform users of data changes. |
| 2.4 | Forms and Validation:<br><br>- Implement at least one form with validation for creating and editing models in the backend. | Implementation of forms for creating and editing models with proper field validation.<br><br>User-friendly and accessible form design, with clear labels and input fields.<br><br>Clear and informative error messages for invalid form submissions. |

<p align="right"><a href="#individual-full-stack-project-assessment-guide">🔺 Back To Top</a></p>

## LO3:
Learners will be able to implement and configure authorization, authentication, and permission features in a Full-Stack web application.

| Criterion | Assessment Criteria | Expected Performance |
|:-:|:-|:-|
| 3.1       | Role-Based Login and Registration:<br><br>- Implement role-based login (user/admin/etc.) and registration functionality.               | Implementation of a secure role-based login and registration system.<br><br>Clear differentiation between user roles (e.g., user, admin) with appropriate permissions.<br><br>Secure handling of user credentials and sensitive information.<br><br>User-friendly registration and login interfaces with validation and error handling. |
| 3.2       | Reflect Login State:<br><br>- Ensure the current login state is accurately reflected to the user.                                      | Accurate reflection of the current login state across all pages of the application.<br><br>Clear visual indicators of login status (e.g., user avatar, logout button).<br><br>Conditional rendering of content based on user’s login state and role.                                                                                    |
| 3.3       | Access Control:<br><br>- Prevent users from accessing restricted content or functionality before logging in with the appropriate role. | Proper implementation of access control to restrict content and functionality based on user roles.<br><br>Clear error messages or redirects for unauthorised access attempts. |

<p align="right"><a href="#individual-full-stack-project-assessment-guide">🔺 Back To Top</a></p>

## LO4:
Learners will be able to design, create, and execute manual or automated tests for a Full-Stack Web application using Django Web framework and related contemporary technologies.

| Criterion | Assessment Criteria | Expected Performance |
|:-:|:-|:-|
|4.1|Python Test Procedures:<br><br>- Design and implement manual or automated Python test procedures to evaluate the functionality, usability, responsiveness, and data management of the web application.|Clear and organized test cases for different application components (If automated tests are not implemented).<br><br>Detailed test results showing pass/fail status and if applicable coverage metrics.|
|4.2|JavaScript Test Procedures(if applicable):<br><br>- Design and implement manual or automated JavaScript test procedures to evaluate the functionality, usability, responsiveness, and data management of the web application, if javascript is being utilised.|Clear and organised test cases for different application components (If automated tests are not implemented).<br><br>Detailed test results showing pass/fail status and if applicable coverage metrics.|
|4.3|Testing Documentation:<br><br>- Document all testing procedures and results in the README file.|Detailed documentation of all testing procedures, including manual and/or automated tests.<br><br>Clear explanations of test cases, expected outcomes, and actual results.<br><br>Well-organised README file summarising the testing approach and results.|

<p align="right"><a href="#individual-full-stack-project-assessment-guide">🔺 Back To Top</a></p>

## LO5:
Learners will be able to utilise a distributed version control system and a repository hosting service to document, develop, and maintain a Full-Stack Web application using Django Web framework and related contemporary technologies.

| Criterion | Assessment Criteria | Expected Performance |
|:-:|:-|:-|
|5.1|Version Control with Git & GitHub:<br><br>- Use Git for version control and GitHub (or a similar repository hosting service) to document the development process, including meaningful commit messages.|Use of Git for version control with meaningful and descriptive commit messages.<br><br>Regular commits reflecting incremental development and progress.<br><br>Comprehensive commit history documenting the development process.|
|5.2|Secure Code Management:<br><br>- Ensure the final committed code is free of passwords or security-sensitive information before deployment to the repository and hosting platform|Ensuring no passwords or sensitive information are committed to the repository.<br><br>Use of environment variables and .gitignore for managing secret keys and configurations.|

<p align="right"><a href="#individual-full-stack-project-assessment-guide">🔺 Back To Top</a></p>

## LO6:
Learners will be able to deploy a Full-Stack Web application using Django Web framework and related contemporary technologies to a cloud-based platform, ensuring proper functionality and security.

| Criterion | Assessment Criteria | Expected Performance |
|:-:|:-|:-|
|6.1|Deploy Application to Cloud Platform:<br><br>- Successfully deploy the final version of the Full-Stack application to a cloud-based hosting platform and verify that it matches the development version.|Successful deployment of the application to a cloud-based platform.<br><br>Verification that the deployed version matches the development version in functionality.<br><br>Proper configuration of the hosting environment to support the application.|
|6.2|Document Deployment Process:<br><br>- Clearly document the deployment process in a README file.|Clear and detailed documentation of the deployment process in the README file.<br><br>Step-by-step instructions for setting up and deploying the application.|
|6.3|Ensure Security in Deployment:<br><br>- Secure the deployed application by:<br><br>- Not including passwords or sensitive information in the git repository.<br>- Using environment variables or .gitignore for secret keys.<br>- Ensuring DEBUG mode is turned off.|No inclusion of passwords or sensitive information in the git repository.<br><br>Use of environment variables or .gitignore to manage secret keys and configurations.<br><br>Ensuring DEBUG mode is turned off in the deployed application.|

<p align="right"><a href="#individual-full-stack-project-assessment-guide">🔺 Back To Top</a></p>

## LO7:
Learners will be able to demonstrate the use of object-based software concepts by designing and implementing custom data models in their Full-Stack Web application development.

| Criterion | Assessment Criteria | Expected Performance |
|:-:|:-|:-|
| 7.1 | Design and Implement a Custom Data Model:<br><br>- Design and implement a custom data model that fits the specific purpose and requirements of the project. | Design of a custom data model that fits the project’s specific requirements.<br><br>Proper implementation of the data model using Django’s ORM. |

<p align="right"><a href="#individual-full-stack-project-assessment-guide">🔺 Back To Top</a></p>