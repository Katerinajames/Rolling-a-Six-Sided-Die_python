import random
frequency1 = 0; # maintains count of 1s rolled
frequency2 = 0; #count of 2s rolled
frequency3 = 0; # count of 3s rolled
frequency4 = 0; #count of 4s rolled
frequency5 = 0; # count of 5s rolled
frequency6 = 0; # count of 6s rolled
print("------------------------------------------")

for roll in range (1,600000):
 face =random.randint( 1, 6 )
 if face==1:
    	  frequency1=frequency1+1
 elif face==2:
	  frequency2=frequency2+1	 
 elif face==3:
	  frequency3=frequency3+1
 elif face==4:
	  frequency4=frequency4+1  
 elif face==5:
	  frequency5=frequency5+1
 elif face==6:
	  frequency6=frequency6+1

print("1\t%d\n2\t%d\n3\t%d\n4\t%d\n5\t%d\n6\t%d\n"%(frequency1, frequency2, frequency3, frequency4, frequency5, frequency6)) 


