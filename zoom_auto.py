import schedule as sc
from time import sleep
import webbrowser
from syori import aurugori,datascience
import streamlit as st
def data_zoom(time):
    sc.every().friday.at(time).do(datascience)
    while True:
        sc.run_pending()
        sleep(59)
def arugo_zoom(time):
    sc.every().friday.at(time).do(aurugori)
    while True:
        sc.run_pending()
        sleep(59)