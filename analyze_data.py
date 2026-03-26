import boto3
import json
import pandas as pd
import os

s3 = boto3.client('s3', endpoint_url='http://localhost:4566', region_name='us-east-1')
bucket_name = 'coldchain-vaccine-data-lake'

def fetch_data():
    all_data = []
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' not in response:
            print(" المخزن فارغ حالياً.. تأكد من تشغيل producer.py أولاً.")
            return

        for obj in response['Contents']:
            file = s3.get_object(Bucket=bucket_name, Key=obj['Key'])
            content = file['Body'].read().decode('utf-8')
            
            for line in content.splitlines():
                if line.strip():
                    all_data.append(json.loads(line))
        
        df = pd.DataFrame(all_data)
        
        print("\n---  succ (Cold Chain) ---")
        print(df.head()) 
        
        output_file = 'coldchain_analytics_data.csv'
        df.to_csv(output_file, index=False)
        print(f"\n  succ: {os.getcwd()}\\{output_file}")
        print(" Excel أو Power BI.")

    except Exception as e:
        print(f"  erros: {e}")

if __name__ == "__main__":
    fetch_data()
