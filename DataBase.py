import base64

import mysql.connector
try:
    mydb=mysql.connector.connect(
    port=3308,
    host="127.0.0.1",
    user="root",
    passwd='pass',
    # passwd="rT4yT2O4Sk",
    database="found",
    auth_plugin = 'mysql_native_password'
    )
    mycursor = mydb.cursor(buffered=True)
# ------------------------------------------parent -------------------------------------------

    # parent have Name , ChildId , NationalId , IdPhoto

    # mycursor.execute("CREATE TABLE IF NOT EXISTS parent(ChildId int ,Name VARCHAR(40), NationalId varchar(100) , IdPhoto varchar(255))")

# ------------------------------------- childNotFound ------------------------------------------

    # childNotFound have  ChildID , Name , Age , Description  , Location , Image

    # mycursor.execute("CREATE TABLE IF NOT EXISTS childNotFound ( ChildID int ,Name VARCHAR(50) , Age varchar(3) , Description VARCHAR(100) , Location VARCHAR(50) , Image varchar(255) ) ")

# --------------------------------------- someOne-----------------------------------------------

    # someOne have Name , Phone , ChildID

    # mycursor.execute("CREATE TABLE IF NOT EXISTS someOne(ChildID int, Name varchar(50) , Phone varchar(50) )")

# ---------------------------------------childFounded---------------------------------------------

    # childFounded have Name  ,Location, Description , Image , ChildID

    # mycursor.execute ( "CREATE TABLE IF NOT EXISTS childFounded(ChildID int , Name varchar(50)  , Location varchar(50), Description varchar(255) , Image varchar(255) )")

# ---------------------------------------imageTest---------------------------------------------

# the image test table for receive one image
# imageTest have image , indx
#     mycursor.execute("CREATE TABLE IF NOT EXISTS imageTest(image varchar(1500), indx int);")


# -----------------------------------------------------------------------------------------
# --------------------------------------- INSERT ------------------------------------------
# -----------------------------------------------------------------------------------------

    def insertINChildNotFound(NChildName, NChildAge, NChildDescription,image):
        childNotFound = (NChildName, NChildAge, NChildDescription,image)
        mycursor.execute("INSERT INTO childNotFound (Name , Age , Description ,Image ) VALUES ( %s, %s, %s, %s )" , childNotFound)
        mydb.commit()

    def insertINChildFounded(FChildName, FChildLocation, Fage, Fdescription,FChildImage):
        childFounded = (FChildName, FChildLocation, Fage, Fdescription, FChildImage)
        mycursor.execute(
            "INSERT INTO childFounded (Name , Location , age , Description , Image  ) VALUES (%s, %s, %s,%s,%s)",
            childFounded)
        mydb.commit()

    def insertINSomeOne(SName, SPhone, ChildID):
        someOne = (SName, SPhone, ChildID)
        mycursor.execute(
            "INSERT INTO someOne (Name , Phone ,ChildID) VALUES ( %s, %s,%s)",
            someOne)
        mydb.commit()

    def insertINParents(PName, PNationalId, PAddress):
        parent = (PName, PNationalId, PAddress)
        mycursor.execute(
            "INSERT INTO parent (Name , NationalId ,IdPhoto) VALUES ( %s, %s, %s)",
            parent)
        mydb.commit()

    def insertINimageTest(image, index, type, id):
        image = (image, index, type, id)
        mycursor.execute(
            "INSERT INTO imageTest (image,indx,typ,id) VALUES (%s, %s, %s, %s)",
            image)
        mydb.commit()
    def insert_result(FoundID,NotFoundID):
        s = "INSERT INTO results (FoundID,NotFoundID) VALUES ("+str(FoundID)+","+str(NotFoundID)+")"
        mycursor.execute(s)
        mydb.commit()
