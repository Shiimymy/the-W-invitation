# Testing

Extensive testing has been done on [The W Invitation](https://the-w-invitation-104939a4f065.herokuapp.com/) website to ensure a good user experience. 

*Go back to [README.md](README.md)*


## Table of Content

- [Testing](#testing)
  - [Table of Content](#table-of-content)
  - [Responsiveness Testing](#responsiveness-testing)
  - [Manual Testing](#manual-testing)
  - [Validator Testing](#validator-testing)
  - [Performance Testing](#performance-testing)
  - [Fixed issues](#fixed-issues)


## Responsiveness Testing

The responsivennes was tested thanks to [Chrome Device toolbar](https://developer.chrome.com/docs/devtools/device-mode). Different screen sizes were tested to inspect the responsiveness of the website.
To implement an easy responsiveness, Bootstrap to enable responsive development for a better user experience.

## Manual Testing

| Page | Test  | Expected result | Passed |
| ----- | ------------- | --------------- | ---- |
| All pages | Heroku Testing | The program is connect and interacts with the Survey_data sheet | YES |
| | Click on website name | Redirectling to home page | YES |
| | Click on Home link | Redirectling to home page | YES |
| | Click on footer email | Opening the device email app | YES |
| | Click on footer social icon | Opening new tab as no socials yet | YES |
| | | | |
| Home page | Clik on Register link (navbar) | Redirectling to Register page | YES |
| | Click on Login link (navbar) | Redirectling to Sign in page | YES |
| | Clik on Register link (article) | Redirectling to Register page | YES |
| | Click on Login link (article) | Redirectling to Sign in page | YES |
| | Restrict content | The home page has general information about the event only | YES |
| | | | |
| Home page - authenticated user | Click on Memories link (navbar)| Redirect to the Memories Page | YES |
| | Click on Logout link (navbar)| Redirect to sign out page | YES |
| | Updated Home page content | The home page has more information about the event | YES |
| | | | |
| Register page | Enter invalid email | Field will only accept email address format | YES |
| | Enter valid email | No error | YES |
| | Email field left empty | Email is optional | YES |
| | Type invalid password | Error message: Must contain at least 8 characters, similar to the username, not too common and  can’t be entirely numeric. | YES |
| | Type valid password | No error | YES |
| | Type password again (different) | Error message, password must be the same | YES |
| | Click Sign Up with empty form | Fill in the form fields | YES |
| | Click Sign In if you have an account | Redirect to Sign in page | YES |
| | Fill all the form fields | Account created, alert message that you Signed in | YES |
| | | | |
| Login page | Click on Sign Up link, if you don't have an account | Redirect to Sign Up page | YES |
| | Try invalid username | Error message show invalid username | YES |
| | Try invalid password | Error message show invalid password | YES |
| | Valid password and username | Logs in, redirect to Home page with message that you signed in | YES |
| | Click Sign In with empty form | Message to complete the fields | YES |
| | | | |
| Logout page | Click on Sign Out link | Sign user out, redirect to Home page with message that user signed out	| YES |
| | | | |
| Memories page | Memories page access| Only authenticated users can access the page | YES |
| | Approuved Memories only | Only admin approuved Mememories are visible | YES |
| | Click on Add Memory button | Redirect to Add memory page | YES |
| | Select location filter and click on Filter button | Show only the Memories with selected location | YES |
| | Tick Guest box and click filter | Show only the Memories with selected bridal guest | YES |
| | Use both filter at the same time | Show only Memories that meet all filter conditions | YES |
| | Click on Clear button | Clear all filters | YES |
| | Show Edit & Delete buttons | Only show the buttons if the authenticated user is the Memory's author | YES |
| | Click on Edit button | Redirect on Edit Memory page | YES |
| | Click on Delete button | Delete the Memory post | YES |
| | | | |
| Add Memory page | Add Memory page access | Only authenticated user can access the page | YES |
| | Click add with empty form | Message to complete fields | YES |
| | Click add with empty location, inviter or content field | Message to complete fields | YES |
| | Image field left empty | Field optional and image placeholder added | YES |
| | Valid form with all required fields | Form post for admin approval and redirect to Memories page with submitted message | YES |
| | Click on Cancel button | Redirect to Memories page | YES |
| | | | |
| Edit Memory page | Edit Memory access | Only authenticated user can access the page | YES |
| | Click edit with empty form | Message to complete fields | YES |
| | Click edit with empty location, inviter or content field | Message to complete fields | YES |
| | Image field left empty | Field optional and image placeholder added | YES |
| | Valid form with all required fields | Form post for admin approval and redirect to Memories page with submitted message | YES |
| | Click on Cancel button | Redirect to Memories page | YES |
| | | | |
| 404 Error Page | Type in URL that does not exists | Custom 404 Error page is displayed | YES |
| | | | |
| 500 Error Page | | | YES |
| | User raise exception in with forms | Custom 500 Error page is displayed | YES |
| | | | |
| Admin Panel | CRUD functionality | Working as expected | YES |


## Validator Testing

HTML Testing: No HTML error found with  [W3C Markup Validation Service](https://validator.w3.org/)
CSS Testing: No CSS error found with [CSS Validation Service](https://jigsaw.w3.org/css-validator/).
JavaScript:  No JS error with [Jshint](https://jshint.com/) with the mention /*jshint esversion: 6*/.
Python Testing: Few E501 error as undivisible lines [Pep8ci](https://pep8ci.herokuapp.com/#)

## Performance Testing

[Lightouse](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?pli=1) was used for performance testing.

1. Home page

![Home perf](/static/home_perf.png)

2. Home page (sign in user)

![Home sign in perf](/static/home-login_perf.png)

3. Sign in page

![Sign in perf](/static/signin_perf.png)

4. Register page

![Register perf](/static/register_perf.png)

5. Logout page

![Logout perf](/static/signout_perf.png)

6. Memories page

![Memories perf](/static/memories_perf.png)

1. Add Memory page

![Add Memory perf](/static/add_perf.png)

8. Edit Memory page

![Edit Memory perf](/static/edit_perf.png)

## Fixed issues

| Issues  | Description | Steps done to fix |
| -------- | --------------- | --------------- |
|  No error page | When testing, generic error page rendering with no seamless redirecting to website | Created customized 404 and 500 error pages |
| No images on deployed website| Images that taken from the static file were not rendering | Replace the image linked to static file by Cloudinary URLs |
| Register and Sign out pages not working | IDE was auto formatting on save those pages which broke Django logic | Disabled auto formatting and rewritted the code as per Django logic |
| Inconsistent filter design | Filters were not rendering properly | Updated CCS to match the website design |
| Filter not firltering | Filter function was enable to associate filter name with Memory information in the DB | Updated the Database to have location and inviter in Memories instead of Foreign Keys |
| Edit and Delete buttons not showing | The buttons were not showing when the user was the author of a post | Updated if statment in templates/memories.html |
| Registration 500 | When adding an email while user register, system throwing a 500 error | Add ACCOUNT_EMAIL_VERIFICATION = 'none' in settings.py |

*Go back to [README.md](README.md)*