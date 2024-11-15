from torch.utils import data
import os
import json

path='data/train'
folder_name = os.listdir(path)
train_set = []
labels = []
        
for file_name in folder_name:
    file_path = os.path.join(path, file_name)
            
    with open(file_path, 'r', encoding='utf-8') as file:
        current_data = json.loads(file.readline().strip())
        print(current_data["rating"])
        print(current_data["text"])
        
        
            
            