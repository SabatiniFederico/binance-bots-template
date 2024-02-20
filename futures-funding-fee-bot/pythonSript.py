from binance import Client
from datetime import datetime, timedelta
from time import sleep
import schedule

api_key=""
api_secret=""

binance = Client(api_key, api_secret)

myLeverage = 5
binance.futures_change_leverage(symbol='TRBUSDT', leverage=myLeverage)
print("Leverage setted in: ", myLeverage)

def binanceBuyOrder(coinSymbol, coinQuantity):
    binance.futures_create_order(symbol=coinSymbol, 
                            side='BUY',
                            positionSide='BOTH',
                            type='MARKET', 
                            quantity=coinQuantity,
                            reduceOnly=False,
                            newClientOrderId='web_smOHI5SNYSOFDKEMjEIJ', 
                            closePosition=False,
                            workingType='CONTRACT_PRICE',
                            priceProtect=False)

def binanceSellOrder(coinSymbol, coinQuantity):
    binance.futures_create_order(symbol=coinSymbol, 
                            side='SELL',
                            positionSide='BOTH',
                            type='MARKET', 
                            quantity=coinQuantity,
                            newClientOrderId='web_smOHI5SNYSOFDKEMjEIJ', 
                            workingType='CONTRACT_PRICE',
                            priceProtect=False)

def sleepUntilCountdown(target):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    while(now < target):
        now = datetime.now()
        if abs(now - target) < timedelta(seconds=2):
            sleep(0.001)
        else:
            sleep(1)

def BinanceTRBUSDTBot(cutHour):
    print("--- Starting Scheduled bot for TRBUSDT ---")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Starting Hour is: ", current_time)
    print("expected cut hour is: ", cutHour)

    print("Executing Buy Long order for 5 TRBUSDT aprox 100 USDT")
    buyOrderInExecution=True

    while buyOrderInExecution:
        try:
            binanceBuyOrder(coinSymbol='TRBUSDT', coinQuantity='4')
            buyOrderInExecution=False
        except:
            print("Error has ocurred!, executing order again!")
            sleep(1)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Buy order executed at time! ", current_time)

    print("Waiting 40 minutes until sell.....")
    sleepUntilCountdown(cutHour)
    print("Done!")
    
    print("Executing Sell Short order for 5 TRBUSDT aprox 100 USDT")
    sellOrderInExecution=True

    while sellOrderInExecution:
        try:
            responseSell = binanceSellOrder(coinSymbol='TRBUSDT', coinQuantity='4')
            sellOrderInExecution=False
        except:
            print("Error has ocurred!, executing order again!")
            sleep(1)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Sell order executed at time! ", current_time)


#Automated cut off scheduled functions

def schedule0100CoinTRBUSDT():
    cutHour=(datetime.today()- timedelta (days=0)).replace(hour=0, minute=59, second=50)
    removeMiliseconds = cutHour.strftime("%Y-%m-%d %H:%M:%S")
    cutHour=datetime.strptime(removeMiliseconds, "%Y-%m-%d %H:%M:%S")
    BinanceTRBUSDTBot(cutHour)

def schedule0500CoinTRBUSDT():
    cutHour=(datetime.today()- timedelta (days=0)).replace(hour=4, minute=59, second=50)
    removeMiliseconds = cutHour.strftime("%Y-%m-%d %H:%M:%S")
    cutHour=datetime.strptime(removeMiliseconds, "%Y-%m-%d %H:%M:%S")
    BinanceTRBUSDTBot(cutHour)

def schedule0900CoinTRBUSDT():
    cutHour=(datetime.today()- timedelta (days=0)).replace(hour=8, minute=59, second=50)
    removeMiliseconds = cutHour.strftime("%Y-%m-%d %H:%M:%S")
    cutHour=datetime.strptime(removeMiliseconds, "%Y-%m-%d %H:%M:%S")
    BinanceTRBUSDTBot(cutHour)

def schedule1300CoinTRBUSDT():
    cutHour=(datetime.today()- timedelta (days=0)).replace(hour=12, minute=59, second=50)
    removeMiliseconds = cutHour.strftime("%Y-%m-%d %H:%M:%S")
    cutHour=datetime.strptime(removeMiliseconds, "%Y-%m-%d %H:%M:%S")
    BinanceTRBUSDTBot(cutHour)

def schedule1700CoinTRBUSDT():
    cutHour=(datetime.today()- timedelta (days=0)).replace(hour=16, minute=59, second=50)
    removeMiliseconds = cutHour.strftime("%Y-%m-%d %H:%M:%S")
    cutHour=datetime.strptime(removeMiliseconds, "%Y-%m-%d %H:%M:%S")
    BinanceTRBUSDTBot(cutHour)

def schedule2100CoinTRBUSDT():
    cutHour=(datetime.today()- timedelta (days=0)).replace(hour=20, minute=59, second=50)
    removeMiliseconds = cutHour.strftime("%Y-%m-%d %H:%M:%S")
    cutHour=datetime.strptime(removeMiliseconds, "%Y-%m-%d %H:%M:%S")
    BinanceTRBUSDTBot(cutHour)

def helloBot():
    print("Im alive! the actual hour is: ", datetime.now())

schedule.every(10).minutes.do(helloBot)
schedule.every().day.at("00:20").do(schedule0100CoinTRBUSDT)
schedule.every().day.at("04:20").do(schedule0500CoinTRBUSDT)
schedule.every().day.at("08:20").do(schedule0900CoinTRBUSDT)
schedule.every().day.at("12:20").do(schedule1300CoinTRBUSDT)
schedule.every().day.at("16:20").do(schedule1700CoinTRBUSDT)
schedule.every().day.at("20:20").do(schedule2100CoinTRBUSDT)

print("Everything Ok, starting bot!!!")
now = datetime.now()
startTime = now.strftime("%H:%M:%S")
print("Nested Hour is: ", startTime)
while True:
   schedule.run_pending()
   sleep(1)




