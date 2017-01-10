num = raw_input("enter a number to get its divisor:")
con_num = int(num)
new_list = []
range = list(range(1,con_num+1))
print "the divisors of",con_num,"is:"
for number in range:
 if con_num%number==0:
  new_list.append(number)
print new_list
