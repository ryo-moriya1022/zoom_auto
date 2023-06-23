import schedule as sc
from time import sleep
import webbrowser
from pywinauto import Desktop
from syori import aurugori,datascience
import streamlit as st
def data_zoom(time):
    sc.every().friday.at(time).do(datascience)
    st.write("データサイエンス入門の予約をしています。スリープモードにしないようにしてください")
    while True:
        sc.run_pending()
        sleep(10)
def arugo_zoom(time):
    sc.every().friday.at(time).do(aurugori)
    st.write("アルゴリズム基礎の予約をしています。スリープモードにしないようにしてください")
    while True:
        sc.run_pending()
        sleep(10)