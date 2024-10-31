from crc import *
from haming_code import *

def crc_capcibity():
    c = CRC()
    real_data = '100100001'
    data = '1100011011'
    key = '1011'
    result = c.reciverSide(data,key)
    expected_result = 'Error detected'
    print(f'sender send {real_data}\nbut reciever got {data}\ncrc result:{result}\nexpected result: {expected_result}')
def hamming_code_capcibity():
    h = HammingCode()
    real_data = '0111001'
    data =   '10011101111' 
    result = h.receiver_side(data)
    expected_result = 'Error detected'
    print(f'sender send {real_data}\nbut reciever got {data}\nhamming code result:{result}\nexpected result: {expected_result}')

crc_capcibity()
print('-------------------------------------------')
hamming_code_capcibity()