import smtplib

try:
    while 1:
        fromaddr = 'seu_email@gmail.com'
        toaddrs  = 'email_do_destinatario@yahoo.com'
        msg = 'Mensagem'

        username = 'seu_email@gmail.com'
        password = 'sua_senha'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        print('email enviado')
except:
    print('falha ao enviar email')
