#!/usr/bin/env python
import os 
import sys
import subprocess

#Git Clone this repository and CD into said repo to grab the filelist
git_fetch = subprocess.call(["git", "clone","http://git.shikata.xyz:3000/root/Pi-Hole-SelfServe.git"])

#Get lines of the Git Script
try:
    ImportFile = open("./Pi-Hole-SelfServe/HostList.txt",'r')
except FileNotFoundError:
    print("Error: File not found!")
    exit(1)
except IndexError:
    print("Error: No Argument Given")
    exit(1)
ImportFile_Lines = ImportFile.read().splitlines()
ImportFile.close()

#Get lines of Pi-Hole's list DNS list
try:
    ServerHosts = open('/etc/pihole/local.list','r')
except FileNotFoundError:
    print("Error: PiHole local file not found!")
    exit(1)
ServerHosts_Lines = ServerHosts.read().splitlines()
ServerHosts.close()

#KnownGoodLines
HostAdditions = []

# Go through each line in ImportFile,
# If it doesn't exist, add it to HostAdditions to be added 
for line in ImportFile_Lines:
    if line not in ServerHosts_Lines:
        HostAdditions.append(str(line))

#Iterate lines to be added
print("-Lines to be added-")
for line in HostAdditions:
    print(str(line))

#Add Host file to append to
try:
    ServerHosts = open('/etc/pihole/local.list','w')
except FileNotFoundError:
    print("Error: Pi-Hole Local.list file not found!")
    exit(1)

#For each of those lines, we add to the bottom of the hosts file
for line in ImportFile_Lines:
    ServerHosts.write(line + "\n")
    print("Added " + str(line))

#Close ServerHosts file so Python doesn't bug out
ServerHosts.close()

#Restart Pi-Holes DNS
restart_process = subprocess.call(["pihole", "restartdns"])
if restart_process == 0:
    print("DNS Restart Successful!")
else:
    print("Error Restarting DNS Service")

#Remove Git Repo after execution
git_remove = subprocess.call(["rm", "-rf", "Pi-Hole-SelfServe"])
if git_remove == 0:
    print("Git Repo Removal Successful!")
else:
    print("Error Restarting DNS Service")