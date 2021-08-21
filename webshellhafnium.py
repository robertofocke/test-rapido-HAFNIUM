import shodan
import sys
import os

if len(sys.argv)<2:
	print ("webshellhafnium.py apishodan country:af")
	sys.exit()

api=shodan.Shodan(sys.argv[1])
result=api.search("http.title:outlook exchange port:443 "+sys.argv[2])
for item in result["matches"]:
	print(item["ip_str"])
	os.system("echo https://"+item["ip_str"]+" | nuclei -t hafnium_detect.yaml -v")
