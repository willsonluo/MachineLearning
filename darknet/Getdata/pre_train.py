import os,shutil
import xml.etree.ElementTree as ET


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def convert_annotation(in_file_name, out_file_name):
    in_file = open(in_file_name)
    out_file = open(out_file_name, 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


path = os.getcwd() # r'C:\Willson_Works\MachineLearning资料\Getdata\tempdata\Getdata'
image_list = [ file for file in os.listdir(path+os.sep+'Image') if "jpg" in file]
#print(image_list)
validation = 16
classes = ["character"]
trainId = open(path+os.sep+"trainId.txt","w")
trainPath = open(path+os.sep+"trainPath.txt","w")
validationId = open(path+os.sep+"validationId.txt","w")
validationPath = open(path+os.sep+"validationPath.txt","w")
for i in range(len(image_list)):
    file_core = image_list[i].split(".")[0]
    print(file_core)
    if i > validation:
        shutil.copy(path+os.sep+"Image"+os.sep+file_core+".jpg",path+os.sep+"train"+os.sep+"image"+os.sep+file_core+".jpg")
        shutil.copy(path+os.sep+"Image"+os.sep+file_core+".xml",path+os.sep+"train"+os.sep+"xml"+os.sep+file_core+".xml")
        trainId.write(file_core+"\n")
        trainPath.write(path+os.sep+"train"+os.sep+"image"+os.sep+file_core+".jpg"+"\n")
        convert_annotation(path+os.sep+"Image"+os.sep+file_core+".xml",path+os.sep+"train"+os.sep+"image"+os.sep+file_core+".txt")

    else:
        shutil.copy(path+os.sep+"Image"+os.sep+file_core+".jpg",path+os.sep+"validation"+os.sep+"image"+os.sep+file_core+".jpg")
        shutil.copy(path+os.sep+"Image"+os.sep+file_core+".xml",path+os.sep+"validation"+os.sep+"xml"+os.sep+file_core+".xml")
        validationId.write(file_core+"\n")
        validationPath.write(path+os.sep+"validation"+os.sep+"image"+os.sep+file_core+".jpg"+"\n")
        convert_annotation(path+os.sep+"Image"+os.sep+file_core+".xml",path+os.sep+"validation"+os.sep+"image"+os.sep+file_core+".txt")


trainId.close()
trainPath.close()
validationId.close()
validationPath.close()

