import json
import os
import traceback
import urllib.parse

from botocore.vendored import requests

URL = "https://api.telegram.org/bot1057097448:AAEojH8infz-eemFpJTOBb8kwM-e-kSP-Po/"

requests.get('https://api.telegram.org/bot1057097448:AAEojH8infz-eemFpJTOBb8kwM-e-kSP-Po/sendMessage?chat_id=99999999999999&text=starting_bot')

def send_message(text, chat_id):
    final_text = str(text)
    query = urllib.parse.urlencode({'chat_id':chat_id, 'text':text})
    requests.get(URL+"sendMessage?"+query)


try:
    


    def lambda_handler(event, context):
        if 'body' in event:
            body = json.loads(event['body'])
            send_message(
                json.dumps(body, sort_keys=True, indent=4),
                '99999999999999'
            )
            if 'message' in body:
                message = body['message']
                if 'chat' in message and 'text' in message:
                    chat_id = message['chat']['id']
                    text = message['text']
                    send_message("You said: " + text, chat_id)
                if 'entities' in message and 'text' in message:
                    text = message['text']
                    entities = message['entities']
                    for ent in entities:
                      offset = ent['offset']
                      length = ent['length']
                      if 'bot_command'==ent['type']:
                        command = text[offset:offset+length]
                        if '/start'==command:
                          pass

        return {'statusCode': 200}
except:
    requests.get(URL+'sendMessage?chat_id=999999999999999999&text=%s'%(str(traceback.format_exc())))

