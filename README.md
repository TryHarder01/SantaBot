# SantaBot

A slackbot to manage office "secret santa" arrangements.

## Description:
A sentient slack bot will take in users name, department, three things they like, and three things they don't like.

The responses will be inserted into a DynamoDB.

A Python brute force method will pair up people with the following conditions:
1. no one will give to someone in the same department
2. no on will give to someone who is giving to them
3. (obviously) no one will give to themselves

Santabot will inform users of their match and the information about them. Users will then be able to direct message the Santabot at any time to hear it again. The lookup will key off the userID from slack, therefore it is impossible for anyone to return gifting information about anyone else.

## Technologies:
* Slack API
* Python backend
* AWS DynamoDB 

## Roadmap:
* Slack bot conversation strings / logic
* DB inserts
* DB queries
* Matching pairs up

