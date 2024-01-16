input_value = list(input("Enter the Character or String : "))

if not input_value:
    print(" Either given is empty or Invalid Character")
else:
    if len(input_value)>=2:
        del input_value[1::2]
    else:
        print("Incorrect value")
    output_value = ''.join(reversed(input_value))
    print(output_value)
    