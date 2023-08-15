import math 
import pandas as pd
import sys

def LOG(a):
    if(a==0):
        return 0
    return math.log2(a)

def Entropy_initial(df):
    Label=df.keys()[-1]
    Labels=df[Label].unique()
    yes=0
    no=0

    for i in range(len(df)):
        if(df.iat[i,len(df.columns)-1]=="yes"):
            yes+=1
        else:
            no+=1
    
    entropy=0
    entropy+=-(yes/(yes+no)*LOG(yes/yes+no) + no/(yes+no)*LOG(no/yes+no))

    return entropy

def Entropy(df,attribute,atb):
    columns=list(df.columns)
    col=0
    for i in range(len(columns)):
        if(columns[i]==attribute):
            col=i
            break
    
    counter=0
    yes=0
    no=0
    for i in range(len(df)):
        if(df.iat[i,col]==atb):
            counter+=1
            if(df.iat[i,len(columns)-1]=="yes"):
                yes+=1
            elif(df.iat[i,len(columns)-1]=="no"):
                no+=1

    entropy=0
    entropy+=-(yes/(yes+no)*LOG(yes/yes+no) + no/(yes+no)*LOG(no/yes+no))
    return entropy

def Gain(attb,entropy_attb,parent_entropy):  #Return gain of all the attributes 
    gain={}
    for i in entropy_attb:
        gain[attb]=(parent_entropy-entropy_attb)
    return gain
    # return [max(gain, key=gain.get),gain]



def buildTree(df,parent):
    # num=0
    atbts=list(df.columns)
    columns=list(df.columns)

    
    ListOfEntropys=[]
    parentEntropy=Entropy_initial(df)
    for j in range(len(atbts)-1):
        # x=list(set(df.iloc[:,j]))
        unique_value=list(df[columns[j]].unique())
        entpy={}
        for i in range(len(unique_value)):
            entpy[unique_value[i]]=Entropy(df,unique_value[i],j)
        ListOfEntropys.append(entpy)
    # x=Gain(ListOfEntropys,parentEntropy)
    gain_list=Gain(ListOfEntropys,parentEntropy)
    # root=atbts[x[1]]
    root=max(gain_list, key=gain_list.get) #get the max attribute with max gain from list
    print(root)
    p=ListOfEntropys[x[1]].keys()
    for value in p:
        if ListOfEntropys[x[1]][value][0]==0:

            print("the edge is from ",root," to ",end="")
            

            # print("the edge is from ",root," to ",end="")
            for j in range(len(df)):
                if (df.iloc[j,atbts.index(root)]==value):
                    # print(df.iloc[atbts.index(root),len(atbts)-1],value)
                    print(df.iloc[j,len(atbts)-1]," with name ",value)
                    break
            # pass
        elif len(atbts)==2:
            print("the edge is from ",root," to ",end="")
            yes=0
            no=0
            for j in range(len(df)):
                if (df.iloc[j,atbts.index(root)]==value):
                    if df.iloc[j,len(atbts)-1]=="yes":
                        yes=yes+1
                    else:
                        no=no+1
            # print("no(",no/(no+yes), ") with name ",value)
            if(no>yes):
                print("no with name ",value)
            else:
                print("yes with name ",value)
            # break
        else:
            # print("the edge name is ",value)
            # print("the edge is from ",root," to ",num+1," with name ",value)
            print("the edge  name is ",value," that is from ",root," to",end=" ")
            # print(df.iloc[j,len(atbts)-1]," with name ",value)
            # print("statring to get data from ",value)# value is edge name
            df_s=df.copy()
            data=df_s[df_s[root]==value]
            data=data.drop(root, axis='columns')
            # print(data)
            # print("starting id")
            buildTree(data)






f=open(sys.argv[1])
df = pd.read_csv(sys.argv[1], sep="\t")
print (df)
# buildTree(df) 
