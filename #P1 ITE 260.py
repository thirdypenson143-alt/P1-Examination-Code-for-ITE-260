#P1 ITE 260
#Customer Information
print("=====================================================")
name = str(input("Customer Name: "))
contact_no = str(input("Contact No.: "))
address = str(input("Address: "))
print("-----------------------------------------------------")
#First Product
product_1 = str(input("Product: "))
price_1 = float(input("Price: "))
quantity_1 = int(input("Quantity: "))
print("-----------------------------------------------------")
#Second Product
product_2 = str(input("Product: "))
price_2 = float(input("Price: "))
quantity_2 = int(input("Quantity: "))
print("-----------------------------------------------------")
#Third Product
product_3 = str(input("Product: "))
price_3 = float(input("Price: "))
quantity_3 = int(input("Quantity: "))
print("-----------------------------------------------------")
#Discounts
discount_1 = float(input("10% Discount: "))
discount_2 = float(input("10% Discount: "))
discount_3 = float(input("10% Discount: "))
print("-----------------------------------------------------")
#Subtotal and Total Calculation
subtotal_1 = price_1 * quantity_1
subtotal_2 = price_2 * quantity_2
subtotal_3 = price_3 * quantity_3
total_1 = subtotal_1 - discount_1
total_2 = subtotal_2 - discount_2
total_3 = subtotal_3 - discount_3
amount = price_1 * quantity_1
subtotal = total_1 + total_2 + total_3
discount = subtotal + discount_1 + discount_2 + discount_3
total_discount = subtotal - discount
#Receipt
print("====================================================")
print("                THIRDY'S Store                      ")
print("====================================================")
print("----------------------------------------------------")
print("  PRODUCT  ")
print("----------------------------------------------------")
print(":",product_1)
print(":",product_2)
print(":",product_3)
print("----------------------------------------------------")
print("   PRICE  ")
print("----------------------------------------------------")
print(": ",subtotal_1)
print(": ",subtotal_2)
print(": ",subtotal_3)
print("----------------------------------------------------")
print("  QUANTITY  ")
print("----------------------------------------------------")
print(":   ",quantity_1)
print(":   ",quantity_2)
print(":   ",quantity_3)
print("-----------------------------------------------------")
print("discount: ",total_discount)
print("                                    =================")
print("                                    total: ",total_1 + total_2 + total_3)
print("=====================================================")
print("         Thank you for your purchase          ")
print("             Please come again!               ")
print("=====================================================")