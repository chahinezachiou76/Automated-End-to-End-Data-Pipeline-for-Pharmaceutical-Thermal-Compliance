import boto3
import json
import time
import random
from datetime import datetime

# إعداد الاتصال بـ LocalStack
# نستخدم 'test' كـ مفاتيح وهمية لأننا في بيئة محلية
firehose = boto3.client(
    'firehose',
    endpoint_url='http://localhost:4566',
    region_name='us-east-1',
    aws_access_key_id='test',
    aws_secret_access_key='test'
)

# تأكد أن هذا الاسم يطابق الاسم الموجود في ملف Terraform الخاص بك
STREAM_NAME = "coldchain-vaccine-firehose"

def generate_sensor_data():
    """توليد بيانات شحنة (حرارة عشوائية)"""
    # توليد حرارة بين -25 و -10 (درجة التجميد المطلوبة عادة هي تحت -18)
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
    print(f"📡 البدء في إرسال بيانات سلسلة التبريد إلى {STREAM_NAME}...")
    try:
        while True:
            payload = generate_sensor_data()
            print(f"📦 إرسال شحنة: {payload}")
            
            # إرسال السجل إلى Kinesis Firehose
            firehose.put_record(
                DeliveryStreamName=STREAM_NAME,
                Record={'Data': json.dumps(payload) + '\n'}
            )
            
            # انتظر ثانيتين قبل إرسال القراءة التالية
            time.sleep(2)  
    except KeyboardInterrupt:
        print("\n🛑 توقف المولد يدوياً.")

if __name__ == "__main__":
    run_producer()