from random import random


def send_email(message, recipient, sender = 'university.help@gmail.com'):
        recipient = (recipient)
        sender = (sender)
        list_recipient = list(recipient)
        list_sender = list(sender)
        if '@' in list_recipient and '@' in list_sender:
            pass
        else:
            print('Невозможно отправить письмо с адреса', (sender), 'на адрес', (recipient), '.')
            return
        variants = ('.com', '.ru', '.net',)
        if recipient.endswith(variants) and sender.endswith(variants) :
            pass
        else:
            print('Невозможно отправить письмо с адреса', (sender), 'на адрес', (recipient), '.')
            return
        if recipient == sender:
           print('Письмо нельзя отправить себе самому.')
           return
        if sender == ('university.help@gmail.com'):
           print('Письмо успешно отправлено с адреса', (sender), 'на адрес', (recipient), '.')
        else:
           print( 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', (sender), 'на адрес', (recipient), '.')







send_email('Привет!','rskle@yandex.ru',)