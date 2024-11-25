# Testing & Validation

<p align="center">
| <a href="https://pixel-to-page-b4e4b9d4d8dd.herokuapp.com/">Live Project</a> |
  <a href="#">Admin Panel</a> |
  <a href="https://github.com/users/TheRickyroy/projects/3">Project Board</a> |
</p>


This is the TESTING file for the [Project](#) website.

Return back to the [README.md](#) file.

## Table of Contents  
  
- [Testing & Validation](#testing--validation)
  - [Table of Contents](#table-of-contents)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Evaluation](#wave-accessibility-evaluation)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Browser Compatibility](#browser-compatibility)
    - [Testing User Stories](#testing-user-stories)
    - [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Bugs](#bugs)
    - [Bug Status](#bug-status)
    - [Bugs - Additional Detail](#bugs---additional-detail)

<p align="right"><a href="#testing--validation">🔺 Back To Top</a></p>

## Validation

<p align="right"><a href="#testing--validation">🔺 Back To Top</a></p>

### HTML Validation

<p align="right"><a href="#testing--validation">🔺 Back To Top</a></p>

### JavaScript Validation

<p align="right"><a href="#testing--validation">🔺 Back To Top</a></p>

### Python Validation

<p align="right"><a href="#testing--validation">🔺 Back To Top</a></p>

### CSS Validation

<p align="right"><a href="#testing--validation">🔺 Back To Top</a></p>

### Lighthouse Scores

<p align="right"><a href="#testing--validation">🔺 Back To Top</a></p>

### Wave Accessibility Evaluation

<p align="right"><a href="#testing--validation">🔺 Back To Top</a></p>

## Virtual Test Environment

Using [statcounter](https://gs.statcounter.com/screen-resolution-stats) to attain the latest (_October 2024_) usage stats, I compiled a virtual testing environment using [Responsive Viewer](https://chromewebstore.google.com/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en) with the six most popular worldwide screen resolutions. Although the most popular resolution globally is **1920x1080**, the [data](https://gs.statcounter.com/platform-market-share/desktop-mobile-tablet) shows usage stats for **61.63% - Mobile**, **36.52% - Desktop** and the remaining **1.85% - Tablet**, thus reinforcing a mobile first approach to responsive design and UX.

| Rank | Resolution | Global Usage |
| :--: | :--: | --: |
| 1 | 1920x1080 | 9.24% |
| 2 | 350x800 | 6.77% |
| 3 | 375x812 | 4.63% |
| 4 | 390x844 | 4.49% |
| 5 | 1366x768 | 4.28% |
| 6 | 1536x864 | 4.15% |

<p align="right"><a href="#testing--validation">🔺 Back To Top</a></p>

## Bugs

As this is my first Full Stack project 

### Bug Status

This table can be used to identify all bugs throughout the project including their resolution status.\
Additional details about each bug, including screenshots, resolution steps and potential future solutions can be found [here](#bugs---additional-detail).

<details>
<summary>Bug Status Key</summary>

| ID | Status | 
|:-:|:-|
| 🔴 | Unresolved | 
| 🟡 | Partially Resolved | 
| 🟢 | Fully Resolved | 

</details>


| No. | Bug | Status | Solution Credit | Commit no. |
| :--: | :-- | :--: | :-- | --: |
| 1 | Database Migration - Syntax Error | 🟢 | Bash Terminal Error | [ef4ef38](https://github.com/TheRickyroy/pixel-to-page/commit/ef4ef3867d31ea2762afa447bfe4ef8849102eb9) |
| 2 | Database Migration - Syntax Error | 🟢 | Bash Terminal Error | [ef4ef38](https://github.com/TheRickyroy/pixel-to-page/commit/ef4ef3867d31ea2762afa447bfe4ef8849102eb9) |
| 3 | Heroku Application Error | 🟢 | Debugging & Slack Coding Coach Channel | [f1efeb0](https://github.com/TheRickyroy/pixel-to-page/commit/f1efeb0e2f6fe703e79bf5fdab7953d8ed85f6ce) |
| 4 | Procfile - Syntax Error | 🟢 | Identified as part of Bug #3 | [aa63bd6](https://github.com/TheRickyroy/pixel-to-page/commit/aa63bd6bd083caf5125419e8955d9354af4d07c8) |
| # | - | - | [Credited Source](Link) | [Commit](Link) |

<p align="right"><a href="#testing--validation">🔺 Back To Top</a></p>

### Bugs - Additional Detail

<details><summary>Bug #1 - Database Migration - Syntax Error</summary>

Commit [ef4ef38](https://github.com/TheRickyroy/pixel-to-page/commit/ef4ef3867d31ea2762afa447bfe4ef8849102eb9)

After attempting to migrate the database I received an indentation error within the terminal. 
This was the result of pasting the required code from the Django Setup & Deployment document and it losing the correct indentation in the process. 

`Indentation Error: expected an indented block after 'if' statement on line 16`

![Bash Terminal Error](../documentation/images/bugs/bug-1.webp)

Thanks to the terminal identifying this error it was a simple fix adding the correct indentation of two spaces on line 17 and repeating the migration command.

`python3 manage.py migrate`

</details>

<details><summary>Bug #2 - Database Migration - Syntax Error</summary>

Commit [ef4ef38](https://github.com/TheRickyroy/pixel-to-page/commit/ef4ef3867d31ea2762afa447bfe4ef8849102eb9)

Following the debugging of Bug #1 the bach terminal returned an additional syntax error. 

This was a rogue `-` on line 43 of **settings.py** which was accidentally typed in whilst making notes on the deployment process for the **README** docs whilst the IDE Workspace was still my active window. 

</details>

<details><summary>Bug #3 - Heroku Application Error</summary>

Commit [f1efeb0](https://github.com/TheRickyroy/pixel-to-page/commit/f1efeb0e2f6fe703e79bf5fdab7953d8ed85f6ce)

Application error returned upon deploying the app in Heroku.
![Heroku Application Error](../documentation/images/bugs/bug-3-1.webp)

Attempted to run server from IDE thus identifying error in terminal
![Run Server Error](../documentation/images/bugs/bug-3-2.webp)

Corrected cloudinary environ in **env.py** file after incorrect copy and paste from API & Heroku.

I also updated method to `setdefaul()` as oppose to assigning the value as per LMS.
![Set Default](../documentation/images/bugs/bug-3-3.webp)

Before submitting a support request I checked through the channel and found another student had already sought out a solution which reminded me to set `DEBUG = True` as it was still set to False from my deployment attempt. 

After double checking through all steps I also realised I had missed a step in adding to the **blog** **views.py**

During the debugging process I also identified Bug #4 which was resolved prior to this bug closure. 

</details>

<details><summary>Bug #4 - Procfile Syntax</summary>

Commit [aa63bd6](https://github.com/TheRickyroy/pixel-to-page/commit/aa63bd6bd083caf5125419e8955d9354af4d07c8)

Project name identified to be using wrong sytnax in **Procfile** as part of Bug #3 debugging process.

Incorrect - `web: gunicorn pixel-to-page.wsgi`\
Correct - `web: gunicorn pixel_to_page.wsgi`


</details>

<details><summary>Bug #</summary>

</details>



<p align="right"><a href="#testing--validation">🔺 Back To Top</a></p>
