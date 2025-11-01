import boto3
import pandas as pd
import sys
import os
from botocore.exceptions import ClientError


os.makedirs("output", exist_ok=True)
sys.stdout = open("output/boto3_s3_output.txt", "w")

s3 = boto3.client("s3", region_name="us-east-1")

bucket_name = "likhith-week1-demo"
file_path = "data/raw/local_sales.csv"
object_name = "sales/local_sales.csv"

sample_df = pd.DataFrame({
    "OrderId":[1,2,3],
    "Customer":["Likhith","Sasank","Siva"],
    "Amount":[120,160,280]
})

sample_df.to_csv(file_path,index=False)

print(f"Created local file: {file_path}\n")



#  Here I am sending the files to S3 BUCKET after Creating S3 bucket

try:
    s3.create_bucket(Bucket = bucket_name)
except ClientError as err:
    if(err.response["Error"]["Code"] == "BucketAlreadyOwnedByYou"):
         print(f"Bucket already exists: {bucket_name}")
    else:
        print("Error creating bucket:", err)


try:
    s3.upload_file(file_path,bucket_name,object_name)
    print(f"Uploaded {file_path} to s3://{bucket_name}/{object_name}")
except ClientError as err:
    print("Upload failed: ",err)

print("\n Files in S3 bucket:")
objects = s3.list_objects_v2(Bucket = bucket_name)
if "Contents" in objects:
    for obj in objects["Contents"]:
        print("  .",obj["Key"])
else:
    print(" (Bucket is empty) ")




 # Here I am downloading from s3
download_path = "data/s3_upload/sales_downloaded.csv"
os.makedirs("data/s3_upload", exist_ok=True)

try:
    s3.download_file(bucket_name,object_name,download_path)
    print(f"\n Downloaded file is in {download_path}")
except ClientError as err:
    print("Download failed:", err)



df = pd.read_csv(download_path)
print("\n Data Loaded Back from S3:")
print(df, "\n")



# Here I am adding a new column after computation 

df["Tax"] = [round(a* 0.1,2) for a in df["Amount"]]
df["TotalWithTax"] = df["Amount"]+df["Tax"]

print("After doing Tax calculation: ")
print(df,"\n")

final_path = "data/s3_upload/sales_with_tax.csv"
df.to_csv(final_path,index=False)

print(f"Final data saved locally in {final_path}")

# Here I am uploading the final calculated version of file
s3.upload_file(final_path,bucket_name,"sales/sales_with_tax.csv")
print(f"Uploaded final version to  s3://{bucket_name}/sales/sales_with_tax.csv")


sys.stdout.close()