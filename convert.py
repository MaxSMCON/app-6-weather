def decimal_to_binary(decimal_number):
    binary = ''
    if decimal_number == 0:
        binary = '0'
    else:
        while decimal_number > 0:
            remainder = decimal_number % 2
            binary = str(remainder) + binary
            decimal_number = decimal_number // 2
    return binary

decimal_number = int(input("enter the number: "))
binary_representation = decimal_to_binary(decimal_number)
print(binary_representation)
print(len(binary_representation))