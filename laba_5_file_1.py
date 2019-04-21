import cv2
import numpy	

from time import sleep
from matplotlib import pyplot as plt

#delete error ... pythonvalue() not implemented
import zeep
from onvif import ONVIFCamera, ONVIFService
def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue
zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

from onvif import ONVIFCamera
mycam = ONVIFCamera('192.168.15.43', 80, 'esvolkova5', 'UF8OMwhzaG07')

#steram
str=cv2.VideoCapture('rtsp://192.168.15.43:554')

#���������� �����������
fig=plt.figure(figsize=(2, 2))
color = ('b','g','r')
ret,frame=str.read()
cv2.imshow('qwerty',frame)
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(2, 2, 1)
plt.imshow(hist,interpolation = 'nearest')

fig.add_subplot(2, 2, 2)
for i,col in enumerate(color): #������ �������� ������������� ���������� �������� � ���� ����������� � ��������������� ��������� ������� RGB
      histr = cv2.calcHist([frame],[i],None,[256],[0,256])
      plt.plot(histr,color = col)
      plt.xlim([0,256])

# �������� �����-�������
media = mycam.create_media_service()
# �������� ptz 
ptz = mycam.create_ptz_service()
# ��������� ��������
media_profile = media.GetProfiles()[0]
image = mycam.create_imaging_service()
# ��������� ������
token = media_profile.VideoSourceConfiguration.SourceToken
SY = image.create_type('GetImagingSettings')
SY.VideoSourceToken = token
request = image.GetImagingSettings(SY)
print(request)


#�����������
brightness=request42.Brightness
if brightness <48.0:
    while brightness < 48.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Brightness = request42.Brightness + 1.0
        brightness = brightness+1.0
if brightness > 50.0:
    while brightness > 50.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Brightness = request42.Brightness - 1.0
        brightness = brightness - 1.0

s42=request42.ColorSaturation

if s42 <59.0:
    while s42 <59.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.ColorSaturation = request42.ColorSaturation + 1.0
        s42 = s42+1.0
if s42 > 61.0:
    while s42 > 61.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.ColorSaturation = request42.ColorSaturation - 1.0
        s42 = s42 - 1.0
        
contr42=request42.Contrast

if contr42 <49.0:
    while contr42 <49.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Contrast = request42.Contrast + 1.0
        contr42 = contr42+1.0
if contr42 > 51.0:
    while contr42 > 51.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Contrast = request42.Contrast - 1.0
        contr42 = contr42 - 1.0


str=cv2.VideoCapture('rtsp://192.168.15.43:554')
ret,frame=str.read()
cv2.imshow('qwerty',frame)
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(2, 2, 3)
plt.imshow(hist,interpolation = 'nearest')

fig.add_subplot(2, 2, 4)
for i,col in enumerate(color): #������ �������� ������������� ���������� �������� � ���� ����������� � ��������������� ��������� ������� RGB
      histr = cv2.calcHist([frame],[i],None,[256],[0,256])
      plt.plot(histr,color = col)
      plt.xlim([0,256])
plt.show()

