#! /bin/sh
## variables
token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoia3Jpc2huYSIsImV4cCI6MTU2NDUwMjEwOX0.U8tnl9KmXEDbDfETCC2bqcPP52b2sTUTBvqKWH7lGrA"
url="https://bankapp-fyle.herokuapp.com/"
bank_name="STATE BANK OF INDIA"
city="RANCHI"
offset=2
limit=5
ifsc="SBIN0006355"

echo "\n\t\t\tTASK: Fyle BE Coding Challenge: Banks Search Application (v1)\n"
echo "\t\t\t\tSubmitted BY: Krishna Kumar Dey"

echo "======================================================================================================\
=====================================\n\n\n"
echo "\t\tValidating GET API to fetch all details of branches, given bank name and a city"
echo "\t\t_______________________________________________________________________________\n"
echo "Case I: Using the default offset\n"
echo "**********************************************************************\n"
echo "Bank Name: $bank_name"
echo "City     : $city"
echo "Default Offset = 0\nDefault LIMIT = 20\n"
echo "\nRESULT:\n"

## GET API to fetch all details of branches, given bank name and a city 
output=`curl -s --header "Authorization: $token" -H "username: krishna" -G "${url}branch" \
        --data-urlencode "bank_name=$bank_name" --data-urlencode "city=$city"`

echo $output
echo "\n************************************************************************\n\n"

echo "Case II: Changing the offset and LIMIT\n"
echo "************************************************************************\n"
echo "Bank Name: $bank_name"
echo "City     : $city"
echo "OFFSET   : $offset"
echo "LIMIT    : $limit"
echo "\nRESULT:\n"

## GET API to fetch all details of branches, given bank name and a city 
output=`curl -s --header "Authorization: $token" -H "username: krishna" -G "${url}branch"\
         --data-urlencode "bank_name=$bank_name" --data-urlencode "city=$city"\
        --data-urlencode "offset=$offset" --data-urlencode "limit=$limit"`

echo $output

echo "======================================================================================================\
=====================================\n\n\n"
echo "\t\tValidating GET API to fetch a bank details, given branch IFSC code"
echo "\t\t__________________________________________________________________\n"
echo "IFSC     : $ifsc"
echo "\nRESULT:\n"
## GET API to fetch a bank details, given branch IFSC code
output=`curl -s --header "Authorization: $token" -H "username: krishna" -G "${url}bank" --data-urlencode "ifsc=$ifsc"`

echo $output

echo "======================================================================================================\
=====================================\n"

echo "======================================================================================================\
=====================================\n\n\n"
echo "\t\tGenerating a Token, given a username"
echo "\t\t____________________________________\n"
username="krishna"
echo "username     : $username"
echo "\nRESULT:\n"
## GET API to fetch a bank details, given branch IFSC code
output=`curl -s -G "${url}generate" --data-urlencode "name=$username"`

echo $output

echo "======================================================================================================\
=====================================\n"