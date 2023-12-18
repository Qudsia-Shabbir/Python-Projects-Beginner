import smtplib as smt
ob = smt.SMTP('smpt.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('qs991549@gmail.com','mypassword')
subject= " HI, i am a web developer , i would like to create a website for your business"
body = "here's my phone number +923003088164 ,lets connect"
message= "subject:{}\n\n{}".format(subject,body)
listadd= ['qs991549@gmail.com,zainhaib@gmail.com']
ob.sendmail('qs991549@gmail.com',listadd,message)
print("send mail")
ob.quit
