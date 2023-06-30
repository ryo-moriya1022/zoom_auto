import webbrowser
from time import sleep
import streamlit as st
def aurugori():
    webbrowser.open("https://us06web.zoom.us/j/83536050418?pwd=RUttbDVyMm1KVTYyQkRoL3VKK0ZTdz09",new=0)
    sleep(5)
    st.stop()
def datascience():
    st.write("実行中です")
    webbrowser.open("https://us06web.zoom.us/j/88055930614?pwd=TC9rYkRFbHBvOXRRSjVybTdUZlJsdz09",new=0)
    sleep(10)
    st.stop()
