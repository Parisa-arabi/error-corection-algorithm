class CRC:
	
	def __init__(self):
		self.cdw = ''

	def xor(self,a,b):
		result = []
		for i in range(1,len(b)):
			if a[i] == b[i]:
				result.append('0')
			else:
				result.append('1')


		return  ''.join(result)



	def crc(self,message, key):
		pick = len(key)

		tmp = message[:pick]

		while pick < len(message):
			if tmp[0] == '1':
				tmp = self.xor(key,tmp)+message[pick]
			else:
				tmp = self.xor('0'*pick,tmp) + message[pick]

			pick+=1

		if tmp[0] == "1":
			tmp = self.xor(key,tmp)
		else:
			tmp = self.xor('0'*pick,tmp)

		checkword = tmp
		return checkword

	def encodedData(self,data,key):
		l_key = len(key)
		append_data = data + '0'*(l_key-1)
		remainder = self.crc(append_data,key)
		codeword = data+remainder
		self.cdw += codeword
		return (codeword)


	def reciverSide(self,data,key):
		# todo
		r = self.crc(data,key)
		size = len(key)-1
		# print(r)
		if int(r) == size*0:
			return "No error detected"
		else:
			return "Error detected"



data = '100'
key = '10'

c = CRC()
print(c.encodedData(data,key))



# # print('---------------')
print(c.reciverSide('1001','10'))
# # print('---------------')
# print(c.cdw)