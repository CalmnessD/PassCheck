import re

psd = input('Hello to password checker! it checks your password with the following conditions:\n1- Length between 8-12.\n2- Must contains a-z, A-Z, 0-9 and @#$.\nPlease enter password: ')

psdlen = len(psd) > 7 and len(psd) <13

searchPass = re.search(r'[a-z]' and '[A-Z]' and '[0-9]' and '[@#$]',psd)

if searchPass and psdlen:
    print('OK!')
else:
    print('Try again')
