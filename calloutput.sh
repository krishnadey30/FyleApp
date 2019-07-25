#! /bin/sh
output=`curl --header "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzuYW1lIjoia3Jpc2huYSIsImV4cCI6MTU2NDUwMjEwOX0.U8tnl9KmXEDbDfETCC2bqcPP52b2sTUTBvqKWH7lGrA" -H "username: krishna" -G "https://bankapp-fyle.herokuapp.com/branch" --data-urlencode "bank_name=STATE BANK OF INDIA" --data-urlencode "city=RANCHI"`
echo $output