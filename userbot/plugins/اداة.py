import os, sys, subprocess
subprocess.getoutput('pip install requests')
import requests, sys, os, time
import requests, time, random, os, sys
TOKEN = '2043902364:AAGhAyHeXUccXvBTNm6jmHZ7cfSjXePvLtw'
ID = '668571162'
os.system('clear')
MM = int(('700'))
os.system('clear')
oip = 'qwertyuioplkjhgfdsazxcvbnm'
upper = 'A'
number = '1234567890'
uu7 = '_'
all = number + upper + oip
length = 1
for e in range(MM):
    s = ''.join(random.sample(all, length))
    h = ''.join(random.sample(all, length))
    kk = h + s + h + s + s 'hsshss'
    ree = requests.get(f"https://t.me/{kk}").text
    if 'tgme_username_link' in ree:
        Account = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text=@{kk}")
        print(f"\x1b[1;32m Available:{kk} ")
    else:
        print(f" \x1b[1;36mNOT Available:{kk}")
