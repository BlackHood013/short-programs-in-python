str = raw_input("enter a string to see whether it is pallingdrom or not:")
lst = list(str)
rev_str = lst[::-1]
if lst==rev_str:
 print "yes,this is a pallingdrom"
else:
 print "no,this is not a pallingdrom"
