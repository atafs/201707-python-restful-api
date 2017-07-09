from bottle import run, get, post, request, delete
import simplejson as json
import requests
import yaml
import logging

# functions
def config_logger():
	logging.basicConfig(filename='log/logger.log',level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def read_from_config():
	with open('config/config.yml', 'r') as ymlfile:
	     cfg = yaml.load(ymlfile)

	logging.debug('read_from_config')
	return cfg

def write_to_json(text):
	data = json.loads(text)
	with open('data/data.json', 'w') as jsonfile:
	     json.dump(data['document_tone'], jsonfile)

	logging.debug('write_to_json')

def request_https(cfg, text):
	url = cfg['url'] + text

	logging.debug('request_https url [%s]', url)
	return requests.get(url)

def analyse_positive_comment(data):
	data_tones = data["document_tone"]["tone_categories"][0]['tones']
	for array in data_tones:
	    if array['tone_name'] == 'Joy' and array['score'] > 0.5 :
			logging.debug('analyse_positive_comment: it is a positive comment!!!')
			return True

	logging.debug('analyse_positive_comment: it is a negative comment...')
	return False

def get_message(is_analyses_positive):
	# change color to blue or red (True or False respectivaly)
	if (is_analyses_positive == True):
		message = "<h3 style='color: blue'>Is it a positive comment: [%s]</h3>" %is_analyses_positive
	else:
		message = "<h3 style='color: red'>Is it a positive comment: [%s]</h3>" %is_analyses_positive

	logging.debug(message)
	return message


# restful api
@get('/watson-api/<text>')
def getText(text):
	# config logger
	config_logger()
	logging.debug('message to be analysed: [%s]\n', text)

	# open the config file
	cfg = read_from_config()

	# make the https request and get a response in a string
	response_text = request_https(cfg, text.replace(" ", "%20")).text

	# writing json data
	write_to_json(response_text)

	# analyse if a comment is positive or negative and get a messaege to print on screen
	is_analyses_positive =  analyse_positive_comment(json.loads(response_text))
	message = get_message(is_analyses_positive)

	return {message}

run(reloader=True, debug=True)
