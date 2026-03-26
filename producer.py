import boto3
import json
import time
import random
from datetime import datetime

# Initialize Firehose client for LocalStack
firehose = boto3.client(
    'firehose',
    endpoint_url='http://localhost:4566',
    region_name='us-east-1',
    aws_access_key_id='test',
    aws_secret_access_key='test'
)

STREAM_NAME = "coldchain-vaccine-firehose"

def generate_sensor_data():
    """Generate random cold chain sensor data (Temperature Monitoring)"""
    temperature = random.uniform(-25, -10) 
    
    data = {
        "sensor_id": f"SENSOR-{random.randint(1, 10)}",
        "shipment_id": f"SHIP-{random.randint(1000, 9999)}",
        "temperature": round(temperature, 2),
        "timestamp": datetime.now().isoformat(),
        "status": "OK" if temperature <= -18 else "CRITICAL"
    }
    return data

def run_producer():
    print(f"📡 Starting data stream to {STREAM_NAME}...")
    try:
        while True:
            payload = generate_sensor_data()
            print(f"📦 Sending payload: {payload}")
            
            # Send record to Kinesis Firehose
            firehose.put_record(
                DeliveryStreamName=STREAM_NAME,
                Record={'Data': json.dumps(payload) + '\n'}
            )
            
            # Wait 2 seconds before next reading
            time.sleep(2)  
    except KeyboardInterrupt:
        print("\n🛑 Producer stopped manually.")

if __name__ == "__main__":
    run_producer()