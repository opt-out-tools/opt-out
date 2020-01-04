
# Opt Out <img src='opt_out_logo.png' align="right" height="140" />
[![CircleCI](https://circleci.com/gh/opt-out-tools/opt-out.svg?style=svg)](https://circleci.com/gh/opt-out-tools/opt-out)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://forthebadge.com)

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

Opt Out is a browser extension for Firefox that filters online misogyny from an individual’s twitter feed.

The General Data Protection Regulation (GDPR) has changed our lives online on social media platforms. We have the right to be forgotten, to see what is being collected about us and to opt-out if we wish. The current abuse that those who identify as women suffer is not avoidable. We see Opt Out as an extension of the GDPR that also protects the human rights of women and those with intersecting identities online. While steps have been made to protect these people online, not enough has been done. This is a global tragedy affecting the well-being, economical potential and political representation of these people. Let's __Opt Out.__

To learn more about this problem and explore the steps Opt Out is taking to combat it, see the [Opt Out Wiki](https://github.com/malteserteresa/opt-out/wiki/The-Problem).

The project is still in its infancy. Please see 'Project Development' below for the current status.

## Test / Deploy
Running the prototype is done with [web-ext](https://extensionworkshop.com/documentation/develop/getting-started-with-web-ext), from mozilla. It streamlines the development, build process, and deployment of web extensions.

To run the prototype:
1. Clone a local copy of the master branch of this repo
2. `npm run start:firefox`

The module hot-refreshes the browser when there is a change in the source code. To force an update in the browser, simply press `r` in the terminal where web-ext is running.

<details>
<summary>Show instructions to run dev environment without web-ext</summary>

1. Clone a local copy of the master branch of this repo
2. Start Mozilla Firefox
3. Set the url to `about:debugging#/runtime/this-firefox` and hit enter
4. In the `Load Teporary Add-ons` box, open and load `manifest.json` which can be found in the `extensions` folder of this repo you cloned locally
5. Open Twitter and test!
6. If you make changes to the code you would like to test, make sure you click "reload" (left of the "remove" button) to apply new changes to script
</details>

This command will open a new firefox window which has the extension installed. However the default settings will not persist any login data, and you will need to sign in to twitter each time you stop running the command. 

To persist your twitter login data after stopping the process, follow these instructions:
* Create a new profile on firefox (at `about:profiles`)
* Open an instance of firefox as this profile
  - `firefox --new-instance -p your_profile_name`
* Sign in to twitter in the browser that opens, you can then close the browser
* Run the development environment start command with a flag to point to this profile.
  - `npm run start:firefox -- -p=your_profile_name`

**Important** Make sure that you do not choose a 'default' profile, such as the profile you use for your personal browsing. Here's why
> This option makes the profile specified by --firefox-profile completely insecure for daily use. It turns off auto-updates and allows silent remote connections, among other things. Specifically, it will make destructive changes to the profile that are required for web-ext to operate.

## Project Development

Opt Out is an open source project under active development. Currently, machine learning models are being evaluated for their ability to classify sexual harassment text. If you would like to test the current model (trained on troll data), please see the 'Installation Instructions' below. If you would like to contribute to the project, please see [Contributing](https://github.com/malteserteresa/opt-out/blob/master/contributing.md) first, and then check out the find-out and try-out repos.


### Continuous Integration

This project is set up to use [Circle CI](https://circleci.com/) as the CI tool.
Every Pull request (from branches or forks) and every version of the `master` will automatically start a new build on circle ci.
This will run the following checks:
- eslint to ensure coding style guidelines are followed
- tests TBD

A pull request can only be merged if all checks are successful.
To avoid any last minute failures, we recommend to use eslint locally before making your commit:

```
npm run lint
```
This will run eslint on all js files and try to fix all problems it finds.
What can't be fixed automatically will be raised as error.

### Adding a local pre-commit hook

In case you want to be 100% sure that the linter is always running before you commit you can add this as a [git hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks).
This means it will run the linter before every commit you try to make:

#### The easy way:

If you do not have a pre-commit hook defined yet, there is a script that will copy the file for you.
Run this command and it will create the pre-commit from a template for you:
```
npm run git:initHook
```

If you already have a pre-commit hook defined but don't care about overwriting it, you can use the same command with the `-f` flag.
This will copy the template even if the file exists already.
```
npm run git:initHook -f
```


#### The slightly harder way

1. Open the file `.git/hooks/pre-commit`
2. If the file does not exist, create it.
2. Add the following to the file and save it:
```
npm run lint
RESULT=$?
[ $RESULT -ne 0 ] && exit 1
exit 0
```


## Funding
If you would like to fund the project or make a donation, please email [Opt Out](mailto:opt-out-tool@gmail.com).

***

> Please note that this project is released with a [Contributor Code of Conduct](https://github.com/malteserteresa/opt-out/blob/master/CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.


