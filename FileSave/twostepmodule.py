#!/usr/bin/env python3
import smtplib
import os
import random

# Use sms gateway provided by mobile carrier:
# at&t:     number@mms.att.net
# t-mobile: number@tmomail.net
# verizon:  number@vtext.com
# sprint:   number@page.nextel.com

def verification(phone, carrier):
    userinfo = phone + carrier

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP( "smtp.gmail.com", 587 )

    #generates reandom number for code
    code_gen = int((random.random()) * 1000000)

    #code gen
    code = 'Subject:Filesave Code: {}'.format(code_gen)

    server.starttls()

    server.login( '1FileSafe1@gmail.com', 'yespcheneqycrzpv' )

    # Send text message through SMS gateway of destination number
    server.sendmail('FileSave', userinfo, code)
    #3234949031@pm.sprint.com
    #3236371711@mms.att.net
