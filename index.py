import json
from web3 import Web3

while True:
    # input 
    welcome = """
    create wallet ethereum, binance smart chain, polygon, avalanche, fantom, ....\n
    """
    numWallet = int(input("How many wallets do you need (default 50 wallet): ") or "50")
    fileName = input("Desired filename (default: wallet.txt)? ") or "wallet"
    key = "9dca15bb1bac45fc8de29167e1fd1a3c"
    apiUrl = "https://mainnet.infura.io/v3/"+key

    data = Web3(Web3.HTTPProvider(apiUrl))

    wallet = open(fileName+".txt", "w")

    for i in range(numWallet):
        integate = i+1
        account = data.eth.account.create()
        wallet.write("ACCOUNT %s: \n" % integate)
        wallet.write("Public Key: %s\n" % account.address)
        wallet.write("Private Key: %s\n" % account.privateKey.hex())
        wallet.write("===============================================\n\n")

    wallet.close()
    print("Complete!")

    while True:
        answer = str(input('Do you want to restart program? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("Wrong! Please input again")
    if answer == 'y':
        continue
    else:
        print("Thank you so much!!!")
        break