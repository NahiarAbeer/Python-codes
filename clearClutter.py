import os 
class fileManupulation():
    def __init__(self ,folder_path,fileType):
        self.folder_path=folder_path
        self.fileType= fileType
    
    def chageClutter(self):
        try:
            os.chdir(self.folder_path)
            files= os.listdir()
            for i in range(len(files)):
                    if files[i].endswith(self.fileType) :
                        newname= str(i+1)+self.fileType
                        print(newname)
                        os.rename(files[i], newname )
        except FileNotFoundError:
            print("Your file doesn't exist")              
            return "Your file doesn't exist"              

folder_path = "F:\\Downloads\\clutter\\images"
fileType = ".png"

test = fileManupulation(folder_path, fileType)
test.chageClutter()
