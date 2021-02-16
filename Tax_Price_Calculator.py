#Filename: Tax_Price_Calculator.py
#Author: Valay Shah
#Date Created: April 4, 2012
#Description: This program asks for a price, calculates the price with tax
#and outputs the result.

#Output: Header Information

print ("Filename: Tax_Price_Calculator.py")
print ("Author: Valay Shah")
print ("Date Created: April 4, 2012")
print ("""Description: This program asks for a price, calculates the price with tax
and outputs the result.""")

# ----- Definitions: Variables, Constants, and Functions -----
# Defintions: Variables, Constants, and Functions

#Variables: orignalPrice, totalPrice

#Constants: TAX_RATE
TAX_RATE = 0.14

#Function: calculateTaxedPrice(price)
#function calculateTaxedPrice (price:float):float takes the price and returns 
#the total price with tax
def calculateTaxedPrice(price):
    total=price+(price*TAX_RATE)
    return total
#end of calculateTaxPrice(price)
# ----- end of Definitions -----

#Input
orignalPrice = input("Enter a price: $")

#Processing
totalPrice = calculateTaxedPrice(orignalPrice)

#Output
print ("The total price for the $%4.2f item with tax is $%4.2f." %(orignalPrice,totalPrice))
