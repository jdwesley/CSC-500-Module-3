#Define food total as an input string 
#Define calculation total
#convert input string to an integer 
#print calculation total

resturaunt_bill_before_tax = input('Food total: $')
resturaunt_bill_total = int(resturaunt_bill_before_tax) * 1.18 * 1.07
print('$' + str(resturaunt_bill_total))

#Define current time as a input string
#Define calculation total
#convert input sting to an integer
#print calculation total

currenttime = input('Current time on a 24hr clock: ')
time50hrslater = int(currenttime) + 2
print(str(time50hrslater) + ':00')
