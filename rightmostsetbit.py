def rightmost_set_bit(n: int) -> int:
    
    if n == 0:
        return 0  
    return n & -n  

try:
    num = int(input("Enter a positive integer: "))
    if num < 0:
        raise ValueError("Number must be non-negative.")
    
    bit_value = rightmost_set_bit(num)
    if bit_value == 0:
        print("No set bits found.")
    else:
        position = bit_value.bit_length()  
        print(f"Rightmost set bit value: {bit_value} (binary: {bin(bit_value)})")
        print(f"Position from right (1-based): {position}")

except ValueError as e:
    print(f"Invalid input: {e}")
