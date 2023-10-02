import concurrent.futures
import json
import os
import queue
import sys
import time

import cv2
import numpy as np
import requests
import torch
import torchvision
from flask import Flask, jsonify, render_template, request, send_file
from PIL import Image

from demo import automask_image_app, automask_video_app, sahi_autoseg_app

sys.path.append(sys.path[0] + "/tracker")
sys.path.append(sys.path[0] + "/tracker/model")
from .track_anything import TrackingAnything, parse_augment

# ... (all the functions defined in the original code except the Gradio part)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./uploaded_videos"
app.config["ALLOWED_EXTENSIONS"] = {"mp4", "avi", "mov", "mkv"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload_video", methods=["POST"])
def upload_video():
    # ... (handle video upload and processing)
    return jsonify(status="success", data=video_data)


@app.route("/template_select", methods=["POST"])
def template_select():
    # ... (handle template selection and processing)
    return jsonify(status="success", data=template_data)


@app.route("/sam_refine", methods=["POST"])
def sam_refine_request():
    # ... (handle sam refine and processing)
    return jsonify(status="success", data=sam_data)


@app.route("/track_video", methods=["POST"])
def track_video():
    # ... (handle video tracking and processing)
    return jsonify(status="success", data=tracking_data)


@app.route("/track_image", methods=["POST"])
def track_image():
    # ... (handle image tracking and processing)
    return jsonify(status="success", data=tracking_data)


@app.route("/download_video", methods=["GET"])
def download_video():
    try:
        return send_file("output.mp4", attachment_filename="output.mp4")
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=args.port)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12212, debug=True)
