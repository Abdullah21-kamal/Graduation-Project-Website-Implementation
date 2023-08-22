
#!/bin/bash

folder="/media/dell/HDD/GradPro/uploads/"
new_filename="input.mp4"

find "$folder" -type f -name "*.mp4" -exec mv {} "$folder/$new_filename" \;
