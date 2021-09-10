# Step 1 receive user input and remove spaces from each element in string
string1 = input().split(' ')

# Step 2 create a new variable to change data type to set where no duplicates are allowed
set1 = set(string1)

# Step 3 if string length is greater than set1 length, there was at least a duplicate, and return no, else return yes.
if len(string1) > len(set1):
    answer = 'no'
else:
    answer = 'yes'
print(answer)
