slices = party_pizza_mini + large + medium
print("Total number of slices: {slices}")

people  += 1
share = slices // people
leftover = slices % people
print("Each person gets: {share}")
print("Leftover slices: {leftover}")

people += 2
share = slices // people
leftover = slices % people
print ("Each person gets : {share}")
print ("Leftover slices: {leftover}")



slices += 14
share = slices // people
leftover = slices % people
print("Each person gets: {share}")
print("Leftover slices: {leftover}")
print("...for Mr. Hollow Leg")
