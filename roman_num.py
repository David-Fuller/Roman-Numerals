numerals = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV": 4, "I":1}

def convert_roman(input_number):
	result = ""
	for rn_symbol, rn_number in numerals.items():
		t = int(input_number/rn_number)
		if t > 0:
			result += (t * rn_symbol)
			input_number -= (t * rn_number)
	return result

input_number = int(input("Enter a number you wish to convert to roman numerals: "))
print(convert_roman(input_number))
