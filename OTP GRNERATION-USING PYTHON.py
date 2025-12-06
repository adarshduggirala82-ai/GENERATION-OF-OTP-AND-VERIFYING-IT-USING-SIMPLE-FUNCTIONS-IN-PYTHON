import random
d = ['1','2','3','4','5','6','7','8','9','0']
random.shuffle(d)
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
random.shuffle(a)
c = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
random.shuffle(c)
s = ['!','@','$','%','^','&','*','/',';','=','+','-','_','?','/','<','>']
random.shuffle(s)
o = c[0]+a[4]+d[7]+s[9]+a[3]+d[4]+c[25]+a[15]+s[7]+a[19]
import smtplib
from email.message import EmailMessage
e = input ("enter your mail")

sending_email = "enter email"     
app_password = "enter pass key"   
receiver_email = e 


output = o


msg = EmailMessage()
msg['Subject'] = "otp"
msg['From'] = sending_email
msg['To'] = receiver_email
msg.set_content(output)


with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()          
    server.login(sending_email, app_password)
    server.send_message(msg)

print("Email sent successfully!")
otp = input("enter otp").strip()
if otp == o:
   print("verified")

else:
    
    print("incorrect")