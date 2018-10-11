import git
import os
import shutil

giturl = "https://github.com/BoseCorp/py-googletrans.git"

# print((bool(os.path.isdir("./googltrans"))))

os.mkdir("googletrans")
 
repo = git.Repo.init("googletrans")
origin = repo.create_remote('origin',giturl)
origin.fetch()
origin.pull(origin.refs[0].remote_head)


# print((bool(os.path.isdir("./amigo/dependency/googltrans"))))
# print (os.path.isdir("./amigo/googltrans"))
if (bool(os.path.isdir("./amigo/dependency/googltrans")))==False:
        shutil.rmtree("./amigo/dependency")
        shutil.move("googletrans/googletrans","./amigo/dependency")
else:
    shutil.move("googletrans/googletrans","./amigo/dependency")



shutil.rmtree("./googletrans")