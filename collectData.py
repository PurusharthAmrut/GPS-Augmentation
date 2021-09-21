import urllib.request
import math
import time
import datetime

def getData(filenumber):
    urlhandle = urllib.request.urlopen('https://sih.isro.gov.in/samples/P2/214_19MAR01_000000.GPS')
    filehandle = open('214_19MAR01_000000-'+str(filenumber)+'.GPS', 'wb')

    start_time = math.floor(time.time())
    temp = start_time
    count = 0
    for line in urlhandle:
        filehandle.write(line)
        count = count + 1
        current_time = math.floor(time.time())
        if temp!=current_time and (current_time - start_time)%10==0:
            print(count,"lines written")
            temp = current_time

    print("Download complete for file number",filenumber,"\nLines written:",count)
    print("Time of completion:",str(datetime.datetime.now()))
    urlhandle.close()
    filehandle.close()

startfilenumber = int(input("Starting file number: "))
endfilenumber = int(input("Ending file number: "))
for filenumber in range(startfilenumber, endfilenumber + 1):
    print('\n***************** Writing file number',filenumber,'********************')
    getData(filenumber)
    if filenumber < endfilenumber:
        print('\n5 minutes left for next write.....')
        time.sleep(300)
