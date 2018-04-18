n= int(input("nhap N="))
dem = 0
for i in range(1,n+1):
	print i
	if (i%2 == 0):
		dem = dem+i
print "tong =", dem
