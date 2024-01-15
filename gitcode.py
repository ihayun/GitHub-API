import requests
import json
from pprint import pprint
import logging
import yaml

logging.basicConfig(level=logging.DEBUG, filename='logging.log')

def get_user_data() -> dict:
  logging.info('Getting user token...')
  token_path = 'config.yml'

  config = {}

  print('Loading ' + token_path)
  with open(token_path, 'r') as f:
    config = yaml.safe_load(f)

  token = config['token']

  logging.info('Getting user information..')
  response = requests.get(url='https://api.github.com/user',
                          headers={'Authorization': 'Bearer ' + token})
  # parse json
  response_json = json.loads(response.text)

  if 'message' in response_json and response_json['message'] == 'Bad credentials':
    logging.error('Bad credentials')
    return None

  return response_json


