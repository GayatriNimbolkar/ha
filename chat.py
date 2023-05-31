#BOT

pip install chatterbot


pip install chatterbot_corpus
pip install chatterbot_corpus

import spacy

fromspacy. cli . downloadimportdownload
download(model="en_core_web_sm")

fromchatterbot importChatBot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('name')

trainer = ListTrainer ( chatbot)
trainer . train ([
 "Hi, can I help you?" ,
 "Sure, I'd like to book a flight to Iceland." ,
 "Your flight has been booked."
])
response = chatbot. get_response('I would like to book a flight.' )
print (response)

while True:
    query= input ()
    if query == 'exit' :
        break
    ans=chatbot. get_response( query)
    print ( "Bot:" , ans)

