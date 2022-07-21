# 把label.png改名為xx.png
import os
import re
from shutil import copyfile

# path = "/media/user/Extreme SSD/yolo/yolo_test2_data/111/"

# name_list = os.listdir(path)
# # print(name_list)

# length = 0
# filesnames = []
# for dirpath, dirnames, filesnames in os.walk(path):
#     length = len(filesnames)
#     print(length)
#     print(filesnames)
#     filesnames.sort(key = lambda i: int(i.rstrip(".jpg")))
#     #print(filesnames)
#     for i in range(length):
#         newfilename = str(i)
#         #print(newfilename)
#         originalName = path + filesnames[i]
#         # print(originalName)
#         newfilename = path + str(i+151) + ".jpg"
#         print(newfilename)
#         os.rename(originalName,newfilename)

# import os Annotations2
path='/home/user/imageTest/tools-master/DataAugForObjectDetection/data/Annotations/'
# path='/home/user/imageTest/tools-master/DataAugForObjectDetection/data/img_new/'
# path='/home/user/imageTest/tools-master/DataAugForObjectDetection/data/txt/' #這就是欲進行檔名更改的檔案路徑，路徑的斜線是為/，要留意下！
# path="/home/user/imageTest/tools-master/DataAugForObjectDetection/data/2222/"
files=sorted(os.listdir(path))
# files.sorted(path)

# print(files) #印出讀取到的檔名稱，用來確認自己是不是真的有讀到


# def rename(path_name,new_name):
#     try:
#         os.rename(path_name,new_name)
#     except Exception as e:
#         if e.args[0] ==17: #重命名
#             fname, fename = os.path.splitext(new_name)#分割一下符号以及别的 然后重命名
#             rename(path_name, fname+"-1"+fename)#递归玩法


n=0 #設定初始值
for i in files: #因為資料夾裡面的檔案都要重新更換名稱
        oldname=path+files[n] #指出檔案現在的路徑名稱，[n]表示第n個檔案
        newname=path+str(n+1594)+'.xml' #在本案例中的命名規則為：年份+ - + 次序，最後一個.wav表示該檔案的型別
        # os.chdir("/home/user/imageTest/tools-master/DataAugForObjectDetection/data/11111")
        os.rename(oldname,newname)
        print(oldname+'>>>'+newname) #印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應
        n=n+1 #當有不止一個檔案的時候，依次對每一個檔案進行上面的流程，直到更換完畢就會結束

# import os
# import random
# class ImageRename():
#     def __init__(self):
#         self.path = '/media/user/Extreme SSD/yolo/yolo_test2_data/img_0309/'#图片所在文件夹
 
#     def rename(self):
#         filelist = os.listdir(self.path)
#         random.shuffle(filelist)
#         total_num = len(filelist)
#         print(len(filelist))
 
#         i = 0
 
#         for item in filelist:
#                 print(item)
#                 if item.endswith('.jpg'):
#                         src = os.path.join(os.path.abspath(self.path), item)
#                         dst = os.path.join(os.path.abspath(self.path),  str(i) + '.jpg')
#                         os.rename(src, dst)
#                         print ('converting %s to %s ...' % (src, dst))
#                         i = i + 1
#                 print ('total %d to rename & converted %d jpgs' % (total_num, i))
 
# if __name__ == '__main__':
#     newname = ImageRename()
#     newname.rename()

# for filename in files:    
#     portion = os.path.splitext(filename)#将文件名拆成名字和后缀
#     if portion[1] == filetype:#检查文件的后缀        
        
#         newname = str(L[i]) + filetype
#         print(newname)
#         os.rename(filename, newname)#修改名称
#         i=i+1

        


# for parent, _, files in os.walk(path):
#     files.sort()  # 排序一下
#     # print(files)
#     for file in files: 
#         cnt = 0
#         # print(file)
#         while range <need_aug_num:
#             dot_index = file.rfind('_')
#             dot_index_2 = file.rfind('.')
#             _file_prefix = file[:dot_index]
#             # print(_file_prefix)

#             _file_suffix = file[dot_index_2:]
            
#             old_name = _file_prefix +'_'+ str(range+1)+'.jpg'
#             print(old_name)
#             # new_name = '{}{}'.format(cnt + 1, _file_suffix)
#             # # print(old_name)
#             # # os.rename(old_name,new_name)
#             # cnt =cnt+ 1 
#             range +=1
            
#         # '{}{}'.format(_file_prefix,_file_suffix)
    


  

# for root, dirs, names in os.walk(r'/home/user/imageTest/DataAugForObjectSegmentation/data2'):   # 改成你自己的json文件夹所在的目录    
#     for dr in dirs:
#         print(dr)
        # file_dir = os.path.join(root, dr)
        # # print(dr)
        # file = os.path.join(file_dir, dr.split('_')[0] + '.png')
        # # print(file) 
        # new_name = 'img.png'
        # new_file_name = os.path.join(file_dir, new_name)
        # os.rename(file, new_file_name)






# def quadrant1_cut_right_up():
        

        


    
