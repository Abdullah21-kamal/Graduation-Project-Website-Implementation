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

# Example usage
input_video_path = "D:\\GradPro\\uploads\\test_out.mp4"
output_video_path = "D:\\GradPro\\uploads\\test_out2.mp4"
target_data_rate = "9332k"  # Set the desired data rate (e.g., 9999 kilobits per second)

change_data_rate(input_video_path, output_video_path, target_data_rate)
print("Video with suitbale data rate is created!!")
os.remove("D:\\GradPro\\uploads\\input.mp4")