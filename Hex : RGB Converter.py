""" 
This is a converter that allows 
* RGB to Hex
* Hex to RGB
"""

def rgb_hex():
	invalid_msg = "Well it looks like you entered the wrong value"
  
	red = int(raw_input("Enter a value for red(R): "))
	if red < 0 or red > 255:
  		print invalid_msg
  		return
  
	green = int(raw_input("Enter a value for green(G): "))
	if green < 0 or red > 255:
 		print invalid_msg
		return
  
	blue = int(raw_input("Enter a value for blue(B): "))
	if blue < 0 or red > 255:
 		print invalid_msg
		return

	val = (red << 16) + (green << 8) + blue
	print "%s" % (hex(val[2:])).upper()

def hex_rgb():
	hex_val = raw_input("Enter a hexadecimal value: ")
                
	if len(hex_val) != 6:
			print invalid_msg
			return
	else:
			hex_val = int(hex_val, 16)
			# The 16 indicates to the int() function that hex_val is in base 16 (a hexadecimal number).
	two_hex_digits = 2**8
	blue = hex_val % two_hex_digits
	hex_val = hex_val >> 8
	green = hex_val % two_hex_digits
	hex_val = hex_val >> 8  
	red = hex_val % two_hex_digits
	print "Red: %s, Green: %s, Blue: %s" % (red, green, blue)
                
def convert():
                
	while True:
		option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
		if option == "1":
			print "ok, RGB to Hex..."
			rgb_hex()
		elif option == "2":
			print "ok, Hex to RGB..."
			hex_rgb()
		elif option == "X" or option == "x":
			break
		else:
			print "Error: Input not recognized"

convert()



