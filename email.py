import yagmail
yag = yagmail.SMTP(host="127.0.0.1")
yag.send(to"fvural@aktasholding.com", subject="subject", contents="content")