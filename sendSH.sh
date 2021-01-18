#!/bin/sh

message="BC Message: When are you going to work on installing Endevor on CA66. (userid)"
todayDate=$(date)

if [ -z "$message" ]
then
      echo " "
      echo "Message IS EMPTY"
      echo "----------------------------" 
      echo " " >> send.txt
      echo "Message IS EMPTY" >> send.txt
      echo "$todayDate">> send.txt
      echo "----------------------------" >> send.txt
      echo " " >> send.txt
      # git add *
      # git commit -m "add new line of information"
      # git push
      # git pull
else
      echo " "
      echo "Message IS NOT EMPTY"
      echo "----------------------------"
      echo " " >> send.txt
      echo "Message IS NOT EMPTY" >> send.txt
      echo "$message" >> send.txt
      echo "$todayDate">> send.txt
      echo "-----------------------------------">> send.txt
      echo " " >> send.txt

      # git add *
      # git commit -m "add new line of information"
      # git push
      # git pull
fi

