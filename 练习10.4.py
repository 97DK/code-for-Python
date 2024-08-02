from pathlib import Path
path = Path('guest.txt')
a=input("Please input your name:")
path.write_text(a)