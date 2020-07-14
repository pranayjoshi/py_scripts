import smtplib 
resipiant = "deepak joshi"
content = "your forte 40 has been cracked"

# init gmail SMTP
mail = smtplib.SMTP('smtp.gmail.com', 587)

# identify to server
mail.ehlo()

    # encrypt session
mail.starttls()

    # login
mail.login('pranayjoshi446677@gmail.com', 'narayan446677')

    # send message
mail.sendmail('Deepak Chandra', 'dcjoshi1996@gmail.com', content)

    # end mail connection
mail.close()

print('Email sent.')
