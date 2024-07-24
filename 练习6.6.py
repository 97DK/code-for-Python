favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
namelist=['jack','tom','sarah','jenny','phil']
for name in namelist:
    if name in favorite_languages.keys():
        print(f"{name} Thank you for us investigation")
    else:
        print(f"{name},Can you answer our investigation about your favorite languages?")