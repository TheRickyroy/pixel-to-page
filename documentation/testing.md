# Testing & Validation

<p align="center">
| <a href="https://pixel-to-page-b4e4b9d4d8dd.herokuapp.com/">Live Project</a> |
  <a href="https://github.com/TheRickyroy/pixel-to-page/blob/main/README.md">README</a> |
  <a href="https://github.com/users/TheRickyroy/projects/3">Project Board</a> |
</p>

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

This being my first Full Stack Project, I anticipated running into bugs and issues offering opportunity to debug and problem solve.\
As part of my learning experience, and for future reference, I chose to fully document all bugs encountered and the steps taken during the debugging process.\
By doing so I hope to continue developing my understanding and thus increase my efficiency by having effective solutions to refer back to, but just as importantly, failed solutions to potential avoid in future. 

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
| 5 | Commit Push Failure | 🟢 | [Medium](https://medium.com/@rajlaxmii/git-error-you-have-divergent-branches-and-need-to-specify-how-to-reconcile-them-75e97bd8abd2) & [Graphite](https://graphite.dev/guides/understanding-your-branch-is-ahead-of-origin-main-by-1-commit) | [923e65f](https://github.com/TheRickyroy/pixel-to-page/commit/923e65fcb58a6436f1f6540841b7aac3c78fe630) |
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

<details><summary>Bug #5 - Commit Push Failure</summary>

Commit [923e65f](https://github.com/TheRickyroy/pixel-to-page/commit/923e65fcb58a6436f1f6540841b7aac3c78fe630)

**Identification**

Discussion during guided session highlighted **runtime.txt** requirement absent from the walkthrough documentation, but present within the LMS.

Upon creation of this file I attempted a `git add .` `git commit` and `git push` at which point I received an error in the terminal.

**Resolution Steps**

`git pull main`
```
fatal: 'main' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

`git pull`
```
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
```

Sourced a possible [solution](https://medium.com/@rajlaxmii/git-error-you-have-divergent-branches-and-need-to-specify-how-to-reconcile-them-75e97bd8abd2)

`git pull --rebase origin main`

```
From https://github.com/TheRickyroy/pixel-to-page
 * branch            main       -> FETCH_HEAD
Successfully rebased and updated refs/heads/main.
```

`git status`
```
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

Sourced actual [solution](https://graphite.dev/guides/understanding-your-branch-is-ahead-of-origin-main-by-1-commit)

`git push origin main`
```
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 32 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 342 bytes | 342.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/TheRickyroy/pixel-to-page.git
   ff76d71..923e65f  main -> main
```

</details>

<details><summary>Bug #</summary>

</details>

<p align="right"><a href="#testing--validation">🔺 Back To Top</a></p>
