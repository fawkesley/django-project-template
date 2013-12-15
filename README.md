# Django Project Template

## Features

This tool creates a blank Django 1.4 project and app with a reasonable default 
heroku-friendly layout. Featuring the following:

- virtualenv (venv) environment
- modular settings file for development, staging and production environments
- modular requirements.txt: dev, staging, prod
- static and media files use Amazon AWS on staging and production (local on dev)
- sensitive settings are retrieved from the environment
- secrets file is automatically generated
- reasonable default log configuration
- email via local smtp (dev), database backend (staging) and gmail (production)

## Usage 

Invoke the install script with the full path of the destination directory, the
project name and the app name, like so:

```
./install.sh /path/to/repo myproject myapp
```

## Version control

The script will run 'git init' in the destination directory, then make an
'install' branch. It will check in each install step to the install branch.

At the end, you can do something clever or simply merge into master and delete
the branch:

```
git checkout master
git merge install
git branch -d install
```
