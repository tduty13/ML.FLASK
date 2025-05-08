import streamlit as st
import pickle
import sklearn
from sklearn.linear_model import LinearRegression
import numpy as np

model=pickle.load(open('lr_model.pkl','rb'))

st.title('Прогнозирование Tensile Elastic Modulus')

st.write('Это приложение позволяет предсказать <Модуль упругости композита при растяжении>')
st.write("Введите значения характеристики")
         
mat_F_rat=st.number_input('Matrix-Filler Ratio')
dens=st.number_input('Density')  
elast_mod=st.number_input('Elastic Modulus')
cur_ag_quan=st.number_input('Curing Agent Quantity')
ep_gr_con=st.number_input('Epoxy Groups Content')       
fl_po_temp=st.number_input('Flash Point Temperature')
res_cons=st.number_input('Resin Consumption')
l_step=st.number_input('Layup Step')
sur_dens=st.number_input('Surface Density') 
l_dens=st.number_input('Layup Density') 
layup_0=st.number_input('Layup_0') 
layup_90=st.number_input('Layup_90')

if st.button('Рассчитать модуль упругости при растяжении'):
    input_data=np.array([mat_F_rat, dens,elast_mod,cur_ag_quan,ep_gr_con,fl_po_temp,res_cons,l_step,sur_dens,l_dens,layup_0,layup_90]).reshape(1, -1)

    prediction=model.predict(input_data)[0]
    st.success(f'Прогнозируемый модуль упругости при растяжении: {prediction: .10f}')






