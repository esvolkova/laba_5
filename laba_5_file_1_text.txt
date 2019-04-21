import cv2
import numpy	

from time import sleep
from matplotlib import pyplot as plt

#Удаление данной ошибки pythonvalue() not implemented
import zeep
from onvif import ONVIFCamera, ONVIFService
def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue
zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

#Подключение к камере
from onvif import ONVIFCamera
mycam = ONVIFCamera('192.168.15.43', 80, 'admin', 'Supervisor')

#Получаем поток
str=cv2.VideoCapture('rtsp://192.168.15.43:554/2')

#Создаём гистограмму
fig=plt.figure(figsize=(2, 2))
color = ('b','g','r')
ret,frame=str.read()
cv2.imshow('qwerty',frame)
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #Оттенок 180 Насыщенность 256
fig.add_subplot(2, 2, 1)
plt.imshow(hist,interpolation = 'nearest')

fig.add_subplot(2, 2, 2)
for i,col in enumerate(color): #each value corresponds to number of pixels in that image with its corresponding pixel value RGB
    histr = cv2.calcHist([frame],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

# Создание медиа-сервиса
media = mycam.create_media_service()
#ptz = mycam.create_ptz_service()
# Получение профилей
media_profile = media.GetProfiles()[0]
image = mycam.create_imaging_service()
# Получение токена
token = media_profile.VideoSourceConfiguration.SourceToken
SY = image.create_type('GetImagingSettings')
SY.VideoSourceToken = token
request = image.GetImagingSettings(SY)
print(request)



#Изменение параметров на правильные 
b=request.Brightness
if b <48.0:
    print("Camera Brightness")


    #цикл для плавного изменения картинки
    while b < 48.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.Brightness = request.Brightness + 2.0
        print(request.Brightness)
        b = b+2.0
if b > 50.0:
    print("Camera Brightness")
    while b > 50.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.Brightness = request.Brightness - 2.0
        print(request.Brightness)
        b = b - 2.0
      
s=request.ColorSaturation

if s <59.0:
    print("Camera Saturation")
    while s <59.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.ColorSaturation = request.ColorSaturation + 2.0
        print(request.ColorSaturation)
        s = s+2.0

if s > 61.0:
    print("Camera Saturation")
    while s > 61.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.ColorSaturation = request.ColorSaturation - 2.0
        print(request.ColorSaturation)
        s = s - 2.0
        
c=request.Contrast
if c <49.0:
    print("Camera Contrast")
    while c <49.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.Contrast = request.Contrast + 2.0
        print(request.Contrast)
        c = c+2.0


if c > 51.0:
    print("Camera Contrast")
    while c > 51.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.Contrast = request.Contrast - 2.0
        print(request.Contrast)
        c = c - 2.0
 
        
#Баланс белого
cr = request.WhiteBalance.CrGain
cb = request.WhiteBalance.CbGain   

if cr >41.0:
    print("Camera White Balance Cr gain")
    while cr > 41.0: 
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.WhiteBalance.CrGain = request.WhiteBalance.CrGain - 1.0
        print(request.WhiteBalance.CrGain)
        cr = cr - 1.0
        cr=request.WhiteBalance.CrGain    
if cr <39.0:
    print("Camera White Balance Cr gain")
    while cr <39.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.WhiteBalance.CrGain = request.WhiteBalance.CrGain + 1.0
        print(request.WhiteBalance.CbGain)
        cr = cr+1.0
if cb >61.0:
    print("Camera White Balance Cb gain")
    while cb > 61.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.WhiteBalance.CbGain = request.WhiteBalance.CbGain -1.0
        print(request.WhiteBalance.CbGain)
        cb = cb - 1.0  
if cb <59.0:
    print("Camera White Balance Cb gain")
    while cb <59.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.WhiteBalance.CbGain = request.WhiteBalance.CbGain + 1.0
        print(request.WhiteBalance.CbGain)
        cb = cb + 1.0  


#Построение гистограммы
#color = ('b','g','r')
ret,frame=str.read()
cv2.imshow('qwerty',frame)
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #Оттенок 180 Насыщенность 256
fig.add_subplot(2, 2, 3)
plt.imshow(hist,interpolation = 'nearest')
    
fig.add_subplot(2, 2, 4)
for i,col in enumerate(color): #каждое значение соответствует количеству пикселей в этом изображении с соответствующим значением пикселя RGB
    histr = cv2.calcHist([frame],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    
plt.show()	 


#для другой камеры
"""



cam_42 = ONVIFCamera('192.168.15.42', 80, 'admin', 'Supervisor') 
fig=plt.figure(figsize=(3, 2))
 
str=cv2.VideoCapture('rtsp://192.168.15.42:554/2')
ret,frame=str.read()
cv2.imshow('qwerty',frame)
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #Оттенок 180 Насыщенность 256
fig.add_subplot(3, 2, 1)
plt.imshow(hist,interpolation = 'nearest')


#Полутон
fig.add_subplot(2, 3, 2)
plt.hist(frame.ravel(),256,[0,256]); 
fig.add_subplot(3, 2, 2)
for i,col in enumerate(color):
    histr = cv2.calcHist([frame],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    
media_service = cam_42.create_media_service()
profiles = media_service.GetProfiles()[0]
token = media_service.GetProfiles()[0].token
ptz = cam_42.create_ptz_service()
ptz_token = profiles.PTZConfiguration.token


#Абсолютный ход
ptz.create_type('AbsoluteMove')
pos = ptz.GetStatus({'ProfileToken': token}).Position
x0 = pos.PanTilt.x
y0 = pos.PanTilt.y
print(x0,y0) #current coordinates
if x0 >= 0 and x0 <=1:
    ptz.AbsoluteMove({'ProfileToken': token, 'Position':{'PanTilt':{'x': x0 - 0.5,'y': y0}}})
else:
    ptz.AbsoluteMove({'ProfileToken': token, 'Position':{'PanTilt':{'x': x0 + 0.5,'y': y0}}})
if y0 >= 0 and y0 <=1:
    ptz.AbsoluteMove({'ProfileToken': token, 'Position':{'PanTilt':{'x': x0,'y': y0 - 0.5}}})
else:
    ptz.AbsoluteMove({'ProfileToken': token, 'Position':{'PanTilt':{'x': x0,'y': y0 + 0.5}}})
 

str=cv2.VideoCapture('rtsp://192.168.15.42:554/2')
ret,frame=str.read()
cv2.imshow('qwerty',frame)
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(3, 2, 3)
plt.imshow(hist,interpolation = 'nearest')
fig.add_subplot(3, 2, 4)
for i,col in enumerate(color):
    histr = cv2.calcHist([frame],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])


#Изменение параметров на правильные
b=request.Brightness
if b <48.0:
    print("Camera Brightness")
    while b < 48.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.Brightness = request.Brightness + 2.0
        print(request.Brightness)
        b = b+2.0
if b > 50.0:
    print("Camera Brightness")
    while b > 50.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.Brightness = request.Brightness - 2.0
        print(request.Brightness)
        b = b - 2.0
      
s=request.ColorSaturation
if s <59.0:
    print("Camera Saturation")
    while s <59.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.ColorSaturation = request.ColorSaturation + 2.0
        print(request.ColorSaturation)
        s = s+2.0
if s > 61.0:
    print("Camera Saturation")
    while s > 61.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.ColorSaturation = request.ColorSaturation - 2.0
        print(request.ColorSaturation)
        s = s - 2.0
        
c=request.Contrast
if c <49.0:
    print("Camera Contrast")
    while c <49.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.Contrast = request.Contrast + 2.0
        print(request.Contrast)
        c = c+2.0
if c > 51.0:
    print("Camera Contrast")
    while c > 51.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.Contrast = request.Contrast - 2.0
        print(request.Contrast)
        c = c - 2.0
 
        
#Баланс белого
cr = request.WhiteBalance.CrGain
cb = request.WhiteBalance.CbGain   
if cr >41.0:
    print("Camera White Balance Cr gain")
    while cr > 41.0: 
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.WhiteBalance.CrGain = request.WhiteBalance.CrGain - 1.0
        print(request.WhiteBalance.CrGain)
        cr = cr - 1.0
        cr=request.WhiteBalance.CrGain    
if cr <39.0:
    print("Camera White Balance Cr gain")
    while cr <39.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.WhiteBalance.CrGain = request.WhiteBalance.CrGain + 1.0
        print(request.WhiteBalance.CbGain)
        cr = cr+1.0
if cb >61.0:
    print("Camera White Balance Cb gain")
    while cb > 61.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.WhiteBalance.CbGain = request.WhiteBalance.CbGain -1.0
        print(request.WhiteBalance.CbGain)
        cb = cb - 1.0  
if cb <59.0:
    print("Camera White Balance Cb gain")
    while cb <59.0:
        image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
        request.WhiteBalance.CbGain = request.WhiteBalance.CbGain + 1.0
        print(request.WhiteBalance.CbGain)
        cb = cb + 1.0  
        
'''
while True:
    b=request.Brightness
    if b < 48.0:
        while b<48.0: 
            image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
	    request.Brightness = b+2.0
    if b > 50.0:
	while b > 50.0:
	    image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
	    request.Brightness = b-2.0
	    
    s=request.ColorSaturation ####
    if s < 29.0:
	while s < 29.0:
	    image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
	    request.ColorSaturation = s+2.0
    if s > 31.0:
	while s > 31.0:
	    image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
	    request.ColorSaturation = s-2.0
	    
    c=request.Contrast
    if c < 48:
	while c < 48:
	    image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
	    request.Contrast = c+2.0	    
    if c > 48:
	while c > 48:
	    image.SetImagingSettings({'VideoSourceToken' : token, 'ImagingSettings' : request})
	    request.Contrast = c-2.0	
	#add white balance    
	    
    if cv2.waitKey(20)&0xFF==ord('q'):
        break
str=cv2.VideoCapture('rtsp://192.168.15.42:554/2')
ret,frame=str.read()
cv2.imshow('qwerty',frame)
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(3, 2, 5)
plt.imshow(hist,interpolation = 'nearest')
    
    
fig.add_subplot(3, 2, 6)
for i,col in enumerate(color):
    histr = cv2.calcHist([frame],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()    
'''    
'''
while True:
 if cv2.waitKey(20)&0xFF==ord('q'):
   break
'''
 
str=cv2.VideoCapture('rtsp://192.168.15.42:554/2')
ret,frame=str.read()
cv2.imshow('qwerty',frame)
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(3, 2, 5)
plt.imshow(hist,interpolation = 'nearest')
fig.add_subplot(3, 2, 6)
for i,col in enumerate(color):
    histr = cv2.calcHist([frame],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
