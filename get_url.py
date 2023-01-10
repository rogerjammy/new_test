import time
import os
import requests
import sys

start_date_human=sys.argv[1]
end_date_human=sys.argv[2]
data_frequency_in_seconds=int(sys.argv[3])

#start_date_human = '2022-12-01 10:00:00'
#end_date_human = '2022-12-01 10:02:00'
#data_frequency_in_seconds = 120


base_url = "https://api.data.gov.sg/v1/transport/traffic-images"
# https://api.data.gov.sg/v1/transport/traffic-images?date_time=2022-12-28T13%3A00%3A00Z

# Code to delete the output_stage.txt in case it exists.
if os.path.exists("output_stage.txt"):
    # Delete the file
    os.remove("output_stage.txt")

# Code to delete the output.txt in case it exists.
if os.path.exists("output.txt"):
    # Delete the file
    os.remove("output.txt")


header = "urls"
with open("output_stage.txt", "w") as output_file:
        output_file.write(header)
        output_file.write('\n')


start_date_epoch = int(time.mktime(time.strptime(start_date_human, "%Y-%m-%d %H:%M:%S")))
end_date_epoch = int(time.mktime(time.strptime(end_date_human, "%Y-%m-%d %H:%M:%S")))

# Start the while loop
while start_date_epoch < end_date_epoch:
  gmt_timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(start_date_epoch))
  modified_string = gmt_timestamp.replace(" ", "T").replace(":", "%3A")+'Z'
  url = f"{base_url}?date_time={modified_string}"
  response = requests.get(base_url)
  print(url)  
  # Open the file in write mode
  
  with open("output_stage.txt", "a") as output_file:
    # Write the string to the file
    output_file.write(url)
    output_file.write('\n')
    
  start_date_epoch += data_frequency_in_seconds

os.chmod("output_stage.txt", 0o777)
os.rename("output_stage.txt","output.txt")
os.chmod("output.txt", 0o777)

output_file.close()
