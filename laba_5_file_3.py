#Изменение параметров на правильные 
b42=request42.Brightness 
if b42 <48.0: 
print("Camera 42 Brightness") 
while b42 < 48.0: 
image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42}) 
request42.Brightness = request42.Brightness + 2.0 
print(request42.Brightness) 
b42 = b42+2.0 
if b42 > 50.0: 
print("Camera 42 Brightness") 
while b42 > 50.0: 
image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42}) 
request42.Brightness = request42.Brightness - 2.0 
print(request42.Brightness) 
b42 = b42 - 2.0 
b43=request43.Brightness 
if b43 <48.0: 
print("Camera 43 Brightness") 
while b43 < 48.0: 
image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43}) 
request43.Brightness = request43.Brightness + 2.0 
print(request43.Brightness) 
b43 = b43+2.0 
if b43 > 50.0: 
print("Camera 43 Brightness") 
while b43 > 50.0: 
image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43}) 
request43.Brightness = request43.Brightness - 2.0 
print(request43.Brightness) 
b43 = b43 - 2.0 

s42=request42.ColorSaturation 
if s42 <59.0: 
print("Camera 42 Saturation") 
while s42 <59.0: 
image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42}) 
request42.ColorSaturation = request42.ColorSaturation + 2.0 
print(request42.ColorSaturation) 
s42 = s42+2.0 
if s42 > 61.0: 
print("Camera 42 Saturation") 
while s42 > 61.0: 
image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42}) 
request42.ColorSaturation = request42.ColorSaturation - 2.0 
print(request42.ColorSaturation) 
s42 = s42 - 2.0 
s43=request43.ColorSaturation 
if s43 <59.0: 
print("Camera 43 Saturation") 
while s43 <59.0: 
image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43}) 
request43.ColorSaturation = request43.ColorSaturation + 2.0 
print(request43.ColorSaturation) 
s43 = s43+2.0 
if s43 > 61.0: 
print("Camera 43 Saturation") 
while s43 > 61.0: 
image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43}) 
request43.ColorSaturation = request43.ColorSaturation - 2.0 
print(request43.ColorSaturation) 
s43 = s43 - 2.0 

c42=request42.Contrast 
if c42 <49.0: 
print("Camera 42 Contrast") 
while c42 <49.0: 
image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42}) 
request42.Contrast = request42.Contrast + 2.0 
print(request42.Contrast) 
c42 = c42+2.0 
if c42 > 51.0: 
print("Camera 42 Contrast") 
while c42 > 51.0: 
image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42}) 
request42.Contrast = request42.Contrast - 2.0 
print(request42.Contrast) 
c42 = c42 - 2.0 
c43=request43.Contrast 
if c43 <49.0: 
print("Camera 43 Contrast") 
while s43 <49.0: 
image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43}) 
request43.Contrast = request43.Contrast + 2.0 
print(request43.Contrast) 
c43 = c43+2.0 
if c43 > 51.0: 
print("Camera 43 Contrast") 
while c43 > 51.0: 
image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43}) 
request43.Contrast = request43.Contrast - 2.0 
print(request43.Contrast) 
c43 = c43 - 2.0