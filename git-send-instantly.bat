@echo off
cls
echo -----------
git init
echo -----------
git add .
echo Done!!!
echo -----------
git status
echo -----------
git commit -m "Update files"
echo -----------
git push
echo -----------
pause
exit