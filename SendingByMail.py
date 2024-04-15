import smtplib
import os

def send_email(message):
    sender = 'почта'
    password = 'пароль'

    server = smtplib.SMTP('smtp.mail.ru', 465)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, 'куда отправить', message)

        return "The message was sent successfully!"
    except Exception as _ex:
        return f'{_ex}\nCheck your email or password'

def main():
    message = input("Type your message...")
    print(send_email(message=message))

if __name__ == '__main__':
    main()

