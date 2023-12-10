print ("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give?\n"))
ppl = int(input("How many people are splitting this bill?\n"))
atip = (tip / 100) + 1

total = (bill * atip)

amt_per_persn = total/ppl

print("Your total bill comes to " + str(total))

print(f"Each person in your group will pay {amt_per_persn}")
