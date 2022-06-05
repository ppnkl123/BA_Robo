import csv

class csvFile:
    
    def __init__(self, file_path):
        self.file_path = file_path
        
    def print_instance(self):
        print("filepath: ", self.file_path)
        
    def create(self):
        header = ['time', 'action', 'text', 'subtext']
        with open(self.file_path, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
    
    def log(self, msg):
        with open(self.file_path, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(msg)
