import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load dataset
try:
    data = pd.read_excel("Citation Data.xlsx")
except FileNotFoundError:
    print("Error: File 'Citation Data.xlsx' not found. Please check the file path.")
    exit()
    
data = pd.read_excel("Citation Data.xlsx")
print(data.columns)  # Check column names