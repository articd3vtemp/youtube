import subprocess
import streamlit as st

# Streamlit UI
st.title("YouTube RTMP Streamer")
st.write("Stream a video with an audio source to YouTube Live.")
st.write("Starting the stream...")

# Download FFmpeg
subprocess.run(["curl", "-O", "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz"])
subprocess.run(["tar", "-xvf", "ffmpeg-release-amd64-static.tar.xz"])

# FFmpeg path and command
ffmpeg_path = "./ffmpeg-7.0.2-amd64-static/ffmpeg"
stream_command = [
    ffmpeg_path, "-stream_loop", "-1", "-re", "-i", "room.mp4",
    "-stream_loop", "-1", "-re", "-i", "https://stream.zeno.fm/9kaed9hws98uv",
    "-vcodec", "libx264", "-pix_fmt", "yuvj420p", "-maxrate", "512k", "-preset", "veryfast", "-r", "12",
    "-framerate", "30", "-g", "50", "-c:a", "aac", "-b:a", "98k", "-ar", "44100", "-strict", "experimental",
    "-video_track_timescale", "1000", "-b:v", "150k", "-f", "flv",
    "rtmp://a.rtmp.youtube.com/live2/qp0u-wb9b-3ptq-adxz-9rdj"
]

process = subprocess.Popen(stream_command)
st.write("Streaming started!")

# Optionally, provide a way to stop the stream
if st.button("Stop Stream"):
    process.terminate()
    st.write("Stream stopped!")
