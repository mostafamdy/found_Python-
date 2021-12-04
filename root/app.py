import os
import DataBase
from flask import Flask, request, url_for, render_template
import json
import base64
from datetime import datetime
import numpy as np
import face_recognition

# compare take two string and change from string base64 to byte
# then set its in file after that compare
projectPath=os.getcwd()
def compare_face(image1, image2):
     # image1 is string for path
     known_image = face_recognition.load_image_file(projectPath+image1)
     unknown_image = face_recognition.load_image_file(projectPath+image2)
     biden_encoding = face_recognition.face_encodings(known_image)[0]
     unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
     results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
     if results[0]==True:
         print("found it")
         return True
     else:
         return False
app = Flask(__name__)

#  child found     works well
#  child notFound  works well
#  parent works good
#  someone works good
@app.route('/')
def showIt():
    print("url is ")
    print(url_for('static', filename='image.jpg'))
    DataBase.Update_Child_Found("Image", "newImage", "ChildID = " + '1')
    DataBase.mydb.commit()
    # return """<img src="{{url_for('static', filename='image.jpg')}}">"""
    return url_for('static', filename='image.jpg')

@app.route('/ChildNotFound')
def ChildNotFounded():
    x = []
    li = DataBase.selectALLFromChildNotFound('*')
    DataBase.mydb.commit()
    for i in li:
        x.append({"name": i[1], 'description': i[3],'location': i[0],'age': i[2], 'image': i[4]})
    return json.dumps(x, indent=4)

# sendNotFoundChild?name=mohamed&age=10&location=x=0y=5&description=444&image=14235&ChildID=5
@app.route('/sendNotFoundChild', methods=['POST'])
def getNotFoundChild():
    data = request.get_json()
    name = str(data['name'])
    age = str(data['age'])
    description = str(data['description'])
    image64 = str(data['imagebase64'])
    now = datetime.now()
    imageName = now.strftime("%d%m%y%H%M%S")
    image = base64.b64decode(image64)
    path = os.getcwd() + "\\static\\" + imageName + ".jpg"
    file = open(path, 'wb')
    file.write(image)
    file.close()
    url = url_for('static', filename=imageName + '.jpg')

    DataBase.insertINChildNotFound(name, age, description, url)
    DataBase.mydb.commit()
    print("wait for matched")
    matched = DataBase.selectFromChildFounded("*", "name = \'" + name + "\'")
    ismatched=False
    foundUrl=""
    for matchedData in matched:
        print(matchedData[5])
        ismatched=compare_face(url,matchedData[5])
        if ismatched:
            foundUrl=matchedData[5]
            break
    #  get child found images where name = name
    #  compare images with this image
    #  get from child found where image = current image
    #  return child
    if ismatched:
        d=DataBase.selectFromChildFounded('*',"Image = \'"+foundUrl+"\'")
        print(d)
        DataBase.mydb.commit()
        x=[]
        phone=[[0],[1]]
        x.append({"name": d[0][1], 'age': d[0][3], 'description': d[0][4], 'location': d[0][2], 'image': d[0][5],'phone':phone[0][0]})
        return json.dumps(x, indent=4)
    else:
        return "not found "

#___________________________________________________________________________________________
@app.route('/ChildFound')
def ChildFound():
    x = []
    li = DataBase.selectALLFromChildFounded('*')
    DataBase.mydb.commit()
    for i in li:
        print(i[0])
        if i[0]==1:
            print("i[0]=1")
            continue
        phone = DataBase.selectFromSomeOne('phone', "ChildID = " + str(i[0]))
        DataBase.mydb.commit()
        print(phone)

        # phone=[[0],[1]]
        x.append({"name": i[1], 'age': i[3], 'description': i[4], 'location': i[2], 'image': i[5],'phone':phone[0][0]})
    return json.dumps(x, indent=4)

#sendFoundChild?name=mohamed&age=10&location=x=0y=5&description=444&image=14235&ChildID=5
@app.route('/sendFoundChild', methods=['POST'])
def getFoundChild():
    data = request.get_json()
    print(data)
    age = data['age']
    name = data['name']
    location = data['location']
    description = data['description']
    image64 = data['imageBase64']
    founderName=data["founderName"]
    founderPhone=data["phone"]

    # save image
    now = datetime.now()
    imageName = now.strftime("%d%m%y%H%M%S")
    image = base64.b64decode(image64)
    path = os.getcwd() + "\\static\\" + imageName + ".jpg"
    file = open(path, 'wb')
    file.write(image)
    file.close()
    url = url_for('static', filename=imageName + '.jpg')
    print("Waitting 1")
    DataBase.insertINChildFounded(name, location, age, description, url)
    DataBase.mydb.commit()
    print("waitting here 0")
    id=DataBase.selectFromChildFounded("ChildID","Image = \'"+url+"\'")
    print("end Waiting 0")
    print(id[0][0])
    DataBase.mydb.commit()
    DataBase.insertINSomeOne(founderName, founderPhone, str(id[0][0]))
    DataBase.mydb.commit()
    return str(id[0][0])
