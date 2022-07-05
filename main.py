import operator
print("...Quotes...")
# creating var to storage data in a list
candits = list()
quotes = list()

# creating loop for iterating the input data and then storage at the lists
print("..Enter the name of the candidates and his respective quote.. ")
for i in range(5):

    input_candits = input("Enter the name of de candidate" + str(i + 1) + " : ")
    candits.append(input_candits)
    input_quotes = int(input("Enter the value of the quote" + str(i + 1) + " : "))
    quotes.append(input_quotes)

# creating another loop to identify the quotes of each candidate and storing in a dictionary
unique_code_id = dict()
for i in range(len(candits)):
    unique_code_id[candits[i]] = quotes[i]

# Control flow data to eliminate high and low cost of quotes
unique_code_id_v2 = unique_code_id.copy()  # copy of the main dictionary

max_val_candits = max(unique_code_id_v2.items(),
                      key=operator.itemgetter(1))[0]  # control flow of maximum values
min_val_candits = min(unique_code_id_v2.items(),
                      key=operator.itemgetter(1))[0]  # control flow of minimum values

[unique_code_id_v2.pop(key, None) for key in [max_val_candits, min_val_candits]]  # deleting the max and min value

# Average for the rest of valid quotes with a simple for loop and operators
avg = 0
for i in unique_code_id_v2.values():
    avg += i

# print(int(avg/3))

# out-put data to visualize average and deleted quotes
print("Dictionary with keys and values", unique_code_id)
print("Dictionary with deleted maximum and minimum values", unique_code_id_v2)

print("..Deleted Quotes..")
print("Maximum value: ", max_val_candits)
# print(max_val_candits)
print("Minimum value: ", min_val_candits)
# print(min_val_candits)

print("..Average for the valid quotes..")
print(int(avg / 3))

# Cambio para github