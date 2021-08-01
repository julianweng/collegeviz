import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import base64

st.set_page_config(layout="wide")

@st.cache
def load_data():
    df = pd.read_csv("reportcard.csv",index_col=0)
    return df

df = load_data()

# df['School Name'].values.tolist()
st.sidebar.title('CollegeViz')
cols = list(df.columns.values)
option = st.sidebar.radio('College Search', ('Drill-Down Scatter', 'Drill-Down Map', 'Pair-Plot','Mobility'))
if option == 'Drill-Down Scatter' or option == 'Drill-Down Map':
    fil1 = st.sidebar.selectbox('Filter 1', cols, index=cols.index("Admission rate"))
    txt1 = st.sidebar.text_input('Range 1','0.0-1.0')
    #val1 = st.sidebar.slider('Range 1',0.0, 1.0, (0.03, 0.5))
    fil2 = st.sidebar.selectbox('Filter 2', cols, index=cols.index("Undergraduate Enrollment"))
    txt2 = st.sidebar.text_input('Range 2','1000-50000')

    try :
        val1 = [float(x) for x in txt1.split('-')]
    except:
        st.sidebar.write("Error parsing "+txt1)
        val1 = [0,100000]

    try :
        val2 = [float(x) for x in txt2.split('-')]
    except:
        st.sidebar.write("Error parsing "+txt2)
        val2 = [0,100000]

    xcol = st.sidebar.selectbox('X-Axis', cols, index=cols.index("Admission rate"))
    ycol = st.sidebar.selectbox('Y-Axis', cols, index=cols.index("90% earnings 10Yr"))
    cat = st.sidebar.selectbox('Category', ['Tier Name','REGION'], index=0)
    bubble_col = st.sidebar.selectbox('Bubble Size', cols, index=cols.index("Undergraduate Enrollment"))

    c = (df[fil1]>=val1[0]) & (df[fil1]<=val1[1]) & (df[fil2]>=val2[0]) & (df[fil2]<=val2[1])

    columns = st.multiselect('Columns', cols,default=['College','Undergraduate Enrollment',
    'CITY','STABBR','ZIP','REGION','Admission rate','Mean Earnings 10Yr'])

    plot = df[c][df[c][bubble_col].notna()]
    tbl = plot[columns]
    st.header("Selected Colleges (#:"+str(tbl.shape[0])+")")
    st.dataframe(tbl, width=1200)
    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
        href = f'<a href="data:file/csv;base64,{b64}" download="colleges.csv">Download CSV File</a>'
        return href
    st.markdown(filedownload(tbl), unsafe_allow_html=True)

    if option == 'Drill-Down Scatter':
        fig = px.scatter(plot, x=xcol, y=ycol, hover_data=["College"],size=bubble_col,color=cat,height=600)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.title("Map View Coming!")
elif option == 'Pair-Plot':
    columns = st.multiselect('Columns', cols, default=['Admission rate','Median child individual earnings','Median parent household income'])
    fig = sns.pairplot(df[columns]) # , hue="Tier Name"
    st.pyplot(fig)
else:
    st.write("Mobility View is not implemented yet!")
