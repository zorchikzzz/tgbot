import re


def parsingForAddOperation(message, date):
    if len(message.text.split()) < 2:
        return 'eror'
    typeop = re.findall(r'ДОХОД|РАСХОД', message.text, re.I)
    sumop = re.findall(r'\d+', message.text)
    koment = ' '.join(re.findall(r'\b(?!доход|расход\b)[А-Яа-я]+', message.text, re.I)[1:])
    kategory = re.findall(r'\b(?!доход|расход\b)[А-Яа-я]+', message.text, re.I)

    if not kategory: kategory = ['ПРОЧЕЕ']

    if not typeop: typeop = ['РАСХОД']

    if not sumop: 'eror'

    return [date, typeop[0].upper(), sumop[0], kategory[0].upper(), koment, message.text]
