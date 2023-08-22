import os

def delete_video_file(filename):
    if os.path.isfile(filename):
        try:
            os.remove(filename)
            print(f"File '{filename}' deleted successfully.")
        except OSError as e:
            print(f"Error occurred while deleting '{filename}': {e}")
    else:
        print(f"File '{filename}' not found.")

# Set the filename you want to search for and delete
filename = "test.mp4"
filename2 = "test_out.mp4"
# Call the function to delete the file
delete_video_file(filename)
delete_video_file(filename2)
print("cleared!!")