# 201707-python-restful-api
A simple RESTfull API that takes and stores comments identified by an SKU.

# Specs and Description:
The API should have a way in which the comment has been analysed to tell us whether the comment is positive or not. To do this, you'll use the Watson Tone Analyser for emotional tone. https://watson-api-explorer.mybluemix.net/apis/tone-analyzer-v3#!/tone/GetTone

### Test Run in the web browser (changing the string(the message that is going to be analysed))
- http://localhost:8080/watson-api/I am happy in London

### Test Third party service API (curl)
- curl -v -H "Accept: application/json" 'https://watson-api-explorer.mybluemix.net/tone-analyzer/api/v3/tone?text=I%20am%20very%20happy%20to%20be%20in%20London&tones=emotion&sentences=true&version=2017-07-01'

# Additional Information:
### Set up Python3 (linux ubuntu) and development envirnment:
- sudo apt-get update
- sudo apt-get -y upgrade
- python3 -V
- sudo apt-get install -y python3-pip
- alias python=python3
- sudo pip install <module>

### Done:
- understand better the watson-api-explorer
- make a curl/postman request with success in my terminal
- make a https request in python3
- save the data in a json (read and write)
- loop the dictionary for the data I need
- create the config file
- create the logic (scale...) to get the positive or negatice result

### Todo:
- answer to the question in the specs (the important part of the test)
- research unit tests

### Improvements:
