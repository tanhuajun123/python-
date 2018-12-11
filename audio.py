#coding: utf-8
#!/usr/bin/env python
import wave
import  matplotlib.pyplot as plt
import numpy as up
import os
filepath = "./data/"
filename = os.listdir(filepath)
f = wave.open(filepath+filename[1],'rb')
params = f.getparams()
nachannels,sampwidth,framerate,nframes = params[:4]
strData = f.readframes(nframes)
waveData = np.fromstring(strData,dtype=np.int16)
waveData = waveData*1.0/(max(abs(waveData)))
#plot the wave
time = np.arange(0,nframes)*(1.0 / framerate)
plt.plot(time,waveData)
plt.xlabel('时间(秒/s)')
plt.ylabel('振幅频率')
plt.title('单通道波段数据')
plt.grid('on')

nchannels = 1 #单通道为例
sampwidt = 2
fs = 8000
data_size = len(outData)
framerate = int(fs)
nframes = data_size
comptype = "NONE"
compname = "not compressed"
ouwave.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
