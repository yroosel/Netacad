REM # TESTING FROM THE COMMAND LINE
REM # test script for flask_app_login.py -- use in Windows OS, not in Docker
REM # programm flask_app_login needs to be running
REM # curl needs double quotes for https in microsoft windows
cls
date /T > curl_login.txt
echo START CURL LOGIN SCRIPT >> curl_login.txt
echo Deleting all test records >> curl_login.txt
curl -k -X DELETE "https://127.0.0.1:5555/delete/all" >> curl_login.txt
echo Creating new user v1 insecure >> curl_login.txt
curl -k -X POST -F "username=bbinsec" -F "password=123456" "https://127.0.0.1:5555/signup/v1" >> curl_login.txt
echo Testing login v1 >> curl_login.txt
curl -k -X POST -F "username=bbinsec" -F "password=123456" "https://127.0.0.1:5555/login/v1" >> curl_login.txt
echo Creating new user v2 secure >> curl_login.txt
curl -k -X POST -F "username=bbsec" -F "password=123951" "https://127.0.0.1:5555/signup/v2" >> curl_login.txt
echo Testing login v2 >> curl_login.txt
curl -k -X POST -F "username=bbsec" -F "password=123951" "https://127.0.0.1:5555/login/v2" >> curl_login.txt
echo END CURL LOGIN SCRIPT >> curl_login.txt
more curl_login.txt
