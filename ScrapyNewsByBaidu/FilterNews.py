import shutil
import os
import os.path

rootdir = "/home/yoshipark/PycharmProjects/digital_governance/news/"

count = 0
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        data = open(os.path.join(parent, filename)).read()
        if len(data) < 10:
            print("filename is:" + filename)
            count += 1
        else:
            targetdir = parent.replace("news", "newsFilter")
            if not os.path.exists(targetdir):
                print(targetdir)
                os.makedirs(targetdir)
            shutil.copyfile(os.path.join(parent, filename), targetdir + '/' + filename)
print(count)