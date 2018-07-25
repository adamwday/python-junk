import subprocess
import fileinput
import os
from time import sleep

#set a file for stats
statsfile = "/opt/dataplatform/metrics/stats.txt"

try:
    file = open(statsfile, 'r')
except IOError:
    file = open(statsfile, 'w')

## get docker stats
dockerStatsToText = "docker stats --no-stream --format '{{ .Container }},{{ .MemPerc }},{{ .CPUPerc }},{{ .NetIO }},{{ .Name }}' >>" + statsfile
subprocess.Popen(dockerStatsToText, shell=True)

## remove ecs-agent lines
for line in fileinput.input(statsfile, inplace =1):
    line = line.strip()
    if not 'ecs-agent' in line:
        print line
    metrics = line.split()
    name = metrics[-1]

from time import sleep
sleep(6)

##parse metrics and send to ecs
#this could be cleaned up a lot
with open(statsfile) as metricfile:
    for line in metricfile:
        print line
        metricsReplace = line.replace(" / ", ",").replace("[", "").replace("\n","")
        metrics = metricsReplace.split(",")
        print metrics
        print len(metrics)
        containerID = metrics[0]
        memPercent = metrics[1].replace("%","")
        cpuPercent = metrics[2].replace("%","")
        contName = metrics[5]
        if contName == "ecs-agent":
            continue
        IOreceivedRaw = metrics[3]
        print IOreceivedRaw
        IOsentRaw = metrics[4]
        ##convert to MB
        IOreceivedMB = 0
        if IOreceivedRaw.endswith('kB'):
            IOreceivedMB = float(IOreceivedRaw.replace("kB",""))*.001
        if IOreceivedRaw.endswith('MB'):
            IOreceivedMB = float(IOreceivedRaw.replace("MB",""))
        if IOreceivedRaw.endswith('GB'):
            IOreceivedMB = float(IOreceivedRaw.replace("GB",""))*1000
        print IOreceivedMB
        print memPercent
        print contName
        print cpuPercent
        IOsentMB = 0
        if IOsentRaw.endswith('kB'):
            IOsentMB = float(IOsentRaw.replace("kB",""))*.001
        if IOsentRaw.endswith('MB'):
            IOsentMB = float(IOsentRaw.replace("MB",""))
        if IOsentRaw.endswith('GB'):
            IOsentMB = float(IOsentRaw.replace("GB",""))*1000
        print IOreceivedMB
        print IOsentMB
        taskID = contName[-20:]
        print taskID

        print "Put CPU Command: aws cloudwatch put-metric-data --metric-name CPUPercentage --namespace DataplatformECS --unit Percent --value " + cpuPercent + " --dimensions ContainerID="+ containerID +",ContainerName="+ contName +",taskID=" + taskID +" --region us-east-1"
        subprocess.Popen("aws cloudwatch put-metric-data --metric-name CPUPercentage --namespace DataplatformECS --unit Percent --value " + cpuPercent + " --dimensions ContainerID="+ containerID +",ContainerName="+ contName +",taskID=" + taskID +" --region us-east-1", shell=True)

        print "Put Mem Command: aws cloudwatch put-metric-data --metric-name memoryPercentage --namespace DataplatformECS --unit Percent --value " + memPercent + " --dimensions ContainerID="+ containerID +",ContainerName="+ contName +",taskID=" + taskID +" --region us-east-1"
        subprocess.Popen("aws cloudwatch put-metric-data --metric-name memoryPercentage --namespace DataplatformECS --unit Percent --value " + memPercent + " --dimensions ContainerID="+ containerID +",ContainerName="+ contName +",taskID=" + taskID +" --region us-east-1", shell=True)


        print "Put IO Rec Command: aws cloudwatch put-metric-data --metric-name IOreceived --namespace DataplatformECS --unit Megabytes --value " + str(IOreceivedMB) + " --dimensions ContainerID="+ containerID +",ContainerName="+ contName +",taskID=" + taskID +" --region us-east-1"
        subprocess.Popen("aws cloudwatch put-metric-data --metric-name IOreceived --namespace DataplatformECS --unit Megabytes --value " + str(IOreceivedMB) + " --dimensions ContainerID="+ containerID +",ContainerName="+ contName +",taskID=" + taskID +" --region us-east-1", shell=True)

        print "Put IO sent Command: aws cloudwatch put-metric-data --metric-name IOsent --namespace DataplatformECS --unit Megabytes --value " + str(IOsentMB) + " --dimensions ContainerID="+ containerID +",ContainerName="+ contName +",taskID=" + taskID +" --region us-east-1"
        subprocess.Popen("aws cloudwatch put-metric-data --metric-name IOsent --namespace DataplatformECS --unit Megabytes --value " + str(IOsentMB) + " --dimensions ContainerID="+ containerID +",ContainerName="+ contName +",taskID=" + taskID +" --region us-east-1", shell=True)

        print "Next line"


os.remove(statsfile)

print "finished"
