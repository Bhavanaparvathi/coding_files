#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# # tipsp

# In[3]:


x=np.genfromtxt(r"C:\Users\97158\Downloads\tipsf.csv",delimiter=",",skip_header=1)


# In[4]:


x


# #### 1.what is the total bill value

# In[29]:


print(f"The total bill value is :  {sum(x[::,1])}")


# In[32]:


np.sum(x[:,1])


# #### 2. What is the total tip value

# In[35]:


print(f"total tip value is : {np.sum(x[::,2])}")


# #### 3. Count how many sundays,saturdays,thursdays and fridays are there

# In[37]:


z=np.unique(x[:,5],return_counts=True)
a,b=z
j=0
for i in a:
    if(i==0):
        print("sunday are = ",b[j])
        j+=1
    elif(i==1):
        print("saturday are = ",b[j])
        j+=1
    elif(i==2):
        print("thursday are = ",b[j])
        j+=1
    elif(i==3):
        print("friday are = ",b[j])
        j+=1   


# #### 4. How many smokers are there

# In[39]:


print(f"The total number of smokers are :  {np.sum(x[:,4])} ")


# #### 5. What is an average tip given by male and female

# In[9]:


a=np.sum(x[:,2].take(np.where(x[:,3]==0)))
b=np.sum(x[:,2].take(np.where(x[:,3]==1)))


# #### 6. How much amount spent by female and male

# In[8]:


print(f"The total amount spent by females are :  {sum(x[x[:,3] == 0][:,1])}")
print(f"The total amount spent by males are :  {sum(x[x[:,3] == 1][:,1])}")


# #### 7. What is the min and max tip given

# In[10]:


max_tip=np.max(x[:,2])
min_tip=np.min(x[:,2])
print("maximum tip is ",max_tip)
print("minimum tip is ",min_tip)


# #### 8. How many males and females are going for lunch and dinner

# In[12]:


print(f"The number of 'Females' going for dinner are :  {np.unique(x[x[:,3] ==0,6],return_counts = True)[1][0]}")
print(f"The number of 'Females' going for lunch are :  {np.unique(x[x[:,3] ==0,6],return_counts = True)[1][1]}")
print(f"The number of 'Males' going for dinner are :  {np.unique(x[x[:,3] ==1,6],return_counts = True)[1][0]}")
print(f"The number of 'Males' going for lunch are :  {np.unique(x[x[:,3] ==1,6],return_counts = True)[1][1]}")


# #### 9. Find out average size

# In[18]:


avg=np.sum(x[:,7])/np.sum(b)
print("average of size = ",np.round(avg))


# #### 10. How many female smokers are there and how many male smokers are there

# In[5]:


z=np.unique(x[:,3].take(np.where((x[:,4]==1))),return_counts=True)
a,b=z
print(f"The total number of smokers : {sum(x[:,4])}")
for i in a:
    if(i==0):
        print("female smokers are : ",b[0])
    else:
        print("male smokers are : ",b[1])


# # train_extended

# In[4]:


a=np.genfromtxt(r"C:\Users\97158\Downloads\train_extended.csv",delimiter=",",skip_header=1)


# In[5]:


a


# #### 1. What is the max and min length

# In[8]:


print(f"The max lenght is :  {max(a[:,0])}")
print(f"The min lenght is :  {min(a[:,0])}")


# #### 2. Difference between max and min length

# In[6]:


max(a[:,0]) - min(a[:,0])


# #### 3. Find column wise avg

# In[7]:


np.mean(a,axis = 0)


# #### 4. Find all the age whose age is greater than 0.4

# In[9]:


a[a[:,2]>0.4,7]


# #### 5. What is the avg weight and height of a person whose age is 10

# In[10]:


print(f"The average height of the persons whose age is 10 is :  {np.mean(a[a[:,7] == 10,2])}")
print(f"The average weight of the persons whose age is 10 is :  {np.mean(a[a[:,7] == 10,3])}")


# #### 6. What is the total shell weight

# In[11]:


np.round(np.sum(a[:,6]))


# #### 7. how many persons belongs to each and every unique age
# 

# In[12]:


np.unique(a[:,7],return_counts=True)


# #### 8 . what is the difference between shucked weight and viscera weight

# In[13]:


z=np.sum(a[:,4])
x=np.sum(a[:,5])
print("the difference between shucked weight and viscera weight is ",np.round(z-x))


# #### 9. What is the avg height of a person whose age is between 14 and 19

# In[16]:


np.mean((a[:,7]>=14) & (a[:,7]<=19))


# #### 10. what is the avg weight if we include shucked weight, Viscera weight and shell weight

# In[20]:


np.mean(a[:,4] + a[:,5] + a[:,6])


# In[ ]:




