import pandas as pd
import sys
import os
import json



os.makedirs("output", exist_ok=True)
sys.stdout = open("output/pandas_basics_output.txt", "w")



print("OUBT Week 1 - Day 2-3: Python for Data Engineering")
print("Topic: Pandas for Data Manipulation\n")


sales_data  = pd.DataFrame({
    "orderId": [101,102,103,104,105,106,107,108,109,110],
    "Customer":["Likhith","Sasank","Prathyush","Anushka","Sasank","Likhith","Prathyush","Anushka","Likhith","Sasank"],
    "Product":["Laptop","Mobile","Tablet","Laptop","Tablet","Mobile","Laptop","Tablet","Mobile","Laptop"],
    "Quantity":[1,2,1,1,3,2,1,2,1,1],
    "Price":[800,500,300,800,300,500,800,300,800,500]
})

print(f"Sales Data: {sales_data}\n")

sales_data.to_csv("data/raw/sales_data.csv", index=False)

print("Created sample sales_data.csv\n")

df = pd.read_csv("data/raw/sales_data.csv")
print(f"Data read from csv:{df} \n")

print(df.head(5))

print(df.info())

print("\n Summary Statistics:")
print(df.describe(), "\n")


print(" Data cleaning : ")
print(f"Duplicate rows before the data cleaning are: {df.duplicated().sum()}")

df.drop_duplicates(inplace=True)
print(f"Duplicate rows before the data cleaning are: {df.duplicated().sum()}")


df["total"] = df["Quantity"] * df["Price"]
print("I have added total column after calculating")
print(df.head(),"\n")


print("Total Revenue per customer:")
print(df.groupby("Customer")["total"].agg("sum"),"\n")


print("Total Quantity per Product:")
print(df.groupby("Product")["Quantity"].agg("sum"),"\n")



#Dataframes - merging

invoice_data = [
    {"InvoiceId" : "I101","Customer":"Likhith"},
    {"InvoiceId" :"I102","Customer":"Sasank"}
]

with open("data/raw/invoice.json","w") as f:
    json.dump(invoice_data,f)


invoice_df = pd.read_json("data/raw/invoice.json")

print("Invoice Data : ")
print(invoice_data,"\n")


merged_df = pd.merge(df,invoice_df,on="Customer",how="left")
print("Merged Sales and Invoice Data:")
print(merged_df.head(), "\n")

merged_df.to_csv("data/processed/cleaned_sales_data.csv",index=False)


print("Cleaned data saved to data/processed/cleaned_sales_data.csv\n")
print("Day 2–3 Pandas Practice Completed Successfully!")

sys.stdout.close()