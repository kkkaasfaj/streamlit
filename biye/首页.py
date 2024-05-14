import streamlit as st
import pandas as pd
import base64
import uuid
# 设置网站标题
st.title('体检数据输入')
C21,C22=st.columns([1,1])
# 接收用户输入体检数据
key1 = str(uuid.uuid4())
key2 = str(uuid.uuid4())
key3 = str(uuid.uuid4())
key4 = str(uuid.uuid4())
key5 = str(uuid.uuid4())
key6 = str(uuid.uuid4())
key7 = str(uuid.uuid4())
key8 = str(uuid.uuid4())
with C21:
    height = st.number_input('请输入身高（cm）：', min_value=None, format="%f")
    weight = st.number_input('请输入体重（kg）：', min_value=None, format="%f")
    Ggr = st.number_input('请输入：', min_value=0, step=1,key=key5)
    RP = st.number_input('请输入：', min_value=0, step=1,key=key6)
with C22:
    age = st.number_input('请输入年龄：', min_value=0, step=1, key=key7)
    stage = st.number_input('请输入：', min_value=0, step=1, key=key8)
    Ts = st.number_input('请输入：', min_value=0, step=1, key=key1)
    adn = st.number_input('请输入：', min_value=0, step=1, key=key2)
# 将输入数据保存为DataFrame

if st.button('保存体检数据'):
    df = pd.DataFrame({'age': [height], 'wight': [weight], 'Ts': [Ggr], 'stage': [Ts], 'adn': [RP], 'Ggr': [adn] })

    # 显示DataFrame
    st.write('体检数据：')
    st.write(df)

    # 允许用户下载数据
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # 转换为base64编码
    href = f'<a href="data:file/csv;base64,{b64}" download="health_checkup_data.csv">点击此处下载体检数据</a>'
    st.markdown(href, unsafe_allow_html=True)




