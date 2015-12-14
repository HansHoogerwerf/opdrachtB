#!/bin/bash

echo"checking out master"

git checkout master

echo "adding everything"

git add *

echo "commiting master build"

git commit -am "master build"

echo "pushing"

git push

echo "done pushing"

echo "opening webbrowser and starting build!"

xdg-open http://localhost:8080/job/opdrachtB/build?delay=0sec

echo "http://localhost:8080/job/opdrachtB open the job!"

xdg-open http://localhost:8080/job/opdrachtB/


