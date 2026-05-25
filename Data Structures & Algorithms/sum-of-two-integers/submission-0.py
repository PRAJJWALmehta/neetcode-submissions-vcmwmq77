class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Step 1: Mask inputs to 32-bit unsigned integers
        # This converts negative numbers to their 32-bit Two's Complement equivalent
        a = a & 0xFFFFFFFF
        b = b & 0xFFFFFFFF
        
        c = 0
        res = 0
        
        # Step 2: Explicitly loop over the 32-bit integer boundaries
        for i in range(32):
            da = a & 1
            db = b & 1

            # Your corrected logic works beautifully here
            s = da ^ db ^ c
            c = (da & db) | (db & c) | (c & da)

            a = a >> 1
            b = b >> 1

            res = res | (s << i)
            
        # Step 3: Handle the 32-bit signed integer conversion
        # If the 31st bit (sign bit) is set, it means the result is negative
        if res & (1 << 31):
            # Convert back to Python's internal infinite negative format
            return ~(res ^ 0xFFFFFFFF)
        
        return res