# __________________________________________________________________________
@app.route('/parent')
def Parent():
    parent = []
    li = DataBase.selectALLFromParents('*')
    DataBase.mydb.commit()
    for i in li:
        parent.append({"name": i[0]})
    return json.dumps(parent, indent=4)

#sendParent?name=parentName&address="address"&id="id"
@app.route('/sendParent', methods=['GET'])
def getParent():
    name = str(request.args['name'])
    address = str(request.args['address'])
    id = str(request.args['id'])
    DataBase.insertINParents(name, id, address)
    DataBase.mydb.commit()
    return "HI"

# _________________________________________________________________________________
@app.route('/someone')
def Someone():
    someone = []
    li = DataBase.selectALLFromSomeOne('*')
    DataBase.mydb.commit()
    for i in li:
        someone.append({"name": i[0], 'phone': i[1],'ChildID':i[2]})
    return json.dumps(someone, indent=4)

# sendSomeOne?name=ahmed&phoneNumber=0100014584&ChildID=5
@app.route('/sendSomeOne', methods=['GET'])
def getSomeOne():
    name = str(request.args['name'])
    phoneNumber = str(request.args['phoneNumber'])
    ChildID= str(request.args['ChildID'])
    print("error1")
    DataBase.insertINSomeOne(name, phoneNumber, ChildID)
    print("error2")
    # DataBase.Update_IDs('childfound',ChildID)
    print("error3")
    # DataBase.mydb.commit()
    print("error4")
    return "GOOD WORK"

















@app.route('/sendImage', methods=['GET'])
def getImage():
    image1 = str(request.args['image'])
    index = str(request.args['index'])
    lastIndex = str(request.args['lastIndex'])
    if(lastIndex=='false'):
        DataBase.insertINimageTest(image1, index)
    else:
        list = DataBase.selectAllImageTest()

    return "Done"


@app.route('/Post', methods=['POST'])
def post():
    if request.is_json !=None:
        data = request.get_json()
        DataBase.insertINimageTest(data['name'], data['index'], data['type'], data['id'])
        DataBase.mydb.commit()
        real_length1 = DataBase.select_From_Image('indx','image=" "')
        # if all data sent while do this statements
        # save image in one attribute in database as base64 string
        # after that compare the face with other faces by using compare_face
        if len(real_length1) != 0:
            current_length = len(DataBase.selectAllImageTest())
            real_length = real_length1[0][0]
            if current_length-1 == int(real_length):
                full_image = ""
                lit = []
                for i in range(int(real_length)):
                    lit.append(DataBase.select_From_Image('image', 'indx = '+str(i))[0][0])
                # List and full_image Now have All image

                full_image = full_image.join(lit)

                typ = DataBase.select_From_Image('typ', where='indx=0')[0][0]

                id = DataBase.select_From_Image('id', where='indx=0')[0][0]

                # Now we delete all sub images in ImageTest for Next upload
                DataBase.truncateImageTest()
                DataBase.mydb.commit()
                # save image in right position and compare this image with other

                if(str(typ) == 'ChildNotFound'):
                     DataBase.Update_Child_NotFound('Image', full_image, "ChildID = "+str(id))
                     DataBase.mydb.commit()
                     compare_face(full_image, typ)
                elif(str(typ) == 'ChildFound'):
                     DataBase.Update_Child_Found('Image', full_image, 'ChildID='+str(id))
                     DataBase.mydb.commit()
                     compare_face(full_image, typ)
        else:
          name1 = request.FILES['file']
        # name1 = request.form['name']
        # DataBase.insertINimageTest("NOT JSON", 3)
        # DataBase.mydb.commit()
    return "GOOD WORK"
#
@app.route('/sendimage', methods=['POST'])
def saveImage():
    data=request.get_json()
    img64=data["imageBase64"]
    childID=data["childID"]

    # save image
    now=datetime.now()
    imageName=now.strftime("%d%m%y%H%M%S")
    # imageName="iam2"
    path=os.getcwd()+"\\static\\"+imageName+".jpg"

         # "image1.jpg"
         # imageName
    img=base64.b64decode(img64)

    file=open(path,'wb')
    file.write(img)
    file.close()
    # end

    # update image in found child
    url=url_for('static', filename=imageName+'.jpg')
    DataBase.Update_Child_Found("Image",url,"ChildID = "+str(childID))
    DataBase.mydb.commit()
    # end
    print(path)
    return path

# @app.route('/IDs')
# def get_IDs():
#     IDs = []
#     li = DataBase.selectALLfromIDs('*')
#     DataBase.mydb.commit()
#     print(li)
#     for i in li:
#         IDs.append({
#             "childNotFound": i[0],
#             'childfound': i[1],
#             'parent': i[2],
#             'someone': i[3]
#         }
#         )
#
#     return json.dumps(IDs, indent=4)

