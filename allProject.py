from pathlib import Path

"""
nama_folder = ambil dari looping count folder *kecuali alpro-env
fileName = ambil dari looping count folder kemudian nama file

"""
n = 1
path            = Path(str(Path.cwd()))
exclude         =  ['alpro-env','.git','.gitignore','Flowgorithm','.ipynb_checkpoints','allProject.py','requirements.txt']


folderProject   = []
filesProject    = []
choosenFolder   = path

for folder in path.iterdir():
    if folder.name not in exclude :
       folderProject.append(folder.name)



def showProject() :
    listFolder = []
    for folder in path.iterdir():
        if folder.name not in exclude :
           listFolder.append(folder.name)

folderProject.sort()

def printProject(listProject,i) :
    for fn in listProject :
        print(i,'.) ',fn)
        i+=1



try :
    print("---------  Pilih Folder Project ---------")
    printProject(folderProject,n)
    a   = int(input("==> Pilih Project : "))

except :
    print("Nomor yang anda pilih tidak ada di menu")

else :
    choosenFolder   = Path(str(path)+"/"+folderProject[a-1])


    for filePrj in choosenFolder.iterdir():

        print(n,".) ",filePrj.name)
        filesProject.append(filePrj.name)
        n+=1

    try :
        b = int(input("==> Pilih File Project : "))
        print(filesProject[b-1])

    except :
        print("Nomor Project yang anda pilih tidak ada dimenu")
        #print(folderProject[a-1])
        #print(pilihFolder)

    else :
        print("""

        |-------- Menjalankan File | %s | --------|


                    """ % (filesProject[b-1]))
        try :
            exec(open(str(choosenFolder)+"/"+filesProject[b-1]).read())

        except :
            print("Project yang anda jalankan gagal")

        else :
            print("Project Berhasil Dijalankan")
