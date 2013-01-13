#!/bin/bash -ex


if [ -d venv ]; then
   echo "Remove venv/ directory first."
   exit 1
fi

virtualenv venv
echo 'export DJANGO_SETTINGS_MODULE=MYPROJECTNAME.settings.dev' >> venv/bin/activate
source venv/bin/activate
pip install -r requirements/dev.txt
