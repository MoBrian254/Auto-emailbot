import smtplib


def send_mail():
  server = smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  
  with open('password.txt', 'r') as p:
    password = p.read()

  server.login('ENTER YOUR EMAIL HERE', 'ENTER PASSWORD HERE')
  
  subject = "Good morning from SENDER..."
  
  with open('body.txt', 'r') as b:
    b = b.read()

  msg = f"Subject: {subject} \n\n\n {b}"
  
  server.sendmail(
    'FROM',
    'TO',
    msg
  )
  print('Message is sent successfully...')


if __name__ == "__main__":
  send_mail()



