
principle_amount=int(input  ( "Enter the amount that  you are ready to invest:  "))

interest_rate=int(input ('\nEnter intrest rate per mount: '))

time=int(input("\nEnter the time duration in years: "))

month= time*12
interst= interest_rate/100


while month >=1:

    intrest = principle_amount*interst
    Return=intrest+principle_amount
    print(Return)
    principle_amount = Return
    month=month-1
