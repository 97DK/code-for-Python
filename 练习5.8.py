namelist=['Tom','jackey','John','admin','linda']
for i in namelist:
    if i =='admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {i}, thank you for logging in again.")