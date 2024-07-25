message1={"name":"dahuang","type":'dog',"host":"Jack"}
message2={"name":"taizi","type":'cat',"host":"Jay"}
message3={"name":"billy","type":'dog',"host":"Jenny"}
pets=[message1,message2,message3]
for message in pets:
    print(f"{message['name']} is a {message['type']} it host's  is {message['host']}")
