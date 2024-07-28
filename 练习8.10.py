def send_messages(info):
    sent_messages=[]
    for i in info:
        print(i)
        sent_messages.append(i)
    print(sent_messages)
messages=['Hello,How are you?','Where are you go?','Goodafternoon']
send_messages(messages)