#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st


def prediction(x):
    y = ""
    if(len(x) == 17):
        y = x
    else:
        y = "Chassis no is not valid"
    return y 





def main(): 
      # giving the webpage a title 
    st.title("VIN") 
      
    # here we define some of the front end elements of the web page like  
    # the font and background color, the padding and the text to be displayed 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Chassis Number Validation </h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction 
    x = st.text_input("VIN", "Type Here")
    result ="" 
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    if st.button("Validate"): 
        result = prediction(x) 
    st.success('The output is {}'.format(result)) 
     
if __name__=='__main__': 
    main() 


# In[ ]:




