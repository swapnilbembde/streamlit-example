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




def trim_video(video_path, start_time, end_time):
    with VideoFileClip(video_path) as video:
        new_video = video.subclip(start_time, end_time)
        new_video_path = f"{video_path}_trimmed.mp4"
        new_video.write_videofile(new_video_path)
        return new_video_path

st.title(" Video Editing Capabilities")

if video_file_path:
    st.video(video_file_path)
    
    # Trim functionality
    st.header("Trim Video")
    start_time = st.number_input("Start Time (seconds)", min_value=0, max_value=600, value=0)
    end_time = st.number_input("End Time (seconds)", min_value=1, max_value=600, value=10)
    if st.button("Trim Video"):
        trimmed_video_path = trim_video(video_file_path, start_time, end_time)
        st.video(trimmed_video_path)

# Cropping can be added similarly using moviepy's crop functionality.
      
# To run the Streamlit app
# streamlit run app.py
# Replace 'MINIO_ENDPOINT', 'YOUR_ACCESS_KEY', 'YOUR_SECRET_KEY', 'your-bucket-name', and 'your-video-name.mp4' with the appropriate values for your MinIO setup.
