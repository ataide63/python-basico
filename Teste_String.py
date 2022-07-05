
from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry(  '400x300') # dimensão da tela
root.configure(bg='blue')

import cv2

#read image
img = cv2.imread('C:\Cartao Sd\Cursos\Python\FullStack\Modulo CSS\TecBlog\Imagens\imagem4.jpg', cv2.IMREAD_UNCHANGED)

position = (10,50)

cv2.putText(
     img, #numpy array on which text is written
     "Python Examples", 
     position, 
     cv2.FONT_HERSHEY_SIMPLEX, #font family
     1, #font size
     (209, 80, 0, 255), #font color
     3) 


#show image
cv2.imshow('Example - Show image in window',img)
cv2.waitKey(0) # waits until a key is pressed

