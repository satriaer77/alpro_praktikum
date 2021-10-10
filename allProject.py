from pathlib import Path

"""
nama_folder = ambil dari looping count folder *kecuali alpro-env
fileName = ambil dari looping count folder kemudian nama file

"""
n = 1
path            = Path(str(Path.cwd())+"/")
exclude         =  ['alpro-env','.git','.gitignore','Flowgorithm','.ipynb_checkpoints','allProject.py','requirements.txt'] 


folderProject   = []
filesProject    = []
choosenFolder   = str(path)


for folder in path.iterdir():
    if folder.name not in exclude :
       folderProject.append(folder.name)


folderProject.sort()

def printProject(folderList,i) : 
    for fn in folderList :
        print(i,'.) ',fn)
        i+=1

  


def chooseProject(arrFoProj,pathFolder) :
    try :
        print("""
      ---------  Pilih Folder Project ---------
        """,printProject(arrFoProj),"""

        """)
        a               = int(input("==> Pilih Project : "))
    except :
        print("Nomor yang anda pilih tidak ada di menu")
    else :
        choosenFolder   = pathFolder+""+arrFoProj[a-1]
        return choosenFolder

  
def printFProject(arrFoProj,pathFolder,i) :
    for filePrj in pathFolder.iterdir():

        print(n,".) ",filePrj.name)
        filesProject.append(filePrj.name)
        i+=1

def runProject(arrFoProj,pathFolder) :
    try :
        b = int(input("==> Pilih File Project : "))
        print(arrFoProj[b-1])
    except : 
        print("Nomor Project yang anda pilih tidak ada dimenu")
        #print(folderProject[a-1])
        #print(pilihFolder)
    else :
        try : 
            open(str(pathFolder)+"/"+arrFoProj[b-1]).read()
        except :
            print("Project yang anda jalankan gagal")
        else : 
            exec(open(str(pathFolder)+"/"+arrFoProj[b-1]).read())


chooseProject(folderProject,str(path))
printFProject(folderProject,Path(choosenFolder),n)
runProject(filesProject,choosenFolder)


