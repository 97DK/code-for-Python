message1={'first_name':'zhang','last_name':'huan','city':'heyuan'}
message2={'first_name':'Karry','last_name':'Wang','city':'chongqing'}
message3={'first_name':'Roy','last_name':'Wang','city':'chongqing'}
message4={'first_name':'Jackson','last_name':'Yee','city':'beijing'}
people=[message1,message2,message3,message4]
for messages in people:
    print(f"{messages['first_name']} {messages['last_name']} come from {messages['city']}")