#importing the libraries
import numpy as np
from keras.preprocessing import image

#prediction
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from keras.models import load_model
#classifier = load_model('cancer_class_model_with_test.h5')
classifier = load_model('D:\Project_AI\model_op\crop_protection_model.h5')

classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    x = openfn()
    test_image = image.load_img(x, target_size = (64,64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict_classes(test_image)
    print(result)
    if result==0:
        print('Gulls')
    elif result==1:
        print('Herons')
    elif result==2:
        print('Hornbill')
    elif result==3:
        print('Peacock')
    elif result==4:
        print('Sparrow')
    else:
        print('Nan')
    index=["Gulls","Herons","Hornbill","Peacock","Sparrow"]
    label = Label( root, text="Prediction : "+index[result[0][0]])
    label.pack()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()

btn = Button(root, text='open image', command=open_img).pack()

root.mainloop()

