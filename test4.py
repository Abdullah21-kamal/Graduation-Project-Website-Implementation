import os
import subprocess
from subprocess import call
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import time
import os
from moviepy.editor import VideoFileClip



def change_data_rate(input_path, output_path, target_data_rate):
        if os.path.exists(output_path):
            os.remove(output_path)
            print('it exists')
        else: 
            print("it does not exist!")
        video = VideoFileClip(input_path)
        video.write_videofile(output_path, bitrate=target_data_rate)


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/favicon.ico")
async def get_favicon():
    return {"status": "No Content"}


@app.post("/processvideo/")
async def process_video(file: UploadFile = File(...), model_type: str = Form(...)):
    
    

    filename = file.filename
    file_path = os.path.join("uploads", filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
     # renaming the file   
    
   
    script_path = '/media/dell/HDD/GradPro/rename_input.sh'
    subprocess.run(['bash', script_path])

    if model_type == "Tracking":
       
        result=subprocess.run(['bash', '/home/dell/ByteTrack_HOME/station/runweb.sh'],capture_output=True, text=True)
        output = result.stdout
        error_message = result.stderr
        return_code = result.returncode
        # Example usage
        input_video_path = "/media/dell/HDD/GradPro/output/out.mp4"
        output_video_path = "/media/dell/HDD/GradPro/output/output.mp4"
        target_data_rate = "9332k"  # Set the desired data rate (e.g., 9999 kilobits per second)

        change_data_rate(input_video_path, output_video_path, target_data_rate)
        print("Video with suitbale data rate is created!!")
        output_file = 'output.mp4'
        print('the file name is:', output_file)
        output_path = os.path.join("/media/dell/HDD/GradPro/output", output_file)
        print('the output_path name is:', output_path)
        os.remove("/media/dell/HDD/GradPro/uploads/input.mp4")


    elif model_type == "Action Spotting":
        call(["python", "/media/dell/HDD/GradPro/Action_pipeline.py"])
        
        output_file = 'output.mp4'
        print('the file name is:', output_file)
        output_path = os.path.join("/media/dell/HDD/GradPro/output", output_file)
        print('the output_path name is:', output_path)
        os.remove("/media/dell/HDD/GradPro/uploads")
    else:
        return {"error": "Invalid model type"}
    


    

    return HTMLResponse(content=f"<video controls><source src='/{output_file}' type='video/mp4'></video>")
    # or use the following line if you want to return the file for download
    # return FileResponse(output_path, media_type="video/mp4")
