banner = """
\033[0;31m
████████ ██   ██ ████████        ██████  ███████ ███    ██ 
   ██     ██ ██     ██          ██       ██      ████   ██ 
   ██      ███      ██    █████ ██   ███ █████   ██ ██  ██ 
   ██     ██ ██     ██          ██    ██ ██      ██  ██ ██ 
   ██    ██   ██    ██           ██████  ███████ ██   ████                                                   
\033[32;1m
Author		: Shahed Noor
Tools Name	: TXT - Generator
Version		: 1.0                                                  
"""
print(banner)
text = input("Please Enter Your Text Sir: ")
numberoftexts = int(input("Enter The Number Of Text: "))
counter = 1
while counter <= numberoftexts:
 print(text)
 counter = counter + 1