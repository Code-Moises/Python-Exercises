sum_odd_digits = 0
sum_even_digits = 0
total = 0


# Step 1
card_number = input("Enter a credit card number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1] # this will reverse our string

# Step 2
for x in card_number[::2]: # we need every second digit
    sum_odd_digits += int(x)

# Step 3
for x in card_number[1::2]: # Every second digit, but we will start in the second index which is 1
    x = int(x) * 2
    if x > 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# Step 4
total = sum_odd_digits + sum_even_digits

# Step 5
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")


