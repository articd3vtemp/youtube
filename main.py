import os
import streamlit as st

# Streamlit UI
st.title("YouTube RTMP Streamer")
st.write("Stream a video with an audio source to YouTube Live.")

if st.button("Start Streaming"):
    st.write("Starting the stream...")
    # os.system("ffmpeg -stream_loop -1 -re -i room.mp4 -stream_loop -1 -re -i https://stream.zeno.fm/6hszhrzidmcuv -vcodec libx264 -pix_fmt yuvj420p -maxrate 512k -preset veryfast -r 12 -framerate 30 -g 50 -c:a aac -b:a 98k -ar 44100 -strict experimental -video_track_timescale 1000 -b:v 150k -f flv  rtmp://a.rtmp.youtube.com/live2/qp0u-wb9b-3ptq-adxz-9rdj")
    os.system("pip install ffmpeg-python")
    os.system("ls")
    os.system("curl -O https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz")
    # ffmpeg_path = "/home/appuser/.local/bin"  # Path to the local FFmpeg binary
    st.write("Streaming started!")
