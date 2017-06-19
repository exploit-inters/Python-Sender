#/$$      /$$           /$$$$$$$$           /$$   /$$           /$$ /$$
# $$  /$ | $$          |_____ $$           | $$  | $$          | $$| $$
# $$ /$$$| $$  /$$$$$$      /$$/   /$$$$$$ | $$  | $$  /$$$$$$ | $$| $$
# $$/$$ $$ $$ |____  $$    /$$/   /$$__  $$| $$$$$$$$ /$$__  $$| $$| $$
# $$$$_  $$$$  /$$$$$$$   /$$/   | $$$$$$$$| $$__  $$| $$$$$$$$| $$| $$
# $$$/ \  $$$ /$$__  $$  /$$/    | $$_____/| $$  | $$| $$_____/| $$| $$
# $$/   \  $$|  $$$$$$$ /$$$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$| $$| $$
#__/     \__/ \_______/|________/ \_______/|__/  |__/ \_______/|__/|__/
#                                                                      
#         
#
#for more infos go to https://docs.python.org/2/library/smtplib.html

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText




# func to connect to smtp 
def smtp_Connect(host, port, tls, user, passw):
    try:
        connect = smtplib.SMTP(server, port)
        connect.ehlo()
        if tls:
          connect.starttls()
          connect.ehlo()
        connect.login(user, passw)
        return connect
    except:
        return False


# func to get user inputs and sending mails	
def go_to_Send(host, port, tls, user, passw, maillist, From, subject, mailtext):
    smtpConnect = smtp_connect(host, port, tls, user, passw)
    #count mails 
    mailss = len(maillistt)
    for success, sendto in enumerate(maillist):
        content = MIMEMultipart()
        content['From'] = From
        content['To'] = sendto.rstrip()
        content['Subject'] = subject
        htmlscript = mailtext.rstrip()
        content.attach(MIMEText(htmlscript, 'html'))
        print('Python Email Sender >>> You are going to send to '+sendto.rstrip())
        smtp_Connect.go_to_Send(From, sendto.rstrip(), content.as_string())
    smtpConnect.quit()
    print('\n Python Email Sender >>> Email to '+str(success+1)+'/'+str(mailss)+' Done H5H \n')
    
    
print('''
 /$$      /$$           /$$$$$$$$           /$$   /$$           /$$ /$$
| $$  /$ | $$          |_____ $$           | $$  | $$          | $$| $$
| $$ /$$$| $$  /$$$$$$      /$$/   /$$$$$$ | $$  | $$  /$$$$$$ | $$| $$
| $$/$$ $$ $$ |____  $$    /$$/   /$$__  $$| $$$$$$$$ /$$__  $$| $$| $$
| $$$$_  $$$$  /$$$$$$$   /$$/   | $$$$$$$$| $$__  $$| $$$$$$$$| $$| $$
| $$$/ \  $$$ /$$__  $$  /$$/    | $$_____/| $$  | $$| $$_____/| $$| $$
| $$/   \  $$|  $$$$$$$ /$$$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$| $$| $$
|__/     \__/ \_______/|________/ \_______/|__/  |__/ \_______/|__/|__/
                                                            ''')

print('Python SMTP Email Sender')





#smtp connect 

smtphost = raw_input('\n SMTP Server ? : ')

smtpPort = input('SMTP Port ? : ')

smtpTLS = input('TLS ? For yes enter [1] For No Enter [0]) : ')

smtpUsername = raw_input('SMTP Username ? : ')

smtpPass = raw_input('SMTP Password ? : ')

#check if smtp connected 
if smtp_Connect(smtphost, smtpPort, smtpTLS, smtpUsername, smtpPass,):
    print('\n Python Email Sender >>> SMTP Status // Connected!')
    
    
    sendFrom = raw_input('\n Enter Sender Name: ')
    sendSubj = raw_input('Enter Subject: ')
    maillistt = raw_input('Enter Email List as txt file: ')
    
    #open mail list 
    try:
        maillist1 = open(maillistt).readlines()
        print('\nPython mail Sender >>> Have '+str(len(maillist1))+' Mail .')
        htmlmsg = raw_input('\n Enter Path HTML msg: ')
	
		#open html file 
        try:
            html = open(htmlmsg).read()
            raw_input('ENTER, To Start Send'+str(len(maillist1))+' ...\n')
	    
	    	# let's go lol 
            try:
                go_to_Send(smtphost, smtpPort, smtpTLS, smtpUsername, smtpPass, maillist1, sendFrom, sendSubj, html)
            except:
                print('ERROR: I CANT USE THE EMAIL!')
        except:
            print('The HTML File cannot get readed yet or is empty.')
    except:
        print('The .txt File cannot get readed or is empty.')
else:
    print('No Connetoin in the Server -_- ')
    
    

    
    
    
    
   



















   
