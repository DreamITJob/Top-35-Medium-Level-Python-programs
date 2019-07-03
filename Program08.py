#Python program for calculating simple interest...

principle = int(input("Enter principle value: "))
rate = float(input("Enter rate of interest per year: "))
year = float(input("Enter no of year: "))

simple_interest = principle*rate*year/100
print("Simple interest is Rs.", simple_interest)
