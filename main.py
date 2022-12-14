import streamlit as st
import pandas as pd
import base64

st.title('πν‘λ¨λ³΄λ λΆλ² μ°νμ  νμ§')

col1, col2 = st.columns(2)


"""### μ€μκ° μμ"""
file_ = open("f3.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

"""### λΆμ κ²°κ³Ό"""
file_ = open("o3.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)



data_2021 = {'μ¬κ³ κ±΄μ': [140,126,189,201,217,200,177,168,191,216,222,179],
        'μ¬λ§μμ': [4,1,3,2,2,1,0,1,2,2,2,1,],
        'λΆμμμ': [141,131,196,211,230,210,188,177,199,223,238,187]}

data_2020 = {'μ¬κ³ κ±΄μ': [170,150,138,143,163,190,187,144,168,231,191,140],
        'μ¬λ§μμ': [3,1,2,0,4,0,2,2,1,5,5,1],
        'λΆμμμ': [177,156,142,150,178,204,190,150,175,237,191,146]}

data_2019 = {'μ¬κ³ κ±΄μ': [175,161,200,195,212,185,199,181,203,208,224,192],
        'μ¬λ§μμ': [2,1,5,2,0,3,3,4,4,2,6,5],
        'λΆμμμ': [184,178,207,211,225,188,214,188,214,219,238,201]}

data_2018 = {'μ¬κ³ κ±΄μ': [177,172,202,197,174,183,182,150,170,195,209,183],
        'μ¬λ§μμ': [5,3,6,1,0,3,2,7,4,5,2,3],
        'λΆμμμ': [182,186,207,204,195,193,193,156,200,206,214,194]}

data_2017 = {'μ¬κ³ κ±΄μ': [98,71,111,102,118,120,86,167,205,171,212,160],
        'μ¬λ§μμ': [2,1,2,1,3,5,1,3,7,2,6,3],
        'λΆμμμ': [101,79,119,114,129,125,94,174,214,182,223,166]}

index_name = ['1μ','2μ','3μ','4μ','5μ','6μ','7μ','8μ','9μ','10μ','11μ','12μ']

df_2021 = pd.DataFrame(data_2021, index = index_name)
df_2020 = pd.DataFrame(data_2020, index = index_name)
df_2019 = pd.DataFrame(data_2019, index = index_name)
df_2018 = pd.DataFrame(data_2018, index = index_name)
df_2017 = pd.DataFrame(data_2017, index = index_name)

st.subheader('')

st.subheader('πμ¬κ³ νν©')
option = st.selectbox(
    'πμ°λ',
    (['2021', '2020', '2019', '2018', '2017']))


if option == '2021':
    st.table(df_2021)
if option == '2020':
    st.table(df_2020)
if option == '2019':
    st.table(df_2019)
if option == '2018':
    st.table(df_2018)
if option == '2017':
    st.table(df_2017)


col3, col4 = st.columns(2)

with col3:
    if option == '2021':
        st.line_chart(df_2021)
    if option == '2020':
        st.line_chart(df_2020)
    if option == '2019':
        st.line_chart(df_2019)
    if option == '2018':
        st.line_chart(df_2018)
    if option == '2017':
        st.line_chart(df_2017)

with col4:
    if option == '2021':
        st.bar_chart(df_2021)
    if option == '2020':
        st.bar_chart(df_2020)
    if option == '2019':
        st.bar_chart(df_2019)
    if option == '2018':
        st.bar_chart(df_2018)
    if option == '2017':
        st.bar_chart(df_2017)
