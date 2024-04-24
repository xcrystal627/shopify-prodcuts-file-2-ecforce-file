import os



current_dir = os.getcwd() + '/imgs'


files = os.listdir(current_dir)

for file in files:
    newName = file.split(".")[0] + '_0.' +  file.split(".")[1]

    current_path = os.path.join(current_dir, file)
    new_path = os.path.join(current_dir, newName)
    

    os.rename(current_path, new_path)