import streamlit as st
from minio import Minio
import tempfile

# Setup MinIO client
minioClient = Minio('MINIO_ENDPOINT',
                    access_key='YOUR_ACCESS_KEY',
                    secret_key='YOUR_SECRET_KEY',
                    secure=False)  # Change to True if your MinIO setup uses HTTPS

def fetch_video_from_minio(bucket_name, object_name):
    try:
        # Get the video stream from MinIO
        video_stream = minioClient.get_object(bucket_name, object_name)

        # Save the video stream to a temporary file
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        for d in video_stream.stream(32*1024):
            tfile.write(d)

        return tfile.name
    except Exception as e:
        st.write(f"Error fetching video: {str(e)}")
        return None

st.title("MinIO Video in Streamlit")

# Fetch and display video from MinIO
bucket = "your-bucket-name"
object_name = "your-video-name.mp4"
video_file_path = fetch_video_from_minio(bucket, object_name)
if video_file_path:
    st.video(video_file_path)

# To run the Streamlit app
# streamlit run app.py
# Replace 'MINIO_ENDPOINT', 'YOUR_ACCESS_KEY', 'YOUR_SECRET_KEY', 'your-bucket-name', and 'your-video-name.mp4' with the appropriate values for your MinIO setup.
