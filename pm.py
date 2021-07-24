# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import numpy as np
import pandas as pd
pd.get_option("display.max_columns")
pd.set_option('display.max_columns', 1000)
pd.get_option("display.max_rows")
pd.set_option('display.max_rows', 1000)

f=open('aaindex1.dat', 'r')
pm=open('pm.fas','r')

fragI=0
raw=''
ID=''
ID_array=[]
AAall=[[]]

while True:
    data = f.readline()
    data = data.rstrip()
    if data.startswith('I'):
        fragI = 1
    elif data.startswith('H'):
        ID=data[2:]
    elif fragI==1 and not data.startswith('//'):
        raw+=data
    elif data.startswith('//'):
        para = raw.split()
        AAall.append(para)
        ID_array.append(ID)
        raw=''
        fragI=0
    elif data == '':
        break

AAall.remove([])

columns=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']

df_index=pd.DataFrame(AAall,index=ID_array,columns=columns)

#df_index


# +
pm=open('pm.fas','r')

fas = [[]]

abc = 1

while True:
    reading = pm.readline()
    reading = reading.rstrip()

    if not reading.startswith('>'):
        if reading == '':
            break
        fas.append(list(reading))

fas.remove([])
columns=list(range(-15,26))
df_pm=pd.DataFrame(fas,columns=columns)

df_pm

# +
ALLave=[[]]


k=0
while k<len(df_index.index):
    l=0
    value=[]
    NAcount=0
    NAelse_sum=0
    NAvalue=0
    while l<len(df_index.columns):
        if df_index.iat[k,l]=="NA":
            NAcount=NAcount+1
            value.append('NA')
        else:
            NAelse_sum=NAelse_sum+float(df_index.iat[k,l])
            value.append(float(df_index.iat[k,l]))
        l=l+1
        
    NAvalue=NAelse_sum/(20-NAcount)
    
    while l<len(df_index.columns):
        if df_index.iat[k,l]=="NA":
            value[l]=float(NAvalue)
        l=l+1
    
    
    j=0
    AAnum=[[]]
    while j<len(df_pm.index):
        i=0
        AA=[]
        while i<=40:
            AA.append(df_pm.iat[j,i])
            if AA[i]=="A":
                AA[i]=value[0]
            elif AA[i]=="R":
                AA[i]=value[1]
            elif AA[i]=="N":
                AA[i]=value[2]
            elif AA[i]=="D":
                AA[i]=value[3]
            elif AA[i]=="C":
                AA[i]=value[4]
            elif AA[i]=="Q":
                AA[i]=value[5]
            elif AA[i]=="E":
                AA[i]=value[6]
            elif AA[i]=="G":
                AA[i]=value[7]
            elif AA[i]=="H":
                AA[i]=value[8]
            elif AA[i]=="I":
                AA[i]=value[9]
            elif AA[i]=="L":
                AA[i]=value[10]
            elif AA[i]=="K":
                AA[i]=value[11]
            elif AA[i]=="M":
                AA[i]=value[12]
            elif AA[i]=="F":
                AA[i]=value[13]
            elif AA[i]=="P":
                AA[i]=value[14]
            elif AA[i]=="S":
                AA[i]=value[15]
            elif AA[i]=="T":
                AA[i]=value[16]
            elif AA[i]=="W":
                AA[i]=value[17]
            elif AA[i]=="Y":
                AA[i]=value[18]
            elif AA[i]=="V":
                AA[i]=value[19]
            elif AA[i]=="X":

                AA[i]=NAvalue

            i=i+1
        AAnum.append(AA)
        j=j+1
    df_AAnum=pd.DataFrame(AAnum)
    #print (df_AAnum)

    ave=df_AAnum.mean()
    ALLave.append(ave)

    k=k+1

#print ('fin!')

# +

columns=list(range(-15,26))
ID_array.insert(0,'0')
pmave=pd.DataFrame(ALLave,index=ID_array,columns=columns)

pmave


# +
npm=open('nonpm.fas','r')

fas = [[]]

while True:
    reading = npm.readline()
    reading = reading.rstrip()

    if not reading.startswith('>'):
        if reading == '':
            break
        fas.append(list(reading))

fas.remove([])
columns=list(range(-15,26))
df_npm=pd.DataFrame(fas,columns=columns)

df_npm

# +
ALLave=[[]]


k=0
while k<len(df_index.index):
    l=0
    value=[]
    NAcount=0
    NAelse_sum=0
    NAvalue=0
    while l<len(df_index.columns):
        if df_index.iat[k,l]=="NA":
            NAcount=NAcount+1
            value.append('NA')
        else:
            NAelse_sum=NAelse_sum+float(df_index.iat[k,l])
            value.append(float(df_index.iat[k,l]))
        l=l+1

    
    NAvalue=NAelse_sum/(20-NAcount)
    
    while l<len(df_index.columns):
        if df_index.iat[k,l]=="NA":
            value[l]=float(NAvalue)
        l=l+1
    
    j=0
    AAnum=[[]]
    while j<len(df_npm.index):
        i=0
        AA=[]
        while i<=40:
            AA.append(df_npm.iat[j,i])
            if AA[i]=="A":
                AA[i]=value[0]
            elif AA[i]=="R":
                AA[i]=value[1]
            elif AA[i]=="N":
                AA[i]=value[2]
            elif AA[i]=="D":
                AA[i]=value[3]
            elif AA[i]=="C":
                AA[i]=value[4]
            elif AA[i]=="Q":
                AA[i]=value[5]
            elif AA[i]=="E":
                AA[i]=value[6]
            elif AA[i]=="G":
                AA[i]=value[7]
            elif AA[i]=="H":
                AA[i]=value[8]
            elif AA[i]=="I":
                AA[i]=value[9]
            elif AA[i]=="L":
                AA[i]=value[10]
            elif AA[i]=="K":
                AA[i]=value[11]
            elif AA[i]=="M":
                AA[i]=value[12]
            elif AA[i]=="F":
                AA[i]=value[13]
            elif AA[i]=="P":
                AA[i]=value[14]
            elif AA[i]=="S":
                AA[i]=value[15]
            elif AA[i]=="T":
                AA[i]=value[16]
            elif AA[i]=="W":
                AA[i]=value[17]
            elif AA[i]=="Y":
                AA[i]=value[18]
            elif AA[i]=="V":
                AA[i]=value[19]
            elif AA[i]=="X":
                AA[i]=NAvalue

            i=i+1
        AAnum.append(AA)
        j=j+1
    df_AAnum=pd.DataFrame(AAnum)
    #print (df_AAnum)

    ave=df_AAnum.mean()
    ALLave.append(ave)

    k=k+1

#print ('fin!')

# +

columns=list(range(-15,26))
npmave=pd.DataFrame(ALLave,index=ID_array,columns=columns)

npmave


# +
import matplotlib.pyplot as plt


for index_pm, row_pm in pmave.iterrows():
    for index_npm, row_npm in npmave.iterrows():
        if index_pm==index_npm:
            print (index_pm)
            plt.figure(figsize=(12,6))
            plt.plot(columns , row_pm  , color = 'red'  , marker = 'o' )
            plt.plot(columns , row_npm , color = 'blue' , marker = 'v' )
            plt.xlabel('amino acid')
            plt.ylabel('value')
            plt.show()
                
