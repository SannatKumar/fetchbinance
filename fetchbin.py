from binance.client import Client
import config

client = Client(config.apiKey, config.apiSecurity)
print("Logged In")

'''
#Get all the info for any specific symbol
info = client.get_symbol_info('BNBBTC')
for i in info:
    print(info)

'''

#Get all the info from exchange

info = client.get_exchange_info()
for i in info:
    print(i)

# Getting the Time Zone

timez = info['timezone']
print(timez)


# Getting the Server time

