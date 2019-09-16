import os

APP_PATH = os.path.dirname(__file__)

IMAP_EMAIL = os.environ.get('IMAP_EMAIL', '')
IMAP_PASSWORD = os.environ.get('IMAP_PASSWORD', '')
IMAP_SERVER = os.environ.get('IMAP_SERVER', '')
SMTP_SERVER = os.environ.get('SMTP_SERVER', '')
SMTP_PORT = os.environ.get('SMTP_PORT', 993)


if IMAP_EMAIL == '' and not os.path.exists('/tmp/cvbot.env'):
    print('CV Bot - First Run Configuration')
    print('cvbot.env does not exist.  It will be created.')
    IMAP_EMAIL = '"' + input('Specify email address: ') + '"'
    IMAP_PASSWORD = '"' + input('Enter password for account: ') + '"'
    IMAP_SERVER = '"' + input('Enter IMAP server address: ') + '"'
    SMTP_SERVER = '"' + input('Enter SMTP server address: ') + '"'
    SMTP_PORT = '"' + input('Enter SMTP port: ') + '"'
    
    # write settings to cvbot.env file:
    f = open("/tmp/cvbot.env", "w")
    f.write('IMAP_EMAIL="' + IMAP_EMAIL + '"')
    f.write('IMAP_PASSWORD="' + IMAP_PASSWORD + '"')
    f.write('IMAP_SERVER="' + IMAP_SERVER + '"')
    f.write('SMTP_SERVER="' + SMTP_SERVER + '"')
    f.write('SMTP_PORT="' + SMTP_PORT + '"')
    f.close()
    
if IMAP_EMAIL.startswith('"') and IMAP_EMAIL.endswith('"'):
    IMAP_EMAIL = IMAP_EMAIL[1:-1]
if IMAP_PASSWORD.startswith('"') and IMAP_PASSWORD.endswith('"'):
    IMAP_PASSWORD = IMAP_PASSWORD[1:-1]
if IMAP_SERVER.startswith('"') and IMAP_SERVER.endswith('"'):
    IMAP_SERVER = IMAP_SERVER[1:-1]
if SMTP_SERVER.startswith('"') and SMTP_SERVER.endswith('"'):
    SMTP_SERVER = SMTP_SERVER[1:-1]
if SMTP_PORT.startswith('"') and SMTP_PORT.endswith('"'):
    SMTP_PORT = SMTP_PORT[1:-1]

print('Using the following settings:')
print('IMAP_EMAIL=' + IMAP_EMAIL)
print('IMAP_PASSWORD=' + IMAP_PASSWORD)
print('SMTP_SERVER=' + SMTP_SERVER)
print('SMTP_PORT=' + str(SMTP_PORT))