one_to_eighteen = list(range(1,19)) # List of number from 1 to 18
squared_one_to_eighteen = [square ** 2 for square in one_to_eighteen] #square of each element in the list from 1 to 18
squared_two_to_eighteen = squared_one_to_eighteen[1:] #Index 1 to the last index in the last
squared_three_to_six = squared_one_to_eighteen[2:6] #Index 2 to index 6


#sum all elements in the list of squared_one_to_eighteen
sum = 0
for num in squared_one_to_eighteen:
    sum += num
    sum_squared_one_to_eighteen = sum
#print(sum_squared_one_to_eighteen)


#sum all elements in the list of squared_two_to_eighteen
total = 0
for i in squared_two_to_eighteen:
    total += i
    sum_squared_two_to_eighteen = total
#print(sum_squared_two_to_eighteen)


#sum all elements in the list of squared_three_to_six
total_sum = 0
for j in squared_three_to_six:
    total_sum += j
    sum_squared_three_to_six = total_sum
#print(sum_squared_three_to_six)

year_2022 = sum_squared_two_to_eighteen - sum_squared_three_to_six
year_2023 = sum_squared_one_to_eighteen - sum_squared_three_to_six

print('Three days to the end of', year_2022)
print('Three days to',year_2023)


