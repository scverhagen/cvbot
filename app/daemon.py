import time

from app import config
from app import mail

def mainloop():
    while(1):
        print('Checking email...')
        if not config.IMAP_SERVER == '':
            mail.checkformail()
        else:
            print('No IMAP server specified.  Doing nothing...')
        print('Sleeping for 5 minutes...')
        time.sleep( (5*60) ) # check mail every 5 minutes

def start():
	mainloop()