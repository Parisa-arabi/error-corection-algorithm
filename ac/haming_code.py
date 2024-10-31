class HammingCode:
    def __init__(self):
        pass

    def generate_hamming_data(self, data):
        """Encode data using Hamming Code."""
        m = len(data)
        r = self._calc_redundant_bits(m)
        arr = self._position_redundant_bits(data, r)

        # Calculate parity bits and encode the data
        for i in range(r):
            arr = self._calculate_parity_bits(arr, i)

        # print("Data transferred is:", ''.join(arr))
        return ''.join(arr)

    def receiver_side(self, received_data):
        """Detect errors in the received data (similar to CRC receiver side)."""
        n = len(received_data)
        r = self._calc_redundant_bits(n - len(bin(n)[2:]))
        correction = self._detect_error(received_data, r)
        if correction == 0:
            return "No error detected"
        else:
            error_position = len(received_data) - correction
            return f"Error detected at bit position: {error_position}"

    def _calc_redundant_bits(self, m):
        """Calculate the number of redundant bits needed."""
        for i in range(m):
            if (2**i >= m + i + 1):
                return i

    def _position_redundant_bits(self, data, r):
        """Position redundant bits within the data."""
        j = 0
        k = 1
        m = len(data)
        res = ''

        # Inserting redundant bits
        for i in range(1, m + r + 1):
            if i == 2**j:
                res = res + '0'
                j += 1
            else:
                res = res + data[-1 * k]
                k += 1
        
        # Return reversed list, since we constructed it backwards
        return list(res[::-1])

    def _calculate_parity_bits(self, arr, parity_pos):
        """Calculate parity bits for the given data."""
        n = len(arr)
        parity = 0
        for i in range(parity_pos + 1, n + 1):
            if i & (2**parity_pos) != 0:
                parity ^= int(arr[-1 * i])
        
        arr[-1 * (2**parity_pos)] = str(parity)
        return arr

    def _detect_error(self, arr, nr):
        """Detect and determine the bit position of an error."""
        n = len(arr)
        res = 0

        # Recalculate parity bits
        for i in range(nr):
            val = 0
            for j in range(1, n + 1):
                if j & (2**i) == (2**i):
                    val ^= int(arr[-1 * j])

            res += val * (10**i)

        # Convert binary to decimal
        return int(str(res), 2)

# Example usage of the HammingCode class
hamming = HammingCode()
# data = "1001001"
# encoded_data = hamming.generate_hamming_data(data)
# print(encoded_data)

# # Simulate error in transmission
received_with_error = '11010000101'   # Introduced error
result = hamming.receiver_side(received_with_error)
print(result)
