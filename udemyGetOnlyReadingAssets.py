import os
import zipfile


for (dirnames, dirs, files) in os.walk('.'):
    print(dirnames)
    print("------")
    for filename in files:
        if filename.endswith('.DS_Store'):
            print(filename)
            file_f = dirnames+'/'+filename
            file_f = file_f.replace(" ","\ ")
            command = 'git rm '+ file_f         #dirnames+'/'+filename
            # command = command.replace(" ","\ ")
            print("command", command)
            os.system(command)
        if filename.endswith('.mp4'):
            print(filename)
            os.remove(dirnames+"/"+filename)

        elif filename.endswith('.zip'):
            nameOfFile = filename.split(".")
            os.remove(dirnames+"/"+filename)
            '''
            os.mkdir(dirnames+"/"+nameOfFile[0])
            
            zip_ref = zipfile.ZipFile(dirnames+"/"+filename, 'r')
            zip_ref.extractall(dirnames+"/"+nameOfFile[0])
            zip_ref.close()
            '''

