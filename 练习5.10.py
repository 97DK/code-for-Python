current_users=['Tom','jackey','John','admin','linda']
m=0
for i in current_users:
    current_users[m]=i.lower()
    m=m+1
new_users=['Jenny','tony','tom','jay','john']
for i in new_users:
    if i.lower() in current_users:
        print("Please input other user name")