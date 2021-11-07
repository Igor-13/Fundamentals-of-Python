# Модуль utils из задания 4.2 (конвектор валют)
import datetime
import requests

result = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
result_2 = result.text


def currency_rates(currency):
    currency = currency.upper()
    if result_2.find(currency) < 0:
        return print('None')
    text = result_2.find(currency)
    editing = result_2[text: text + result_2.index('ID')]
    editing_1 = editing.replace('</CharCode><Nominal>', ': ')
    editing_2 = editing_1.replace('</Nominal><Name>', ' ')
    editing_3 = editing_2.replace('</Name><Value>', ' составляет ')
    editing_4 = editing_3.replace('</Value></Valute><Valute ', ' руб. ')
    rate = editing_4[0: editing_4.index('ID')]
    time = datetime.datetime.now()
    print(f'{rate} по состоянию на {time}')


