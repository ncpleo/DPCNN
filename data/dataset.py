from torch.utils import data
import os
import json


class TextDataset(data.Dataset):

    def __init__(self, path):
        self.file_name = os.listdir(path)
        self.train_set = []
        self.labels = []
        
        for file_name in self.file_name:
            file_path = os.path.join(path, file_name)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    current_data = json.loads(line.strip())
                    self.train_set.append(current_data["text"])
                    self.labels.append(current_data["rating"])

    def __getitem__(self, index):
        return self.train_set[index], self.labels[index]

    def __len__(self):
        return len(self.train_set)
    

