import streamlit as st
from zoom_auto import data_zoom,arugo_zoom
from group_number import a_group_number,d_group_number
st.set_page_config(
    page_title="Zoom自動入室",
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://www.google.com"
    }
)
st.title("on-line授業自動入室予約システム")
st.header("概要")
st.write("このプログラムはon-line授業を寝ながらでも受けたい勤勉な生徒の学業を補助するシステムとなっています")

st.header("グループワーク時間")
st.write("ここではグループワーク番号からグループワーク時間を出力します")
data_number=st.text_input("データサイエンスグループワーク番号") 
d_zyu_time,d_hour,d_minute=d_group_number(data_number)
if d_zyu_time is not None:
    st.markdown(d_zyu_time)
arugo_number=st.text_input("アルゴリズム基礎グループ番号")
arugo_number,a_hour,a_minute=a_group_number(arugo_number)
if arugo_number is not None:
    st.markdown(arugo_number)
st.write("")
st.write("")
st.header("ZOOM予約")
st.write("ここでは各授業の予約をします。グループワーク番号入力欄を入力すると出力された時間に予約するキーを表示します\n現在目的の時間が過ぎた後に予約すると、処理が発生しているバグあり注意")
st.write("")
st.write("データサイエンス入門(9:00)の予約")
if st.button("予約",key="data"):
    times="09:00"
    data_zoom(times)
st.write("")
if data_number:
    times=str(d_hour)+":"+str(d_minute)
    text="データサイエンス入門 グループワーク("+times+")の予約"
    st.write(text)
    if st.button("予約",key="sabo"):
        data_zoom(times)
st.write("")
st.write("アルゴリズム基礎(13:15)の予約")
if st.button("予約",key="ri"):
    times="13:15"
    arugo_zoom(times)
st.write("")
if arugo_number:
    times=str(a_hour)+":"+str(a_minute)
    text="アルゴリズム基礎 グループワーク("+times+")の予約"
    st.write(text)
    if st.button("予約",key="qq"):
        arugo_zoom(times)
st.write("")
st.write("予約の取り消しをします")
if st.button("取消",key="tor"):
    st.stop()