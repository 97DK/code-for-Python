from pathlib import Path
files = ['cats.txt', 'dogs.txt']
try:
    for file in files:
        path = Path(file)
        content = path.read_text(encoding='utf-8')
        print(content)
except FileNotFoundError:
    pass