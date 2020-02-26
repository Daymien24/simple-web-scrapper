import smtplib, ssl
from bs4 import BeautifulSoup
import requests

URL = 'https://allegro.pl/oferta/choinka-sztuczna-sosna-diamentowa-220-cm-stojak-7606909265'
cena = 0
def check_price():
    global cena
    page = requests.get(URL)

    soup = BeautifulSoup(page.text, 'lxml')

    title = soup.find('div', class_='_1h7wt _15mod').h1.text 
    cena = soup.find('div', class_='_wtiln _bdn9q _9a071_2MEB_').text
    print(title + "\nCENA: " + cena +"\n")

    

    converted_cena = cena[0:6].replace(',', '.')
    converted_cena2 = converted_cena.replace(' ', '')
    print("Price of the christmas tree: ")
    print(float(converted_cena2))
    if(float(converted_cena2) < 100):
        send_mail()
    else:
        print("It's too much for now")

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    context = ssl.create_default_context()
    server.starttls(context=context)
    server.ehlo()

    server.login('your_adress@gmail.com', 'password')

    msg = f"Christmas tree on sale !!! It costs {cena} ;)".encode('utf-8') # remember to always encode a message !

    server.sendmail('your_adress@gmail.com', 'receivers_adress@gmail.com', msg)

    print("email has been sent")
    server.quit()


check_price()

