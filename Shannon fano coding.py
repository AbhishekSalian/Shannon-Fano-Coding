#!/usr/bin/env python
# coding: utf-8

# # SHANNON FANO CODING

# In[1]:


string=input("Enter the string:")


# The quick brown fox jumps over the lazy dog.

# # Probability Calculation of Symbols:-

# In[2]:


from collections import Counter
def symProb(String):
    sc=dict(Counter(String.upper()));
    return {k: v / sum(sc.values()) for k, v in sc.items()}
symd=symProb(string) #symd-symbols Dictionary


# In[3]:


import matplotlib.pyplot as plt 
plt.style.use('ggplot')
plt.figure(figsize=(15,5))
plt.bar(symd.keys(),symd.values(), width=0.6, align='center',color='b')
plt.xlabel("Symbols")
plt.ylabel("Probability")
plt.title("unordered probabilties")
plt.show()


# # Sorting

# In[4]:


from collections import OrderedDict
symdn = OrderedDict(sorted(symd.items(), key=lambda kv:kv[1], reverse=True))
plt.figure(figsize=(15,5))
plt.bar(symdn.keys(),symdn.values(), width=0.6, align='center',color='b')
plt.xlabel("Symbols")
plt.ylabel("Probability")
plt.title("Ordered probabilties")
plt.show()


# In[16]:


# separating keys and values of ordered dictionary
sk=list(symdn.keys())
sv=list(symdn.values())


# # Partition and recursive looping

# In[6]:


def best_partition(initial,final):
    pts=[]  #points
    for i in range(initial+1,final):
        diff=abs(sum(sv[initial:i])-sum(sv[i:final]))
        pts.append((diff))
        #print(abs(sum(sv[initial:i])-sum(sv[i:final])),sv[initial:i],sv[i:final],i)
        #print("\n",[sum(sv[initial:i]),sum(sv[i:final])],"\n")
    print(pts.index(min(pts))+initial)
    plt.plot([*range(initial,final-1)],pts,color="r")
    plt.scatter([*range(initial,final-1)],pts,color="k")     
    plt.scatter(initial+pts.index(min(pts)),min(pts),color='b',label="lowest point")
    plt.xlabel("Index")
    plt.ylabel("Probability")
    plt.legend() 
    plt.show()
    if pts.index(min(pts))<initial : return pts.index(min(pts))+initial; 
    else: return pts.index(min(pts))


# In[7]:


def up(initial,final):
    for i in range(initial,final) : sc[i]=sc[i]+'0'
def down(initial,final):
    for i in range(initial,final) : sc[i]=sc[i]+'1'


# In[8]:


initial=0
final=len(sv)
sc=['']*(len(sv))
current_index=[(initial,final)]
new_index=[]
stage=1
while current_index!=[]:
    print("---","stage:-",stage,"----");print(sc);new_index=[];print(current_index)
    for index in current_index:
            if (index[1]-index[0])==2: sc[index[0]]=sc[index[0]]+'0'; sc[index[1]-1]=sc[index[1]-1]+'1';
                
            if (index[1]-index[0])>2:
                index_ptr=best_partition(index[0],index[1])+1;
                new_index.append((index[0],index_ptr));up(index[0],index_ptr);
                new_index.append((index_ptr,index[1]));down(index_ptr,index[1]);
            current_index=new_index
    print("\n") 
    stage=stage+1
# for last stage 
if current_index==[]:
    print("---","stage:-",stage,"----");print(sc);new_index=[];print(current_index)


# In[9]:


dummy=[]
for i in range(0,len(sv)):dummy.append((sk[i],sc[i]));
encoded_dictionary=OrderedDict(dummy)    


# In[10]:


import pandas as pd
data={'Symbol':sk,'probability':sv,'codeword':sc,}
df=pd.DataFrame(data)
df.head(len(sk))


# # Encoded Message

# In[11]:


encoded_message=''.join(sc)
print("For message:-",string,"\nEncoded message is:-",encoded_message)


# # Entropy Calculation:-

# In[12]:


import math
H=0
for i in range(0,len(sv)):H=H+sv[i]*math.log((1/sv[i]),2);
print("Entropy is:-",H,"bits/message")


# # Average Codeword Length

# In[13]:


L=0
for i in range(0,len(sc)):L=L+len(sc[i])*sv[i];
print("Average Codeword length is:-",L,"bits/message")


# # Compression

# In[14]:


print("Coding efficiency is :-",(H/L)*100)


# In[ ]:





# In[ ]:




