from email import message
from urllib import response
import requests
import sys
import getopt

# Send Slack Message Using Slack API


endpoint = "https://hooks.slack.com/services/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"

message = "Hello from Python"


def send_slack_message():
  payload = '{"text":"%s"}' % message
  response = requests.post(endpoint, data=payload)
  print(response.text)

send_slack_message()