import timeit
from crc import * 

def setup_crc_function():
    # Create an instance of the CRC class
    c = CRC()
    return c

def crc_performance(c):
    # Call the reciverSide method
    c.reciverSide('100110001', '1101')

if __name__ == '__main__':
    # Create a setup function to initialize CRC object
    c_instance = setup_crc_function()
    time_exe = timeit.timeit(lambda: crc_performance(c_instance))
    
    print(time_exe)
