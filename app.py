import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import cv2
import os

st.title("Steel Defect Detection")

model = YOLO("steel_defect_best.pt")

uploaded_file = st.file_uploader(
    "Upload Image or Video",
    type=["jpg", "jpeg", "png", "mp4", "avi", "mov"]
)

if uploaded_file:

    # ================= IMAGE =================
    if uploaded_file.type.startswith("image"):

        image = Image.open(uploaded_file)

        results = model.predict(
            source=image,
            conf=0.05
        )

        result = results[0]

        # Bounding boxes + defect names
        annotated_image = result.plot()

        st.image(
            annotated_image,
            caption="Detected Steel Defects",
            use_container_width=True
        )

        # Defect details
        if len(result.boxes) > 0:

            st.subheader("Detected Defects")

            for box in result.boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                st.write(
                    f"**{model.names[class_id]}** "
                    f"- Confidence: {confidence:.2f}"
                )

        else:
            st.warning("No defects detected.")

        # ================= VIDEO =================
    else:

        st.subheader("Processing Video...")

        input_video = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        )

        input_video.write(uploaded_file.read())
        input_video.close()

        cap = cv2.VideoCapture(input_video.name)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        output_path = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        ).name

        # Use avc1 codec for browser-compatible MP4
        fourcc = cv2.VideoWriter_fourcc(*"avc1")

        out = cv2.VideoWriter(
            output_path,
            fourcc,
            fps,
            (width, height)
        )

        while cap.isOpened():

            ret, frame = cap.read()

            if not ret:
                break

            results = model.predict(
                frame,
                conf=0.05,
                verbose=False
            )

            annotated_frame = results[0].plot()

            out.write(annotated_frame)

        cap.release()
        out.release()

        st.success("Video detection completed!")

        with open(output_path, "rb") as video_file:
            video_bytes = video_file.read()

        st.video(video_bytes)

        os.remove(input_video.name)
        os.remove(output_path)