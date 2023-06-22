prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]


def krw_to_usd(krw):
    return krw * 1000
    
def usd_to_jpy(usd):
    return usd / 8 * 1000
    

print("한국 화폐 :" + str(prices))

usd_prices = [krw_to_usd(x) for x in prices]

jpy_prices = [usd_to_jpy(x) for x in usd_prices]

print(usd_prices)
print(jpy_prices)

