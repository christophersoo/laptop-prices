import pandas as pd
import re


def extract_brand(data):
    brands = ['Acer', 'Dell', 'HP', 'Lenovo', 'Asus', 'Apple', 'MSI', 'Samsung']
    for brand in brands:
        if brand in data:
            return brand
    return "Others"

def extract_os(data):
    pass

def transform(df_raw):
    pass
    
