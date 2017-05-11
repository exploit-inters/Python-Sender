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
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


#check connectoin class 
def checkConnection(server, port, tls, user, passw):
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
	
	
	
	#mail info 
def mailSend(server, port, tls, user, passw, maillist, From, subject, mailtext):
    smtpConnect = checkConnection(server, port, tls, user, passw)
    emails = len(maillist)
    for success, sendto in enumerate(maillist):
        content = MIMEMultipart()
        content['From'] = From
        content['To'] = sendto.rstrip()
        content['Subject'] = subject
        htmlscript = mailtext.rstrip()
        content.attach(MIMEText(htmlscript, 'html'))
        print('Python Email Sender >>> You are going to send to '+sendto.rstrip())
        smtpConnect.sendmail(From, sendto.rstrip(), content.as_string())
    smtpConnect.quit()
    print('\n Python Email Sender >>> Email to '+str(success+1)+'/'+str(emails)+' Done H5H \n')
    
    
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

smtpServer = raw_input('\n SMTP Server: ')

smtpPort = input('SMTP Port : ')

smtpTLS = input('TLS ? For yes enter [1] For No Enter [0]): ')

smtpUser = raw_input('SMTP Username: ')

smtpPass = raw_input('SMTP Password: ')

#check if smtp connected 
if checkConnection(smtpServer, smtpPort, smtpTLS, smtpUser, smtpPass,):
    print('\n Python Email Sender >>> SMTP Status // Connected!')
    
    
    sendFrom = raw_input('\n Enter Sender Name: ')
    sendSubj = raw_input('Enter Subject: ')
    userlist = raw_input('Enter Email List as txt file: ')
    
    
    try:
        maillist = open(userlist).readlines()
        print('\nPython mail Sender >>> Have '+str(len(maillist))+' Mail .')
        htmlscript = raw_input('\n Enter Path HTML msg: ')
	
	
        try:
            html = open(htmlscript).read()
            raw_input('ENTER, To Start Send'+str(len(maillist))+' ...\n')
	    
	    
            try:
                mailSend(smtpServer, smtpPort, smtpTLS, smtpUser, smtpPass, maillist, sendFrom, sendSubj, html)
            except:
                print('ERROR: I CANT USE THE EMAIL!')
        except:
            print('The HTML File cannot get readed yet or is empty.')
    except:
        print('The .txt File cannot get readed or is empty.')
else:
    print('No Connetoin in the Server -_- ')
    
    

    
    
    
    
   



















   