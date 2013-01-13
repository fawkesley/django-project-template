#!/bin/bash -ex

if [ $# -lt 3 ]; then
    echo "Usage: $0 /path/to/empty/repo MYPROJECTNAME MYAPPNAME"
    exit 1
fi

SKEL_DIR=$PWD/skel
REPO=$1
PROJECT=$2
APP=$3

cd $REPO
git init

echo "# README for $MYPROJECT" >> README.md
git add README.md
git commit -m "First commit, added README file."

git branch install
git checkout install

# Copy top-level skeleton items
for dir in db deploy logs scripts
do
    cp -R $SKEL_DIR/root/$dir .
    git add $dir
done
git commit -m "Added top-level directories."

# Add gitignore file
cp $SKEL_DIR/root/.gitignore .
git add .gitignore
git commit -m "Added gitignore file."

# add requirements files
cp -R $SKEL_DIR/root/requirements .
cp $SKEL_DIR/root/requirements.txt .
git add requirements.txt requirements/*
git commit -m "Added requirements files."

# Create virtual environment for python
virtualenv venv
source venv/bin/activate
pip install -r requirements/dev.txt

# create a new Django project
django-admin.py startproject $PROJECT ./
mkdir $PROJECT/apps $PROJECT/libs

# replace vanilla settings file with new settings module
mkdir $PROJECT/settings
mv $PROJECT/settings.py $PROJECT/settings/settings.vanilla.py
cp $SKEL_DIR/project/settings/*.py $PROJECT/settings/
git add $PROJECT
git commit -m "Added project $MYPROJECT."

# copy skeleton apps and libraries into project
cp -R $SKEL_DIR/project/apps/* $PROJECT/apps/
cp -R $SKEL_DIR/project/libs/* $PROJECT/libs/
git add $PROJECT/apps $PROJECT/libs
git commit -m "Added skeleton libs and apps."

# create our first app
mkdir $PROJECT/apps/$APP
python manage.py startapp $APP $PROJECT/apps/$APP

# replace MYAPP with app name in settings: INSTALLED_APPS etc
sed -Ri "s/MYAPP/$APP/g" .
sed -Ri "s/MYPROJECT/$PROJECT/g" .
git add $PROJECT/apps/$APP
git commit -m "Added app $APP."

# use the new settings module (dev)
export DJANGO_SETTINGS_MODULE=$PROJECT.settings.dev

# perform initial migration for app
python manage.py schemamigration $APP --initial
python manage.py migrate $APP
git add $PROJECT/apps/$APP/migrations
git commit -m "Initial migration for $APP."

