import streamlit as st
import pandas as pd 

tabla = {
    "fiuk":[1,2,3,4,5],
    "lányok":[5,6,7,8,9]
}

bum = pd.DataFrame(tabla)

st.write(bum)

