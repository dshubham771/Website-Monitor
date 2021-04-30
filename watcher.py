import requests
import time
import smtplib
import datetime
from pytz import timezone
from email.message import EmailMessage
import hashlib
from urllib.request import urlopen
# from google.colab import output

url = 'https://www.youtube.com/'
# response = urlopen(url).read()
resp = requests.get(url)
responseOld = resp.text
# currentHash = hashlib.sha256(response.encode('utf-8')).hexdigest()

while True:

    try:
        # response = urlopen(url).read()
        # currentHash = hashlib.sha224(response).hexdigest()

        # Set the time interval for checking the website in seconds
        time.sleep(10)
        # response = urlopen(url).read()
        resp = requests.get(url)
        response = resp.text
        # newHash = hashlib.sha256(response.encode('utf-8')).hexdigest()

        # if newHash == currentHash:
        #     continue
        # if difference between old and new content is less than or equal to 5 characters then ignore the changes
        if abs(len(responseOld) - len(response))<= 5:
            continue

        else:
            # get current time
            utc_time = datetime.datetime.now()
            ist_time = utc_time.astimezone(timezone('Asia/Kolkata'))
            tim = (""+str(ist_time.hour)+":"+str(ist_time.minute)+":"+str(ist_time.second))
            print("data changed at "+tim)
            # Prints difference of number of characters between old and new response
            print(abs(len(responseOld) - len(response)))
            responseOld = response

            # To notify via email
            msg = EmailMessage()
            msg.set_content(url)
            msg['From'] = 'Watcher Bot'
            msg['To'] = 'toaddress@example.com'

            msg['Subject'] = "Site updated at "+tim
            fromaddr = 'fromaddress@example.com'
            toaddrs = ['toaddress@example.com']
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('youremail@example.com', 'yourpassword')
            server.send_message(msg)
            server.quit()
            # # response = urlopen(url).read()
            # # currentHash = hashlib.sha224(response).hexdigest()
            continue


    except Exception as e:

        msg = EmailMessage()
        msg.set_content(url)
        msg['From'] = 'fromaddress@example.com'
        msg['To'] = 'toaddress@example.com'
        msg['Subject'] = 'DAR NETWORK FAILURE'
        fromaddr = 'fromaddress@example.com'
        toaddrs = ['toaddress@example.com']
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('youremail@example.com', 'yourpassword')
        server.send_message(msg)
        server.quit()

