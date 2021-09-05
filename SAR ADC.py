Vin=float(input("Enter the input voltage: "))        #Taking the value of Input voltage
Vref=15                                            #Assuming reference voltage to be 15volts
N=8                                                #Number of bits in SAR ADC convertor
s=Vref/(2**N-1)                                    #Calculating Step size
def dec(n):                                        #Defining a fuction to return decimal value from binary
    S=0                                            #Sets intial value of S and i to zero
    i=0
    while(n!=0):                                   #The loops runs till k is not equal to zero
        r=n%10                                     #Takes remainder by dividing k by 10
        S=S+r*(2**i)                               #Increases value of S accordingly
        n=n//10                                    #Loop to reduce value of k
        i=i+1
    return S                                       #returns final value
k=0                                                 #Initial value of k=0
for m in range(N):                                  #A loop to convert input voltage to binary value using SAR ADC principles
    k=k+10**(N-1-m)                                 #Assigning most significant bit 1
    V_DAC=dec(k)*s                                 #Finding value of V_DAC by using step size
    if V_DAC>Vin:                                  #Comparing with Vin
     k=k-10**(N-1-m)                               #If Vin is less than V_DAC then setting that significant bit to 0
r=len(str(k))                                      #Taking the length of output k
D= str(k)                                          # D is value as standard output to ensure printing of preceeding zeroes
Q=Vin-s*dec(k)                                     # Calculating quantization error
Q="{:.3f}".format(Q)                               #Printing value of Q upto 3 decimals
print('Digital Equivalent:',D)                    
print('Quantization Error:',Q)
#APPROACH:-
"""I assumed the value of k to be zero initially(LINE 14).Then I set the most significant bit to 1 as done in SAR ADC conversion(LINE 16).
Then the function returns value in decimal which is the DAC voltage.It compares the V_DAC to Vin.If value is less it sets that significant bit to zero(LINE 19).
The loop repeates above function for 8 times as it is a 8 bit convetor"""