# -----------------------------------------------------------------------------------------
# --------------------------------------- Select ------------------------------------------
# -----------------------------------------------------------------------------------------

    def selectFromChildNotFound(column, where):
        s="SELECT "+column+" FROM childNotFound WHERE "+where+" ;"
        mycursor.execute(s)
        result = mycursor.fetchall()
        mydb.commit()
        return result

    def selectALLFromChildNotFound(column):
        s="SELECT "+column+" FROM childNotFound  ;"
        mycursor.execute(s)
        result = mycursor.fetchall()
        mydb.commit()
        return result

    def selectFromChildFounded(column,where):
        s="SELECT "+column+" FROM childFounded WHERE "+where+" ;"
        mycursor.execute(s)

        result = mycursor.fetchall()
        mydb.commit()
        return result

    def selectALLFromChildFounded(column):
        s="SELECT "+column+" FROM childFounded  ;"
        mycursor.execute(s)

        result = mycursor.fetchall()
        mydb.commit()
        return result

    def selectFromSomeOne(column,where):
        s="SELECT "+column+" FROM someOne WHERE "+where+" ;"
        mycursor.execute(s)

        result = mycursor.fetchall()
        mydb.commit()
        return result

    def selectALLFromSomeOne(column):
        s="SELECT "+column+" FROM someOne ;"
        mycursor.execute(s)
        result = mycursor.fetchall()
        mydb.commit()
        return result

    def selectFromParents(column,where):

        s = "SELECT " + column + " FROM parent WHERE " + where + " ;"
        mycursor.execute(s)

        result = mycursor.fetchall()
        mydb.commit()
        return result

    def selectALLFromParents(column):

        s = "SELECT " + column + " FROM parent ;"
        mycursor.execute(s)

        result = mycursor.fetchall()
        mydb.commit()
        return result

    def select_From_Image(column, where):

        s = "SELECT " + column + " FROM imageTest WHERE " + where + " ;"
        mycursor.execute(s)
        result = mycursor.fetchall()
        mydb.commit()
        return result

    def selectAllImageTest():
        mycursor.execute("select image from imageTest ;")
        res = mycursor.fetchall()
        l=[]
        for i in res:
           l.append(i[0])
        mydb.commit()
        return l

    # def selectALLfromIDs(column):
    #     s = "SELECT " + column + " FROM IDs ;"
    #     mycursor.execute(s)
    #     result = mycursor.fetchall()
    #     mydb.commit()
    #     return result

# -----------------------------------------------------------------------------------------
# ------------------------------------ Delete ---------------------------------------------
# -----------------------------------------------------------------------------------------

    def deleteFromChildNotFound( where):
        s="DELETE FROM childNotFound WHERE "+where+" ;"
        mycursor.execute(s)
        mydb.commit()

    def deleteFromChildFounded(where):
        s="DELETE  FROM childFounded WHERE "+where+" ;"
        mycursor.execute(s)
        mydb.commit()
    def deleteFromSomeOne(where):
        s = "DELETE  FROM someOne WHERE "+where+" ;"
        mycursor.execute(s)
        mydb.commit()
    def deleteFromParents(where):

        s = "DELETE  FROM parent WHERE " + where + " ;"
        mycursor.execute(s)
        mydb.commit()
    def deletefromImageTest(where):
        s = "DELETE  FROM imageTest WHERE " + where + " ;"
        mycursor.execute(s)
        mydb.commit()
# -----------------------------------------------------------------------------------------
# ------------------------------------ truncate ---------------------------------------------
# ---------------------------------------------------------------------------------------
    def truncateImageTest():
        s = "truncate table imageTest;"
        mycursor.execute(s)
        mydb.commit()
    def truncateTest():
         s = "truncate table ChildNotFound;"
         mycursor.execute(s)
         mydb.commit()
# -----------------------------------------------------------------------------------------
# ------------------------------------ Updata ---------------------------------------------
# -----------------------------------------------------------------------------------------

    def Update_Child_NotFound(column,value,where):
        s="UPDATE childNotFound SET "+ column +'=\"'+value+'\" WHERE +'+where+';'
        mycursor.execute(s)
        mydb.commit()
    def Update_Child_Found(column,value,where):
        s="UPDATE childFounded SET "+ column +'=\"'+value+'\" WHERE +'+where+';'
        mycursor.execute(s)
        mydb.commit()
    def Update_parent(column,value,where):
        s="UPDATE parent SET "+ column +'='+value+' WHERE +'+where+';'
        mycursor.execute(s)
        mydb.commit()
    def Update_someone(column,value,where):
        s="UPDATE someOne SET "+ column +'='+value+' WHERE +'+where+';'
        mycursor.execute(s)
        mydb.commit()
    def Update_imageTest(column,value,where):

        s="UPDATE imageTest SET "+ column +'='+value+' WHERE +'+where+';'

        mycursor.execute(s)
        mydb.commit()
    # def Update_IDs(column, value):
    #     s = "UPDATE IDs SET " + column +' = ' + value + ';'
    #     mycursor.execute(s)
    #     mydb.commit()

    # image1 = open('mostafa.jpg', 'rb')
    # strImage = base64.b64encode(image1.read()).decode("utf-8")
    # Update_Child_Found('Image',strImage, "Name=\'mostafa\'")
    # mydb.commit()

    # image=open('image.jpg','wb')
    # s = selectFromChildFounded('Image',"Name='mostafa'")
    # image.write(base64.b64decode(s[0][0]))
    # image.close()
    # insertINChildNotFound("hamdy",15,"hhhhh","x=5,y=6","image","id")
    # mydb.commit()


except mysql.connector.Error as e:
      str(e)
      print(e)