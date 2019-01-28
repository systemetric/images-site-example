import os

names = os.listdir("D:\Documents\My Documents (Edwin)\School-work\HRSFC\Robotics\ImagesSite\selected images")

for i in range (0, len(names)):
    print("<img class='myImg' src='selected images/"+names[i]+"'/>")
