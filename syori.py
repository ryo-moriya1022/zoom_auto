import webbrowser
from pywinauto import Desktop
from pywinauto.application import Application
from pywinauto.keyboard import SendKeys
from time import sleep
import streamlit as st
def aurugori():
    webbrowser.open("https://us06web.zoom.us/j/83536050418?pwd=RUttbDVyMm1KVTYyQkRoL3VKK0ZTdz09",new=0)
    sleep(5)
    #app=Desktop(backend="uia")
    #sleep(10)
    #zoomw1=app.Zoom
    #zoomw1["ミュート"].click()
    st.stop()
def datascience():
    st.write("実行中です")
    webbrowser.open("https://us06web.zoom.us/j/88055930614?pwd=TC9rYkRFbHBvOXRRSjVybTdUZlJsdz09",new=0)
    sleep(10)
    #app=Desktop(backend="uia")
    #zoomw1=app.Zoom
    #sleep(10)
    #zoomw1["ミュート"].click()
    st.stop()
