import streamlit as st
from minio import Minio

# Setup MinIO client
minioClient = Minio('MINIO_ENDPOINT',
                    access_key='YOUR_ACCESS_KEY',
                    secret_key='YOUR_SECRET_KEY',
                    secure=False)  # Change to True if your MinIO setup uses HTTPS

def fetch_data_from_minio(bucket_name, object_name):
    try:
        data = minioClient.get_object(bucket_name, object_name)
        return data.read().decode('utf-8')
    except Exception as e:
        st.write(f"Error fetching data: {str(e)}")
        return None

st.title("MinIO Data in Streamlit")

# Fetch and display data from MinIO
bucket = "your-bucket-name"
object_name = "your-object-name"
data = fetch_data_from_minio(bucket, object_name)
if data:
    st.write(data)

# To run the Streamlit app
# streamlit run app.py
