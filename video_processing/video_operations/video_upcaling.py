import cv2

def upscale_video(input_path, output_path, scale_factor=2):
    """
    Upscales a video by a given scale factor using OpenCV.

    Parameters:
    - input_path: str, path to the input video file.
    - output_path: str, path to save the upscaled video file.
    - scale_factor: int, factor by which to upscale the video dimensions.
    """
    # Open the input video
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {input_path}")
        return

    # Get original video properties
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change codec as needed

    # Calculate new dimensions
    new_width = original_width * scale_factor
    new_height = original_height * scale_factor

    # Create VideoWriter object to write the upscaled video
    out = cv2.VideoWriter(output_path, fourcc, fps, (new_width, new_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Upscale the frame
        upscaled_frame = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

        # Write the upscaled frame to the output video
        out.write(upscaled_frame)

    # Release resources
    cap.release()
    out.release()
    print(f"Upscaled video saved to {output_path}")

def upscale_video_dnn(input_path, output_path, model_name, model_path, scale_factor=2):
    """
    Upscales a video using a DNN super-resolution model.
        
    Parameters:
    - input_path: str, path to input video
    - output_path: str, path for output video
    - model_name: str, name of the DNN model (e.g., "espcn", "fsrcnn")
    - model_path: str, path to the ESPCN/FSRCNN model file
    - scale_factor: int, upscaling factor (should match model)
    """
    # Load the model
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(model_path)
        
    # Set the model and scale factor
    sr.setModel(model_name, scale_factor)

    # Open video and create writer
    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * scale_factor)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * scale_factor)
    writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
                
        # Upscale frame using DNN
        upscaled = sr.upsample(frame)
        writer.write(upscaled)

    cap.release()
    writer.release()
    print(f"DNN upscaled video saved to {output_path}")