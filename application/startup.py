import socket        
import multiprocessing
import subprocess,time
import os
import sys
import thread
from shutil import copyfile

def StartTask():
	data=""
	data+="<h1> Ivis International Pvt LTD </h1>"+str(89)
    return data
    
def readFile(txt):
    data=""
    data=txt
    try:
    	data=txt
    except:
    	pass
    return data

def ld():
    print("data Loaded..");

def get(data):
    return (open("bin/" + data + ".txt", 'r').read())
