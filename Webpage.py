#!/usr/bin/env python
# coding: utf-8

# In[105]:


import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st


def AshokLeyland(x):
    df = pd.DataFrame({
        'Jan':['A','B','C','D','E','F','G','H','J','K','L','M','N','P','R','S','T','V'],
        'Feb':['Y','A','B','C','D','E','F','G','H','J','K','L','M','N','P','R','S','T'],
        'Mar':['X','Y','A','B','C','D','E','F','G','H','J','K','L','M','N','P','R','S'],
        'Apr':['W','X','Y','A','B','C','D','E','F','G','H','J','K','L','M','N','P','R'],
        'May':['V','W','X','Y','A','B','C','D','E','F','G','H','J','K','L','M','N','P'],
        'Jun':['T','V','W','X','Y','A','B','C','D','E','F','G','H','J','K','L','M','N'],
        'Jul':['S','T','V','W','X','Y','A','B','C','D','E','F','G','H','J','K','L','M'],
        'Aug':['R','S','T','V','W','X','Y','A','B','C','D','E','F','G','H','J','K','L'],
        'Sep':['P','R','S','T','V','W','X','Y','A','B','C','D','E','F','G','H','J','K'],
        'Oct':['N','P','R','S','T','V','W','X','Y','A','B','C','D','E','F','G','H','J'],
        'Nov':['M','N','P','R','S','T','V','W','X','Y','A','B','C','D','E','F','G','H'],
        'Dec':['L','M','N','P','R','S','T','V','W','X','Y','A','B','C','D','E','F','G']
    }).set_index([pd.Index([str(2011 + i) for i in range(18)])])

    temp = [str(2011 + i) for i in range(20)]
    temp1 = ["B","C","D","E","F","G","H","J","K","L","M","N","P","R","S","T","V","W","X","Y"]
    year_dict = dict()
    for i in range(len(temp)):
        year_dict[temp1[i]] = temp[i]

    a = df.loc[year_dict[x[9]],]

    temp = list(a.index)
    temp1= list(a)
    temp2 = dict()
    for i in range(len(temp)):
        temp2[temp1[i]] = temp[i] 

        
    return([year_dict[x[9]],temp2[x[11]]])


def TataMotors(x):
    month_dict = {"A":"Jan",
                  "B":"Feb",
                  "C":"Mar",
                  "D":"Apr",
                  "E":"May",
                  "F":"Jun",
                  "G":"Jul",
                  "H":"Aug",
                  "J":"Sep",
                  "K":"Oct",
                  "N":"Nov",
                  "P":"Dec"}
    temp = [str(2011 + i) for i in range(24)]
    temp1 = ["B","C","D","E","F","G","H","J","K","L","M","N","P","R","S","T","V","W","X","Y","1","2","3","4"]
    year_dict = dict()
    for i in range(len(temp)):
        year_dict[temp1[i]] = temp[i]
    
    return([year_dict[x[9]],month_dict[x[11]]])


def Validate(x):
    y = ""
    if(x[0:3] == 'MAT' and len(x) == 16):
        res = TataMotors(x)
        y = {"Manufacturer":"Tata Motors","Year" : res[0],"Month":res[1]}
    elif(x[0:2] == 'MB' and len(x) == 17):
        res = AshokLeyland(x)
        y = {"Manufacturer":"Ashok Leyland","Year" : res[0],"Month":res[1]}
    
    else:
        y = "Chassis no is not valid"
    return y 

#x = "MAT491125FJC0189"
#x = "MB1AA22E9FRD95267"
#Validate(x)



def main(): 
      # giving the webpage a title   
    # here we define some of the front end elements of the web page like  
    # the font and background color, the padding and the text to be displayed 
    html_temp = """ 
    <h1 style ="color:black;text-align:center;">Chassis Number Validation </h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction 
    x = st.text_input("VIN", "")
    result ="" 
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    if st.button("Validate"): 
        result = Validate(x) 
    st.success('The output is {}'.format(result)) 
     
if __name__=='__main__': 
    main() 


# In[ ]:




