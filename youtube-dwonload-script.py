from pytube import YouTube

while 1:
  
 try:
  link=input("Put link youtube to download in 720p OR (0 To Exit) : \n")
  if(link=='0'): break 
  else:
  	Y=YouTube(link)
  	Y=Y.streams.get_highest_resolution()
  	Y.download('/home/wasim/Downloads')
  	print('Done')  
 except:
 	print("Error")
  
  
