import re

def email_parse(email):
    RE_EMAIL = re.compile(r'^[a-zA-Z.+]+[@][a-zA-Z]+[.][a-zA-Z]+')
    RE_EMAIL_FIN = re.compile(r'^(?P<username>[a-zA-Z.+]+)[@](?P<domain>[a-zA-Z]+[.][a-zA-Z]+)')
    if re.match(RE_EMAIL,email):
        return map(lambda x: x.groupdict(), RE_EMAIL_FIN.finditer(email))
    else:
        msg = f' wrong email {email}'
        raise ValueError(msg)

#print(re.search(RE_EMAIL,'someone@geekbrains.ru'))
try:
    print(*email_parse('someone@geekbrains.ru'))
    print(*email_parse('somed.fone@geekbrains.ru'))
    print(*email_parse('cool@gmail.com'))
    print(*email_parse('someone@geekbrainsru'))
except ValueError as err:
    print(err)


