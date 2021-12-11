from web3 import Web3
from hashAddressList import list
import time

def transactionCheck():
    
    w3 = Web3(Web3.HTTPProvider('https://speedy-nodes-nyc.moralis.io/cd376ab3618d8de1de47dd49/bsc/mainnet'))
    file = 'dataResult.txt'
    # transaction = w3.eth.get_transaction(hash)
    try:
        for line in list:
            time.sleep(3)
            trans_receipt = w3.eth.get_transaction_receipt(line['hash'])
            for i in trans_receipt['logs']:
                    if (i['address']).lower() == (line['address']).lower():
                        f = open(file, 'a')
                        f.write(line['hash']), f.write(',') ,f.write(line['address']),f.write(','), f.write(str(int(i['data'],16))) ,f.write('\n')
                        f.close()
                        print('done')
    except Exception as error:
        
        f = open(file, 'a')
        f.write(line['hash']), f.write(',') ,f.write(line['address']),f.write(','), f.write('no_Data_Recieved') ,f.write('\n')
        f.close()
        print(error)

transactionCheck()
