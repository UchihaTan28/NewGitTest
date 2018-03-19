import os
def rename_files():
    global file_list
    file_list = os.listdir(r"H:\Projects\Python\prank")
    #print(os.listdir(r"H:\Projects\Python\prank"))

rename_files()

path=os.getcwd()
print("Current working directory is "+ path)
os.chdir(r"H:\Projects\Python\prank")
for file_name in file_list:
    print(file_name)
    os.rename(file_name, file_name.translate(None,"0123456789"))
os.chdir(path)
              
rename_files()
