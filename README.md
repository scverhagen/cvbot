# Introduction 
I created this project to demonstrate the use of Tensorflow's object detection capabilities. When running, the application checks an email account every 5 minutes. If a new email is found with image attachments, the attachments are processed via a RCNN model and a response is sent back to the user.  Tensorflow's objection detection source can be found here:  https://github.com/tensorflow/models/tree/master/research/object_detection

# Getting Started
The easiest way to get started is to use the docker container published on docker hub:
https://hub.docker.com/r/scverhagen/cvbot

docker run --env IMAP_SERVER=imap.gmail.com --env IMAP_EMAIL=someemailaddress@gmail.com --env IMAP_PASSWORD=passwordgoeshere --env SMTP_SERVER=smtp.gmail.com --env SMTP_PORT=587 scverhagen/cvbot
