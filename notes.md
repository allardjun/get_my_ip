# on ricotta

cp get_my_ip_ricotta.py ~/bin/. 
chmod a+x ~/bin/get_my_ip_ricotta.py    

crontab -e

#0 0 * * MON /Users/jun/git/pub/get_my_ip/get_my_ip_ricotta.py
0 * * * * /Users/jun/git/pub/get_my_ip/get_my_ip_ricotta.py