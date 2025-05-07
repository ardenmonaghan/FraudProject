import streamlit as st


class FraudDetectionApp:
    def __init__(self):
        self.df = pd.read_csv("AIML_Dataset.csv")
        self.df.head()


class CSV_to_SQL:
    def __init__(self):
        self.df = pd.read_csv("AIML_Dataset.csv")
        self.df.head()


app = FraudDetectionApp()
